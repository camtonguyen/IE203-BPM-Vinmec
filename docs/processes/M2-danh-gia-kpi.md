# M2 – Đánh giá KPI (chất lượng khám ngoại trú)

- **Loại:** Quản lý
- **Người phụ trách viết:** Nguyễn Quang Hòa (26410042)
- **Phạm vi:** đo lường, đánh giá và cải tiến các chỉ số hiệu suất (KPI) của khu khám ngoại trú theo kỳ (tháng / quý /
  6 tháng): từ thu thập dữ liệu đến báo cáo, so sánh mục tiêu và giao kế hoạch cải tiến. KPI ở đây là **chỉ số chất lượng
  dịch vụ của khoa/bệnh viện**; đánh giá KPI cá nhân nhân viên Vinmec không có nguồn công khai nên chỉ nêu ở mức ⚠.
- **Nguồn bằng chứng** (truy cập 17/11/2026):
  1. Thông tư 19/2013/TT-BYT – quản lý chất lượng dịch vụ khám chữa bệnh tại bệnh viện (Điều 5: xây dựng và đo lường bộ
     chỉ số chất lượng; Điều 10–12: Hội đồng QLCL, phòng QLCL):
     https://caselaw.vn/van-ban-phap-luat/265779-thong-tu-19-2013-tt-byt-huong-dan-thuc-hien-quan-ly-chat-luong-dich-vu-kham-chua-benh-tai-benh-vien-do-bo-truong-bo-y-te-ban-hanh
  2. Quyết định 6858/QĐ-BYT ngày 18/11/2016 – Bộ tiêu chí chất lượng bệnh viện Việt Nam (83 tiêu chí; A1.3, A1.5, A4.6,
     D2.2, D3.2):
     https://caselaw.vn/van-ban-phap-luat/138727-quyet-dinh-6858-qd-byt-nam-2016-ve-bo-tieu-chi-chat-luong-benh-vien-viet-nam-do-bo-truong-bo-y-te-ban-hanh
  3. Quyết định 3652/QĐ-BYT ngày 03/12/2024 – kiểm tra, đánh giá chất lượng bệnh viện 2024–2025 (khảo sát hài lòng người
     bệnh ngoại trú theo QĐ 56/QĐ-BYT/2024):
     https://kcb.vn/upload/2005611/20241206/3652-qdbyt_signed_61852.pdf
  4. Quyết định 3869/QĐ-BYT ngày 28/8/2019 – mẫu phiếu khảo sát hài lòng (Mẫu 2: người bệnh ngoại trú, 5 nhóm, thang 5 mức):
     https://hethongphapluat.com/decision-no-3869-qd-byt-dated-august-28-2019-on-issuance-of-forms-and-guidance-on-patient-and-health-worker-satisfaction-survey.html
  5. Luật Thời đại – *Hệ thống y tế Vinmec: Vị thế mới cho Việt Nam trên bản đồ y tế thế giới* (10/11/2025; Vinmec đo PROM,
     đo hài lòng tại nhiều điểm chạm, mô hình y học dựa trên giá trị):
     https://lsvn.vn/he-thong-y-te-vinmec-vi-the-moi-cho-viet-nam-tren-ban-do-y-te-the-gioi-a165812.html
  6. Vinmec – *Tầm nhìn và sứ mệnh* (công bố NES 85%; bản lưu 25/01/2026):
     https://www.vinmec.com/vie/tam-nhin-va-su-menh
  7. Pháp luật TP.HCM – *Vinmec Central Park … chứng chỉ JCI lần thứ 3* (01/04/2024; chỉ số nhiễm khuẩn, sai sót thuốc):
     https://plo.vn/vinmec-central-park-xuat-sac-dat-dau-vang-chat-luong-chung-chi-jci-lan-thu-3-post783150.html
  8. Phỏng vấn bác sĩ, điều dưỡng, thu ngân (T24, T25) – *chưa thực hiện*.

> Mục đánh dấu **⚠** là suy luận theo khung Thông tư 19 / QĐ 6858, cần xác minh qua phỏng vấn
> (câu 5, 15, 16, 17, 20 trong `interviews/questions.md`).

## Bộ KPI đề xuất cho khu khám ngoại trú

Bảng 1 dùng làm danh mục chỉ số cho M2 và cho dashboard (T46, T53). Mục tiêu cụ thể của Vinmec chưa có nguồn ⚠.

| Nhóm | KPI | Cách tính | Nguồn dữ liệu | Căn cứ |
|---|---|---|---|---|
| Thời gian | Thời gian chờ khám | Từ tiếp đón đến khi được gọi vào khám (phút) | Event log / HIS | [2] A1.3, A1.5 |
| Thời gian | Tổng thời gian một lượt khám | Từ tiếp đón đến khi rời bệnh viện (phút) | Event log | [2] A1.3 |
| Thời gian | Thời gian trả kết quả cận lâm sàng | Từ lấy mẫu đến có kết quả (phút) | LIS / RIS ⚠ | [2] |
| Thời gian | Thời gian chờ duyệt bảo lãnh | Từ gửi yêu cầu đến có phản hồi (phút) | Quầy bảo hiểm | C3 |
| Hài lòng | Tỉ lệ hài lòng người bệnh ngoại trú | % phiếu mức 4–5 | Khảo sát theo QĐ 56/2024 | [3][4] |
| Hài lòng | NES (Net Excellence Score) | Theo phương pháp Vinmec ⚠ | Khảo sát Vinmec | [6] |
| Hài lòng | Số khiếu nại / 1.000 lượt khám | | S3 | [2] |
| An toàn | Số sự cố y khoa / 1.000 lượt khám, tỉ lệ near-miss | | M3 | [2] D2.2 |
| An toàn | Tỉ lệ RCA hoàn thành trong 60 ngày | | M3 | TT 43/2018 |
| Hiệu suất | Số lượt khám / bác sĩ / buổi | | HIS, lịch M1 | |
| Hiệu suất | Tỉ lệ lấp đầy khung giờ hẹn; tỉ lệ không đến (no-show) | | Hệ thống đặt lịch (C4) | |
| Tài chính | Doanh thu, chi phí trung bình / lượt khám | | Thu ngân (C3), T48 | |

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Phòng / Tổ Quản lý chất lượng | Đầu mối: xây dựng bộ chỉ số, thu thập, tổng hợp, phân tích, báo cáo [1, Điều 5, 12] |
| Hội đồng QLCL (Giám đốc làm chủ tịch) | Xem xét kết quả, phê duyệt mục tiêu và đề án cải tiến [1, Điều 10–11] |
| Trưởng khoa khám bệnh, các trưởng khoa liên quan | Cung cấp dữ liệu, giải trình chỉ số không đạt, thực hiện kế hoạch cải tiến ⚠ |
| Mạng lưới QLCL ở các khoa | Thu thập số liệu tại khoa, phát phiếu khảo sát ⚠ [1, Điều 10] |
| Phòng CNTT / hệ thống HIS | Trích xuất dữ liệu thời gian, lượt khám, doanh thu [1, Điều 5] ⚠ |
| CSKH | Khảo sát hài lòng, tổng hợp phản hồi, khiếu nại ⚠ |
| Người bệnh | Trả lời phiếu khảo sát hài lòng [4] |
| Bộ Y tế / Sở Y tế, JCI *(bên ngoài)* | Nhận kết quả khảo sát (chatluongbenhvien.vn) và đánh giá chất lượng hằng năm [3]; JCI thẩm định 3 năm/lần ⚠ |

## Khách hàng của quy trình

- **Chính:** Ban giám đốc, Hội đồng QLCL (ra quyết định cải tiến dựa trên số liệu).
- **Nội bộ:** các khoa (biết mình đang ở đâu so với mục tiêu).
- **Bên ngoài:** Bộ Y tế, Sở Y tế (đánh giá chất lượng bệnh viện), tổ chức JCI; gián tiếp là người bệnh (dịch vụ được cải tiến).

## Các bước (mô tả bằng lời)

**A. Chuẩn bị (đầu năm / đầu kỳ)**

1. Phòng QLCL **rà soát bộ chỉ số** theo Bộ tiêu chí 6858, yêu cầu JCI và chiến lược bệnh viện; đề xuất mục tiêu cho từng
   KPI [1, Điều 5][2] ⚠.
2. Hội đồng QLCL **phê duyệt** bộ chỉ số và mục tiêu ⚠.

**B. Thu thập dữ liệu** (song song)

3. Trích xuất **dữ liệu hệ thống** (HIS, đặt lịch, thu ngân): lượt khám, thời gian từng phân đoạn, doanh thu ⚠.
4. **Khảo sát hài lòng** người bệnh ngoại trú theo mẫu và cỡ mẫu quy định [3][4]
   (500–4.999 lượt/ngày → ≥ 200 phiếu; 100–499 lượt/ngày → ≥ 100 phiếu [4]).
5. Lấy **số liệu sự cố** từ M3 và **khiếu nại** từ S3.

**C. Phân tích, đánh giá**

6. QLCL **làm sạch, tính toán** KPI; kiểm tra số liệu bất thường, thiếu → yêu cầu khoa bổ sung ⚠.
7. **So sánh với mục tiêu** và với kỳ trước; vẽ biểu đồ theo dõi thời gian chờ theo tuần/tháng [2] ⚠.
8. Với KPI **không đạt**: trưởng khoa giải trình, phân tích nguyên nhân (fishbone, Pareto) ⚠.

**D. Báo cáo, cải tiến**

9. QLCL lập **báo cáo** gửi Hội đồng QLCL / Ban giám đốc; công khai thời gian chờ [2] ⚠.
10. Hội đồng **quyết định**: duy trì, hoặc giao **kế hoạch / đề án cải tiến** (PDCA) cho khoa [1, Điều 11] ⚠.
11. Khoa **thực hiện cải tiến**; QLCL **theo dõi** ở kỳ sau (quay lại bước 3).
12. Định kỳ: nộp kết quả **tự đánh giá chất lượng** và khảo sát hài lòng cho Bộ Y tế / Sở Y tế [3].

## Các kết quả có thể

- Tất cả KPI đạt mục tiêu → báo cáo, duy trì.
- Một số KPI không đạt → có kế hoạch cải tiến, người chịu trách nhiệm, thời hạn.
- Dữ liệu không đủ tin cậy → bổ sung thu thập, lùi báo cáo.
- Mục tiêu không còn phù hợp → điều chỉnh bộ chỉ số ở kỳ sau.

## Cổng điều kiện dự kiến (nếu mô hình hóa)

1. Bộ chỉ số được Hội đồng phê duyệt? → Duyệt / Sửa lại
2. Dữ liệu đầy đủ, hợp lệ? → Đủ / Thiếu (yêu cầu bổ sung)
3. Đủ cỡ mẫu khảo sát? → Đủ / Thiếu (khảo sát thêm)
4. KPI đạt mục tiêu? → Đạt / Không đạt
5. (Không đạt) Mức chênh lệch? → Nhỏ (khoa tự khắc phục) / Lớn (đề án cải tiến cấp bệnh viện)
6. Hội đồng chấp nhận giải trình và kế hoạch? → Chấp nhận / Yêu cầu bổ sung
7. Kỳ đánh giá có nộp báo cáo cho Bộ Y tế? → Có / Không
8. Kỳ sau cải thiện? → Có (đóng kế hoạch) / Không (nâng cấp xử lý)

**Song song (split/join) đề xuất:** bước 3–5 — nhánh 1 *trích dữ liệu HIS*, nhánh 2 *khảo sát hài lòng*,
nhánh 3 *lấy số liệu sự cố, khiếu nại* → join → *tính KPI*.

## Liên kết với quy trình khác

- **C1–C4, S1, S3, M1, M3:** cung cấp dữ liệu cho KPI.
- **Dashboard (T46, T53):** hiển thị bộ KPI ở Bảng 1.
- **Phân tích định lượng (T44, T48):** cách tính thời gian và chi phí theo event log dùng lại cho KPI.
