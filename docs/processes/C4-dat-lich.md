# C4 – Đặt lịch khám

- **Loại:** Cốt lõi
- **Người phụ trách viết:** Huỳnh Duy Phúc (26410092)
- **Phạm vi:** từ lúc người bệnh có nhu cầu khám đến khi check-in tại Quầy tiếp đón vào ngày hẹn (chuyển sang C1),
  gồm cả đổi lịch, đến muộn và không đến. Không gồm đặt lịch tiêm chủng và mua gói khám sức khỏe.
- **Nguồn bằng chứng** (truy cập 17/11/2026):
  1. Vinmec – *Hướng dẫn đặt lịch khám tại Vinmec* (cập nhật 17/08/2026):
     https://www.vinmec.com/vie/bai-viet/huong-dan-dat-lich-kham-tai-vinmec-vi
  2. Vinmec – *Hướng dẫn đặt lịch khám Vinmec trên website Online Vinmec* (cập nhật 28/10/2026):
     https://www.vinmec.com/vie/bai-viet/huong-dan-dat-lich-kham-vinmec-tren-website-online-vinmec
  3. Vinmec – *Hướng dẫn sử dụng dịch vụ Vinmec sau khi đăng ký online* (cập nhật 28/10/2026):
     https://www.vinmec.com/vie/bai-viet/huong-dan-su-dung-dich-vu-vinmec-sau-khi-dang-ky-online
  4. Vinmec – *MyVinmec: Ứng dụng điện thoại giúp quản lý trọn vẹn sức khỏe cá nhân và gia đình* (cập nhật 22/07/2024):
     https://www.vinmec.com/vie/bai-viet/my-vinmec-ung-dung-dien-thoai-giup-quan-ly-tron-ven-suc-khoe-ca-nhan-va-gia-dinh-vi
  5. Vinmec – *Quy trình khám chữa bệnh tại Vinmec* (cập nhật 19/10/2026):
     https://www.vinmec.com/huong-dan-khach-hang/quy-trinh-kham-chua-benh-tai-vinmec/
  6. Phỏng vấn người bệnh / lễ tân (T24, T26, tuần 2) – *chưa thực hiện*.

> Các nguồn 1–5 là hướng dẫn chung của hệ thống Vinmec. Tổng đài đặt hẹn Vinmec Central Park: **028 3622 1166** [1].
> Mục đánh dấu **⚠** là suy luận hoặc nguồn chưa nói rõ, cần xác minh qua phỏng vấn
> (câu 1, 15, 16, 21 trong `interviews/questions.md`).

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Người bệnh / người nhà | Chọn kênh, chọn cơ sở – chuyên khoa – bác sĩ – giờ khám, đến khám hoặc báo đổi lịch |
| Tổng đài đặt hẹn / CSKH | Nhận cuộc gọi, đặt hẹn chuyên khoa, sắp xếp lịch khác khi khách báo không đến được [1]; liên hệ lại khách gửi form tư vấn ⚠ ([1] chỉ ghi "chúng tôi sẽ liên hệ") |
| Hệ thống đặt lịch (online.vinmec.com, ứng dụng MyVinmec) | Hiển thị cơ sở, chuyên khoa, bác sĩ và khung giờ trống; ghi nhận lịch hẹn; thông báo đặt thành công; nhắc lịch [2][4] |
| Quầy tiếp đón | Check-in theo lịch hẹn / mã đăng ký; mở hồ sơ cho khách mới; định danh người bệnh [3][5] |
| Bác sĩ, khoa khám bệnh | Lịch làm việc của bác sĩ là đầu vào cho khung giờ trống (từ M1) |

## Khách hàng của quy trình

- **Chính:** người bệnh muốn khám ngoại trú đúng chuyên khoa, đúng bác sĩ, ít phải chờ.
- **Nội bộ:** khoa khám bệnh và bác sĩ (nhận danh sách lịch hẹn để phân bổ nguồn lực).

## Các bước (mô tả bằng lời)

**A. Đặt lịch**

1. Người bệnh chọn **kênh đặt lịch** [1]:
   - **Tổng đài** của từng bệnh viện (Central Park: 028 3622 1166);
   - **Website** online.vinmec.com;
   - **Ứng dụng MyVinmec** [4];
   - **Form tư vấn** trên vinmec.com (chỉ là yêu cầu liên hệ, không phải đặt lịch trực tiếp);
   - Đến trực tiếp, không hẹn trước ⚠ (nguồn không mô tả; có trong lựa chọn câu hỏi 1).
2. **Kênh website** [2]: vào online.vinmec.com → chọn **cơ sở** → chọn **chuyên khoa** hoặc **bác sĩ cụ thể**
   (xem chuyên môn và lịch làm việc) → chọn **ngày và khung giờ còn trống** → **xác nhận thông tin** đặt lịch.
3. **Kênh ứng dụng MyVinmec** [1][4]: tải ứng dụng; tạo hồ sơ cho bản thân và người thân; đặt lịch, quản lý và theo dõi
   lịch hẹn trong ứng dụng; lưu mã khách hàng Vinmec để check-in nhanh. Bước đăng ký tài khoản lần đầu nguồn không mô tả ⚠.
4. **Kênh tổng đài** [1]: người bệnh gọi tổng đài của bệnh viện, nghe hướng dẫn và đặt hẹn khám chuyên khoa
   với tổng đài viên.
5. **Kênh form tư vấn** [1]: người bệnh điền họ tên, số điện thoại, bệnh viện gần nhất và nội dung cần tư vấn;
   Vinmec liên hệ lại "trong thời gian sớm nhất" (không nêu thời hạn cụ thể) [1]; liên hệ lại có dẫn tới đặt lịch hay
   không ⚠.
6. Nếu **không còn khung giờ phù hợp**, người bệnh chọn ngày, giờ hoặc bác sĩ khác ⚠.
7. Hệ thống **thông báo đặt lịch thành công** [2]. Hình thức xác nhận (SMS, cuộc gọi, email) chưa rõ ⚠.

**B. Trước ngày khám**

8. Ứng dụng MyVinmec **nhắc lịch hẹn** [4].
9. Nếu **không đến được đúng hẹn**, người bệnh thông báo cho bệnh viện qua tổng đài để được bố trí lịch khác [1].

**C. Ngày khám**

10. Người bệnh đến sớm **10–15 phút**, mang giấy tờ tùy thân và hồ sơ, kết quả khám trước (nếu có); làm theo hướng dẫn
    chuẩn bị (vd nhịn ăn) nếu dịch vụ yêu cầu [2][3]. Mỗi lượt khám trung bình khoảng **30 phút** [1].
11. **Check-in** tại Quầy tiếp đón bằng thông tin lịch hẹn hoặc mã đăng ký; thông tin đặt online đã có sẵn trên hệ thống [3].
12. **Khách mới**: mở hồ sơ tại Quầy tiếp đón (họ tên, giấy tờ tùy thân, thẻ bảo hiểm và thẻ ưu đãi nếu có) [5].
13. **Định danh** người bệnh bằng ít nhất 2 thông tin (họ tên đầy đủ, ngày sinh; mã PID nếu cần) [5] → chuyển sang **C1**.
14. Nếu **đến muộn**, người bệnh có thể phải chờ để nhân viên sắp xếp lại lịch khám [1].
    Nếu **không đến và không báo** (no-show), lịch hẹn bị bỏ ⚠.

## Các kết quả có thể

- Lịch hẹn được ghi nhận và người bệnh check-in đúng giờ → bắt đầu C1.
- Người bệnh đến muộn → chờ sắp xếp lại lịch trong ngày [1].
- Người bệnh báo trước không đến được → được bố trí lịch khác [1].
- Người bệnh không đến, không báo (no-show) ⚠ → khung giờ bị lãng phí; được tính vào KPI tỉ lệ no-show (M2).
- Không có khung giờ phù hợp → người bệnh chọn lại hoặc không đặt được ⚠.
- Gửi form tư vấn nhưng chưa thành lịch hẹn ⚠.

## Cổng điều kiện dự kiến (nếu mô hình hóa)

1. Kênh đặt lịch? → Tổng đài / Website / Ứng dụng / Form tư vấn / Đến trực tiếp
2. (Ứng dụng) Đã có tài khoản MyVinmec? → Có / Không (tạo tài khoản) ⚠
3. Chọn theo chuyên khoa hay bác sĩ cụ thể?
4. Còn khung giờ trống phù hợp? → Có / Không (chọn lại)
5. Thông tin đặt lịch đúng? → Xác nhận / Sửa lại
6. Người bệnh có thay đổi lịch trước ngày khám? → Có (báo tổng đài, đặt lại) / Không
7. Ngày khám: đến đúng giờ / đến muộn / không đến → *event-based gateway* (sự kiện check-in hoặc hết giờ hẹn) ⚠
8. Khách mới hay khách cũ? → Mở hồ sơ / Dùng hồ sơ có sẵn
9. Định danh khớp thông tin lịch hẹn? → Có / Không (kiểm tra lại) ⚠

**Song song (split/join) gợi ý:** sau khi lịch hẹn được ghi nhận — *gửi xác nhận cho người bệnh* ‖ *cập nhật danh sách
hẹn cho khoa khám bệnh* → join ⚠.

## Liên kết với quy trình khác

- **M1 Lập lịch bác sĩ:** cung cấp lịch làm việc, tức khung giờ có thể đặt.
- **C1 Khám ngoại trú:** C4 kết thúc khi check-in, chuyển sang C1.
- **C3 Thanh toán:** thông tin bảo hiểm khai báo khi mở hồ sơ (bước 12).
- **M2 Đánh giá KPI:** tỉ lệ no-show (câu 15), thời gian chờ từ check-in đến khi được khám (câu 20).
