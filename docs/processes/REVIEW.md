# Review chéo 10 mô tả quy trình (T22)

- **Người review:** Huỳnh Duy Phúc (26410092). Ngày review: 20/11/2026, trên `main` commit `78316bf`.
- **Phạm vi:** `C1`–`C4`, `M1`–`M3`, `S1`–`S3` trong `docs/processes/`.
- **Cách review:** mở từng nguồn mà chính file trích (trang Vinmec, văn bản pháp luật, Bộ Y tế; ảnh sơ đồ trên trang Vinmec),
  đối chiếu từng ý. Chỉ ghi "sai" khi đã đọc nguồn. Phần nào nguồn không mở được thì ghi ở mục "Chưa kiểm được".
- **C3, C4 do người review viết** và phần sửa nằm ở PR #80: cần **Nguyễn Quang Hòa** review C3, C4 bản sau khi #80 merge.
  Người review: ____________, ngày: __/__/2026.
- **Số dòng** tính theo `main` commit `78316bf`, **trước** khi PR #80 merge. Sau khi #80 merge, số dòng trong các file sẽ lệch
  vài dòng; tìm theo nội dung được trích.

## 1. Tiêu chí

Rubric hạng mục 1 (Liệt kê quy trình) yêu cầu **≥ 3 quy trình quản lý, ≥ 3 cốt lõi, ≥ 3 hỗ trợ; mỗi quy trình có actor, các
bước, khách hàng, kết quả** (yêu cầu do nhóm trưởng nêu khi review PR #79). Nhóm có 3 quản lý (M1–M3), 4 cốt lõi (C1–C4),
3 hỗ trợ (S1–S3): **đạt số lượng**. Từng mô tả được review theo các tiêu chí:

**Bảng 1. Tiêu chí review**

| # | Tiêu chí | Căn cứ |
|---|---|---|
| 1 | Có actor, các bước, khách hàng, kết quả; đủ các mục còn lại của mẫu (Loại, Người phụ trách viết, Nguồn bằng chứng, Cổng điều kiện) | Rubric hạng mục 1; `docs/processes/_template.md` |
| 2 | Nguồn có link và ngày truy cập; mở được | `_template.md` (Nguồn bằng chứng); quy ước ghi nguồn |
| 3 | Ý gắn nguồn đúng với nguồn; ý chưa có nguồn đánh ⚠ hoặc ghi là giả định | Quy ước nhóm (các file C1–C4) |
| 4 | > 7 cổng điều kiện, có cặp split/join (để vẽ BPMN) | Checklist trong `.github/pull_request_template.md`; CONTRIBUTING mục 4 |
| 5 | Không có tên, chẩn đoán, ảnh người bệnh | Quy tắc bảo mật y tế trong file phân công |

## 2. Bảng tổng hợp

Ký hiệu: ✓ đạt · △ đạt một phần · ✗ chưa đạt.

**Bảng 2. Kết quả review 10 mô tả quy trình**

| Mã | Người viết | 1. Đủ mục | 2. Nguồn | 3. Đúng nguồn / ⚠ | 4. Cổng | Split/join | 5. Bảo mật | Kết luận |
|---|---|---|---|---|---|---|---|---|
| C1 | Cẩm Tố | ✓ | ✓ | △ (3 chỗ nhỏ) | 9 | ✓ (⚠) | ✓ | Sửa nhỏ |
| C2 | Tú Phương | ✓ | △ ([2] là trang danh sách) | △ (3 chỗ) | 9 | ✓ (⚠) | ✓ | Sửa nhỏ |
| C3 | Duy Phúc | ✓ | ✓ | △ (5 chỗ) | 11 | ✓ (⚠) | ✓ | Sửa nhỏ |
| C4 | Duy Phúc | ✓ | ✓ | △ (2 chỗ nhỏ) | 9 | ✓ (⚠) | ✓ | Sửa nhỏ |
| M1 | Quang Hòa | ✓ | ✓ | △ (2 chỗ) | 9 | ✓ | ✓ | Sửa nhỏ |
| M2 | Quang Hòa | ✓ | △ ([6] ghi "bản lưu" nhưng là trang đang chạy) | ✗ (4 chỗ, có mâu thuẫn QĐ 3869 / QĐ 56) | 8 | ✓ | ✓ | Cần sửa |
| M3 | Quang Hòa | ✓ | △ ([1] bị chặn khi truy cập tự động) | ✗ (6 chỗ lệch Thông tư 43/2018) | 10 | ✓ (2 cặp) | ✓ | Cần sửa |
| S1 | Hoàng Phát | △ (tên mục khác mẫu; kết quả chỉ có nhánh thành công) | ✗ (không có link, ngày truy cập) | ✗ | 9 | ✓ | ✓ | Cần sửa |
| S2 | Hoàng Phát | △ (như S1) | ✗ (link tuyển dụng không truy cập được) | ✗ | 10 | ✓ | ✓ | Cần sửa |
| S3 | Hoàng Phát | △ (như S1) | ✗ (không có link) | ✗ (sai số điều luật) | 9 | ✓ | ✓ | Cần sửa |

## 3. Chi tiết từng quy trình

### C1 – Khám ngoại trú

**Lệch nguồn (đã đọc nguồn):**
- Dòng 33, 58: gắn [1] cho "Lễ tân / quầy sao chụp giấy tờ". Trang chỉ ghi "Sao chụp các loại giấy tờ tùy thân, thẻ Bảo hiểm", không nói ai làm.
- Dòng 141 (cổng 8), nhánh "Từ chối: … về bước kết luận [1]": trang chỉ có "phiếu từ chối thực hiện"; sơ đồ không vẽ nhánh từ chối.
- Dòng 32, "đến trực tiếp … [1]": trang không nói đến khám không hẹn trước (dòng 56 đã có ⚠, dòng 32 chưa).

**Đúng nguồn:** mô tả sơ đồ (dòng 20–24, 94–96) và bảng đối chiếu 8 bước (dòng 104–111) khớp ảnh sơ đồ Vinmec.

**Gợi ý:** C1 dẫn câu 22 cho hội chẩn, chuyển viện (dòng 39, 84, 89, 122, 140). Câu 22 trong `interviews/questions.md` là
câu dự phòng, chỉ hỏi số ca chuyển **nhập viện**. Cần thêm câu hỏi riêng về hội chẩn, chuyển viện (Tường Vy, T18), sau đó
C1 cập nhật lại số câu.

### C2 – Cận lâm sàng

**Lệch nguồn (đã đọc nguồn):**
- Dòng 80–81: "ký thêm thanh toán bảo hiểm [3][4]". [3] có nói; [4] không có, nên bỏ [4].
- Cổng 4 (dòng 140) và dòng 170, "đã thanh toán **hoặc bảo lãnh** chưa?", không có ⚠. Theo [4], bảo lãnh làm **sau** khi khám
  xong; trước khi làm dịch vụ người bệnh "đóng tạm ứng". Nên đổi thành "đã thanh toán / tạm ứng chưa" hoặc gắn ⚠.
- Dòng 95–96: theo bảng so sánh gói trên [5], gói nữ **tiêu chuẩn** đã có xét nghiệm HPV; tế bào học (Liqui Prep) và PSA
  (gói nam) chỉ có ở gói nâng cao và toàn diện. Câu cũ dễ hiểu là HPV chỉ có từ gói nâng cao.

**Thiếu [n] hoặc ⚠:**
- Bảng Actor dòng 41–48: KTV đọc hình, KTV lấy mẫu, Thu ngân.
- Dòng 35: xếp nội soi vào "thăm dò chức năng". [1] tách nội soi thành nhóm riêng.
- Dòng 121–123: các kết quả ra về, tái khám, nhập viện. Có trong sơ đồ [3] nhưng chưa gắn [3].
- Dòng 115, 125; cổng 5 và 8 (dòng 141, 144).

**Nguồn:** [2] là trang danh sách bài viết, nên dẫn thẳng bài "Khám lâm sàng là gì?". [3], [4] chưa ghi ngày cập nhật
(trang ghi 19/10/2026 và 09/05/2026).

### C3 – Thanh toán, bảo lãnh bảo hiểm

**Lệch nguồn (đã đọc nguồn):**
- Dòng 31, 57: gắn [1] cho "Quầy bảo hiểm gửi yêu cầu bảo lãnh". Nguồn chỉ ghi Vinmec liên hệ công ty bảo hiểm.
- Dòng 30, 64: gắn [1] cho "Thu ngân hoàn tạm ứng". Nguồn chỉ ghi bệnh viện hoàn trả.
- Dòng 68: trang chỉ khuyên liên hệ khi khám ngoài giờ hành chính, ngày nghỉ, lễ. Trang không khuyên gọi để xác nhận cơ sở có khám BHYT hay không.
- Dòng 84: "trái tuyến được hưởng tỉ lệ thấp hơn" chưa đúng mọi trường hợp. Ở cơ sở chuyên sâu, có trường hợp ngoại trú vẫn
  được 100% mức hưởng.
- Dòng 96: Bước 7–8 đang đánh ⚠ "nhiều khả năng nội trú", nhưng sơ đồ [4] ghi rõ "Tạm ứng nhập viện", "Thanh toán ra viện".
  Có thể bỏ ⚠ và dẫn [4].

**Thiếu [n] hoặc ⚠:** dòng 101–103, 107 (các kết quả); các cổng 1–3, 5–7, 11. Cổng 7 (thu thêm / hoàn / vừa đủ) là suy luận,
cần ⚠.

### C4 – Đặt lịch khám

**Lệch nguồn (nhỏ):**
- Dòng 29: gắn việc "liên hệ lại khách gửi form" cho Tổng đài / CSKH. Nguồn chỉ ghi "chúng tôi sẽ liên hệ".
- Dòng 43–51: kênh MyVinmec gắn [1] dựa vào phần chân trang của [1]; nên dẫn [4] là chính.

**Thiếu ⚠:** cổng 4 nhánh "Không (chọn lại)" (bước 6 đã có ⚠); cổng 5 nhánh "Sửa lại". Nguồn [2] chỉ có bước "xác nhận".

### M1 – Lập lịch bác sĩ

**Lệch nguồn (đã đọc nguồn):**
- Dòng 50, 84: "tổng đài báo người bệnh khi bác sĩ đổi lịch [2]". [2] chỉ nói tư vấn viên gọi xác nhận thông tin đặt khám. Bỏ [2],
  giữ ⚠.
- Dòng 47: Điều 70 khoản 4 giao việc phân công người trực cho **người đứng đầu cơ sở**, không nhắc Phòng KHTH.

**Thiếu [n] hoặc ⚠:** dòng 39, 49 ("sinh khung giờ trống" là suy luận), 77, 83.

### M2 – Đánh giá KPI

**Lệch nguồn (đã đọc nguồn):**
- Dòng 61 (không có ⚠) và dòng 99: "Hội đồng QLCL phê duyệt / quyết định đề án [1, Điều 11]". Thông tư 19/2013 Điều 11:
  Hội đồng **đề xuất**, Giám đốc **phê duyệt**.
- Dòng 63: nhiệm vụ của mạng lưới QLCL nằm ở **Điều 15**, không phải Điều 10. Không điều nào nói việc phát phiếu.
- Dòng 86–87: cỡ mẫu khảo sát lấy theo QĐ 3869, nhưng [3] (QĐ 3652) ghi khảo sát hài lòng ngoại trú theo **QĐ 56/2024**.
  Chính dòng 29 của file cũng ghi QĐ 56 thay mẫu của QĐ 3869. Cần thống nhất.

**Thiếu [n] hoặc ⚠:** dòng 52–54 (KPI hiệu suất, tài chính để trống căn cứ); dòng 5–6 (kỳ đánh giá).

**Chưa kiểm được:** dòng 51 (RCA 60 ngày, Thông tư 43/2018 không có trong danh sách nguồn của M2); dòng 47 (cách tính theo QĐ 56,
nguồn [9] chỉ là bài báo). Nguồn [6] ghi "bản lưu 25/01/2026" nhưng link trỏ tới trang đang chạy.

### M3 – Quản lý sự cố y khoa

Nguồn [1] (Thông tư 43/2018) bị chặn khi truy cập tự động. Toàn văn được đối chiếu qua bản sao khác, cần mở lại link gốc để xác nhận.

**Lệch nguồn:**
- Dòng 83–84: theo Điều 5.3a, **trưởng khoa** báo cáo lãnh đạo cơ sở. File ghi QLCL báo giám đốc.
- Dòng 56, 96, cổng 7: Điều 8.1b không giới hạn RCA theo mức NC2/NC3. Nhóm chuyên gia phân tích theo danh sách bộ phận QLCL
  đề xuất.
- Dòng 66: "không bị quy lỗi cá nhân [1, Điều 3, 12]". Hai điều này chỉ nói khuyến khích, bảo vệ, giữ bí mật danh tính.
- Dòng 31: Điều 2.2 định nghĩa near-miss là sự cố "đã xảy ra nhưng chưa gây hậu quả hoặc gần như xảy ra". File ghi "chưa xảy ra",
  hẹp hơn.
- Dòng 39: Phụ lục I ghi "kéo dài thời gian **nằm viện**", file ghi "điều trị".
- Dòng 56, 102: Điều 8 không nói giám đốc phê duyệt khuyến cáo.

**Đúng nguồn:** mốc 60 ngày, báo điện thoại trong 1 giờ, tổng hợp 6 tháng/lần, phân loại theo 3 tiêu chí, Luật KBCB các điều trích,
Thông tư 19 các điều trích.

**Thiếu [n] hoặc ⚠:** dòng 7, 67, 81, 113, 114, 119.

### S1 – Cấp phát thuốc

**Lệch nguồn (đã đọc nguồn):**
- Dòng 29: quy tắc "ít nhất 2 định danh" thuộc **IPSG.1** *Identify Patients Correctly*, không phải MMU (dòng 13 ghi đúng
  IPSG); ví dụ định danh gồm họ tên, mã định danh, ngày sinh, không dùng số phòng (JCI Standards for Hospitals bản 5,
  trang mẫu công khai trên digitalassets.jointcommission.org).
- Dòng 30: trang Vinmec "Thủ tục thanh toán bảo hiểm" không có con số "hơn 30 công ty bảo hiểm".
- Dòng 30: bài MyVinmec không nhắc nhận đơn thuốc điện tử.
- Dòng 14: mục tiêu ≤ 10 phút mâu thuẫn với trang bảo hiểm Vinmec (bảo lãnh 15–45 phút) khi người bệnh dùng bảo hiểm tư nhân.

**Không có nguồn, chưa đánh dấu:** dòng 14, 42–44 (3 dược sĩ, mâu thuẫn giả định 2 dược sĩ ở dòng 35), 47 ("LIS" là hệ thống
xét nghiệm), 71–72, 76, 85, 87, 91, 99, 105, 119, 121, 135, 142, 166, 167.

**Cấu trúc:** mục 2.1 không có link và ngày truy cập. Mục 8 chỉ có kết quả thành công (thiếu: bảo lãnh bị từ chối, không lấy thuốc,
đơn bị hủy, sửa). Cổng 2, 9 không có bước tương ứng ở mục 6. Phạm vi có BHYT (dòng 19) nhưng cổng 4 không có nhánh BHYT.

**Căn cứ pháp lý hết hiệu lực (đã đọc văn bản):** dòng 28 dẫn Thông tư 52/2017 và 18/2018 về kê đơn. Thông tư 26/2025/TT-BYT
(bản ký số) Điều 13 khoản 2 ghi hai thông tư này hết hiệu lực từ 01/07/2025; khoản 3 yêu cầu bệnh viện kê đơn điện tử trước
01/10/2025.

### S2 – Tuyển dụng và đào tạo

**Lệch nguồn (đã đọc nguồn):** dòng 31 ghi thử việc 60 ngày (bác sĩ) / 30 ngày (điều dưỡng, KTV) "theo đúng Bộ luật Lao động".
Điều 25 BLLĐ 2019 chỉ quy định mức **tối đa**: không quá 60 ngày nếu trình độ từ cao đẳng trở lên; 30 ngày cho trung cấp.
Điều dưỡng, KTV có bằng cao đẳng trở lên vẫn thuộc mức 60 ngày.

**Không có nguồn, chưa đánh dấu:** dòng 5, 18, 26 (các mục JCI không có link), 70–71, 78, 82, 85, 100, 117, 126, 164.

**Chưa kiểm được:** dòng 27, `careers.vinmec.com` không truy cập được.

**Gợi ý:** thứ tự ở dòng 85–86 (khám sức khỏe trước rồi gửi offer) ngược với cổng 6 dòng 123. Mục 8 thiếu các kết thúc không thành công.

### S3 – Giải quyết khiếu nại

**Lệch nguồn (đã đọc nguồn):** dòng 26 ghi "Điều 8" Luật KBCB 15/2023 quy định quyền được tôn trọng danh dự và quyền khiếu nại.
Theo luật: Điều 8 là "Người đại diện của người bệnh"; quyền danh dự ở **Điều 10**; quyền kiến nghị ở **Điều 14**. Không điều
nào trong Điều 9–15 dùng chữ "khiếu nại, tố cáo".

**Thiếu căn cứ:** file không trích Luật Khiếu nại 2011 hay văn bản hướng dẫn. Dòng 27 dẫn Thông tư 43/2018, nhưng văn bản này
nói về sự cố y khoa, không phải khiếu nại.

**Không có nguồn, chưa đánh dấu:** dòng 15 (các mốc 2 giờ / 24 giờ / 72 giờ / 7 ngày làm việc; lặp lại ở dòng 114, 120),
19, 29, 70, 93–94, 118, 167.

**Chưa kiểm được:** dòng 28 (mục JCI PFR.2, QPS.7: không có trong trang mẫu công khai của JCI, bản đầy đủ phải trả phí), dòng 29 (khảo sát CSAT qua MyVinmec, không có link).

**Gợi ý:** mục 8 thiếu kết thúc khi người bệnh không đồng thuận hoặc chuyển cấp cao (cổng 8).

## 4. Đã sửa theo nguồn ở PR #80

Người review đã sửa các chỗ **lệch nguồn** ở mục 3 (đã đọc nguồn), chỉ đổi câu chữ và trích dẫn, không đổi cấu trúc:
C1 (dòng 32, 33, 58, 141), C2 (bảng thuật ngữ, bước 5, gói khám, cổng 4, liên kết C3), C3 (Actor, bước 6, 10, ghi chú BHYT, mức hưởng,
bước 16), C4 (dòng 29, 46), M1 (Actor), M2 (nguồn [6], Actor, bước 4, 10), M3 (định nghĩa near-miss, NC2, Actor, luồng báo cáo
bắt buộc, RCA, bước 10, cổng 7), S1 (mục 2.1: Thông tư 26/2025, IPSG.1, trang bảo hiểm Vinmec), S2 (giả định 2), S3 (mục 2.1, mục tiêu thời gian).

Phần **thiếu [n] / ⚠**, **chưa kiểm được** và **gợi ý** ở mục 3 chưa sửa, để người viết quyết định.

## 5. Việc cần làm

Các việc còn lại sau khi đã sửa ở mục 4:

**Bảng 3. Việc còn lại của từng người viết**

| Người viết | Quy trình | Việc còn lại |
|---|---|---|
| Hoàng Phát | S1, S2, S3 | Thêm link và ngày truy cập cho nguồn; bổ sung căn cứ pháp lý về khiếu nại (S3); gắn ⚠ hoặc chuyển vào "Giả định" các chi tiết chưa có nguồn; bổ sung kết quả không thành công |
| Quang Hòa | M1, M2, M3 | Gắn [n] / ⚠ cho các dòng ở mục 3; chốt mẫu và cỡ mẫu khảo sát (QĐ 3869 / QĐ 56) |
| Tú Phương | C2 | Gắn [n] / ⚠ cho bảng Actor và kết quả |
| Tường Vy | T18 (bộ câu hỏi) | Thêm câu hỏi phỏng vấn về hội chẩn, chuyển viện |
| Cẩm Tố | C1 | Cập nhật số câu hỏi ở dòng 39, 84, 89, 122, 140 sau khi Tường Vy thêm câu hỏi |
| Duy Phúc | C3, C4 | Gắn [n] / ⚠ cho các cổng; nhờ Quang Hòa review bản sau #80 và ghi tên, ngày ở đầu file |

## 6. Nguồn đã đối chiếu

Các văn bản mà PR #80 dẫn đều đã mở và đọc toàn văn điều được trích (truy cập 20/11/2026):

**Bảng 4. Văn bản pháp luật, tiêu chuẩn và trang web đã đối chiếu**

| Văn bản | Điều đã đọc | Nguồn công khai |
|---|---|---|
| Luật Khám bệnh, chữa bệnh 15/2023/QH15 | Điều 8 (người đại diện của người bệnh), Điều 10 (tôn trọng danh dự, bí mật riêng tư), Điều 14 (kiến nghị và bồi thường) | https://hethongphapluat.com/luat-kham-benh-chua-benh-2023/dieu-8, `/dieu-10`, `/dieu-14` |
| Luật Khám bệnh, chữa bệnh 15/2023/QH15 | Điều 70 (trực khám bệnh, chữa bệnh) | Văn bản hợp nhất 26/VBHN-VPQH: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf |
| Bộ luật Lao động 45/2019/QH14 | Điều 25 (thời gian thử việc) | https://hethongphapluat.com/bo-luat-lao-dong-2019/dieu-25 |
| Thông tư 19/2013/TT-BYT | Điều 10 (hệ thống QLCL, Giám đốc làm chủ tịch hội đồng), Điều 11 khoản 2 điểm a, d (Hội đồng đề xuất đề án với Giám đốc; đề án do Giám đốc phê duyệt), Điều 15 (nhiệm vụ mạng lưới QLCL) | https://caselaw.vn/van-ban-phap-luat/265779-thong-tu-19-2013-tt-byt-huong-dan-thuc-hien-quan-ly-chat-luong-dich-vu-kham-chua-benh-tai-benh-vien-do-bo-truong-bo-y-te-ban-hanh |
| Thông tư 43/2018/TT-BYT | Điều 2, 3, 5, 8, 11, 12, Phụ lục I | Link gốc trên thuvienphapluat chặn truy cập tự động; đã đọc bản toàn văn tại https://docs.google.com/document/d/1F8_12ASslAz3bTrAuVNFadGVZX9fWlul (cần mở link gốc để xác nhận) |
| Thông tư 26/2025/TT-BYT | Điều 13 (hiệu lực, thay thế Thông tư 52/2017, 18/2018; lộ trình kê đơn điện tử) | Bản ký số (xem `docs/tai-lieu-tham-khao.md`, mục 6) |
| Thông tư 01/2025/TT-BYT | Tên văn bản, ngày ban hành | https://caselaw.vn/van-ban-phap-luat/413093-thong-tu-so-01-2025-tt-byt-ngay-01-01-2025-cua-bo-truong-bo-y-te-huong-dan-luat-bao-hiem-y-te |
| JCI Accreditation Standards for Hospitals, 5th ed. | IPSG.1 (trang mẫu công khai) | https://digitalassets.jointcommission.org/api/public/content/assets/1/14/jcih14_sample_pages.pdf |
| Trang Vinmec | Quy trình khám chữa bệnh (kèm ảnh sơ đồ), Thủ tục thanh toán bảo hiểm, Câu hỏi thường gặp BHYT, Dịch vụ Sức khỏe tổng quát, Xét nghiệm cận lâm sàng là gì | Link ở mục Nguồn bằng chứng của từng file |

Danh mục chung: `docs/tai-lieu-tham-khao.md` (đã bổ sung Bộ luật Lao động 2019, Thông tư 01/2025, Thông tư 26/2025, JCI, sách Dumas).
