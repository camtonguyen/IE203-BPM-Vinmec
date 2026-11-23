# S1 – Quy trình Cấp phát thuốc Ngoại trú tại Nhà thuốc Bệnh viện

- **Loại quy trình:** Quy trình Hỗ trợ (Supporting Process)
- **Người phụ trách viết:** Đinh Hoàng Phát (MSSV: 26410086)
- **Phạm vi áp dụng:** Nhà thuốc Ngoại trú – Bệnh viện Đa khoa Quốc tế Vinmec Central Park.

---

## 1. Mục tiêu và Phạm vi

### 1.1. Mục tiêu
- Đảm bảo 100% người bệnh ngoại trú nhận đúng thuốc, đủ số lượng, đúng hàm lượng và rõ ràng hướng dẫn sử dụng.
- Tuân thủ tuyệt đối tiêu chuẩn quốc tế **JCI (Joint Commission International)** về Quản lý & Sử dụng thuốc (MMU) và an toàn người bệnh (IPSG - 2 định danh người bệnh).
- Tối ưu hóa thời gian chờ nhận thuốc của người bệnh ngoại trú (mục tiêu SLA $\le 10$ phút đối với đơn thuốc thông thường).
- Tự động hóa cập nhật dữ liệu dược trên hệ thống HIS, trừ kho theo thời gian thực và quản lý xuất hóa đơn điện tử.

### 1.2. Phạm vi
- Bắt đầu từ khi bác sĩ hoàn tất chỉ định đơn thuốc trên hệ thống EMR/HIS và kết thúc khi người bệnh nhận thuốc, được tư vấn sử dụng và rời quầy thuốc.
- Áp dụng cho toàn bộ các đối tượng: Người bệnh khám tự chi trả viện phí, người bệnh có BHYT nhà nước và người bệnh bảo lãnh qua công ty bảo hiểm tư nhân/quốc tế (BHTN).

---

## 2. Nguồn bằng chứng & Giả định nghiệp vụ

Để đảm bảo tính trung thực học thuật và phương pháp luận của môn học IE203, tài liệu phân định rõ nguồn dữ liệu:

### 2.1. Nguồn bằng chứng công khai & Quy định pháp lý (Evidence-based)
1. **Thông tư 26/2025/TT-BYT** của Bộ Y tế: Quy định về đơn thuốc và việc kê đơn thuốc hóa dược, sinh phẩm trong điều trị ngoại trú tại cơ sở khám bệnh, chữa bệnh; hiệu lực từ 01/07/2025, thay thế Thông tư 52/2017/TT-BYT và Thông tư 18/2018/TT-BYT (Điều 13 khoản 2). Bệnh viện phải kê đơn thuốc bằng hình thức điện tử trước ngày 01/10/2025 (Điều 13 khoản 3). Văn bản (bản ký số, truy cập 20/11/2026): https://storage-vnportal.vnpt.vn/gov-lan/5962/FileQuanTriTinTuc/Th%C3%B4ng%20t%C6%B0%20quy%20%C4%91%E1%BB%8Bnh%20v%E1%BB%81%20%C4%91%C6%A1n%20thu%E1%BB%91c%20v%C3%A0%20k%C3%AA%20%C4%91%C6%A1n%20thu%E1%BB%91c%20trong%20%C4%91i%E1%BB%81u%20tr%E1%BB%8B%20ngo%E1%BA%A1i%20tr%C3%BA%20kcb.signed.pdf
2. **Bộ Tiêu chuẩn Quốc tế JCI (Phiên bản 7/8)**: Chương *Medication Management and Use (MMU)* yêu cầu rà soát đơn thuốc lâm sàng trước khi cấp phát ⚠ (chương MMU nhóm chưa đọc được bản gốc, bộ tiêu chuẩn phải trả phí). Nhận diện người bệnh bằng ít nhất 2 định danh (ví dụ họ tên, mã định danh, ngày sinh; không dùng số phòng) thuộc mục tiêu an toàn người bệnh **IPSG.1** *Identify Patients Correctly*, không thuộc MMU (JCI Accreditation Standards for Hospitals, bản 5, trang mẫu công khai: https://digitalassets.jointcommission.org/api/public/content/assets/1/14/jcih14_sample_pages.pdf). Trang Vinmec *Quy trình khám chữa bệnh tại Vinmec* nêu định danh bằng ít nhất 2 thông số: họ tên đầy đủ, ngày tháng năm sinh và mã PID (nếu cần): https://www.vinmec.com/vie/bai-viet/quy-trinh-kham-chua-benh-tai-vinmec-vi
3. **Cổng thông tin Bệnh viện Vinmec** – *Thủ tục thanh toán bảo hiểm tại Vinmec*: bảo lãnh viện phí chỉ áp dụng với công ty bảo hiểm đã ký bảo lãnh trực tiếp với Vinmec (danh sách trên trang); thời gian xử lý bảo lãnh 15–45 phút tùy công ty bảo hiểm: https://www.vinmec.com/vie/bai-viet/huong-dan-thu-tuc-thanh-toan-bao-hiem-tai-vinmec-vi. Số lượng công ty bảo hiểm và việc nhận đơn thuốc điện tử trên MyVinmec trang không nêu ⚠.

### 2.2. Giả định nghiệp vụ (Business Assumptions - Cần kiểm chứng qua phỏng vấn thực tế)
- **Giả định 1**: Bác sĩ kê đơn trực tiếp trên phần mềm EMR/HIS; ngay khi bác sĩ ký số/lưu đơn, hệ thống tự động truyền thông điệp đơn thuốc đến màn hình chờ của Dược sĩ nhà thuốc ngoại trú.
- **Giả định 2**: Tỷ lệ người bệnh có sử dụng thẻ bảo lãnh bảo hiểm tư nhân tại Vinmec Central Park ước tính khoảng 35% – 45% tổng số lượt ngoại trú.
- **Giả định 3**: Nhà thuốc áp dụng cơ chế kiểm tra chéo độc lập (Double-checking): Một dược sĩ chịu trách nhiệm lấy thuốc và dán nhãn, một dược sĩ khác kiểm tra lại và trực tiếp phát thuốc, tư vấn cho người bệnh.

---

## 3. Tác nhân tham gia (Actors & Roles)

1. **Người bệnh / Thân nhân người bệnh (NB/TN)**: Người mang mã tiếp nhận hoặc mở App MyVinmec đến nhà thuốc nhận thuốc.
2. **Dược sĩ lâm sàng / Tiếp nhận & Thẩm định (DS1)**: Đọc soát đơn thuốc trên hệ thống, kiểm tra chống chỉ định, liều lượng, tương tác thuốc.
3. **Dược sĩ soạn thuốc kho lẻ (DS2)**: Thực hiện lấy thuốc theo đơn từ các ngăn thuốc, kiểm tra hạn dùng, đóng gói và in tem nhãn phụ hướng dẫn sử dụng.
4. **Dược sĩ kiểm soát & Phát thuốc (DS3)**: Kiểm tra chéo đơn thuốc và gói thuốc thực tế, gọi số thứ tự, định danh người bệnh, phát thuốc và tư vấn cách dùng.
5. **Thu ngân / Nhân viên Bảo lãnh viện phí (TN)**: Xử lý thanh toán tiền thuốc đối với đơn tự chi trả hoặc gửi yêu cầu bảo lãnh thuốc đến công ty bảo hiểm.
6. **Bác sĩ kê đơn (BS)**: Nhận phản hồi từ dược sĩ khi đơn thuốc có tương tác hoặc hết thuốc để chỉnh sửa đơn kịp thời.
7. **Hệ thống HIS / LIS / Kho Dược**: Tự động trừ kho, lưu trữ lịch sử cấp phát, xuất hóa đơn VAT điện tử.

---

## 4. Khách hàng của quy trình
- **Khách hàng trực tiếp**: Người bệnh khám ngoại trú và thân nhân.
- **Khách hàng nội bộ**: Khoa Khám bệnh, Kho Dược bệnh viện, Phòng Kế toán tài chính, Bộ phận Quản lý chất lượng bệnh viện.

---

## 5. Đầu vào & Kích hoạt quy trình (Inputs & Triggers)

- **Sự kiện bắt đầu (Trigger)**: Đơn thuốc điện tử được Bác sĩ hoàn thành trên hệ thống EMR của ca khám ngoại trú (C1).
- **Tài liệu / Dữ liệu đầu vào**:
  + Mã hồ sơ bệnh nhân (*Patient ID*) và Mã lượt khám (*Case ID*).
  + Danh mục thuốc kê đơn: Tên biệt dược, hoạt chất, hàm lượng, đường dùng, liều dùng, số ngày dùng, lưu ý uống trước/sau ăn.
  + Tiền sử dị ứng thuốc và bệnh lý nền của người bệnh lưu trong EMR.
  + Thông tin bảo hiểm y tế / bảo hiểm tư nhân (nếu có).

---

## 6. Các bước thực hiện chi tiết (Step-by-Step Description)

1. **Bước 1: Tiếp nhận và hiển thị đơn thuốc trên hệ thống**
   - Hệ thống HIS tự động đẩy đơn thuốc vào hàng đợi (*Queue*) của Nhà thuốc Ngoại trú.
   - Màn hình quầy thuốc hiển thị mã số người bệnh và trạng thái "Đang chuẩn bị".

2. **Bước 2: Thẩm định lâm sàng đơn thuốc (Clinical Screening)**
   - Dược sĩ tiếp nhận kiểm tra sự hợp lý của đơn thuốc: chỉ định, liều lượng, đường dùng, tần suất dùng thuốc phù hợp lứa tuổi, cân nặng.
   - Hệ thống HIS tự động cảnh báo (Drug-Drug Interaction Alert) nếu phát hiện tương tác thuốc mức độ nặng hoặc tiền sử dị ứng đã ghi nhận.
   - *Rẽ nhánh*: Nếu phát hiện đơn thuốc có sai sót hoặc nghi ngờ tương tác nguy hiểm, dược sĩ liên hệ điện thoại nội bộ với bác sĩ kê đơn để điều chỉnh; Nếu đơn thuốc an toàn, chuyển sang bước soạn thuốc.

3. **Bước 3: Kiểm tra tính sẵn sàng của kho thuốc**
   - Dược sĩ kiểm tra tồn kho thuốc thực tế trên hệ thống.
   - *Rẽ nhánh*: Nếu thiếu thuốc hoặc thuốc hết hàng đột xuất, liên hệ bác sĩ để đổi sang biệt dược tương đương hoặc thuốc cùng nhóm điều trị; Nếu đủ thuốc, chuyển tiếp.

4. **Bước 4: Xác nhận quyền lợi thanh toán / Bảo lãnh viện phí**
   - Kiểm tra trạng thái thanh toán của người bệnh:
     + Trường hợp người bệnh tự chi trả đã thanh toán qua App MyVinmec: Hệ thống xác nhận "Đã thanh toán".
     + Trường hợp thanh toán trực tiếp: Người bệnh đến quầy Thu ngân quẹt thẻ/tiền mặt.
     + Trường hợp Bảo hiểm tư nhân (BHTN): Nhân viên gửi thông tin thuốc cần bảo lãnh sang cổng phê duyệt điện tử của công ty bảo hiểm; Nhận kết quả bảo lãnh (Chấp thuận toàn bộ / Đồng chi trả / Từ chối).

5. **Bước 5: Soạn thuốc và xử lý hệ thống song song (Parallel Split & Join)**
   - *Nhánh song song 1 (Soạn thuốc vật lý)*: Dược sĩ kho lẻ lấy đúng loại thuốc, quy cách đóng gói, kiểm tra ngày sản xuất và hạn sử dụng (EXP Date), dán tem nhãn phụ ghi rõ liều dùng (sáng/trưa/chiều/tối, trước/sau ăn) bằng tiếng Việt cho từng hộp/vỉ thuốc.
   - *Nhánh song song 2 (Xử lý hệ thống & Tài chính)*: Hệ thống quản lý kho Dược tự động khóa trừ số lượng thuốc khỏi kho lẻ, ghi nhận dữ liệu kế toán và xuất biên lai / hóa đơn điện tử gửi về email/App người bệnh.
   - *Hội tụ (Parallel Join)*: Khi cả khay thuốc vật lý đã soạn xong và chứng từ/biên lai điện tử đã sẵn sàng, khay thuốc được chuyển sang bàn kiểm soát phát thuốc.

6. **Bước 6: Kiểm tra chéo độc lập (Independent Double-Check)**
   - Dược sĩ phát thuốc tiến hành kiểm tra độc lập đối chiếu giữa đơn thuốc trên màn hình và gói thuốc thực tế: Đúng người bệnh, đúng thuốc, đúng hàm lượng, đúng số lượng, đúng bao bì tem nhãn và hạn dùng.
   - Nếu phát hiện sai sót: Gửi trả lại dược sĩ soạn thuốc để điều chỉnh ngay lập tức.

7. **Bước 7: Gọi số và định danh người bệnh (JCI Patient Identification)**
   - Hệ thống âm thanh và màn hình LED gọi số thứ tự của người bệnh đến quầy phát thuốc số tương ứng.
   - Dược sĩ phát thuốc yêu cầu người bệnh/thân nhân xác nhận 2 thông tin định danh: **Họ và tên đầy đủ** và **Ngày tháng năm sinh** (đối chiếu với thông tin trên hệ thống và thẻ khám/CMND/CCCD/VNeID).

8. **Bước 8: Tư vấn sử dụng thuốc và bàn giao (Medication Counseling)**
   - Dược sĩ giải thích cặn kẽ cho người bệnh công dụng của từng loại thuốc, thời điểm uống thuốc, các tác dụng không mong muốn có thể gặp và cách bảo quản.
   - Nhấn mạnh các lưu ý đặc biệt (ví dụ: không dùng chung với rượu bia, cần uống đủ nhiều nước, thuốc nhỏ mắt mở nắp chỉ dùng trong 15 ngày...).
   - Người bệnh ký xác nhận nhận thuốc trên màn hình cảm ứng hoặc ký vào phiếu xuất thuốc; Dược sĩ bàn giao toàn bộ túi thuốc kèm hóa đơn/hướng dẫn sử dụng. Quy trình kết thúc.

---

## 7. Điều kiện rẽ nhánh và Cổng điều kiện (Gateways)

1. **Gateway 1 (Exclusive - XOR)**: Đơn thuốc có cảnh báo tương tác thuốc / dị ứng không?
   - `[Có cảnh báo nguy cơ]`: Liên hệ bác sĩ kê đơn để tham vấn và hiệu chỉnh đơn.
   - `[An toàn / Không cảnh báo]`: Tiếp tục quy trình thẩm định.
2. **Gateway 2 (Exclusive - XOR)**: Bác sĩ đồng ý đổi thuốc hay xác nhận giữ nguyên chỉ định?
   - `[Bác sĩ đổi thuốc]`: Cập nhật đơn thuốc sửa đổi trên HIS.
   - `[Bác sĩ giữ nguyên & có giải trình lâm sàng]`: Ghi nhận lý do lâm sàng và tiếp tục.
3. **Gateway 3 (Exclusive - XOR)**: Tồn kho thuốc tại nhà thuốc có đáp ứng đủ số lượng không?
   - `[Đủ thuốc]`: Tiếp tục chuẩn bị thuốc.
   - `[Hết hàng / Thiếu số lượng]`: Đề xuất bác sĩ đổi biệt dược hoặc điều chuyển khẩn từ kho trung tâm.
4. **Gateway 4 (Exclusive - XOR)**: Hình thức thanh toán và bảo hiểm của người bệnh?
   - `[Tự chi trả qua App / Kiosk]`: Hệ thống xác nhận trực tuyến ngay lập tức.
   - `[Tự chi trả tại quầy]`: Hướng dẫn người bệnh sang quầy thu ngân.
   - `[Bảo lãnh bảo hiểm tư nhân - BHTN]`: Chuyển dữ liệu sang luồng bảo lãnh viện phí.
5. **Gateway 5 (Exclusive - XOR)**: Kết quả bảo lãnh bảo hiểm tư nhân?
   - `[Được bảo lãnh toàn phần]`: Hoàn tất thủ tục thanh toán bảo hiểm.
   - `[Bảo lãnh một phần / Từ chối]`: Người bệnh thanh toán phần đồng chi trả phát sinh.
6. **Gateway 6 (Parallel Split - AND)**: Tách luồng thực thi song song:
   - Nhánh A: Dược sĩ kho lẻ lấy thuốc, kiểm tra HSD, in và dán nhãn phụ.
   - Nhánh B: Hệ thống tự động trừ kho dược trên HIS và xuất hóa đơn VAT điện tử.
7. **Gateway 7 (Parallel Join - AND)**: Chờ cả khay thuốc thực tế và hóa đơn điện tử hoàn tất trước khi bàn giao sang quầy kiểm soát.
8. **Gateway 8 (Exclusive - XOR)**: Kết quả kiểm tra chéo (Double-check) có đạt tiêu chuẩn không?
   - `[Đạt 100%]`: Chuyển sang hàng chờ phát thuốc.
   - `[Phát hiện sai lệch]`: Trả lại khâu soạn thuốc để hiệu chỉnh ngay lập tức.
9. **Gateway 9 (Exclusive - XOR)**: Đơn thuốc có bao gồm thuốc cần hướng dẫn sử dụng thiết bị chuyên biệt (bình xịt hen, bút tiêm insulin) không?
   - `[Có thiết bị chuyên biệt]`: Dược sĩ đưa người bệnh vào góc tư vấn riêng để thực hành thao tác mẫu.
   - `[Thuốc uống / bôi thông thường]`: Tư vấn tiêu chuẩn tại quầy phát thuốc.

---

## 8. Đầu ra của quy trình (Outputs & Results)
- Gói thuốc hoàn chỉnh kèm tem hướng dẫn sử dụng tiếng Việt dán trên từng bao bì.
- Hóa đơn điện tử VAT / Biên lai thu viện phí gửi vào email và App MyVinmec.
- Dữ liệu tồn kho dược thời gian thực được trừ chính xác trên phần mềm HIS.
- Nhật ký ca bệnh ghi nhận thời điểm hoàn tất cấp phát thuốc và thông tin dược sĩ phụ trách.

---

## 9. Ma trận Phối hợp giữa các Bộ phận (RACI Matrix)

| Bước công việc | Người bệnh | Dược sĩ lâm sàng | Dược sĩ kho | Dược sĩ phát | Thu ngân / Bảo hiểm | Bác sĩ kê đơn | IT / HIS |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1. Nhận đơn thuốc | I | R | I | I | I | A | C |
| 2. Thẩm định lâm sàng | I | R/A | I | I | I | C | S |
| 3. Kiểm tra kho | I | R | C | I | I | I | S |
| 4. Thanh toán / Bảo lãnh | C | I | I | I | R/A | I | S |
| 5. Soạn thuốc & Trừ kho | I | I | R | I | I | I | S/A |
| 6. Kiểm tra chéo | I | I | C | R/A | I | I | I |
| 7. Định danh & Tư vấn phát thuốc | C | I | I | R/A | I | I | S |

*(R: Responsible - Người làm; A: Accountable - Người chịu trách nhiệm; C: Consulted - Người tham vấn; I: Informed - Người nhận thông tin; S: Support - Hệ thống hỗ trợ)*

---

## 10. Các vấn đề tiềm ẩn, Rủi ro và Điểm nghẽn (Pain points & Bottlenecks)

1. **Ùn ứ vào các khung giờ cao điểm (Peak Hours)**: Khung giờ 10:30 – 11:45 sáng khi phần lớn bệnh nhân kết thúc lượt khám và dồn về nhà thuốc, dẫn đến thời gian chờ tăng vọt lên 25–40 phút nếu thiếu nhân sự quầy.
2. **Nghẽn tại khâu bảo lãnh bảo hiểm tư nhân (BHTN)**: Một số công ty bảo hiểm yêu cầu chờ email chấp thuận hoặc xác nhận thủ công danh mục thuốc được chi trả, làm kéo dài thời gian chờ của người bệnh.
3. **Rủi ro sai sót tên biệt dược nhìn giống/đọc giống (LASA - Look Alike Sound Alike)**: Nguy cơ nhầm lẫn giữa các thuốc có tên hoặc bao bì tương tự nếu bỏ qua bước Double-check.
4. **Đổi thuốc do hết hàng**: Gây gián đoạn luồng công việc do phải liên lạc lại với bác sĩ khám khi bác sĩ đang khám ca bệnh tiếp theo.
