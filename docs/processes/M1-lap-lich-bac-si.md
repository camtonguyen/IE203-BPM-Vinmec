# M1 – Lập lịch bác sĩ (khám ngoại trú)

- **Loại:** Quản lý
- **Người phụ trách viết:** Nguyễn Quang Hòa (26410042)
- **Phạm vi:** lập, công bố và điều chỉnh lịch làm việc của bác sĩ tại khu khám ngoại trú Vinmec Central Park
  (theo tuần/tháng), đến khi lịch được mở thành các khung giờ đặt hẹn cho C4. Gồm xử lý thay đổi đột xuất (bác sĩ nghỉ,
  đổi ca). Không gồm lịch trực nội trú / cấp cứu và lịch phẫu thuật, chỉ nêu ở mức ràng buộc.
- **Nguồn bằng chứng** (truy cập 17/11/2026):
  1. Luật Khám bệnh, chữa bệnh số 15/2023/QH15 (văn bản hợp nhất 26/VBHN-VPQH năm 2026), Điều 70 *Trực khám bệnh, chữa bệnh*:
     https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf
  2. Medpro – *3 cách đặt lịch khám Vinmec online dễ dàng, nhanh chóng* (cập nhật 05/11/2026):
     https://medpro.vn/tin-tuc/huong-dan-dat-lich-kham-vinmec-nhanh-chong-va-tien-loi
  3. Vinmec – *Hướng dẫn đặt lịch khám Vinmec trên website Online Vinmec* (cập nhật 28/10/2026; xem thêm C4):
     https://www.vinmec.com/vie/bai-viet/huong-dan-dat-lich-kham-vinmec-tren-website-online-vinmec
  4. HelloBacsi – *Vinmec Central Park – Đặt lịch khám tại BV Vinmec* (giờ làm việc):
     https://hellobacsi.com/care/benh-vien/benh-vien-da-khoa-quoc-te-vinmec-central-park-386/
  5. Vinmec – *Giờ làm việc tại các Bệnh viện Đa khoa Quốc tế Vinmec* (cập nhật 19/10/2026):
     https://www.vinmec.com/vie/bai-viet/gio-lam-viec-tai-cac-benh-vien-da-khoa-quoc-te-vinmec-vi
  6. Quyết định 6858/QĐ-BYT (2016) – Bộ tiêu chí chất lượng bệnh viện Việt Nam, tiêu chí A1.3, A1.5 (thời gian chờ):
     https://caselaw.vn/van-ban-phap-luat/138727-quyet-dinh-6858-qd-byt-nam-2016-ve-bo-tieu-chi-chat-luong-benh-vien-viet-nam-do-bo-truong-bo-y-te-ban-hanh
  7. Phỏng vấn bác sĩ, điều dưỡng (T24, tuần 2) – *chưa thực hiện*.

> Danh mục tài liệu tham khảo chung của nhóm: [`docs/tai-lieu-tham-khao.md`](../tai-lieu-tham-khao.md).

> Vinmec không công bố quy trình lập lịch nội bộ. Từ phía người bệnh có thể thấy: người bệnh chọn **bác sĩ cụ thể** và
> **xem lịch làm việc** của bác sĩ khi đặt trên website [3]; giờ khám đặt "chỉ là thời gian dự kiến", tư vấn viên gọi lại
> xác nhận khung giờ [2] → nghĩa là bên trong phải có một lịch bác sĩ được lập trước và mở thành khung giờ.
> Các bước nội bộ là suy luận theo thực hành chung, đánh dấu **⚠**, cần xác minh ở T24 (câu 6, 11, 12, 16 trong
> `interviews/questions.md` và câu đề xuất ở cuối file).

## Ràng buộc đầu vào

- **Giờ làm việc khu ngoại trú Central Park:** thứ Hai – thứ Bảy sáng 07:30–12:00, chiều 13:00–16:30 [5];
  thứ Bảy chỉ một số chuyên khoa mở khám [4]; cấp cứu 24 giờ [5]. (Chốt theo trang chính thức [5], giống Chương 1.)
- **Trực liên tục** cả ngày lễ, tết, ngày nghỉ với cơ sở có giường nội trú; thành phần trực gồm trực lãnh đạo, lâm sàng,
  cận lâm sàng, hậu cần; người đứng đầu phải **phân công người trực** và bảo đảm báo cáo mỗi phiên trực [1, Điều 70].
  → Bác sĩ vừa khám ngoại trú vừa trực/mổ, nên lịch ngoại trú phải tránh trùng ca trực, lịch mổ ⚠.
- **Thời gian chờ** là tiêu chí chất lượng: bệnh viện phải công khai cam kết thời gian chờ, theo dõi theo tuần/tháng [6]
  → số bác sĩ mỗi khung giờ cần đủ so với nhu cầu dự kiến.

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Trưởng khoa / trưởng chuyên khoa | Lập lịch khám ngoại trú của bác sĩ trong khoa, cân đối với lịch trực, lịch mổ ⚠ |
| Bác sĩ | Đăng ký ngày nghỉ, nguyện vọng ca; xác nhận lịch; báo nghỉ đột xuất ⚠ |
| Giám đốc (người đứng đầu cơ sở); Phòng Kế hoạch tổng hợp | Người đứng đầu cơ sở phân công người trực [1, Điều 70]; Phòng KHTH ban hành, phê duyệt lịch, điều phối bác sĩ giữa các khoa ⚠ (Điều 70 không nhắc Phòng KHTH) |
| Điều dưỡng trưởng khu khám | Bố trí điều dưỡng, phòng khám theo lịch bác sĩ ⚠ |
| Hệ thống đặt lịch (online.vinmec.com, MyVinmec) | Hiển thị lịch làm việc của bác sĩ và khung giờ còn trống cho người bệnh đặt [2][3]; việc sinh khung giờ từ lịch bác sĩ ⚠ |
| Tổng đài / CSKH | Báo cho người bệnh đã đặt hẹn khi bác sĩ thay đổi lịch, sắp xếp lại (C4) ⚠ |
| Người bệnh *(gián tiếp)* | Chọn bác sĩ, khung giờ dựa trên lịch được công bố [3] |

## Khách hàng của quy trình

- **Chính (nội bộ):** khoa khám bệnh, tổng đài và hệ thống đặt lịch (cần lịch chính xác để mở khung giờ – C4, C1).
- **Cuối cùng:** người bệnh – được khám đúng bác sĩ đã chọn, đúng giờ, ít phải đổi lịch.
- **Bác sĩ:** lịch cân bằng giữa khám ngoại trú, trực, mổ và nghỉ.

## Các bước (mô tả bằng lời)

**A. Lập lịch định kỳ**

1. Phòng Kế hoạch tổng hợp / khoa khám bệnh **dự báo nhu cầu** khám theo chuyên khoa, ngày trong tuần, khung giờ, dựa
   trên số lượt khám và lịch hẹn của kỳ trước ⚠.
2. Bác sĩ **đăng ký ngày nghỉ**, lịch học, hội nghị, nguyện vọng ca ⚠.
3. Trưởng khoa **lập lịch nháp**: gán bác sĩ vào buổi khám ngoại trú (sáng/chiều), tránh trùng lịch trực [1, Điều 70],
   lịch mổ, thủ thuật ⚠.
4. Kiểm tra **độ phủ**: mỗi buổi khám đủ số bác sĩ theo nhu cầu dự kiến; chuyên khoa thứ Bảy có bác sĩ [4] ⚠.
   Thiếu → điều chỉnh, xin tăng cường từ khoa khác hoặc giảm khung giờ mở đặt hẹn ⚠.
5. Gửi lịch nháp cho bác sĩ **xác nhận**; có xung đột thì quay lại bước 3 ⚠.
6. Ban giám đốc chuyên môn / Phòng KHTH **phê duyệt** và ban hành lịch (kèm lịch trực) ⚠.

**B. Công bố và mở khung giờ** (song song)

7. **Nhập lịch vào hệ thống đặt lịch**: hệ thống chia buổi khám thành các khung giờ theo thời lượng khám dự kiến mỗi
   lượt, mở cho người bệnh đặt trên website / MyVinmec / tổng đài [2][3] ⚠ (thời lượng mỗi khung chưa rõ).
8. Song song: **thông báo lịch** cho bác sĩ, điều dưỡng trưởng (bố trí điều dưỡng, phòng khám) và tổng đài.

**C. Điều chỉnh đột xuất**

9. Khi bác sĩ **báo nghỉ / đổi ca** (ốm, ca mổ cấp cứu, công tác): trưởng khoa tìm **bác sĩ thay thế** cùng chuyên khoa ⚠.
10. Kiểm tra buổi khám đó **đã có người bệnh đặt hẹn** chưa ⚠.
    - Có bác sĩ thay → cập nhật hệ thống; tổng đài báo người bệnh đổi bác sĩ, người bệnh đồng ý hoặc đổi ngày.
    - Không có bác sĩ thay → **đóng khung giờ**; tổng đài gọi từng người bệnh sắp xếp lịch khác (C4) ⚠.
11. Cập nhật lịch chính thức; ghi nhận số lần thay đổi để theo dõi (đầu vào M2) ⚠.

**D. Theo dõi**

12. Cuối kỳ, so sánh lịch với thực tế: tỉ lệ lấp đầy khung giờ, thời gian chờ, số lượt đổi lịch → điều chỉnh dự báo kỳ sau
    (bước 1) [6] ⚠.

## Các kết quả có thể

- Lịch tuần/tháng được phê duyệt, công bố, mở khung giờ đặt hẹn đúng hạn.
- Lịch thiếu bác sĩ ở một số buổi → giảm khung giờ mở hoặc tăng cường bác sĩ.
- Thay đổi đột xuất có bác sĩ thay thế → người bệnh khám bác sĩ khác hoặc đổi ngày.
- Thay đổi đột xuất không có người thay → hủy khung giờ, người bệnh được đặt lại lịch.
- Lịch bị trả lại khi phê duyệt (trùng trực, vi phạm quy định) → lập lại.

## Cổng điều kiện dự kiến (nếu mô hình hóa)

1. Lịch nháp có trùng lịch trực / mổ / nghỉ? → Có (sửa) / Không
2. Mỗi buổi khám đủ bác sĩ theo nhu cầu? → Đủ / Thiếu
3. (Thiếu) Có bác sĩ tăng cường từ khoa khác? → Có / Không (giảm khung giờ)
4. Bác sĩ xác nhận lịch? → Đồng ý / Có xung đột
5. Ban giám đốc phê duyệt? → Duyệt / Trả lại
6. Có thay đổi đột xuất? → Có / Không
7. Có bác sĩ thay thế cùng chuyên khoa? → Có / Không
8. Buổi khám đã có người bệnh đặt hẹn? → Có (liên hệ người bệnh) / Không
9. Người bệnh đồng ý khám bác sĩ thay thế? → Đồng ý / Đổi ngày

**Song song (split/join) đề xuất:** sau phê duyệt — nhánh 1 *nhập lịch, mở khung giờ trên hệ thống đặt lịch*,
nhánh 2 *thông báo bác sĩ, điều dưỡng, tổng đài*, nhánh 3 *bố trí phòng khám* → join → *lịch có hiệu lực*.

## Liên kết với quy trình khác

- **C4 Đặt lịch:** M1 cung cấp khung giờ trống; thay đổi lịch bác sĩ kích hoạt việc liên hệ đổi lịch trong C4.
- **C1 Khám ngoại trú:** số bác sĩ mỗi buổi quyết định thời gian chờ khám.
- **M2 Đánh giá KPI:** tỉ lệ lấp đầy khung giờ, số lần đổi lịch đột xuất, thời gian chờ theo buổi.

## Câu hỏi đề xuất bổ sung cho phỏng vấn T24

- Lịch khám ngoại trú của anh/chị do ai lập, lập trước bao lâu (tuần/tháng), trên Excel hay phần mềm?
- Mỗi khung giờ đặt hẹn dài bao nhiêu phút? Một buổi nhận tối đa bao nhiêu người bệnh đặt trước?
- Khi bác sĩ nghỉ đột xuất, ai báo cho người bệnh đã đặt hẹn và báo trước bao lâu?
