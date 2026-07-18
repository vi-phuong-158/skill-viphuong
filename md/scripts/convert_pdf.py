#!/usr/bin/env python3
"""
Convert PDF(s) to Markdown with markitdown, falling back to OCR for scanned
pages or embedded images.

Two OCR backends are supported:

  tesseract  - classic, fully offline OCR (pytesseract + pdf2image + poppler).
               No data ever leaves the machine. Best default for privacy.
  llm        - LLM vision OCR via the markitdown-ocr plugin, using any
               OpenAI-compatible client. Point --llm-base-url at a LOCAL
               server (e.g. Ollama at http://localhost:11434/v1) to keep
               this offline too; only use a real cloud endpoint (OpenAI,
               Azure) if the user has explicitly agreed to send data out.

Run with --check first to see what's actually available in this environment
before picking a backend.
"""

import argparse
import json
import sys
from pathlib import Path


def check_environment(lang: str) -> dict:
    status = {
        "markitdown": False,
        "pypdf": False,
        "tesseract": {"available": False, "version": None, "langs": None},
        "poppler": {"available": False},
        "openai_client": False,
    }

    try:
        import markitdown  # noqa: F401

        status["markitdown"] = True
    except ImportError:
        pass

    try:
        import pypdf  # noqa: F401

        status["pypdf"] = True
    except ImportError:
        pass

    try:
        import pytesseract

        version = str(pytesseract.get_tesseract_version())
        langs = pytesseract.get_languages(config="")
        status["tesseract"] = {
            "available": True,
            "version": version,
            "langs": langs,
            "wanted_langs_installed": all(
                code in langs for code in lang.replace("+", " ").split()
            ),
        }
    except Exception as e:
        status["tesseract"] = {"available": False, "error": str(e)}

    try:
        from pdf2image import convert_from_path  # noqa: F401
        from pdf2image.exceptions import PDFInfoNotInstalledError

        status["poppler"] = {"available": True}
    except ImportError:
        status["poppler"] = {"available": False, "error": "pdf2image not installed"}
    except Exception as e:
        status["poppler"] = {"available": False, "error": str(e)}

    try:
        import openai  # noqa: F401

        status["openai_client"] = True
    except ImportError:
        pass

    return status


def count_pages(pdf_path: Path) -> int:
    from pypdf import PdfReader

    return len(PdfReader(str(pdf_path)).pages)


def plain_convert(pdf_path: Path) -> str:
    from markitdown import MarkItDown

    result = MarkItDown().convert(str(pdf_path))
    return result.text_content


def needs_ocr(text: str, page_count: int, threshold_chars_per_page: int = 25) -> bool:
    if page_count == 0:
        return False
    return (len(text.strip()) / page_count) < threshold_chars_per_page


def tesseract_convert(pdf_path: Path, lang: str, dpi: int) -> str:
    import pytesseract
    from pdf2image import convert_from_path

    images = convert_from_path(str(pdf_path), dpi=dpi)
    pages_md = []
    for i, image in enumerate(images, start=1):
        text = pytesseract.image_to_string(image, lang=lang).strip()
        pages_md.append(f"## Page {i}\n\n{text}")
    return "\n\n".join(pages_md)


def llm_convert(pdf_path: Path, base_url: str, api_key: str, model: str) -> str:
    from markitdown import MarkItDown
    from openai import OpenAI

    client = OpenAI(base_url=base_url, api_key=api_key or "not-needed")
    md = MarkItDown(enable_plugins=True, llm_client=client, llm_model=model)
    result = md.convert(str(pdf_path))
    return result.text_content


def convert_one(pdf_arg: str, args) -> dict:
    pdf_path = Path(pdf_arg)
    if not pdf_path.exists():
        return {"input": pdf_arg, "error": "file not found"}

    pages = count_pages(pdf_path)
    text = plain_convert(pdf_path)
    scanned_detected = needs_ocr(text, pages)
    used_ocr = False
    backend_used = None
    warning = None

    should_ocr = (scanned_detected or args.force_ocr) and not args.no_ocr

    if should_ocr:
        backend = args.backend
        if backend == "auto":
            backend = "tesseract"

        if backend == "tesseract":
            try:
                text = tesseract_convert(pdf_path, args.lang, args.dpi)
                used_ocr = True
                backend_used = "tesseract"
            except Exception as e:
                if args.backend == "auto" and args.llm_base_url and args.llm_model:
                    try:
                        text = llm_convert(
                            pdf_path, args.llm_base_url, args.llm_api_key, args.llm_model
                        )
                        used_ocr = True
                        backend_used = "llm"
                    except Exception as e2:
                        warning = f"tesseract failed ({e}); llm fallback failed ({e2})"
                else:
                    warning = f"tesseract OCR unavailable: {e}"
        elif backend == "llm":
            if not (args.llm_base_url and args.llm_model):
                warning = "llm backend requested but --llm-base-url/--llm-model not provided"
            else:
                try:
                    text = llm_convert(
                        pdf_path, args.llm_base_url, args.llm_api_key, args.llm_model
                    )
                    used_ocr = True
                    backend_used = "llm"
                except Exception as e:
                    warning = f"llm OCR failed: {e}"

    out_path = pdf_path.with_suffix(".md")
    out_path.write_text(text, encoding="utf-8")

    return {
        "input": str(pdf_path),
        "output": str(out_path),
        "pages": pages,
        "scanned_detected": scanned_detected,
        "used_ocr": used_ocr,
        "backend_used": backend_used,
        "chars_extracted": len(text.strip()),
        "warning": warning,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pdfs", nargs="*", help="PDF file paths")
    parser.add_argument("--check", action="store_true", help="Print available OCR backends/dependencies as JSON and exit")
    parser.add_argument("--backend", choices=["auto", "tesseract", "llm"], default="auto", help="OCR backend to use when a scanned page is detected")
    parser.add_argument("--lang", default="vie+eng", help="Tesseract language codes, e.g. 'vie+eng'")
    parser.add_argument("--dpi", type=int, default=300, help="Render DPI for tesseract full-page OCR")
    parser.add_argument("--llm-base-url", help="OpenAI-compatible base URL, e.g. http://localhost:11434/v1 for local Ollama")
    parser.add_argument("--llm-api-key", default=None, help="API key for the llm backend (any placeholder works for local servers)")
    parser.add_argument("--llm-model", help="Vision model name for the llm backend")
    parser.add_argument("--force-ocr", action="store_true", help="Always OCR, even if the document doesn't look scanned")
    parser.add_argument("--no-ocr", action="store_true", help="Never OCR, even if the document looks scanned")
    args = parser.parse_args()

    if args.check:
        print(json.dumps(check_environment(args.lang), ensure_ascii=False, indent=2))
        return

    if not args.pdfs:
        parser.error("no PDF files given (or pass --check)")

    results = [convert_one(pdf_arg, args) for pdf_arg in args.pdfs]
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
