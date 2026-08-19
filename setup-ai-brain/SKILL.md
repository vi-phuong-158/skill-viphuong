---
name: setup-ai-brain
description: >-
  Khởi tạo "bộ não dự án dùng chung" (shared AI project brain) cho Claude Code và Codex:
  tạo AGENTS.md, CLAUDE.md và docs/brain/00-06. Dùng skill này BẤT CỨ KHI NÀO người dùng
  muốn thiết lập bộ nhớ/ngữ cảnh dự án cho AI, "onboard" một codebase mới, tạo CLAUDE.md
  hoặc AGENTS.md, dựng docs/brain, lập "code graph"/bản đồ kiến trúc để AI đọc trước khi code,
  hoặc nói các câu như "set up bộ não dự án", "tạo brain", "init project memory", "thiết lập
  quy tắc cho AI agent", "khởi tạo dự án cho Claude/Codex". Kích hoạt cả khi người dùng chỉ
  mô tả ý định (muốn AI nhớ ngữ cảnh, muốn agent đọc tài liệu trước khi sửa code) mà không
  gọi đích danh tên file. KHÔNG kích hoạt chỉ vì một câu hỏi coding bình thường, hoặc vì dự án
  đã có sẵn AGENTS.md/CLAUDE.md chuẩn hóa và agent chỉ cần đọc ngữ cảnh có sẵn — chỉ dùng khi
  người dùng thực sự muốn khởi tạo/nâng cấp bộ tài liệu brain.
---

# Setup AI Project Brain

Mục tiêu: dựng một **bộ nhớ dự án dùng chung** để mọi AI agent (Claude Code, Codex) có cùng
ngữ cảnh và cùng quy tắc trước khi chạm vào code. Bộ này gồm 2 file hướng dẫn agent ở gốc repo
(`CLAUDE.md`, `AGENTS.md`) và 7 file tri thức trong `docs/brain/`.

Vì sao cần: AI agent mặc định không có trí nhớ giữa các phiên và dễ "code mù" — không nắm
kiến trúc, lặp lại sai lầm cũ, đổi stack tùy tiện. Bộ brain biến tri thức ngầm thành tài liệu
sống mà agent đọc trước khi code và cập nhật sau khi code.

## Khi nào dùng

- Bắt đầu một dự án mới, hoặc onboard một codebase đã có.
- Người dùng muốn AI "nhớ" ngữ cảnh, quy tắc, quyết định kỹ thuật giữa các phiên.
- Người dùng muốn agent đọc kiến trúc / code graph trước khi sửa.

## Quy trình

### Bước 1 — Khảo sát dự án trước khi viết gì

Đừng tạo template rỗng. Hãy đọc dự án để điền nội dung thật. Thu thập:

- Stack & công cụ: đọc `package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`,
  `Cargo.toml`, `pom.xml`, `Gemfile`… và file config (Dockerfile, vercel.json, CI yml).
- Cấu trúc thư mục: liệt kê cây thư mục (bỏ qua `node_modules`, `.git`, `dist`, `build`).
- Điểm vào & file quan trọng: entry points, file lớn nhất, file được import nhiều nhất.
- Tài liệu sẵn có: `README*`, `CONTRIBUTING*`, `CLAUDE.md`/`AGENTS.md` cũ, docs/.
- Lịch sử: `git log --oneline -15` để hiểu hướng đi gần đây.

Nếu dự án trống/mới tinh, hỏi người dùng vài câu ngắn: mục tiêu, người dùng chính, stack dự kiến.

### Bước 2 — Xử lý file đã tồn tại (an toàn)

Nếu `CLAUDE.md`, `AGENTS.md` hoặc `docs/brain/` đã có:

- KHÔNG ghi đè mù. Đọc nội dung cũ trước.
- Nếu nội dung cũ có giá trị → hợp nhất (giữ quy tắc riêng của dự án, thêm phần còn thiếu).
- Nếu chỉ là bản mặc định/rỗng → thay bằng bản mới.
- Khi không chắc, hỏi người dùng: ghi đè, hợp nhất, hay bỏ qua từng file.

### Bước 3 — Tạo file từ template

Các template nằm trong `assets/` của skill này. Với mỗi file: đọc template tương ứng, thay
mọi `{{PLACEHOLDER}}` bằng thông tin thật đã khảo sát ở Bước 1, xóa các chú thích hướng dẫn
dạng `<!-- ... -->`, rồi ghi ra đúng đường dẫn.

| Template (trong skill) | Ghi ra (trong dự án) |
|------------------------|----------------------|
| `assets/CLAUDE.md.template` | `CLAUDE.md` |
| `assets/AGENTS.md.template` | `AGENTS.md` |
| `assets/brain/00-project-overview.md` | `docs/brain/00-project-overview.md` |
| `assets/brain/01-architecture.md` | `docs/brain/01-architecture.md` |
| `assets/brain/02-coding-rules.md` | `docs/brain/02-coding-rules.md` |
| `assets/brain/03-decisions.md` | `docs/brain/03-decisions.md` |
| `assets/brain/04-current-tasks.md` | `docs/brain/04-current-tasks.md` |
| `assets/brain/05-testing-and-deploy.md` | `docs/brain/05-testing-and-deploy.md` |
| `assets/brain/06-ai-working-log.md` | `docs/brain/06-ai-working-log.md` |

Quy tắc điền nội dung:
- Chỉ ghi điều bạn xác minh được từ dự án. Không bịa. Nếu chưa biết, để mục đó với ghi chú
  `_(cần bổ sung)_` thay vì đoán.
- Giữ ngôn ngữ của người dùng (mặc định tiếng Việt nếu dự án/giao tiếp bằng tiếng Việt).

### Bước 4 — Dựng Code Graph (bản đồ module)

Đây là phần giá trị nhất và hay bị bỏ qua. Trong `docs/brain/01-architecture.md` có mục
**Code Graph** — điền nó bằng cách quét quan hệ phụ thuộc thật:

- Tìm import/require/include giữa các file nguồn để biết module nào gọi module nào.
- Ghi lại 5–15 module/quan trọng nhất kèm: vai trò, ai gọi nó, nó gọi ai.
- Mô tả luồng xử lý chính (request → handler → service → data) bằng sơ đồ mũi tên đơn giản.

Mục tiêu: agent đời sau đọc Code Graph là hiểu ngay "đụng vào X thì ảnh hưởng Y, Z" mà không
phải đọc lại cả repo.

### Bước 5 — Phần "Cài đặt" và "Đọc Code Graph" trong CLAUDE.md & AGENTS.md

Hai template `CLAUDE.md`/`AGENTS.md` đã có sẵn:
- Mục **Cài đặt nhanh** trỏ tới `docs/brain/05-testing-and-deploy.md` — điền lệnh cài đặt thật.
- Quy tắc bắt buộc **đọc Code Graph trong `01-architecture.md` trước khi code**, và **cập nhật
  lại Code Graph khi thay đổi cấu trúc**. Giữ nguyên các quy tắc này.

### Bước 6 — Báo cáo

Liệt kê các file đã tạo/cập nhật (dạng cây), nêu ngắn gọn những gì đã điền và mục nào còn
`_(cần bổ sung)_` để người dùng hoàn thiện.

## Nguyên tắc

- Đơn giản trước: bộ brain là tài liệu, không phải code. Đừng thêm script/automation trừ khi
  người dùng yêu cầu.
- Trung thực: thà ghi "cần bổ sung" còn hơn điền thông tin sai — vì agent sau sẽ tin tài liệu này.
- Phẫu thuật: không động vào code dự án ở bước setup; chỉ tạo tài liệu.
