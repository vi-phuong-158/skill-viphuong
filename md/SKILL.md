---
name: md
description: Convert PDF files to Markdown, with OCR for scanned pages and embedded images. Use this whenever the user gives you a PDF (or a folder/glob of PDFs) and wants it read, converted, summarized, or turned into text/Markdown — including scanned contracts, invoices, receipts, reports, or any document where a plain text extraction would come back empty. Prioritizes fully offline processing (local Tesseract OCR, or a local LLM vision server like Ollama) so document contents never have to leave the user's machine; only falls back to a cloud OCR/vision API if the user explicitly agrees to it. Trigger on phrases like "đọc giúp tôi file PDF này", "convert PDF sang markdown", "PDF này bị scan, trích xuất chữ ra giúp tôi", "OCR file này", or any request to process a .pdf file, even if the user doesn't say "OCR" or "markdown" explicitly.
---

# MD — PDF to Markdown, privacy-first

Convert one or more PDFs to Markdown using `markitdown`, automatically detecting
scanned/image-only pages and OCR'ing them without sending the document anywhere,
by default.

## Why this exists

Plain-text extraction (what `markitdown` does out of the box) returns almost
nothing for scanned documents — the "text" is actually a picture of text. OCR
fixes that, but most OCR paths people reach for (`gpt-4o` vision, Azure Document
Intelligence, etc.) mean uploading the document to a third party. For anything
sensitive (contracts, IDs, medical records, internal reports), that's often not
acceptable. This skill defaults to OCR backends that never leave the machine,
and only uses a cloud backend when the user has clearly opted in for that
specific run.

## Workflow

### 1. Resolve the input

Expand whatever the user gave you (a path, a folder, a glob like `*.pdf`) into a
concrete list of PDF file paths before doing anything else.

### 2. Check what's available in this environment

Run this once per session (not once per file) — it's cheap and tells you which
OCR path is actually usable right now instead of guessing:

```bash
python <skill_dir>/scripts/convert_pdf.py --check
```

`<skill_dir>` is the directory this SKILL.md lives in. This prints JSON like:

```json
{
  "markitdown": true,
  "pypdf": true,
  "tesseract": {"available": false, "error": "..."},
  "poppler": {"available": true},
  "openai_client": false
}
```

- `markitdown` / `pypdf` false → run `pip install "markitdown[pdf]" pypdf` (ask
  first only if the Python environment is ambiguous, e.g. multiple venvs/condas
  are in play and it's not obvious which one the user means).
- `tesseract.available: false` → classic offline OCR isn't ready. Tell the user
  they can install Tesseract (e.g. `winget install UB-Mannheim.TesseractOCR` on
  Windows, `brew install tesseract` on macOS, `apt install tesseract-ocr` on
  Linux) plus the Vietnamese language pack if needed
  (`tesseract-ocr-vie` / the `vie.traineddata` file), then re-run `--check`.
  Also make sure `pip install pytesseract pdf2image` succeeded and that Poppler
  (`poppler` field) is available — `pdf2image` needs `pdftoppm` on PATH.
- `openai_client: false` and you plan to use the `llm` backend → `pip install
  openai`.

Don't block on fixing everything up front — only install what's actually needed
for the files at hand (e.g. skip Tesseract setup entirely if none of the PDFs
turn out to be scanned).

### 3. Convert

For files that convert fine with plain text extraction, this single command
handles everything — detection and OCR fallback included:

```bash
python <skill_dir>/scripts/convert_pdf.py file1.pdf file2.pdf ...
```

By default (`--backend auto`) it:
1. Converts with plain `markitdown` first (fast, no OCR, best table/layout
   fidelity).
2. If the extracted text is implausibly thin for the page count (i.e. the PDF
   is scanned or image-only), it automatically re-converts using **Tesseract**
   — full offline OCR, page-by-page, at 300 DPI.
3. Writes the result to `<name>.md` next to each input PDF.
4. Prints a JSON summary per file: page count, whether it looked scanned,
   whether OCR ran, which backend, and the output path. Relay this to the user
   in plain language — don't just dump the JSON.

Useful flags:
- `--lang vie+eng` (default) — Tesseract language codes. Add more with `+`
  (e.g. `--lang vie+eng+fra`) if a document mixes languages.
- `--force-ocr` — OCR even if the doc doesn't look scanned (useful when a PDF
  has embedded images with text alongside normal text).
- `--no-ocr` — skip OCR entirely, even for scanned-looking PDFs (fast triage).
- `--backend tesseract|llm` — pin the backend instead of letting it
  auto-choose.

### 4. If Tesseract isn't available and OCR is still needed

Two options, in order of preference:

**a. Local LLM vision (still offline).** If the user has Ollama (or any other
OpenAI-compatible server) running locally with a vision model pulled (e.g.
`qwen2.5vl`, `llava`, `minicpm-v`), use the `llm` backend pointed at that local
server — nothing leaves the machine:

```bash
python <skill_dir>/scripts/convert_pdf.py file.pdf \
  --backend llm --llm-base-url http://localhost:11434/v1 --llm-model qwen2.5vl
```

If no vision model is pulled yet, tell the user the pull command
(`ollama pull qwen2.5vl`) rather than doing it yourself — it's a multi-GB
download they should knowingly kick off.

**b. Cloud vision API.** Only reach for this if the user explicitly says it's
fine to send this specific document to a cloud provider (OpenAI, Azure, etc.).
Never default to this silently just because it's easier — that's the entire
reason this skill exists. If they agree, get their base URL/API key/model the
same way as the `llm` backend above (a real OpenAI/Azure endpoint is just
another OpenAI-compatible base URL).

### 5. Report back

Summarize per file: pages processed, whether it needed OCR and which backend
handled it, and where the `.md` file landed. If a file's OCR failed or was
skipped (check the `warning` field in the JSON output), say so plainly instead
of silently returning a near-empty Markdown file — an empty result reads as
"success" unless you flag it.
