# 02 — Coding Rules

## Nguyên tắc chung

- Viết ít nhất có thể để giải quyết đúng task. Không tính năng speculative.
- Không abstraction sớm: 3 đoạn lặp vẫn tốt hơn 1 abstraction non.
- Không xử lý lỗi cho kịch bản không thể xảy ra.
- Comment WHY, không comment WHAT — tên biến/hàm đã nói WHAT.
- Không refactor code lân cận nếu không liên quan task.

## Nguyên tắc Ponytail ("senior dev lười hiệu quả")

> LUÔN có hiệu lực, trừ khi người dùng nói **"tắt ponytail"** / **"normal mode"**.
> Lười = hiệu quả, không phải cẩu thả. Code tốt nhất là code không cần viết.

### Thang quyết định — dừng ở nấc đầu tiên thỏa mãn
1. Việc này có cần tồn tại không? Nhu cầu suy diễn → bỏ qua, nói rõ 1 dòng. (YAGNI)
2. Thư viện chuẩn (stdlib) làm được? → Dùng nó.
3. Tính năng có sẵn của nền tảng phủ được? → Dùng (ràng buộc DB thay vì code, CSS thay vì JS).
4. Dependency đã cài giải quyết được? → Dùng. KHÔNG thêm thư viện mới cho việc vài dòng.
5. Gói trong 1 dòng được? → Một dòng.
6. Chỉ khi đó: viết lượng code tối thiểu chạy được.

### Quy tắc
- Không abstraction khi chưa được yêu cầu: không interface cho 1 implementation, không factory cho 1 sản phẩm, không config cho giá trị không bao giờ đổi.
- Không boilerplate, không scaffolding "để dành sau".
- Ưu tiên xóa hơn thêm. Đơn giản hơn "thông minh". Ít file nhất, diff ngắn nhất.
- Đánh dấu mọi đơn giản hóa có chủ đích bằng comment `ponytail:` kèm đường nâng cấp.
  Ví dụ: `# ponytail: khóa toàn cục — chuyển sang khóa theo tài khoản nếu cần thông lượng cao`

### TUYỆT ĐỐI KHÔNG được "lười" ở
- Validation dữ liệu đầu vào ở ranh giới tin cậy.
- Xử lý lỗi để tránh mất dữ liệu.
- Các biện pháp bảo mật.
- Bất cứ thứ gì người dùng yêu cầu rõ ràng.
- Logic không tầm thường (nhánh, vòng lặp, parser, đường tiền/bảo mật) → để lại ÍT NHẤT 1 kiểm tra chạy được (assert hoặc test nhỏ).

### Đầu ra
Code trước. Sau đó tối đa 3 dòng: bỏ gì, khi nào nên thêm. Không viết văn dài.

## Style code

<!-- Suy ra từ code hiện tại: ngôn ngữ, format, quy ước. Khớp với linter/formatter nếu có. -->
- Ngôn ngữ / runtime: {{NGÔN_NGỮ}}
- Format: {{INDENT_VÀ_QUY_ƯỚC}}
- Linter / formatter: {{LINTER}}

## Đặt tên

<!-- Quy ước đặt tên thực tế của dự án. -->
- {{QUY_ƯỚC_ĐẶT_TÊN}}

## Bảo mật

<!-- Điều chỉnh theo dự án; đây là các mục mặc định an toàn. -->
- Không hardcode secret/API key — dùng biến môi trường.
- Sanitize và validate mọi input từ người dùng, đặc biệt ở backend.
- Không tin client; kiểm tra phía server.
- Không commit file `.env` hay credential.
- Không log dữ liệu nhạy cảm.
- {{QUY_TẮC_BẢO_MẬT_RIÊNG}}

## Không làm

- {{ĐIỀU_CẤM_RIÊNG_CỦA_DỰ_ÁN}}

## Test

<!-- Cách kiểm tra thay đổi. Nếu chưa có test tự động, ghi rõ checklist thủ công. -->
{{CÁCH_TEST}}

## Git

- Branch từ nhánh chính, đặt tên rõ: `feat/...`, `fix/...`, `docs/...`.
- Commit message ngắn gọn, format: `type: short description`.
- Không push thẳng nhánh chính nếu chưa được yêu cầu.
- Không `--force` push trừ khi được yêu cầu rõ ràng.
