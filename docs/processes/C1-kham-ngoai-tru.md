# C1 – Khám ngoại trú

- **Loại:** Cốt lõi
- **Người phụ trách viết:** Nguyễn Thị Cẩm Tố (26410134)
- **Phạm vi:** từ lúc người bệnh đến khám (đặt lịch trước hoặc đến trực tiếp) đến khi bác sĩ kết luận,
  người bệnh hoàn tất thanh toán và rời khu khám ngoại trú. C1 là quy trình khung; ba đoạn chi tiết nằm ở quy trình
  khác: **C4** (đặt lịch, đến check-in), **C2** (thực hiện cận lâm sàng), **C3** (xác minh hình thức chi trả, bảo lãnh,
  thanh toán). Không gồm điều trị nội trú sau khi nhập viện.
- **Nguồn bằng chứng:**
  1. Vinmec – *Quy trình khám chữa bệnh tại Vinmec* (cập nhật 19/10/2026), truy cập 20/11/2026:
     https://www.vinmec.com/vie/bai-viet/quy-trinh-kham-chua-benh-tai-vinmec-vi
     (đường dẫn rút gọn `https://www.vinmec.com/huong-dan-khach-hang/quy-trinh-kham-chua-benh-tai-vinmec/` chuyển về trang này).
  2. Mô tả C4 Đặt lịch khám (nhóm, nguồn Vinmec truy cập 17/11/2026): `docs/processes/C4-dat-lich.md`.
  3. Mô tả C2 Cận lâm sàng (nhóm, truy cập 18/11/2026): `docs/processes/C2-can-lam-sang.md`.
  4. Mô tả C3 Thanh toán, bảo lãnh (nhóm, truy cập 17/11/2026): `docs/processes/C3-thanh-toan-bao-hiem.md`.
  5. Mô tả M1 Lập lịch bác sĩ (giờ làm việc khu ngoại trú Central Park, nguồn Vinmec cập nhật 19/10/2026):
     `docs/processes/M1-lap-lich-bac-si.md`.
  6. Phỏng vấn bác sĩ, điều dưỡng, lễ tân, thu ngân (T24–T26, tuần 2) – *chưa thực hiện*.
  7. Vinmec – *Thủ tục thanh toán bảo hiểm tại Vinmec* (cập nhật 09/05/2026), truy cập 27/11/2026:
     https://www.vinmec.com/vie/bai-viet/huong-dan-thu-tuc-thanh-toan-bao-hiem-tai-vinmec-vi

> Nguồn [1] là hướng dẫn chung của hệ thống Vinmec, không riêng Vinmec Central Park. Trang gồm một **sơ đồ** (khách hàng
> cũ, mới, tái khám → đăng ký, mở hồ sơ; "tổng đài đặt hẹn và cung cấp thông tin" đi thẳng vào bước tiếp theo → bốt điều dưỡng,
> phòng khám phân loại → bác sĩ khám, tư vấn → thanh toán hoặc chỉ định cận lâm sàng, thủ thuật → thanh toán → bác sĩ đọc,
> giải thích kết quả → ra về (tái khám quay về bốt điều dưỡng) hoặc nhập viện) và danh sách
> chứng từ phải ký ở 8 bước đánh số. Sơ đồ **không có** đo sinh hiệu, nhận biết cấp cứu, hội chẩn, chuyển viện, thời gian
> chờ và nơi thực hiện từng bước. Những phần đó lấy từ kế hoạch mô hình hóa của nhóm và đánh dấu **⚠** (chưa có nguồn
> công khai), cần xác minh qua phỏng vấn T24–T26 (mã câu hỏi trong
> `interviews/questions.md` ghi ở từng mục; dấu hiệu cấp cứu, làm song song và khoản phát sinh chưa có câu hỏi riêng,
> mã ghi ở các mục đó là câu dùng để hỏi dò).

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Người bệnh / người giám hộ | Cung cấp giấy tờ, ký phiếu, đi theo chỉ định, thanh toán [1]; đặt lịch hoặc đến trực tiếp không hẹn trước ⚠ (QL01). Trang chỉ nhắc giấy khai sinh với trẻ em, không nhắc người giám hộ ⚠ (QL08) |
| Lễ tân (Quầy tiếp đón) | Mở hồ sơ khách mới [1]. Sao chụp giấy tờ, check-in, định danh, kiểm tra thẻ BHYT, hẹn lịch tái khám ⚠ (trang không nói ai sao chụp, ai định danh; QL08) |
| Điều dưỡng | Phân loại, đo sinh hiệu, nhận biết dấu hiệu cấp cứu, hướng dẫn người bệnh đến đúng phòng ⚠ (QL06, QL07) |
| Bác sĩ | Khám, chỉ định cận lâm sàng, đọc kết quả, kết luận, kê đơn, hẹn tái khám, chỉ định nhập viện hoặc chuyển viện ⚠ (QL06, QN02, QN03, QLHC08) |
| Kỹ thuật viên xét nghiệm, chẩn đoán hình ảnh | Thực hiện cận lâm sàng (chi tiết ở C2) |
| Thu ngân | Thu tiền, lập bảng kê, biên lai (chi tiết ở C3) ⚠ (trang chỉ nêu chứng từ, không nêu người thu; QL08) |
| Nhà thuốc bệnh viện | Cấp thuốc theo đơn (chi tiết ở S1) |
| Khoa chuyên khoa khác, bệnh viện tuyến trên *(bên ngoài C1)* | Nhận người bệnh hội chẩn hoặc chuyển viện ⚠ (QLHC06, QLHC08) |
| Quầy bảo hiểm, công ty bảo hiểm, cơ quan BHXH *(bên ngoài)* | Xác minh và chi trả theo hình thức bảo hiểm (chi tiết ở C3) |

## Khách hàng của quy trình

| Khách hàng | Loại |
|---|---|
| Người bệnh ngoại trú: người lớn, và trẻ em qua người giám hộ | Chính, nhận dịch vụ khám và kết luận điều trị |
| Người nhà, người giám hộ | Liên quan, thay trẻ em hoặc người bệnh yếu làm thủ tục và ký phiếu |
| Khoa khám bệnh, nhà thuốc, khoa cận lâm sàng | Nội bộ, nhận chỉ định và dữ liệu từ lượt khám |
| Công ty bảo hiểm, cơ quan BHXH | Bên ngoài, nhận hồ sơ chi phí của lượt khám (qua C3) |

## Các bước (mô tả bằng lời)

**A. Tiếp đón và mở hồ sơ**

1. Người bệnh **đến khám** (khách cũ, khách mới hoặc tái khám [1]): đã đặt lịch qua tổng đài hoặc kênh khác (C4, chuyển giao
   ở bước check-in) hoặc đến trực tiếp không hẹn trước ⚠ (QL01).
2. Tại **Quầy tiếp đón**: khách mới mở hồ sơ, cung cấp họ tên, giấy tờ tùy thân (CCCD/CMND/hộ chiếu, trẻ em dùng giấy
   khai sinh), thẻ bảo hiểm và thẻ ưu đãi nếu có, điền **phiếu đăng ký (01 bản)**, sao chụp giấy tờ tùy thân, thẻ bảo hiểm [1]
   (trang không nói ai sao chụp ⚠).
   Khách cũ dùng hồ sơ có sẵn, khách đặt lịch online đã có thông tin trên hệ thống (C4) ⚠ (QL01, QL08).
3. **Định danh** bằng ít nhất 2 thông tin: họ tên đầy đủ, ngày sinh, kèm mã PID nếu cần; thực hiện trước mọi lần thăm
   khám hoặc can thiệp y tế [1].
4. **Xác minh hình thức chi trả** (tự chi trả, BHYT, bảo hiểm tư nhân) và kiểm tra thẻ → chi tiết thủ tục, bảo lãnh,
   tạm ứng ở **C3** (phần A, B của C3). Với bảo hiểm tư nhân có bảo lãnh trực tiếp, người bệnh **đóng tạm ứng** rồi dùng
   dịch vụ; mức tạm ứng tính theo chỉ định ban đầu của bác sĩ [7] (⚠ thời điểm đóng so với lúc khám; phỏng vấn T25).
   C1 chỉ ghi nhận kết quả để biết nhánh thanh toán cuối lượt khám.

**B. Phân loại và đo sinh hiệu**

5. Người bệnh **chờ đo sinh hiệu**, điều dưỡng **đo sinh hiệu** (mạch, huyết áp, cân nặng… theo danh mục ghi thời gian
   của nhóm) ⚠ (QL06, QL07). Sơ đồ Vinmec có bước "Bốt điều dưỡng, phòng khám phân loại người bệnh" ngay sau đăng ký [1]; nhân viên và nội dung đo
   chưa nêu.
6. Nếu có **dấu hiệu cấp cứu**, chuyển ngay xử trí cấp cứu, bỏ qua các bước chờ còn lại ⚠ (QL06, QL07).

**C. Khám và chỉ định**

7. Người bệnh **chờ khám**, bác sĩ **khám, tư vấn** (khám lần 1) [1]; thời gian chờ và nội dung khám ⚠ (QL06, QN02).
8. Bác sĩ quyết định có **cần cận lâm sàng, thủ thuật** không [1]. Nếu không → sang bước 14; tỉ lệ có chỉ định ⚠ (QN03).
9. Nếu cần: bác sĩ **chỉ định**; người bệnh ký **phiếu đồng ý** làm xét nghiệm HIV, phiếu đồng ý thực hiện chẩn đoán
   (nếu có) hoặc **phiếu từ chối** thực hiện (01 bản) [1].
10. **Thanh toán chỉ định** trước khi thực hiện (Bước 4 của Vinmec) [1]: ký chứng từ thanh toán (02 bảng kê + 01 biên lai
    thu tiền viện phí) và ký thanh toán bảo hiểm (01 bản, nếu dùng bảo hiểm tư nhân) → chi tiết ở **C3**.
11. **Thực hiện cận lâm sàng** → chi tiết ở **C2**. Tùy chỉ định: chỉ xét nghiệm, chỉ chẩn đoán hình ảnh, hoặc cả hai. Khi
    bác sĩ chỉ định cả xét nghiệm và chẩn đoán hình ảnh, hai hạng mục có thể làm **song song** ⚠ (QN08).
12. Người bệnh **chờ kết quả**; kết quả trả cho bác sĩ bằng hệ thống, giấy hoặc cả hai ⚠ (QL03, QN08).
13. Bác sĩ **khám lần 2, đọc và giải thích kết quả** [1]. Nếu cần thêm thông tin: chỉ định bổ sung (quay lại bước 9).
    Nếu không, bác sĩ xét có cần **hội chẩn chuyên khoa khác** trước khi kết luận. Sơ đồ Vinmec không có vòng chỉ định bổ sung lẫn hội chẩn ⚠ (QN03, QLHC06).

**D. Kết luận**

14. Bác sĩ **kết luận**: **ra về** hoặc **nhập viện** nội khoa, phẫu thuật, thủ thuật [1]; **chuyển chuyên khoa, chuyển viện**
    không có trên trang Vinmec ⚠ (QLHC08). Khi ra về, đơn thuốc là "(nếu có)", còn **tái khám** đi ra từ "Ra về" rồi quay về
    bốt điều dưỡng, phòng khám phân loại người bệnh [1].
15. Có đơn thuốc: người bệnh **lĩnh thuốc** tại nhà thuốc bệnh viện hoặc mua nơi khác ⚠ (khảo sát người bệnh câu 6, 11) → chi tiết ở **S1**.

**E. Thanh toán và kết thúc**

16. **Thanh toán** trước khi ra về, theo sơ đồ Vinmec [1]: nếu **không làm cận lâm sàng**, thanh toán sau khám (Bước 2 của
    Vinmec) với cùng bộ chứng từ; nếu **có cận lâm sàng**, khoản chính đã thanh toán ở bước 10 (Bước 4), sơ đồ không vẽ
    thanh toán thêm sau khi đọc kết quả. Chi phí phát sinh sau chỉ định ⚠ (QN09) → chi tiết ở **C3**.
    Với bảo lãnh trực tiếp, sau khi khám xong Vinmec liên hệ công ty bảo hiểm để bảo lãnh viện phí, rồi người bệnh ký thư
    bảo lãnh và thanh toán phần ngoài phạm vi (nếu có) [7].
    Ca **nhập viện, chuyển viện**: tạm ứng nhập viện và thanh toán ra viện (Bước 7, 8) thuộc nội trú, ngoài C1 [1]. Khoản
    ngoại trú và tạm ứng đã đóng của hai loại ca này xử lý thế nào thì chưa có nguồn, BPMN chưa mô hình hóa ⚠ (QLHC09).
17. Người bệnh nhận chứng từ, đơn thuốc, lịch hẹn (nếu có) và **rời khu khám** → kết thúc C1.

### Đối chiếu với trang Vinmec

Trang [1] đánh số 8 bước theo chứng từ cần ký, gắn vào sơ đồ. Bước 1–4 thuộc luồng ngoại trú và dùng trong C1; Bước 5–8 là
nhập viện (nội trú) nên **không đưa vào C1**.

| Bước trang Vinmec [1] | Chứng từ | Ứng với bước C1 |
|---|---|---|
| Bước 1 | Phiếu đăng ký (01 bản), sao chụp giấy tờ tùy thân, thẻ bảo hiểm | 2 |
| Bước 2 | Chứng từ thanh toán (02 bảng kê, 01 biên lai), thanh toán bảo hiểm (01 bản, nếu bảo hiểm tư nhân) | 16: thanh toán sau khám khi không có cận lâm sàng (sơ đồ: "Thanh toán (Bước 2)" trên nhánh đơn thuốc) |
| Bước 3 | Phiếu đồng ý xét nghiệm HIV, phiếu đồng ý thực hiện chẩn đoán, hoặc phiếu từ chối | 9 |
| Bước 4 | Chứng từ thanh toán, thanh toán bảo hiểm | 10: thanh toán chỉ định cận lâm sàng, thủ thuật (sơ đồ: "Thanh toán (Bước 4)") |
| Bước 5–6 | Phiếu yêu cầu sử dụng dịch vụ (02 bản), phiếu đồng ý điều trị (01 bản) | Nhập viện nội khoa (Bước 5), nhập viện phẫu thuật, thủ thuật (Bước 6): nội trú, ngoài C1 |
| Bước 7–8 | Cam kết thanh toán, phiếu xác nhận giờ nhận và trả phòng, phiếu xác nhận bồi thường | Tạm ứng nhập viện (Bước 7), thanh toán ra viện (Bước 8): nội trú, ngoài C1 |

Cách ghép trên đọc trực tiếp từ sơ đồ [1]. Việc có thanh toán thêm sau khi đọc kết quả (ví dụ tư vấn thêm, thuốc) sơ đồ không
nêu ⚠ (QL08, QN09).

## Các kết quả có thể

- **Ra về, điều trị ngoại trú:** bác sĩ kết luận, người bệnh thanh toán, nhận đơn (nếu có) và ra về [1].
- **Ra về, có hẹn tái khám:** sơ đồ Vinmec vẽ nhánh "Tái khám" đi ra từ "Ra về", quay về bốt điều dưỡng, phòng khám phân loại người bệnh [1]. Việc đặt lịch
  hẹn cho lượt sau (liên kết C4) và nội dung lịch hẹn ⚠ (QL01).
- **Chỉ định nhập viện:** nhập viện nội khoa hoặc phẫu thuật, thủ thuật [1]; C1 kết thúc, chuyển sang quy trình nội trú (ngoài phạm vi đề tài).
- **Chuyển chuyên khoa hoặc chuyển viện:** người bệnh cần chuyên khoa khác hoặc tuyến trên ⚠ (QLHC06, QLHC08).
- **Xử trí cấp cứu:** có dấu hiệu cấp cứu khi đo sinh hiệu, thoát khỏi luồng khám thường ⚠ (QL06, QL07).
- **Không hoàn tất lượt khám:** người bệnh từ chối chỉ định (ký phiếu từ chối [1]), hủy, hoặc bỏ về giữa chừng ⚠ (QL07, QN10).

## Cổng điều kiện dự kiến (nếu mô hình hóa)

Dùng cho BPMN C1 (T32). Mục tiêu rubric: > 7 cổng điều kiện và có cặp split/join song song. Cổng 1–9 dưới đây lấy từ
kế hoạch mô hình hóa của nhóm, mỗi cổng đặt tên dạng câu hỏi, nhánh ra có điều kiện. Cổng 10–16 bổ sung khi mô hình hóa. Cổng 4, 6, 7 (nhánh chuyển viện), 9, 13, 15, 16 chưa có
nguồn công khai nên đánh ⚠ (mã câu hỏi ở từng dòng). Cổng 8 dựa trên phiếu đồng ý, phiếu từ chối ở Bước 3 [1].

| STT | Cổng điều kiện | Nhánh ra |
|---|---|---|
| 1 | Có đặt lịch trước? | Có: check-in theo lịch hẹn / Không: lấy số, đăng ký tại quầy ⚠ (QL01) |
| 2 | Khách mới hay khách cũ? | Mới: mở hồ sơ / Cũ: dùng hồ sơ có sẵn |
| 3 | Hình thức chi trả? | Tự chi trả / BHYT / Bảo hiểm tư nhân (chi tiết ở C3) |
| 4 | Có dấu hiệu cấp cứu khi đo sinh hiệu? ⚠ (QL06, QL07) | Có: xử trí cấp cứu / Không: chờ khám |
| 5 | Cần cận lâm sàng? | Có: chỉ định, thanh toán, thực hiện (C2) / Không: kết luận, thanh toán sau khám [1] |
| 6 | Cần chỉ định bổ sung? ⚠ (QN03) | Có: chỉ định bổ sung / Không: xét hội chẩn (cổng 15) |
| 7 | Kết luận là gì? | Ra về / Nhập viện [1] / Chuyển viện ⚠ (không có trên trang; QLHC08) |
| 8 | Người bệnh đồng ý thực hiện chỉ định? | Đồng ý: thanh toán chỉ định / Từ chối: ký phiếu từ chối [1], về bước kết luận ⚠ (sơ đồ không vẽ nhánh từ chối) |
| 9 | Có lĩnh thuốc tại bệnh viện? ⚠ (khảo sát người bệnh câu 6, 11) | Có: lĩnh thuốc (S1) / Không: gồm cả ca không có đơn thuốc |
| 10 | Cần kê đơn thuốc? | Có: kê đơn / Không: sang thanh toán (sơ đồ: "đơn thuốc (nếu có)") [1] |
| 11 | Có bảo lãnh trực tiếp? | Có: đóng tạm ứng [7] / Không: sang đo sinh hiệu |
| 12 | Dùng bảo lãnh trực tiếp? | Có: yêu cầu bảo lãnh viện phí [7] / Không: bỏ qua |
| 13 | Còn khoản chưa thanh toán? | Có: thanh toán viện phí [1] / Không: bỏ qua (đã thu ở bước thanh toán chỉ định) ⚠ (QN09) |
| 14 | Có hẹn tái khám? | Có: hẹn lịch tái khám / Không: ra về [1] |
| 15 | Cần hội chẩn chuyên khoa? ⚠ (QLHC06) | Có: hội chẩn rồi kết luận / Không: kết luận |
| 16 | Chỉ định loại nào? ⚠ (QN08) | Chỉ xét nghiệm / Chỉ chẩn đoán hình ảnh / Cả hai (song song) |

**Song song (split/join):** ở nhánh "Cả hai" của cổng 16, *thực hiện xét nghiệm* ∥ *thực hiện chẩn đoán hình
ảnh* → join khi đủ kết quả, rồi mới sang *đọc kết quả* ⚠ (QN08). Cổng tách và cổng gộp cùng là cổng song song (AND).

## Liên kết với quy trình khác

- **C4 Đặt lịch khám:** C4 kết thúc ở check-in và định danh; C1 bắt đầu từ đó. Với khách đến trực tiếp, C1 bắt đầu từ bước 1.
  Bước mở hồ sơ, định danh có ở cả hai: C4 mô tả phía đặt lịch, C1 giữ làm bước của lượt khám.
- **C2 Cận lâm sàng:** C1 bước 8–13 giao sang C2 khi bác sĩ chỉ định và nhận lại khi bác sĩ đọc kết quả.
- **C3 Thanh toán, bảo lãnh:** C3 chạy xuyên suốt: khai báo hình thức chi trả (bước 4), thanh toán chỉ định (bước 10),
  thanh toán cuối (bước 16). C1 không lặp lại các nhánh bảo lãnh, BHYT.
- **S1 Cấp phát thuốc:** nhận đơn thuốc từ bước 14–15.
- **M1 Lập lịch bác sĩ:** giờ làm việc và khung giờ khám của bác sĩ. Khu ngoại trú Central Park làm việc thứ Hai đến thứ Bảy,
  sáng 07:30–12:00, chiều 13:00–16:30 (theo M1, nguồn Vinmec cập nhật 19/10/2026).
- **M2 Đánh giá KPI:** thời gian chờ khám, chờ kết quả, tổng thời gian ở bệnh viện (QN10).
- **T27 Ghi thời gian thực tế:** các hoạt động trong danh mục ghi thời gian của nhóm (tiếp đón, chờ và đo sinh hiệu, chờ khám, khám lần 1, chờ cận lâm sàng, chờ kết quả, khám lần 2, lĩnh thuốc, thanh toán) ứng với bước 2, 5, 7, 11–13, 15, 16.
