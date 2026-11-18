# C2 – Cận lâm sàng (khám ngoại trú)

- **Loại:** Cốt lõi
- **Người phụ trách viết:** Qua Tú Phương (26410095)
- **Phạm vi:** từ lúc bác sĩ chỉ định cận lâm sàng (hoặc người bệnh chọn gói khám sức khỏe tổng quát) đến khi bác sĩ đọc,
  giải thích kết quả. Giao với C3 ở bước thanh toán chỉ định.
- **Nguồn bằng chứng** (truy cập 18/11/2026; link đã kiểm tra mở được):
  1. Vinmec – *Xét nghiệm cận lâm sàng là gì?* (2024): https://www.vinmec.com/vie/bai-viet/xet-nghiem-can-lam-sang-la-gi-vi
  2. Vinmec – *Khám cận lâm sàng*: https://www.vinmec.com/vie/chu-de/kham-can-lam-sang
  3. Vinmec – *Quy trình khám chữa bệnh tại Vinmec*: https://www.vinmec.com/vie/bai-viet/quy-trinh-kham-chua-benh-tai-vinmec-vi
  4. Vinmec – *Thủ tục thanh toán bảo hiểm tại Vinmec*: https://www.vinmec.com/vie/bai-viet/huong-dan-thu-tuc-thanh-toan-bao-hiem-tai-vinmec-vi
  5. Vinmec – *Chuyên khoa Sức khỏe tổng quát – Dịch vụ*: https://www.vinmec.com/vie/chuyen-khoa-suc-khoe-tong-quat-vinmec/dich-vu
  6. Phỏng vấn bác sĩ, điều dưỡng, kỹ thuật viên (T22–T25, tuần 2) – *chưa thực hiện*.

> Các nguồn 1–5 là hướng dẫn chung của hệ thống Vinmec, không riêng Vinmec Central Park.
> Mục đánh dấu **⚠** là suy luận hoặc nguồn chưa nói rõ, cần xác minh qua phỏng vấn.
> Riêng con số "4–6 tiếng" ở nguồn [5] đã đối chiếu lại trên trang gốc; các con số khác (32–91 dịch vụ) chưa đối chiếu.

## Giải thích thuật ngữ

- **Lâm sàng:** phần bác sĩ trực tiếp làm với người bệnh: hỏi bệnh sử, quan sát, nghe, sờ, đo sinh hiệu để đưa ra nhận định ban đầu.
- **Cận lâm sàng:** các kỹ thuật hỗ trợ chẩn đoán đi kèm phần lâm sàng ("cận" nghĩa là gần, bên cạnh). Dùng để phát hiện,
  chẩn đoán, theo dõi bệnh và đánh giá đáp ứng điều trị, đặc biệt khi triệu chứng chưa rõ hoặc không đặc hiệu [1].
  Loại cận lâm sàng do bác sĩ quyết định dựa trên khám lâm sàng [1][2]. Mọi chỉ định đều cần bác sĩ vì có rủi ro
  (đau khi lấy máu, phơi nhiễm phóng xạ khi chụp X-quang hoặc CT, chi phí) [1].

Trong ngoại trú, cận lâm sàng gồm 3 nhóm, tương ứng 3 hoạt động trong danh mục ghi thời gian của nhóm:

Bảng 1. Ba nhóm cận lâm sàng trong ngoại trú

| Nhóm | Là gì | Ví dụ | Hoạt động trong danh mục |
|---|---|---|---|
| Xét nghiệm | Phân tích mẫu lấy từ cơ thể | Máu, nước tiểu, dịch | Xét nghiệm - lấy mẫu |
| Chẩn đoán hình ảnh | Tạo hình ảnh bên trong cơ thể | X-quang, siêu âm, CT, MRI | Chẩn đoán hình ảnh |
| Thăm dò chức năng | Đo hoạt động của cơ quan | Điện tim, nội soi | Thăm dò chức năng |

Hai hoạt động chờ đi kèm là **Chờ cận lâm sàng** và **Chờ kết quả**.

## Actor

Bảng 2. Actor của quy trình C2

| Actor | Vai trò trong C2 |
|---|---|
| Người bệnh (và người nhà) | Nhận chỉ định, ký phiếu, đi làm cận lâm sàng, nhận kết quả |
| Bác sĩ | Chỉ định cận lâm sàng; đọc và giải thích kết quả |
| Điều dưỡng | Phân loại người bệnh, hướng dẫn đến đúng khu vực |
| Kỹ thuật viên xét nghiệm | Lấy mẫu và xử lý mẫu ⚠ |
| Kỹ thuật viên chẩn đoán hình ảnh | Chụp, siêu âm, đọc hình ⚠ |
| Thu ngân | Thu viện phí hoặc xác nhận bảo hiểm cho chỉ định (giao với C3) |

> ⚠ Hai vai kỹ thuật viên là suy luận từ loại cận lâm sàng; nguồn [3] không nêu nhân viên phụ trách.

## Khách hàng của quy trình

Bảng 3. Customer của quy trình C2

| Customer | Vai trò |
|---|---|
| Người bệnh (và người nhà) | Khách hàng chính, người nhận kết quả cận lâm sàng |
| Bác sĩ khám | Khách hàng nội bộ, dùng kết quả để chẩn đoán và quyết định điều trị |

## Giá trị quy trình mang lại cho khách hàng

Bảng 4. Giá trị C2 mang lại cho khách hàng

| Customer | Giá trị nhận được |
|---|---|
| Người bệnh | Biết chính xác tình trạng bệnh qua kết quả khách quan; được giải thích kết quả; biết hướng xử trí tiếp theo (ra về, tái khám, nhập viện); ít phải chờ và đi lại |
| Bác sĩ khám | Có dữ liệu khách quan, đầy đủ và kịp thời để chẩn đoán đúng và chọn phương án điều trị phù hợp |

## Các bước (mô tả bằng lời)

C2 diễn ra theo 2 case, khác nhau ở thứ tự giữa khám lâm sàng và cận lâm sàng.

**Case 1: Khám theo bác sĩ** — thứ tự: khám lâm sàng → chỉ định → thanh toán → thực hiện cận lâm sàng → đọc kết quả.
Các bước theo sơ đồ quy trình khám chữa bệnh của Vinmec [3]:

1. **Đăng ký khám, mở hồ sơ bệnh án** (Bước 1 của Vinmec): người bệnh điền phiếu đăng ký, sao chụp giấy tờ tùy thân và
   thẻ bảo hiểm. Người bệnh đến trực tiếp hoặc qua tổng đài đặt hẹn [3].
2. **Phân loại người bệnh:** điều dưỡng ở bốt điều dưỡng, phòng khám phân loại và đưa người bệnh vào khám [3].
3. **Khám và tư vấn:** bác sĩ khám lâm sàng. Nếu chỉ cần đơn thuốc thì sang thanh toán (Bước 2) rồi ra về; nếu cần
   cận lâm sàng thì sang bước 4 [3].
4. **Chỉ định cận lâm sàng** (Bước 3 của Vinmec): bác sĩ chỉ định; người bệnh ký phiếu đồng ý làm xét nghiệm HIV,
   phiếu đồng ý thực hiện chẩn đoán (nếu có) hoặc phiếu từ chối [3].
5. **Thanh toán chỉ định** (Bước 4 của Vinmec): ký chứng từ thanh toán (2 bảng kê, 1 biên lai thu tiền viện phí);
   với bảo hiểm tư nhân ký thêm thanh toán bảo hiểm [3][4].
6. **Thực hiện cận lâm sàng:** lấy mẫu xét nghiệm, chụp chẩn đoán hình ảnh hoặc thăm dò chức năng. Bước này
   **không được vẽ trong sơ đồ** [3] ⚠.
7. **Đọc và giải thích kết quả:** người bệnh quay lại bác sĩ. Sau bước này luồng rẽ nhánh (xem Các kết quả có thể).

Sơ đồ [3] cho biết thanh toán chỉ định diễn ra **trước** khi thực hiện cận lâm sàng, và việc bác sĩ đọc, giải thích kết
quả là bước kết thúc C2. Sơ đồ **không nêu** nơi thực hiện từng cận lâm sàng, thời gian chờ, cách nhận kết quả và nhân
viên phụ trách ⚠ → cần xác nhận qua phỏng vấn hoặc quan sát thực tế.

**Case 2: Đăng ký khám sức khỏe tổng quát** — thứ tự: cận lâm sàng → khám lâm sàng → đọc kết quả và tư vấn. Người bệnh
làm theo gói khám đã chọn, không cần bác sĩ chỉ định từng hạng mục. Trình tự theo Vinmec [5]:

1. **Đăng ký lịch:** chọn lịch khám.
2. **Tiếp đón:** nhân viên tiếp nhận và hướng dẫn người bệnh.
3. **Lấy mẫu xét nghiệm:** huyết học, sinh hóa máu, tổng phân tích nước tiểu; gói nữ có thêm HPV và tế bào học cổ tử cung,
   gói nam có thêm PSA (nâng cao và toàn diện).
4. **Chẩn đoán hình ảnh:** siêu âm (tuyến giáp, ổ bụng, vú, phụ khoa, tiết niệu), X-quang ngực, điện tim, chụp đáy mắt;
   tùy gói có thêm CT phổi liều thấp hoặc X-quang tuyến vú.
5. **Khám lâm sàng.**
6. **Đọc kết quả và tư vấn:** bác sĩ đọc kết quả và tư vấn.
7. **Nhận kết quả:** người bệnh nghỉ ngơi, nhận kết quả và hướng dẫn các bước tiếp theo.

Thời gian khám dự kiến **4–6 tiếng** [5]. Gói khám chia theo trẻ em (3 nhóm tuổi), nữ giới và nam giới (tiêu chuẩn, nâng
cao, toàn diện) và 12 gói tầm soát chuyên sâu [5]. Trang [5] **chưa nêu** hướng dẫn chuẩn bị trước khám (như nhịn ăn),
thời gian có kết quả xét nghiệm và hình thức tư vấn chi tiết ⚠ → cần xác nhận qua hotline hoặc phỏng vấn.

**So sánh 2 case**

Bảng 5. So sánh hai case của C2

| | Case 1: Khám theo bác sĩ | Case 2: Khám sức khỏe tổng quát |
|---|---|---|
| Ai quyết định cận lâm sàng | Bác sĩ chỉ định sau khám lâm sàng | Theo gói khám đã chọn |
| Thứ tự | Khám lâm sàng, cận lâm sàng, đọc kết quả | Cận lâm sàng, khám lâm sàng, đọc kết quả và tư vấn |
| Số hạng mục | Ít, theo từng người bệnh | Nhiều, theo gói (32–91 dịch vụ ở người lớn, chưa đối chiếu) |
| Thời gian | Chưa có nguồn | Dự kiến 4–6 tiếng |
| Nguồn | [1], [2], [3] | [5] |

## Các kết quả có thể

Bảng 6. Outcome positive và negative của C2

| Loại | Outcome |
|---|---|
| Positive | Có kết quả đầy đủ, bác sĩ đọc và giải thích, người bệnh ra về (kèm đơn thuốc nếu có) |
| Positive | Có kết quả, hẹn tái khám theo kế hoạch điều trị |
| Positive | Có kết quả, người bệnh được nhập viện nội khoa hoặc phẫu thuật, thủ thuật đúng chỉ định |
| Negative | Chưa có kết quả trong ngày, người bệnh phải hẹn trả sau hoặc quay lại ⚠ |
| Negative | Phải làm thêm hoặc làm lại cận lâm sàng (kết quả chưa đủ để kết luận, mẫu không đạt, chưa chuẩn bị đúng yêu cầu) ⚠ |
| Negative | Người bệnh từ chối hoặc hủy chỉ định (ký phiếu từ chối) [3] |
| Negative | Người bệnh chờ lâu hoặc đi lại nhiều giữa các khu vực, trải nghiệm kém ⚠ |

## Cổng điều kiện dự kiến (nếu mô hình hóa)

Dùng cho BPMN C2. Mục tiêu rubric: > 7 cổng điều kiện và có cặp split/join song song.

Bảng 7. Cổng điều kiện dự kiến của C2

| STT | Cổng điều kiện | Nhánh ra |
|---|---|---|
| 1 | Người bệnh khám theo bác sĩ hay khám sức khỏe tổng quát? | Case 1 / Case 2 |
| 2 | Bác sĩ có chỉ định cận lâm sàng không? | Có: sang chỉ định / Không: đơn thuốc, ra về |
| 3 | Người bệnh đồng ý thực hiện chẩn đoán không? | Đồng ý: thanh toán / Từ chối: ký phiếu từ chối |
| 4 | Chỉ định đã được thanh toán hoặc bảo lãnh chưa? | Rồi: thực hiện / Chưa: quay lại thanh toán |
| 5 | Loại chỉ định là xét nghiệm, chẩn đoán hình ảnh hay thăm dò chức năng? | 3 nhánh |
| 6 | Cần chuẩn bị trước (nhịn ăn, nhịn tiểu) không, và đã đạt chưa? ⚠ | Đạt: thực hiện / Chưa đạt: hẹn lại |
| 7 | Có đủ kết quả trong ngày không? ⚠ | Đủ: đọc kết quả / Chưa: hẹn trả sau |
| 8 | Bác sĩ cần chỉ định thêm cận lâm sàng không? | Có: quay lại chỉ định / Không: kết luận |
| 9 | Hướng xử trí sau đọc kết quả là gì? | Ra về / Tái khám / Nhập viện nội khoa / Nhập viện phẫu thuật |

**Song song (split/join):** khi bác sĩ chỉ định nhiều loại cận lâm sàng, *lấy mẫu xét nghiệm* ∥ *chụp chẩn đoán hình ảnh* ∥
*thăm dò chức năng* có thể thực hiện song song, sau đó gộp lại ở bước đọc kết quả ⚠. Trong khám sức khỏe tổng quát [5],
các hạng mục này cũng nằm trong cùng một gói.

## Phân tích lãng phí dự kiến (VA / BVA / NVA)

Bảng dưới là dự kiến, sẽ đối chiếu lại bằng event log.

Bảng 8. Phân tích lãng phí dự kiến của C2 (VA / BVA / NVA)

| Hoạt động | Phân loại dự kiến | Loại lãng phí dự kiến |
|---|---|---|
| Lấy mẫu xét nghiệm, chụp chẩn đoán hình ảnh, thăm dò chức năng | VA | Không |
| Ký phiếu đồng ý, ký chứng từ thanh toán | BVA | Giấy tờ |
| Chờ cận lâm sàng | NVA | Chờ đợi |
| Chờ kết quả | NVA | Chờ đợi |
| Di chuyển giữa khu vực, quay lại thanh toán | NVA | Di chuyển |

## Liên kết với quy trình khác

- **C1 Khám ngoại trú:** C2 là một đoạn của lượt khám, bắt đầu sau khi bác sĩ khám lâm sàng.
- **C3 Thanh toán, bảo lãnh:** bước thanh toán chỉ định (bước 5) và cổng "đã thanh toán hoặc bảo lãnh chưa".
- **M2 Đánh giá KPI:** thời gian chờ cận lâm sàng và chờ kết quả, tỉ lệ làm lại.
