# Quy ước đóng góp

## 1. Cấu hình lần đầu
```bash
git clone https://github.com/camtonguyen/IE203-BPM-Vinmec.git
cd IE203-BPM-Vinmec
git config user.name  "Họ Tên"
git config user.email "email-đã-khai-trong-form"
```

| MSSV | Email commit (theo form) |
|---|---|
| 26410092 | hdphuc201@gmail.com |
| 26410134 | nguyenthicamto@gmail.com |
| 26410095 | 26410095@ms.uit.edu.vn |
| 26410086 | hoangphat310304@gmail.com |
| 26410042 | hoanqfpt@gmail.com |
| 26410158 | nguyenthituongvy28122002@gmail.com |

## 2. Nhánh
- `main`: bản đã review, không push trực tiếp.
- Nhánh làm việc: `<loại>/<mssv>-<mô-tả-ngắn>`, ví dụ `bpmn/26410134-c1-kham-ngoai-tru`.
- Loại: `docs`, `bpmn`, `research`, `analysis`, `infra`, `app`, `design`, `report`.

## 3. Commit message
`<loại>(<phạm vi>): <mô tả>` – ví dụ:
- `bpmn(C1): thêm nhánh hội chẩn chuyên khoa`
- `research(interviews): biên bản phỏng vấn điều dưỡng #2`
- `docs(M2): mô tả quy trình đánh giá KPI`

Ghi mã task (T01, T02…) trong file phân công vào mô tả PR.

## 4. Pull Request
- Mỗi PR gắn 1 task, có ít nhất 1 người review.
- File BPMN: CI tự đếm gateway; mục tiêu **> 7 gateway** và có **split & join** song song.
- Hình: tên hình đặt **dưới** hình, tên bảng đặt **trên** bảng (để ghép báo cáo không phải sửa).

## 5. Đặt tên file
- Quy trình: `docs/processes/C1-kham-ngoai-tru.md`
- BPMN: `bpmn/as-is/C1-kham-ngoai-tru.bpmn`, ảnh `bpmn/png/C1-kham-ngoai-tru.png`
- Biên bản: `interviews/notes/YYYY-MM-DD-<doi-tuong>-<so>.md`
