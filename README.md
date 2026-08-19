# skill-viphuong

Bộ skill cá nhân cho Claude Code của **Vi Ngọc Phương** — đây là **Personal Skill Registry**, kho lưu trữ có version-control của thư mục `~/.claude/skills/`: backup + lịch sử + đồng bộ giữa các máy, và là nguồn sự thật (source of truth) cho các skill cá nhân.

Đây **không phải** bộ định tuyến công cụ toàn workspace — vai trò đó thuộc về `TOOLBOX.md` (`D:\04. Github\TOOLBOX.md`). Repo này chỉ mô tả và quản lý các skill cá nhân; việc chọn dùng Claude/Superpowers/Codex cho một tác vụ vẫn do `TOOLBOX.md`/`CLAUDE.md` ở tầng workspace quyết định.

## Danh mục skill (Registry)

| Skill | Internal name | Category | Status | Trigger / When to use | Notes |
|---|---|---|---|---|---|
| **setup-ai-brain** | `setup-ai-brain` | Workflow | CORE | Khởi tạo/nâng cấp bộ não dự án (`AGENTS.md`, `CLAUDE.md`, `docs/brain/00-06`) khi bootstrap dự án mới hoặc onboard codebase chưa có tài liệu AI. Không kích hoạt cho câu hỏi coding bình thường hay khi dự án đã có AGENTS/CLAUDE chuẩn hóa. | Đã tích hợp Nguyên tắc Ponytail trong template coding-rules. |
| **taste-skill** | `design-taste-frontend` | Frontend General | CORE | Skill mặc định cho chất lượng thiết kế frontend tổng quát: landing page, portfolio, redesign UI không bị "AI slop". | **Không sửa trong task này** — thân skill giữ nguyên 100%. |
| **redesign-skill** | `redesign-existing-projects` | Frontend General | ACTIVE | Audit + nâng cấp một giao diện đã có mà không phá vỡ chức năng hiện tại. Ưu tiên dùng khi mục tiêu là cải thiện UI đang tồn tại. | Hoạt động với mọi CSS framework hoặc CSS thuần. |
| **brandkit** | `brandkit` | Visual Generation | ACTIVE | Sinh brand-kit: logo system, guideline board, identity deck cao cấp. | Chỉ sinh ảnh, không viết code. |
| **imagegen-frontend-web** | `imagegen-frontend-web` | Visual Generation | ACTIVE | Sinh ảnh concept landing page/website, mỗi section một ảnh riêng. | Chỉ sinh ảnh, không viết code. |
| **imagegen-frontend-mobile** | `imagegen-frontend-mobile` | Visual Generation | ACTIVE | Sinh ảnh concept màn hình app mobile (iOS/Android). | Chỉ sinh ảnh, không viết code. |
| **md** | `md` | Documents / Output | ACTIVE | Chuyển PDF sang Markdown, kèm OCR cho trang scan/ảnh nhúng — ưu tiên xử lý offline. | Chỉ fallback sang cloud OCR khi người dùng đồng ý rõ ràng. |
| **brutalist-skill** | `industrial-brutalist-ui` | Frontend Specialized | SPECIALIZED | Chỉ dùng khi người dùng yêu cầu rõ hướng brutalist / công nghiệp / terminal quân sự / tactical telemetry. | Không phải lựa chọn mặc định cho frontend thông thường. |
| **minimalist-skill** | `minimalist-ui` | Frontend Specialized | SPECIALIZED | Chỉ dùng khi người dùng yêu cầu rõ hướng minimalist / warm monochrome / editorial / restrained. | Không phải lựa chọn mặc định cho frontend thông thường. |
| **gpt-tasteskill** | `gpt-taste` | Frontend Specialized | SPECIALIZED | Chỉ dùng khi người dùng yêu cầu rõ hướng Awwwards-style, GSAP-heavy, marketing thử nghiệm cao cấp. | Legacy reference; frontend tổng quát dùng `design-taste-frontend`. **Trigger đã được thu hẹp trong task này.** |
| **soft-skill** | `high-end-visual-design` | Frontend Specialized | SPECIALIZED | Chỉ dùng khi người dùng yêu cầu rõ hướng agency cao cấp / high-motion / cinematic marketing. | Legacy reference; frontend tổng quát dùng `design-taste-frontend`. **Trigger đã được thu hẹp trong task này.** |
| **image-to-code-skill** | `image-to-code` | Frontend Specialized | SPECIALIZED | Chỉ dùng khi người dùng cung cấp ảnh tham chiếu hoặc yêu cầu rõ workflow image-first. | Không kết hợp với skill thẩm mỹ khác trừ khi được yêu cầu. **Trigger đã được thu hẹp trong task này.** |
| **stitch-skill** | `stitch-design-taste` | Frontend Specialized | SPECIALIZED | Chỉ dùng cho Google Stitch / sinh file `DESIGN.md`. | Không dùng cho công việc frontend thông thường. |
| **output-skill** | `full-output-enforcement` | Documents / Output | SPECIALIZED | Chỉ kích hoạt khi người dùng yêu cầu rõ: full file, complete source, exhaustive/unabridged output, "no placeholders", "no truncation". | Không kích hoạt chỉ vì đang sinh code trong task coding/debug thông thường. **Trigger đã được thu hẹp trong task này.** |
| **taste-skill-v1** | `design-taste-frontend-v1` | Compatibility | DEPRECATED / COMPATIBILITY ONLY | Chỉ dùng khi một dự án cụ thể cần tương thích ngược chính xác với hành vi v1. | Không xóa, không archive, không tự động kích hoạt. **Không sửa trong task này.** |

## Routing principles

1. Chỉ dùng **một** skill thẩm mỹ (aesthetic skill) tại một thời điểm, trừ khi người dùng yêu cầu rõ kết hợp nhiều skill.
2. `taste-skill` (`design-taste-frontend`) là skill thiết kế frontend tổng quát mặc định.
3. Các skill thẩm mỹ chuyên biệt (brutalist, minimalist, gpt-tasteskill, soft-skill, stitch-skill) chỉ kích hoạt khi người dùng nêu rõ ý định đó.
4. `redesign-skill` được ưu tiên khi mục tiêu là cải thiện một giao diện đã tồn tại, không phải dựng mới.
5. `image-to-code-skill` yêu cầu có ảnh tham chiếu hoặc ý định image-first rõ ràng.
6. `output-skill` yêu cầu ý định "xuất đầy đủ / không cắt bớt" rõ ràng từ người dùng.
7. `setup-ai-brain` dành cho bootstrap/onboard dự án, không phải cho phát triển thông thường.
8. `taste-skill-v1` chỉ dùng cho tương thích ngược.
9. Không tự ý cài đặt dependency chỉ vì một skill có nhắc tới nó — luôn tuân theo quy tắc công cụ của workspace/dự án (`TOOLBOX.md`, `CLAUDE.md`) trước.

`TOOLBOX.md` vẫn là bộ định tuyến công cụ toàn cục. Repo này là **skill registry**, không phải bộ định tuyến tác vụ toàn cục.

## Đồng bộ với Codex

Kiểm tra thực tế thư mục `~/.codex/skills/` (2026-08-20): thư mục này hiện chỉ chứa `.system/` (các skill hệ thống của Codex: `imagegen`, `openai-docs`, `plugin-creator`, `review-agent`, `skill-creator`, `skill-installer`). **Không có bản sao hoặc symlink nào của các skill trong repo này** (`taste-skill`, `gpt-tasteskill`, `soft-skill`, v.v.) trong `~/.codex/skills/`.

Nói cách khác: hiện **không có đồng bộ tự động** giữa `skill-viphuong` và Codex. Nếu muốn dùng các skill này với Codex, cần copy/symlink thủ công vào `~/.codex/skills/` — đây không phải hành vi mặc định của repo.

## Dùng / khôi phục trên máy mới
```bash
git clone https://github.com/vi-phuong-158/skill-viphuong.git ~/.claude/skills
```
Sau khi clone, mọi skill tự động khả dụng trong Claude Code.
