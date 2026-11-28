# IE203 – Phân tích quy trình khám ngoại trú tại Bệnh viện Vinmec

Đồ án môn **Hệ thống quản trị quy trình nghiệp vụ (IE203.G12)** – Trường ĐH Công nghệ Thông tin, ĐHQG TP.HCM.

**Đề tài:** Phân tích, mô hình hóa và cải tiến quy trình khám chữa bệnh ngoại trú tại Bệnh viện Đa khoa Quốc tế Vinmec (phạm vi khảo sát: Vinmec Central Park, TP.HCM).

## Thành viên

| MSSV | Họ tên | Email | Vai trò | Phụ trách chính |
|---|---|---|---|---|
| 26410134 | Nguyễn Thị Cẩm Tố | nguyenthicamto@gmail.com | Nhóm trưởng | C1, thời gian thực tế, to-be, ghép báo cáo Word |
| 26410092 | Huỳnh Duy Phúc | hdphuc201@gmail.com | Nhóm phó | C3, C4, M1, dashboard demo, theo dõi tiến độ |
| 26410095 | Qua Tú Phương | 26410095@ms.uit.edu.vn | Thành viên | Kiến trúc quy trình, journey map, slide |
| 26410086 | Đinh Hoàng Phát | hoangphat310304@gmail.com | Thành viên | S1–S3, CI, Camunda, mô phỏng |
| 26410042 | Nguyễn Quang Hòa | hoanqfpt@gmail.com | Thành viên | M1–M3, BPMN M3, định lượng (PM4Py), chi phí, review ký hiệu |
| 26410158 | Nguyễn Thị Tường Vy | nguyenthituongvy28122002@gmail.com | Thành viên | Phương pháp, phỏng vấn, biểu mẫu |

**Lịch:** 16/11/2026 – 14/12/2026 (hoàn thành trước 15/12/2026), 4 tuần.

Phân công chi tiết: xem file `PhanCong_DoAn_Vinmec.xlsx` (ngoài repo).

Tiến độ theo task: [GitHub Projects board](https://github.com/users/hdphuc201/projects/3)
(issue #N = task TN; PR ghi `Closes #N` để thẻ tự sang Hoàn thành).

## Cấu trúc thư mục

```
├── docs/            Mô tả 10 quy trình, thuật ngữ, kịch bản demo        (Rubric 1)
├── architecture/    Kiến trúc quy trình 3 tầng (draw.io + PNG)          (Rubric 1)
├── bpmn/            as-is/, to-be/ (.bpmn), png/                         (Rubric 2)
├── evidence/        Bằng chứng công khai, sơ đồ tổ chức, biểu mẫu        (Rubric 3)
├── interviews/      Bộ câu hỏi, biên bản (ẩn danh), khảo sát            (Rubric 3)
├── data/            event_log.csv, cost_rates.csv                       (Rubric 4)
├── analysis/        Định tính, định lượng (PM4Py), hình fishbone/Pareto (Rubric 4)
├── simulation/      Mô phỏng SimPy as-is vs to-be                       (Rubric 4)
├── infra/           docker-compose Camunda                               (Chương 7)
├── app/             Dashboard KPI + form demo (React)                    (Chương 8)
├── design/          Style guide, journey map, wireframe, infographic
├── report/          Báo cáo Word theo mẫu UIT                           (Rubric 5)
├── slides/          Slide thuyết trình                                   (Rubric 5)
├── meetings/        Biên bản họp tuần
├── members/         Nhật ký đóng góp của từng thành viên
└── scripts/         Công cụ kiểm tra (đếm gateway BPMN…)
```

## Quy ước làm việc

Xem [CONTRIBUTING.md](CONTRIBUTING.md). Tóm tắt:

- **Mỗi người commit ít nhất 1 lần mỗi tuần** (rubric: 3 tuần liên tiếp không hoạt động = 0đ).
- Commit bằng **đúng email đã khai trong form đăng ký**: `git config user.email "<email>"`.
- Làm trên nhánh riêng, mở Pull Request vào `main`, cần 1 người review.

## Chạy demo

```bash
docker compose -f infra/docker-compose.yml pull
docker compose -f infra/docker-compose.yml up -d --wait
docker compose -f infra/docker-compose.yml ps
python -m pip install -r requirements.txt
python scripts/test_env.py
python scripts/check_bpmn.py bpmn          # đếm gateway, kiểm tra split/join theo rubric
```

Mở Operate ở `http://localhost:8080/operate` hoặc Tasklist ở
`http://localhost:8080/tasklist` và đăng nhập bằng `demo` / `demo`.
REST API ở `http://localhost:8080/v2` và gRPC ở `localhost:26500`.
Deploy BPMN thực thi được trên Camunda 8 qua `POST /v2/deployments` hoặc
Camunda Desktop Modeler theo [hướng dẫn deploy](infra/README.md#deploy-bpmn).
Để chạy [notebook kiểm thử](analysis/test_environment.ipynb), chọn kernel Python
của môi trường đã cài `requirements.txt`.

## Bảo mật thông tin y tế

Không commit tên, chẩn đoán, ảnh chụp hay giấy tờ của người bệnh. Event log chỉ dùng mã lượt ẩn danh (L01, L02…). Ghi âm phỏng vấn **không** đưa lên repo, chỉ đưa biên bản đã ẩn danh.
