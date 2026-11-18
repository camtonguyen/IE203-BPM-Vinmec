# Hạ tầng Demo & Vận hành Quy trình Camunda (IE203 - Vinmec)

Thư mục này quản lý cấu hình hạ tầng container hóa và triển khai hệ thống BPMN Engine (Camunda 7 Run) phục vụ vận hành quy trình tại Bệnh viện Đa khoa Quốc tế Vinmec Central Park.

## Khởi động nhanh (Quick Start)

```bash
# Khởi động dịch vụ Camunda
docker compose up -d

# Xem logs hoạt động
docker compose logs -f

# Dừng hệ thống
docker compose down
```

- **Địa chỉ truy cập Web:** `http://localhost:8080` (Tài khoản mặc định: `demo` / `demo`)
- **Camunda REST API:** `http://localhost:8080/engine-rest`
- **Cơ chế triển khai:** Hỗ trợ deploy quy trình qua Camunda Modeler trực tiếp tới REST endpoint hoặc đưa file `.bpmn` vào thư mục nạp tài nguyên của engine.
