# 01 — Architecture

## Stack

<!-- Bảng công nghệ theo từng tầng. Chỉ ghi cái đã xác minh từ file config/dependency. -->
| Layer | Công nghệ |
|-------|-----------|
| Frontend | {{FRONTEND}} |
| Backend | {{BACKEND}} |
| Database | {{DATABASE}} |
| Hạ tầng / Hosting | {{HOSTING}} |
| Khác | {{KHÁC}} |

## Cấu trúc thư mục chính

<!-- Cây thư mục rút gọn, kèm 1 dòng mô tả mỗi mục quan trọng. Bỏ node_modules/.git/dist. -->
```
{{CÂY_THƯ_MỤC}}
```

## Code Graph (bản đồ module)

> Mục quan trọng nhất. Agent đọc đây để biết "đụng vào X ảnh hưởng đâu" trước khi sửa.
> Cập nhật lại MỖI KHI thay đổi cấu trúc/quan hệ phụ thuộc.

### Module/file then chốt

<!-- 5-15 module quan trọng nhất. Điền từ việc quét import/require/include thực tế. -->
| Module / file | Vai trò | Được gọi bởi | Phụ thuộc vào |
|---------------|---------|--------------|---------------|
| {{FILE}} | {{VAI_TRÒ}} | {{AI_GỌI_NÓ}} | {{NÓ_GỌI_AI}} |

### Luồng xử lý chính

<!-- Sơ đồ mũi tên cho luồng quan trọng nhất, ví dụ request → handler → service → data. -->
```
{{LUỒNG_XỬ_LÝ}}
```

## Mô hình dữ liệu / API

<!-- Schema database, hoặc danh sách endpoint API chính, hoặc shape dữ liệu cốt lõi. -->
{{DATA_MODEL_HOẶC_API}}

## Biến môi trường

<!-- Chỉ liệt kê TÊN biến, KHÔNG ghi giá trị thật. -->
```
{{DANH_SÁCH_BIẾN_MÔI_TRƯỜNG}}
```

## Lưu ý kiến trúc quan trọng

<!-- Các điểm dễ vấp: cache, giới hạn, cold start, race condition, phần nợ kỹ thuật. -->
- {{LƯU_Ý}}
