# skill-viphuong

Bộ skill cá nhân cho Claude Code của **Vi Ngọc Phương**.

Đây là bản sao có version-control của thư mục `~/.claude/skills/` — backup + lịch sử + đồng bộ giữa các máy.

## Skill hiện có
- **setup-ai-brain** — Khởi tạo "bộ não dự án" cho AI: tạo `CLAUDE.md`, `AGENTS.md` và `docs/brain/00-06` cho bất kỳ codebase nào. Đã tích hợp sẵn **Nguyên tắc Ponytail** trong template coding-rules.
- **taste-skill** (`design-taste-frontend`) — Anti-Slop Frontend Skill: landing page, portfolio, redesign UI không bị "AI slop". Đọc brief, tự suy ra hướng thiết kế, audit-first khi redesign. Nguồn: [taste-skill repo](../../../04.%20Github/Tham%20Khao/taste-skill). Cũng đã cài ở `~/.codex/skills/taste-skill/` để dùng chung với Codex.

## Dùng / khôi phục trên máy mới
```bash
git clone https://github.com/vi-phuong-158/skill-viphuong.git ~/.claude/skills
```
Sau khi clone, mọi skill tự động khả dụng trong Claude Code.
