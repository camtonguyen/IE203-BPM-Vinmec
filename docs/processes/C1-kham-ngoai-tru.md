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

> Nguồn [1] là hướng dẫn chung của hệ thống Vinmec, không riêng Vinmec Central Park. Trang gồm một **sơ đồ** (khách hàng
> cũ, mới, tái khám → đăng ký, mở hồ sơ → bốt điều dưỡng, phòng khám phân loại → bác sĩ khám, tư vấn → thanh toán hoặc
> chỉ định cận lâm sàng, thủ thuật → thanh toán → bác sĩ đọc, giải thích kết quả → ra về hoặc nhập viện) và danh sách
> chứng từ phải ký ở 8 bước đánh số. Sơ đồ **không có** đo sinh hiệu, nhận biết cấp cứu, hội chẩn, chuyển viện, thời gian
> chờ và nơi thực hiện từng bước. Những phần đó lấy từ kế hoạch mô hình hóa của nhóm và đánh dấu **⚠** (chưa có nguồn
> công khai), cần xác minh qua phỏng vấn T24–T26 (số câu hỏi ghi ở từng mục).

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Người bệnh / người giám hộ | Đặt lịch hoặc đến trực tiếp, cung cấp giấy tờ, ký phiếu, đi theo chỉ định, thanh toán. Trẻ em đi cùng người giám hộ [1] |
| Lễ tân (Quầy tiếp đón) | Check-in, mở hồ sơ khách mới, sao chụp giấy tờ và thẻ bảo hiểm, định danh [1] |
| Điều dưỡng | Phân loại, đo sinh hiệu, nhận biết dấu hiệu cấp cứu, hướng dẫn người bệnh đến đúng phòng ⚠ (câu 6, 7) |
| Bác sĩ | Khám, chỉ định cận lâm sàng, đọc kết quả, kết luận, kê đơn, hẹn tái khám, chỉ định nhập viện hoặc chuyển viện ⚠ (câu 6, 12, 13) |
| Kỹ thuật viên xét nghiệm, chẩn đoán hình ảnh | Thực hiện cận lâm sàng (chi tiết ở C2) |
| Thu ngân | Thu tiền, lập bảng kê, biên lai (chi tiết ở C3) [1] |
| Nhà thuốc bệnh viện | Cấp thuốc theo đơn (chi tiết ở S1) |
| Khoa chuyên khoa khác, bệnh viện tuyến trên *(bên ngoài C1)* | Nhận người bệnh hội chẩn hoặc chuyển viện ⚠ (câu 22) |
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
   ở bước check-in) hoặc đến trực tiếp không hẹn trước ⚠ (câu 1).
2. Tại **Quầy tiếp đón**: khách mới mở hồ sơ, cung cấp họ tên, giấy tờ tùy thân (CCCD/CMND/hộ chiếu, trẻ em dùng giấy
   khai sinh), thẻ bảo hiểm và thẻ ưu đãi nếu có, điền **phiếu đăng ký (01 bản)**, quầy sao chụp giấy tờ [1].
   Khách cũ dùng hồ sơ có sẵn, khách đặt lịch online đã có thông tin trên hệ thống (C4) ⚠ (câu 1, 8).
3. **Định danh** bằng ít nhất 2 thông tin: họ tên đầy đủ, ngày sinh, kèm mã PID nếu cần; thực hiện trước mọi lần thăm
   khám hoặc can thiệp y tế [1].
4. **Xác minh hình thức chi trả** (tự chi trả, BHYT, bảo hiểm tư nhân) và kiểm tra thẻ → chi tiết thủ tục, bảo lãnh,
   tạm ứng ở **C3** (phần A của C3). C1 chỉ ghi nhận kết quả để biết nhánh thanh toán cuối lượt khám.

**B. Phân loại và đo sinh hiệu**

5. Người bệnh **chờ đo sinh hiệu**, điều dưỡng **đo sinh hiệu** (mạch, huyết áp, cân nặng… theo danh mục ghi thời gian
   của nhóm) ⚠ (câu 6, 7). Sơ đồ Vinmec có bước "Bốt điều dưỡng, phòng khám phân loại người bệnh" ngay sau đăng ký [1]; nhân viên và nội dung đo
   chưa nêu.
6. Nếu có **dấu hiệu cấp cứu**, chuyển ngay xử trí cấp cứu, bỏ qua các bước chờ còn lại ⚠ (câu 6, 7).

**C. Khám và chỉ định**

7. Người bệnh **chờ khám**, bác sĩ **khám, tư vấn** (khám lần 1) [1]; thời gian chờ và nội dung khám ⚠ (câu 6, 12).
8. Bác sĩ quyết định có **cần cận lâm sàng, thủ thuật** không [1]. Nếu không → sang bước 14; tỉ lệ có chỉ định ⚠ (câu 13).
9. Nếu cần: bác sĩ **chỉ định**; người bệnh ký **phiếu đồng ý** làm xét nghiệm HIV, phiếu đồng ý thực hiện chẩn đoán
   (nếu có) hoặc **phiếu từ chối** thực hiện (01 bản) [1].
10. **Thanh toán chỉ định** trước khi thực hiện (Bước 4 của Vinmec) [1]: ký chứng từ thanh toán (02 bảng kê + 01 biên lai
    thu tiền viện phí) và ký thanh toán bảo hiểm (01 bản, nếu dùng bảo hiểm tư nhân) → chi tiết ở **C3**.
11. **Thực hiện cận lâm sàng** → chi tiết ở **C2**. Khi bác sĩ chỉ định cả xét nghiệm và chẩn đoán hình ảnh,
    hai hạng mục có thể làm **song song** ⚠ (câu 18).
12. Người bệnh **chờ kết quả**; kết quả trả cho bác sĩ bằng hệ thống, giấy hoặc cả hai ⚠ (câu 3, 18).
13. Bác sĩ **khám lần 2, đọc và giải thích kết quả** [1]. Nếu kết quả bất thường hoặc cần thêm thông tin: chỉ định bổ sung (quay lại bước 9)
    hoặc **hội chẩn chuyên khoa khác** ⚠ (câu 22).

**D. Kết luận**

14. Bác sĩ **kết luận**: **ra về** kèm đơn thuốc (nếu có), **tái khám** hoặc **nhập viện** nội khoa, phẫu thuật, thủ thuật [1].
    **Chuyển chuyên khoa, chuyển viện** không có trên trang Vinmec ⚠ (câu 22).
15. Có đơn thuốc: người bệnh **lĩnh thuốc** tại nhà thuốc bệnh viện hoặc mua nơi khác ⚠ (câu 6, 7) → chi tiết ở **S1**.

**E. Thanh toán và kết thúc**

16. **Thanh toán** trước khi ra về, theo sơ đồ Vinmec [1]: nếu **không làm cận lâm sàng**, thanh toán sau khám (Bước 2 của
    Vinmec) với cùng bộ chứng từ; nếu **có cận lâm sàng**, khoản chính đã thanh toán ở bước 10 (Bước 4), sơ đồ không vẽ
    thanh toán thêm sau khi đọc kết quả. Chi phí phát sinh sau chỉ định ⚠ (câu 19) → chi tiết ở **C3**.
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
nêu ⚠ (câu 8, 19).

## Các kết quả có thể

- **Ra về, kê đơn điều trị ngoại trú:** bác sĩ kết luận, người bệnh thanh toán, nhận đơn (nếu có) và ra về [1].
- **Hẹn tái khám:** kết luận kèm lịch hẹn theo kế hoạch điều trị; sơ đồ Vinmec cho khách tái khám quay lại từ đầu [1] (liên kết C4).
- **Chỉ định nhập viện:** nhập viện nội khoa hoặc phẫu thuật, thủ thuật [1]; C1 kết thúc, chuyển sang quy trình nội trú (ngoài phạm vi đề tài).
- **Chuyển chuyên khoa hoặc chuyển viện:** người bệnh cần chuyên khoa khác hoặc tuyến trên ⚠ (câu 22).
- **Xử trí cấp cứu:** có dấu hiệu cấp cứu khi đo sinh hiệu, thoát khỏi luồng khám thường ⚠ (câu 6, 7).
- **Không hoàn tất lượt khám:** người bệnh từ chối chỉ định (ký phiếu từ chối [1]), hủy, hoặc bỏ về giữa chừng ⚠ (câu 7, 20).

## Cổng điều kiện dự kiến (nếu mô hình hóa)

Dùng cho BPMN C1 (T32). Mục tiêu rubric: > 7 cổng điều kiện và có cặp split/join song song. 9 cổng dưới đây lấy từ
kế hoạch mô hình hóa của nhóm, mỗi cổng đặt tên dạng câu hỏi, nhánh ra có điều kiện.

| STT | Cổng điều kiện | Nhánh ra |
|---|---|---|
| 1 | Có đặt lịch trước? | Có: check-in theo lịch hẹn / Không: lấy số, đăng ký tại quầy ⚠ (câu 1) |
| 2 | Khách mới hay khách cũ? | Mới: mở hồ sơ / Cũ: dùng hồ sơ có sẵn |
| 3 | Hình thức chi trả? | Tự chi trả / BHYT / Bảo hiểm tư nhân (chi tiết ở C3) |
| 4 | Có dấu hiệu cấp cứu khi đo sinh hiệu? | Có: xử trí cấp cứu / Không: chờ khám |
| 5 | Cần cận lâm sàng? | Có: chỉ định, thanh toán, thực hiện (C2) / Không: kết luận, thanh toán sau khám [1] |
| 6 | Kết quả có bất thường? | Có: chỉ định bổ sung hoặc hội chẩn / Không: kết luận |
| 7 | Kết luận là gì? | Kê đơn / Hẹn tái khám / Nhập viện / Chuyển viện |
| 8 | Cần hội chẩn chuyên khoa khác? | Có: chuyển chuyên khoa / Không: tiếp tục |
| 9 | Có lấy thuốc tại bệnh viện? | Có: lĩnh thuốc (S1) / Không: ra về |

**Song song (split/join):** khi bác sĩ chỉ định nhiều cận lâm sàng, *thực hiện xét nghiệm* ∥ *thực hiện chẩn đoán hình
ảnh* → join khi đủ kết quả, rồi mới sang *đọc kết quả* ⚠ (câu 18). Cổng tách và cổng gộp cùng là cổng song song (AND).

## Liên kết với quy trình khác

- **C4 Đặt lịch khám:** C4 kết thúc ở check-in và định danh; C1 bắt đầu từ đó. Với khách đến trực tiếp, C1 bắt đầu từ bước 1.
  Bước mở hồ sơ, định danh có ở cả hai: C4 mô tả phía đặt lịch, C1 giữ làm bước của lượt khám.
- **C2 Cận lâm sàng:** C1 bước 8–13 giao sang C2 khi bác sĩ chỉ định và nhận lại khi bác sĩ đọc kết quả.
- **C3 Thanh toán, bảo lãnh:** C3 chạy xuyên suốt: khai báo hình thức chi trả (bước 4), thanh toán chỉ định (bước 10),
  thanh toán cuối (bước 16). C1 không lặp lại các nhánh bảo lãnh, BHYT.
- **S1 Cấp phát thuốc:** nhận đơn thuốc từ bước 14–15.
- **M1 Lập lịch bác sĩ:** giờ làm việc và khung giờ khám của bác sĩ. Khu ngoại trú Central Park làm việc thứ Hai đến thứ Bảy,
  sáng 07:30–12:00, chiều 13:00–16:30 (theo M1, nguồn Vinmec cập nhật 19/10/2026).
- **M2 Đánh giá KPI:** thời gian chờ khám, chờ kết quả, tổng thời gian ở bệnh viện (câu 20).
- **T27 Ghi thời gian thực tế:** các hoạt động trong danh mục ghi thời gian của nhóm (tiếp đón, chờ và đo sinh hiệu, chờ khám, khám lần 1, chờ cận lâm sàng, chờ kết quả, khám lần 2, lĩnh thuốc, thanh toán) ứng với bước 2, 5, 7, 11–13, 15, 16.
