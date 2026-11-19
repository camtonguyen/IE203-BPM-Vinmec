# Kế hoạch tổng – IE203 Vinmec (khám ngoại trú)

> Người lập: Nguyễn Thị Cẩm Tố (26410134, nhóm trưởng). Số liệu **tính lại từ** Google Sheet phân công của nhóm (61 task, 190 giờ); nếu sheet đổi thì tính lại và cập nhật file này.

## 1. Mốc thời gian

- Bắt đầu: thứ Hai 16/11/2026. Hạn chót hoàn thành mọi task: **14/12/2026**; nộp trước 15/12/2026.
- Mỗi người có ≥ 1 task mỗi tuần để luôn có commit (rubric: 3 tuần liên tiếp không hoạt động = 0đ).

| Tuần | Từ | Đến | Trọng tâm |
|---|---|---|---|
| 1 | 16/11 | 22/11 | Repo, CI, bằng chứng, mô tả quy trình, bộ câu hỏi, template báo cáo |
| 2 | 23/11 | 29/11 | Phỏng vấn, khảo sát, ghi thời gian thực tế, journey map, BPMN C1 và M3 |
| 3 | 30/11 | 06/12 | BPMN C3, M1, S1, S3, review ký hiệu, VA/BVA/NVA, fishbone/Pareto, định lượng, to-be |
| 4 | 07/12 | 13/12 | Mô phỏng, Camunda, dashboard, chi phí, các chương, ghép Word, slide, tập thuyết trình |

## 2. Giờ theo người và theo tuần

| Tuần | Tố | Phúc | Phương | Phát | Hòa | Vy | Tổng |
|---|---|---|---|---|---|---|---|
| 1 | 8 | 9 | 9 | 10 | 9 | 13 | 58 |
| 2 | 9 | 4.5 | 9 | 3 | 4.5 | 8 | 38 |
| 3 | 4 | 8.5 | 2 | 6 | 13 | 9 | 42.5 |
| 4 | 14 | 11.5 | 9 | 11 | 3 | 3 | 51.5 |
| **Tổng** | **35** | **33.5** | **29** | **30** | **29.5** | **33** | **190** |

## 3. Hạng mục rubric và người chịu trách nhiệm

Giờ cộng theo người phụ trách chính.

| Hạng mục | Số task | Giờ | Người (giờ) |
|---|---|---|---|
| 0. Quản lý dự án | 11 | 22 | Phát 9, Phúc 7.5, Tố 5, Hòa 0.5 |
| 1. Liệt kê quy trình | 8 | 22 | Phúc 6, Phương 5, Hòa 4, Phát 4, Tố 3 |
| 2. Mô hình hóa | 7 | 25 | Hòa 7, Phúc 7, Phát 6, Tố 5 |
| 3. Phương pháp | 10 | 34 | Vy 24, Phương 5, Phúc 3, Phát 2 |
| 4. Phân tích | 14 | 51 | Hòa 14, Tố 12, Phát 9, Vy 6, Phúc 6, Phương 4 |
| 5. Trình bày – Báo cáo | 11 | 36 | Phương 15, Tố 10, Hòa 4, Phúc 4, Vy 3 |

## 4. Task theo tuần

### Tuần 1

| ID | Hạn | Công việc | Phụ trách | Hỗ trợ | Giờ |
|---|---|---|---|---|---|
| T01 | 22/11 | Đổi tên repo, dựng cấu trúc thư mục, README, mời thành viên, bật bảo vệ nhánh main | Tố | Phát | 2 |
| T02 | 22/11 | Lập kế hoạch tổng, chốt phân công; tạo template báo cáo Word theo mẫu UIT | Tố |  | 3 |
| T03 | 22/11 | Tạo GitHub Projects board, issue template, quy ước commit | Phúc |  | 1.5 |
| T04 | 22/11 | Thiết lập CI (kiểm tra file .bpmn hợp lệ, kiểm tra link) và docker-compose cho Camunda | Phát |  | 4 |
| T05 | 22/11 | Thu thập bằng chứng công khai: quy trình khám, BHYT, bảng giá, app My Vinmec (ảnh chụp + URL + ngày truy cập) | Vy | Phương | 4 |
| T06 | 22/11 | Dựng sơ đồ tổ chức Vinmec (website, tin tuyển dụng) | Vy |  | 3 |
| T07 | 22/11 | Bảng thuật ngữ và viết tắt | Phát |  | 2 |
| T08 | 22/11 | Style guide hình ảnh: màu, font, mẫu sơ đồ, mẫu slide | Phương |  | 4 |
| T09 | 22/11 | Cấu hình git email đúng như form; đọc kế hoạch; commit đầu tiên | Hòa |  | 0.5 |
| T10 | 22/11 | Họp tiến độ tuần, cập nhật board, nhắc thành viên chưa commit | Phúc |  | 1.5 |
| T11 | 22/11 | Mô tả C1 Khám ngoại trú (actor, bước, khách hàng, kết quả) | Tố |  | 3 |
| T12 | 22/11 | Mô tả M3 Quản lý sự cố y khoa | Hòa |  | 2 |
| T13 | 22/11 | Mô tả C3 Thanh toán, bảo lãnh bảo hiểm và C4 Đặt lịch | Phúc |  | 4 |
| T14 | 22/11 | Mô tả C2 Cận lâm sàng | Phương |  | 2 |
| T15 | 22/11 | Mô tả M1 Lập lịch bác sĩ và M2 Đánh giá KPI | Hòa |  | 2 |
| T16 | 22/11 | Mô tả S1 Cấp phát thuốc, S2 Tuyển dụng, S3 Khiếu nại | Phát |  | 4 |
| T17 | 22/11 | Vẽ kiến trúc quy trình 3 tầng (draw.io) | Phương | Phúc | 3 |
| T18 | 22/11 | Bộ ≥24 câu phỏng vấn (10 định tính, 10 định lượng, dự phòng), kịch bản, mẫu biên bản | Vy | Phương | 4 |
| T19 | 22/11 | Google Form khảo sát người bệnh | Vy |  | 2 |
| T20 | 22/11 | Mẫu event log CSV và hướng dẫn ghi thời gian | Hòa |  | 1.5 |
| T21 | 22/11 | Viết chương Giới thiệu doanh nghiệp và phạm vi đề tài | Hòa |  | 3 |
| T22 | 22/11 | Review chéo 10 mô tả quy trình theo rubric | Phúc |  | 2 |

### Tuần 2

| ID | Hạn | Công việc | Phụ trách | Hỗ trợ | Giờ |
|---|---|---|---|---|---|
| T23 | 29/11 | Họp tiến độ tuần, cập nhật board, nhắc thành viên chưa commit | Phúc |  | 1.5 |
| T24 | 29/11 | Phỏng vấn bác sĩ, điều dưỡng (2–3 người), ghi âm có xin phép | Vy | Phương | 5 |
| T25 | 29/11 | Phỏng vấn thu ngân / bộ phận bảo hiểm | Phúc |  | 3 |
| T26 | 29/11 | Phỏng vấn người bệnh + phát khảo sát (mục tiêu ≥30 phản hồi) | Phương | Vy | 5 |
| T27 | 29/11 | Ghi nhận thời gian thực tế ≥3 lượt khám → event_log.csv (ẩn danh) | Tố | Cả nhóm | 4 |
| T28 | 29/11 | Customer journey map của người bệnh (điểm đau) | Phương |  | 4 |
| T29 | 29/11 | Tổng hợp, chuẩn hóa biên bản phỏng vấn | Vy |  | 3 |
| T30 | 29/11 | Dựng Camunda local, môi trường Python (PM4Py, SimPy), notebook mẫu | Phát |  | 3 |
| T31 | 29/11 | Tra đơn giá nhân công (tin tuyển dụng) và bảng giá dịch vụ, ghi nguồn | Hòa |  | 1.5 |
| T32 | 29/11 | BPMN C1 Khám ngoại trú (≥8 gateway, có split/join) | Tố |  | 5 |
| T33 | 29/11 | BPMN M3 Quản lý sự cố y khoa | Hòa |  | 3 |

### Tuần 3

| ID | Hạn | Công việc | Phụ trách | Hỗ trợ | Giờ |
|---|---|---|---|---|---|
| T34 | 06/12 | Họp tiến độ tuần, cập nhật board, nhắc thành viên chưa commit | Phúc |  | 1.5 |
| T35 | 06/12 | BPMN C3 Thanh toán, bảo lãnh bảo hiểm | Phúc |  | 4 |
| T36 | 06/12 | BPMN M1 Lập lịch bác sĩ | Phúc |  | 3 |
| T37 | 06/12 | BPMN S1 Cấp phát thuốc và S3 Khiếu nại | Phát |  | 6 |
| T38 | 06/12 | Review chéo BPMN của Phúc và Phát | Hòa |  | 2 |
| T39 | 06/12 | Review ký hiệu BPMN toàn bộ theo checklist lỗi (−0,25đ/lỗi) | Hòa |  | 2 |
| T40 | 06/12 | Vẽ lại biểu mẫu (phiếu đăng ký khám, phiếu yêu cầu dịch vụ, bảng kê…) | Vy |  | 3 |
| T41 | 06/12 | Chuẩn hóa style và xuất PNG cho 6 sơ đồ | Phương |  | 2 |
| T42 | 06/12 | Phân tích VA/BVA/NVA và lãng phí cho C1, C3 | Hòa | Tố | 4 |
| T43 | 06/12 | Fishbone + Pareto | Vy | Phương | 3 |
| T44 | 06/12 | Định lượng thời gian, chất lượng (PM4Py trên event log) | Hòa |  | 5 |
| T45 | 06/12 | Thiết kế to-be C1, C3 theo heuristic chương 6 | Tố | Phúc | 4 |
| T46 | 06/12 | Thiết kế UI dashboard KPI (wireframe) | Vy |  | 3 |

### Tuần 4

| ID | Hạn | Công việc | Phụ trách | Hỗ trợ | Giờ |
|---|---|---|---|---|---|
| T47 | 13/12 | Họp tiến độ tuần, cập nhật board, nhắc thành viên chưa commit | Phúc |  | 1.5 |
| T48 | 13/12 | Định lượng chi phí mỗi lượt khám | Hòa |  | 2 |
| T49 | 13/12 | Mô phỏng SimPy as-is vs to-be | Phát | Tố | 4 |
| T50 | 13/12 | Deploy C1 to-be lên Camunda (Docker) | Phát | Tố | 5 |
| T51 | 13/12 | Viết chương Phân tích quy trình (định tính + định lượng) | Tố |  | 4 |
| T52 | 13/12 | Thiết kế hình minh họa so sánh as-is / to-be cho báo cáo và slide | Phương |  | 3 |
| T53 | 13/12 | Xây dashboard KPI + form task demo (React) | Phúc |  | 6 |
| T54 | 13/12 | Ghép báo cáo Word: mục lục, mục lục hình/bảng, viết tắt, tài liệu tham khảo | Tố | Phúc | 8 |
| T55 | 13/12 | Viết chương Phương pháp thực hiện | Vy |  | 3 |
| T56 | 13/12 | Slide thuyết trình (1–3 quy trình BPMN) | Phương | Vy | 6 |
| T57 | 13/12 | Kịch bản demo Camunda + dashboard | Phúc |  | 2 |
| T58 | 13/12 | Soát chính tả, định dạng (tên bảng trên, tên hình dưới) | Phúc |  | 2 |
| T59 | 13/12 | Đóng gói demo: docker compose up 1 lệnh, hướng dẫn trong README | Phát |  | 2 |
| T60 | 13/12 | Tập thuyết trình có bấm giờ, bật camera | Tố | Cả nhóm | 2 |
| T61 | 13/12 | Review lần cuối báo cáo và BPMN | Hòa |  | 1 |

## 5. Rủi ro

| Rủi ro | Ảnh hưởng | Giảm thiểu |
|---|---|---|
| T27 cần số liệu quan sát thực tế (≥ 3 lượt), chưa có thì T32, T44, T49, T51 không có số | Mất điểm Phân tích | Lên lịch quan sát ngay tuần 2; xin phép Chăm sóc khách hàng trước; tối thiểu 3 lượt, mục tiêu nhiều hơn |
| T50 Camunda: mô hình to-be không chạy được | Không demo được | Deploy thử sớm bằng `infra/` (Docker); giữ BPMN to-be trong tập phần tử Camunda 7 hỗ trợ |
| 3 tuần liên tiếp không có commit | 0 điểm GitHub | Mỗi người có task mỗi tuần (bảng 2); nhóm trưởng kiểm tra commit cuối mỗi tuần |
| Tuần 4 dồn 51,5 giờ, ghép Word (T54) sát hạn | Trễ nộp | Chương viết xong và merge trước 10/12; T54 chỉ ghép |
| Lộ dữ liệu người bệnh (tên, chẩn đoán, ảnh) | Vi phạm quy định rubric | Event log chỉ mã `Lxx`; review PR kiểm tra; CI chặn file âm thanh |
| Số liệu lệch giữa các chương | Báo cáo thiếu nhất quán | Mọi số truy được về `data/`, `analysis/`, `simulation/`; sửa ở nguồn, không sửa tay trong chương |
| Thuyết trình quá giờ | −1 điểm mỗi 5 phút quá | T60 tập có bấm giờ, bật camera |
