# Hạ tầng Demo & Vận hành Quy trình Camunda (IE203 - Vinmec)

Thư mục này quản lý cấu hình hạ tầng container hóa và triển khai hệ thống BPMN Engine (Camunda 7 Run) phục vụ demo quy trình To-Be tại Bệnh viện Vinmec Central Park.

## Khởi động nhanh (Quick Start)

```bash
# Khởi động dịch vụ Camunda
docker compose up -d

# Xem logs hoạt động
docker compose logs -f

# Dừng hệ thống
docker compose down
```

- **Địa chỉ truy cập Web:** `http://localhost:8080` (Tài khoản: `demo` / `demo`)
- **Camunda REST API:** `http://localhost:8080/engine-rest`
- **Tự động deploy BPMN:** Đặt file `.bpmn` vào thư mục `infra/camunda/deployments/` hoặc chạy `python scripts/deploy_camunda.py <file.bpmn>`.

Xem tài liệu hướng dẫn vận hành chi tiết tại: [camunda/README.md](camunda/README.md).
