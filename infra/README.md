# Camunda 8 cho demo IE203 – Vinmec

Docker Compose chạy Orchestration Cluster **8.9.30** (Zeebe, Operate, Tasklist
và Admin) với H2 lưu trên volume. Cấu hình dùng phần Orchestration Cluster
của [bản Docker Compose nhẹ chính thức của Camunda 8.9](https://docs.camunda.io/docs/8.9/self-managed/quickstart/developer-quickstart/docker-compose/).

## Khởi động và kiểm tra

Từ thư mục `infra/`, dùng Docker Compose v2.24 trở lên.

```bash
docker compose pull
docker compose up -d --wait
docker compose ps
curl --fail-with-body http://localhost:8080/v2/topology
```

Trên Windows PowerShell, dùng `curl.exe` thay cho `curl`.
`docker compose ps` hiển thị dịch vụ `camunda` ở trạng thái `healthy`.
API topology trả thông tin broker, partition và phiên bản cluster.

- **Web** ở cổng `8080` với [Operate](http://localhost:8080/operate),
  [Tasklist](http://localhost:8080/tasklist) và [Admin](http://localhost:8080/admin).
  Đăng nhập bằng `demo` / `demo`.
- **API local** gồm REST tại `http://localhost:8080/v2` và gRPC tại
  `localhost:26500`. Cả hai lắng nghe trên loopback và dùng được trực tiếp.

Xem log bằng `docker compose logs -f camunda`. Dừng demo bằng
`docker compose down` để giữ dữ liệu trong volume.

## Deploy BPMN

Mở hoặc tạo sơ đồ trên **Camunda 8** trong Camunda Desktop Modeler. Sơ đồ phải
có process thực thi được (`isExecutable="true"`) và tương thích Camunda 8.
Trong hộp thoại **Deploy**, chọn **Camunda 8 Self-Managed**, nhập Cluster URL
`http://localhost:8080/v2` và chọn **None** cho xác thực API local.

Có thể deploy trực tiếp qua REST. Từ `infra/`, thay đường dẫn mẫu bằng
đường dẫn đến file BPMN thực tế.

```bash
curl --fail-with-body -F "resources=@../bpmn/to-be/process.bpmn" http://localhost:8080/v2/deployments
```
