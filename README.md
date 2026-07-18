# skill-viphuong

Bộ skill cá nhân cho Claude Code của **Vi Ngọc Phương**.

Đây là bản sao có version-control của thư mục `~/.claude/skills/` — backup + lịch sử + đồng bộ giữa các máy.

## Skill hiện có
- **setup-ai-brain** — Khởi tạo "bộ não dự án" cho AI: tạo `CLAUDE.md`, `AGENTS.md` và `docs/brain/00-06` cho bất kỳ codebase nào. Đã tích hợp sẵn **Nguyên tắc Ponytail** trong template coding-rules.

### Bộ taste-skill (nguồn: [taste-skill repo](../../../04.%20Github/Tham%20Khao/taste-skill)) — cũng cài song song ở `~/.codex/skills/` để dùng chung với Codex
- **taste-skill** (`design-taste-frontend`) — Anti-Slop Frontend Skill: landing page, portfolio, redesign UI không bị "AI slop". Đọc brief, tự suy ra hướng thiết kế, audit-first khi redesign. Skill mặc định/flagship.
- **taste-skill-v1** (`design-taste-frontend-v1`) — Bản v1 gốc, giữ lại cho project cần tương thích ngược với v2.
- **brandkit** — Sinh brand-kit: logo system, guideline board, identity deck cao cấp.
- **brutalist-skill** (`industrial-brutalist-ui`) — UI brutalist/công nghiệp: grid cứng, kiểu terminal quân sự.
- **gpt-tasteskill** (`gpt-taste`) — UX/UI + GSAP motion nâng cao, layout AIDA, bento grid.
- **image-to-code-skill** (`image-to-code`) — Tự sinh ảnh thiết kế rồi code lại đúng như ảnh (tối ưu cho Codex).
- **imagegen-frontend-mobile** — Sinh ảnh concept màn hình app mobile (chỉ tạo ảnh, không code).
- **imagegen-frontend-web** — Sinh ảnh concept landing page, mỗi section một ảnh riêng.
- **minimalist-skill** (`minimalist-ui`) — UI tối giản, editorial, tông màu trầm.
- **output-skill** (`full-output-enforcement`) — Ép AI xuất code đầy đủ, cấm placeholder/rút gọn.
- **redesign-skill** (`redesign-existing-projects`) — Audit + nâng cấp thiết kế web/app cũ lên chuẩn cao cấp.
- **soft-skill** (`high-end-visual-design`) — Thiết kế kiểu agency cao cấp: font, spacing, shadow chuẩn.
- **stitch-skill** (`stitch-design-taste`) — Sinh file `DESIGN.md` cho Google Stitch.

## Dùng / khôi phục trên máy mới
```bash
git clone https://github.com/vi-phuong-158/skill-viphuong.git ~/.claude/skills
```
Sau khi clone, mọi skill tự động khả dụng trong Claude Code.
