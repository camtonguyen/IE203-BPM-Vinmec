# Dữ liệu

> **Ghi chú gửi giảng viên: `event_log.csv` là dữ liệu mô phỏng.**
> Đây không phải thời gian đo thực tế tại Vinmec hay bất kỳ cơ sở nào. Nhóm chưa quan sát trực tiếp được lượt khám nào,
> nên yêu cầu ghi thời gian thực tế ít nhất 3 lượt **chưa được đáp ứng**.
> - L01–L30: giả lập theo một số thông tin Vinmec công bố, phần còn lại là giả định của nhóm.
> - L31–L33: dựng từ vài mốc giờ in trên chứng từ của 3 lượt khám **ngoài Vinmec**; thứ tự bước và các giờ khác là giả định.
>
> Kết quả phân tích từ file này chỉ minh họa phương pháp, không chứng minh điểm nghẽn tại Vinmec. Nhóm xin ý kiến thầy/cô
> về việc dùng dữ liệu mô phỏng cho phần phân tích. Nguồn và giả định: [Bản mô phỏng](#bản-mô-phỏng-của-event_logcsv).

- `event_log.csv`: thời gian lượt khám, cùng định dạng `event_log_template.csv`. **Hiện là bản mô phỏng** (xem mục cuối). **Chỉ dùng mã lượt ẩn danh.** Dòng mẫu trong template là ví dụ định dạng, không phải số liệu thật.
  Cách ghi, danh mục hoạt động và cách kiểm tra: [HUONG-DAN-GHI-THOI-GIAN.md](HUONG-DAN-GHI-THOI-GIAN.md)
  (`python scripts/check_event_log.py data/event_log.csv`).
- `cost_rates.csv`: đơn giá nhân công và giá dịch vụ, mỗi dòng **bắt buộc ghi nguồn + ngày truy cập**.

## Bản mô phỏng của `event_log.csv`

**Không phải số liệu đo tại Vinmec hay bất kỳ cơ sở nào.** Dùng để chạy thử T44, T49; mọi kết quả tính từ file này phải
ghi rõ là *mô phỏng*. File gồm 33 lượt: L01–L30 giả lập theo Vinmec và L31–L33 ngoài Vinmec (mục dưới), sinh bằng `python scripts/sinh_event_log_mau.py`; muốn đổi khoảng thời gian
hay tỉ lệ nhánh thì sửa trong script rồi chạy lại. Thứ tự bước theo [mô tả C1](../docs/processes/C1-kham-ngoai-tru.md).
Lượt làm cả xét nghiệm và chẩn đoán hình ảnh có các dòng chồng giờ (quy tắc 5): người bệnh xếp hàng chẩn đoán hình ảnh
trong lúc chờ và lấy mẫu, nên khi tính thời gian chu kỳ không được cộng dồn thời lượng các dòng.

| Dùng trong mô phỏng | Vinmec công bố | Nguồn (truy cập 27/11/2026) |
|---|---|---|
| Giờ khám 07:30–12:00, 13:00–16:30 | Central Park, thứ Hai – thứ Bảy | [Giờ làm việc](https://www.vinmec.com/vie/bai-viet/gio-lam-viec-tai-cac-benh-vien-da-khoa-quoc-te-vinmec-vi) (cập nhật 19/10/2026) |
| *Khám lần 1*: 20–40 phút | "Mỗi lượt khám bệnh trung bình kéo dài khoảng 30 phút" | [Đặt lịch khám](https://www.vinmec.com/vie/bai-viet/huong-dan-dat-lich-kham-tai-vinmec-vi) (cập nhật 17/08/2026) |
| Có kết quả xét nghiệm sau lấy mẫu 60–120 phút | Xét nghiệm đơn giản chờ 1–2 tiếng (bài chung về xét nghiệm máu) | [Xét nghiệm máu tổng quát](https://www.vinmec.com/vie/bai-viet/xet-nghiem-mau-tong-quat-bao-lau-co-ket-qua-vi) (cập nhật 22/07/2024) |
| *Chờ bảo lãnh*: 15–45 phút | Thời gian xử lý dự kiến, tùy công ty bảo hiểm | [Thanh toán bảo hiểm](https://www.vinmec.com/vie/bai-viet/huong-dan-thu-tuc-thanh-toan-bao-hiem-tai-vinmec-vi) (cập nhật 09/05/2026) |

Vinmec chỉ cho một con số trung bình hoặc một khoảng; việc lấy phân phối đều, và hiểu "30 phút" là thời gian *Khám lần 1*,
là cách hiểu của nhóm. **Giả định của nhóm, chưa có nguồn:** mọi khoảng thời gian còn lại, thời gian trả kết quả hình ảnh,
số lượt mỗi nhánh trong L01–L30 (15 có lịch hẹn, trong đó 2 đến muộn; 18 có cận lâm sàng, trong đó 6 làm cả hai;
9 bảo hiểm tư nhân; 21 có đơn thuốc), giờ đến, ngày 23–28/11/2026 và mọi mức tăng ở bảng điểm nghẽn. Lượt kéo quá giờ
đóng cửa được chọn lại buổi và thời lượng, nên thời lượng trong buổi chiều thiên về ngắn.

### L31–L33: ba lượt ngoài Vinmec dựng từ chứng từ

Hai lượt ở bệnh viện công, một lượt ở phòng khám tư; người đứng tên đã đồng ý. Chỉ **giờ trong ngày** của các mốc in trên
phiếu là lấy từ chứng từ (`note` có chữ "chứng từ"); ngày đã được đổi, còn thứ tự bước và mọi giờ khác là giả định, nên
các lượt này vẫn ghi `mô phỏng`. Không lưu ảnh, tên, cơ sở, chẩn đoán hay hình thức chi trả. Khoảng giữa hai mốc in có thể
không đúng là thời gian chờ thật. Khi phân tích Vinmec thì loại ba lượt này:
`df = df[~df["note"].str.contains("ngoài Vinmec")]`.

### Bằng chứng công khai về điểm nghẽn (truy cập 27/11/2026)

| Bằng chứng | Nguồn, độ tin cậy | Đưa vào mô phỏng |
|---|---|---|
| Bảo lãnh bảo hiểm tư nhân xử lý dự kiến 15–45 phút, tùy công ty | [Vinmec](https://www.vinmec.com/vie/bai-viet/huong-dan-thu-tuc-thanh-toan-bao-hiem-tai-vinmec-vi), chính thức | *Chờ bảo lãnh* 15–45 phút |
| Xét nghiệm đơn giản chờ kết quả 1–2 giờ, phức tạp 3–4 giờ | [Vinmec](https://www.vinmec.com/vie/bai-viet/xet-nghiem-mau-tong-quat-bao-lau-co-ket-qua-vi), bài kiến thức chung, không phải số đo | *Chờ kết quả* theo mức 1–2 giờ |
| Nên đặt hẹn để tránh chờ; đến muộn có thể phải chờ xếp lịch | [Vinmec](https://www.vinmec.com/vie/bai-viet/huong-dan-dat-lich-kham-tai-vinmec-vi), chính thức, không có số phút | Đến trực tiếp hoặc đến muộn: *Chờ khám* thêm 5–20 phút |
| Giờ cao điểm, cuối tuần, lễ đôi khi quá tải, thủ tục và chờ đợi kéo dài | [Med247](https://med247.vn/chia-se-kien-thuc/song-khoe/kham-nhi-o-vinmec-co-tot-khong.html) (23/05/2025), bên thứ ba, nói về khám nhi, **yếu** | Thứ Bảy: tiếp đón và các bước chờ (trừ *Chờ kết quả*, *Chờ bảo lãnh*) nhân 1,5 |
| Một số phụ huynh phản ánh kết quả mất 3–7 ngày làm việc | Cùng bài Med247, **yếu** | Không: ngoài phạm vi một lượt trong ngày |
| Từ chối mẫu 137/546.704 (0,025%), cả nội trú và ngoại trú; lấy lại trong ngày làm chậm kết quả trung bình 72 phút | [Nghiên cứu tại Vinmec Times City, 2024](https://tapchiyhcd.vn/index.php/yhcd/article/view/3945), tạp chí khoa học | Không: quá hiếm so với 30 lượt |

Chưa tìm thấy nghiên cứu công khai nào đo thời gian chờ khám ngoại trú tại Vinmec. **Mô phỏng được dựng theo các bằng chứng
trên, nên điểm nghẽn tính ra từ nó chỉ lặp lại giả định đầu vào, không chứng minh Vinmec Central Park có điểm nghẽn đó.**
Khi phân tích, trích bằng chứng từ nguồn gốc, không trích từ file mô phỏng.
