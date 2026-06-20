# 05 — Testing & Deploy

> Mọi lệnh để dựng môi trường, chạy, test, build, deploy. Agent đọc đây thay vì đoán lệnh.

## Cài đặt môi trường local

<!-- Lệnh thật. Gồm cả tạo file .env nếu cần (chỉ liệt kê tên biến, không ghi giá trị). -->
```bash
{{LỆNH_CLONE_VÀ_CÀI_DEPS}}
```

Biến môi trường cần thiết (tạo file `.env`, không commit):
```
{{DANH_SÁCH_BIẾN_MÔI_TRƯỜNG}}
```

## Chạy local (dev)

```bash
{{LỆNH_CHẠY_DEV}}
```
Truy cập: {{URL_LOCAL}}

## Build (production)

```bash
{{LỆNH_BUILD}}
```

## Test

<!-- Nếu có test tự động, ghi lệnh. Nếu không, ghi checklist kiểm tra thủ công. -->
```bash
{{LỆNH_TEST}}
```

Checklist thủ công trước khi commit/push:
- [ ] {{KIỂM_TRA_1}}
- [ ] {{KIỂM_TRA_2}}

## Deploy

<!-- Deploy thế nào, trigger ra sao, môi trường nào. -->
{{HƯỚNG_DẪN_DEPLOY}}

## Môi trường

| Môi trường | Branch | URL |
|-----------|--------|-----|
| Production | {{BRANCH_PROD}} | {{URL_PROD}} |
| Local | — | {{URL_LOCAL}} |

## Lưu ý

<!-- Giới hạn quota, timeout, rate limit, chi phí, các bẫy khi chạy/deploy. -->
- {{LƯU_Ý}}
