# M3 – Quản lý sự cố y khoa (khu khám ngoại trú)

- **Loại:** Quản lý
- **Người phụ trách viết:** Nguyễn Quang Hòa (26410042)
- **Phạm vi:** từ lúc nhân viên y tế (hoặc người bệnh) phát hiện một sự cố / tình huống suýt xảy ra sự cố (near-miss)
  trong quá trình khám ngoại trú đến khi sự cố được phân tích, có giải pháp phòng ngừa và phản hồi cho người báo cáo.
  Không gồm giải quyết bồi thường, tranh chấp pháp lý (Điều 100–102 Luật KBCB) và khiếu nại của người bệnh (S3).
- **Nguồn bằng chứng** (truy cập 17/11/2026):
  1. Thông tư 43/2018/TT-BYT ngày 26/12/2018 *Hướng dẫn phòng ngừa sự cố y khoa trong cơ sở khám bệnh, chữa bệnh*
     (hiệu lực 01/03/2019):
     https://thuvienphapluat.vn/van-ban/the-thao-y-te/thong-tu-43-2018-tt-byt-huong-dan-phong-ngua-su-co-y-khoa-trong-co-so-kham-benh-chua-benh-366845.aspx
  2. Thông tư 19/2013/TT-BYT *Hướng dẫn thực hiện quản lý chất lượng dịch vụ khám bệnh, chữa bệnh tại bệnh viện*:
     https://caselaw.vn/van-ban-phap-luat/265779-thong-tu-19-2013-tt-byt-huong-dan-thuc-hien-quan-ly-chat-luong-dich-vu-kham-chua-benh-tai-benh-vien-do-bo-truong-bo-y-te-ban-hanh
  3. Luật Khám bệnh, chữa bệnh số 15/2023/QH15 (văn bản hợp nhất 26/VBHN-VPQH năm 2026), Điều 2 khoản 22–23, Điều 42, Điều 71:
     https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf
  4. Pháp luật TP.HCM – *Vinmec Central Park xuất sắc đạt "Dấu vàng" chất lượng chứng chỉ JCI lần thứ 3* (01/04/2024):
     https://plo.vn/vinmec-central-park-xuat-sac-dat-dau-vang-chat-luong-chung-chi-jci-lan-thu-3-post783150.html
  5. FV Hospital – *Safety Goals* (6 mục tiêu an toàn người bệnh quốc tế của JCI, tham khảo bệnh viện JCI cùng thành phố):
     https://www.fvhospital.com/en/safety-goals/
  6. Phỏng vấn bác sĩ, điều dưỡng (T24, tuần 2) – *chưa thực hiện*.

> Nguồn 1–3 là quy định chung áp dụng cho mọi cơ sở khám chữa bệnh; nguồn 4 xác nhận Vinmec Central Park có
> "văn hóa an toàn, văn hóa báo cáo" và khuyến khích báo cáo cả sai sót nhỏ chưa gây hậu quả.
> Vinmec **không công bố** quy trình nội bộ, nên các bước dưới đây dựng theo khung bắt buộc của Thông tư 43 và
> Thông tư 19; mục đánh dấu **⚠** là suy luận, cần xác minh qua phỏng vấn T24 (đề xuất bổ sung câu hỏi ở cuối file).

## Định nghĩa dùng trong quy trình

- **Sự cố y khoa:** tình huống không mong muốn hoặc bất thường xảy ra trong quá trình khám bệnh, chữa bệnh do yếu tố
  khách quan, chủ quan [3, Điều 2 khoản 22]; không phải do diễn biến bệnh lý hoặc cơ địa người bệnh [1, Điều 2].
- **Near-miss (suýt xảy ra sự cố):** tình huống có nguy cơ gây ra sự cố nhưng chưa xảy ra [1, Điều 2].
- **Nguyên nhân gốc:** nguyên nhân ban đầu, có quan hệ nhân quả trực tiếp và có thể khắc phục [1, Điều 2].
- **Mức độ tổn thương** [1, Phụ lục I]:

| Mức | Ý nghĩa | Mục Phụ lục I | Hình thức báo cáo |
|---|---|---|---|
| NC0 | Chưa xảy ra (near-miss) | 1 (A) | Tự nguyện |
| NC1 | Tổn thương nhẹ | 2–4 (B, C, D) | Tự nguyện |
| NC2 | Tổn thương trung bình (phải can thiệp điều trị, kéo dài thời gian điều trị) | 5–6 (E, F) | Tự nguyện, nhưng báo ngay cho người đứng đầu [1, Điều 8] |
| NC3 | Tổn thương nặng (di chứng, cần hồi sức, tử vong) | 7–9 (G, H, I) | **Bắt buộc** |

**Ví dụ sự cố có thể gặp ở khu ngoại trú** ⚠: nhầm người bệnh khi gọi khám / lấy mẫu xét nghiệm, dán nhầm nhãn ống mẫu,
trả nhầm kết quả, kê hoặc phát nhầm thuốc, người bệnh té ngã ở hành lang/nhà vệ sinh, phản ứng sau tiêm/thuốc cản quang,
chậm báo kết quả nguy kịch cho bác sĩ. Các tình huống này ứng với các mục tiêu an toàn người bệnh quốc tế của JCI
(định danh người bệnh, giao tiếp hiệu quả, an toàn thuốc, phòng ngã) [5] và chương trình an toàn người bệnh trong
Thông tư 19 [2, Điều 7].

## Actor

| Actor | Vai trò trong quy trình |
|---|---|
| Nhân viên y tế phát hiện / liên quan (bác sĩ, điều dưỡng, kỹ thuật viên, dược sĩ, lễ tân…) | Xử lý ngay để bảo đảm an toàn người bệnh, sau đó báo cáo sự cố [1, Điều 9] |
| Người bệnh / người nhà | Có thể phát hiện và thông báo sự cố ⚠; được thông tin về sự cố liên quan đến mình ⚠ |
| Trưởng khoa (khoa khám bệnh / khoa có sự cố) | Nhận báo cáo bắt buộc, phối hợp xử lý, triển khai giải pháp tại khoa [1, Điều 5] |
| Phòng / Tổ Quản lý chất lượng (QLCL) – bộ phận tiếp nhận | Tiếp nhận, lưu hồ sơ, phân loại, phân tích sơ bộ, tổng hợp báo cáo, phản hồi người báo cáo, theo dõi khắc phục [1, Điều 5, 7, 8, 9; 2, Điều 12] |
| Giám đốc bệnh viện (người đứng đầu) | Nhận báo cáo NC2/NC3, thành lập nhóm chuyên gia phân tích nguyên nhân gốc (RCA), phê duyệt khuyến cáo [1, Điều 8] |
| Nhóm chuyên gia RCA | Phân tích nguyên nhân gốc, xác định nguyên nhân hệ thống hay đơn lẻ, đề xuất giải pháp trong 60 ngày [1, Điều 8] |
| Hội đồng QLCL | Giám đốc làm chủ tịch; phát hiện nguy cơ an toàn người bệnh, đề xuất đề án cải tiến [2, Điều 10–11] |
| Hệ thống báo cáo sự cố (giấy / trực tuyến) | Ghi nhận và lưu trữ toàn bộ sự cố [1, Điều 5]. Vinmec dùng phần mềm hay phiếu giấy chưa rõ ⚠ |
| Sở Y tế / Bộ Y tế *(bên ngoài)* | Nhận báo cáo bắt buộc và báo cáo định kỳ 6 tháng [1, Điều 5, 6] |

## Khách hàng của quy trình

- **Chính:** người bệnh ngoại trú – được bảo vệ khỏi tổn hại và sự cố không lặp lại.
- **Nội bộ:** các khoa/phòng (nhận khuyến cáo, bài học), ban giám đốc và Hội đồng QLCL (số liệu an toàn người bệnh
  cho M2), nhân viên báo cáo (được phản hồi, được bảo vệ, không bị quy lỗi cá nhân [1, Điều 3, 12]).
- **Bên ngoài:** cơ quan quản lý (Sở Y tế, Bộ Y tế), tổ chức kiểm định JCI.

## Các bước (mô tả bằng lời)

**A. Phát hiện và xử lý ban đầu**

1. Nhân viên y tế (hoặc người bệnh, người nhà) **phát hiện** sự cố hoặc near-miss, nhận diện theo Phụ lục I [1, Điều 4].
2. Nếu sự cố đã ảnh hưởng đến người bệnh, nhân viên **xử lý ngay** để bảo đảm an toàn (sơ cứu, cấp cứu, báo bác sĩ)
   **trước khi báo cáo** [1, Điều 9]. Song song, báo **trưởng khoa** để huy động hỗ trợ ⚠.
3. Ghi nhận và **thông tin cho người bệnh / người nhà** về sự cố ⚠ (Thông tư 43 không quy định; thực hành JCI).

**B. Báo cáo**

4. Nhân viên **xác định hình thức báo cáo** theo mức độ [1, Điều 5]:
   - **Tự nguyện** (NC0–NC2, Mục 1–6): điền phiếu báo cáo sự cố (Phụ lục III) bằng giấy hoặc trực tuyến, có thể ẩn danh;
     trường hợp khẩn được báo trực tiếp / điện thoại rồi bổ sung văn bản.
   - **Bắt buộc** (NC3, Mục 7–9): người gây ra hoặc phát hiện sự cố báo **trưởng khoa** và **bộ phận QLCL** →
     QLCL báo **giám đốc** → bệnh viện báo **cơ quan quản lý** bằng văn bản hỏa tốc hoặc báo cáo điện tử.
5. Nếu là **sự cố nghiêm trọng** (1 người tử vong và nghi có nguy cơ tử vong tiếp theo, hoặc ≥ 2 người tử vong do cùng
   nguyên nhân): bệnh viện **báo cáo trước bằng điện thoại trong 01 giờ** kể từ khi phát hiện [1, Điều 5].
   Thời hạn nộp phiếu nội bộ cho sự cố thường (vd trong 24 giờ) do từng bệnh viện tự quy định ⚠.

**C. Tiếp nhận, phân loại, phân tích**

6. Phòng QLCL **tiếp nhận**, kiểm tra thông tin, **lưu hồ sơ** (giấy hoặc hệ thống trực tuyến) [1, Điều 5]; nếu phiếu
   thiếu thông tin thì liên hệ người báo cáo bổ sung ⚠.
7. QLCL **phân loại** theo 3 tiêu chí: mức độ tổn thương (Phụ lục I), nhóm sự cố (Phụ lục IV mục II), nhóm nguyên nhân
   (Phụ lục IV mục IV); NC3 phân loại thêm theo Phụ lục II [1, Điều 7].
8. QLCL **phân tích sơ bộ** và báo cáo giám đốc **định kỳ 1 tuần/lần**; với **NC2, NC3 phải báo cáo ngay** [1, Điều 8].
9. Với sự cố NC2/NC3 (hoặc sự cố lặp lại ⚠), giám đốc **thành lập nhóm chuyên gia** phân tích **nguyên nhân gốc (RCA)**,
   xác định nguyên nhân hệ thống hay đơn lẻ; trong **60 ngày** kể từ khi nhận báo cáo phải đề xuất **giải pháp,
   khuyến cáo** [1, Điều 8]. Sự cố NC0/NC1 chỉ phân tích tại khoa / QLCL ⚠.

**D. Khắc phục, phòng ngừa, phản hồi**

10. QLCL tham mưu **kế hoạch khắc phục**; giám đốc phê duyệt khuyến cáo phòng ngừa [1, Điều 10–11].
11. Các khoa **triển khai** giải pháp (sửa quy trình, đào tạo lại, thay đổi biểu mẫu, thiết bị…); người chịu trách nhiệm
    chuyên môn **giám sát** việc thực hiện [1, Điều 11].
12. QLCL **phản hồi cho người báo cáo** tại buổi giao ban [1, Điều 9] và chia sẻ bài học toàn viện ⚠
    (danh tính người báo cáo được giữ bí mật [1, Điều 12]).
13. QLCL **tổng hợp** số liệu: số báo cáo bắt buộc / tự nguyện, tần suất từng loại, kết quả RCA, giải pháp đã triển khai;
    gửi cơ quan quản lý **6 tháng/lần** [1, Điều 6] và báo cáo Hội đồng QLCL [2, Điều 11] → làm đầu vào cho **M2**.
14. QLCL **theo dõi hiệu quả**: sự cố tương tự có tái diễn không; nếu có → quay lại bước 9 ⚠.

## Các kết quả có thể

- Near-miss được ghi nhận, phân tích tại khoa, không cần RCA → đóng hồ sơ, đưa vào thống kê.
- Sự cố NC1 được xử lý, có biện pháp khắc phục tại khoa → đóng hồ sơ.
- Sự cố NC2/NC3 được RCA, có khuyến cáo phòng ngừa được triển khai và giám sát.
- Sự cố NC3 / nghiêm trọng được báo cáo bắt buộc lên Sở Y tế, Bộ Y tế; có thể dẫn đến điều tra của cơ quan quản lý
  [1, Điều 9] hoặc quy trình xác định sai sót chuyên môn (ngoài phạm vi).
- Phiếu báo cáo không phải sự cố (do diễn biến bệnh lý) → QLCL phân loại lại và đóng ⚠.
- Giải pháp không hiệu quả, sự cố tái diễn → mở lại phân tích.

## Cổng điều kiện dự kiến (nếu mô hình hóa)

Dùng cho BPMN M3 (T33). Mục tiêu rubric: > 7 cổng điều kiện và có cặp split/join song song.

1. Sự cố đã ảnh hưởng đến người bệnh? → Có (xử lý ngay) / Không (near-miss, báo cáo)
2. Mức độ tổn thương? → NC0–NC1 / NC2 / NC3
3. Là sự cố nghiêm trọng (tử vong, nguy cơ tử vong tiếp theo)? → Có (gọi điện trong 1 giờ) / Không
4. Hình thức báo cáo? → Tự nguyện / Bắt buộc
5. Phiếu báo cáo đủ thông tin? → Đủ / Thiếu (yêu cầu bổ sung)
6. Có đúng là sự cố y khoa (không do diễn biến bệnh)? → Có / Không (đóng hồ sơ)
7. Cần phân tích nguyên nhân gốc (NC2/NC3 hoặc lặp lại)? → Có (lập nhóm RCA) / Không (xử lý tại khoa)
8. Nguyên nhân hệ thống hay đơn lẻ? → Hệ thống (cải tiến quy trình toàn viện) / Đơn lẻ (đào tạo, nhắc nhở tại khoa)
9. Giám đốc phê duyệt khuyến cáo? → Duyệt / Yêu cầu phân tích lại
10. Sự cố có tái diễn sau khi triển khai giải pháp? → Có (quay lại RCA) / Không (đóng hồ sơ)

**Song song (split/join) đề xuất:**
- Sau khi phát hiện sự cố có ảnh hưởng: nhánh 1 *xử lý, cấp cứu người bệnh*, nhánh 2 *báo trưởng khoa*,
  nhánh 3 *thông tin cho người nhà* → join → *lập phiếu báo cáo*.
- Với sự cố NC3: nhánh 1 *báo cáo bắt buộc lên Sở Y tế*, nhánh 2 *lập nhóm RCA* → join → *phê duyệt khuyến cáo*.

**Pool / message flow:** Khoa khám bệnh ↔ Phòng QLCL ↔ Ban giám đốc (cùng tổ chức, có thể dùng lane);
Bệnh viện ↔ Sở Y tế (pool riêng, message flow cho báo cáo bắt buộc và báo cáo định kỳ).

## Liên kết với quy trình khác

- **C1, C2, S1:** nơi phát sinh sự cố (nhầm người bệnh, nhầm mẫu, nhầm thuốc). Bước định danh người bệnh trong C1
  là điểm kiểm soát chính.
- **M2 Đánh giá KPI:** số sự cố / 1.000 lượt khám, tỉ lệ near-miss, tỉ lệ RCA hoàn thành đúng hạn 60 ngày.
- **S3 Khiếu nại:** khiếu nại của người bệnh có thể là nguồn phát hiện sự cố; ngược lại sự cố có thể dẫn tới khiếu nại.
- **S2 Tuyển dụng, đào tạo:** đào tạo lại là một giải pháp khắc phục phổ biến.

## Câu hỏi đề xuất bổ sung cho phỏng vấn T24 (bác sĩ, điều dưỡng)

- Ở khu khám ngoại trú, anh/chị báo cáo sự cố bằng phiếu giấy hay phần mềm? Mất bao lâu để điền một phiếu?
- Bệnh viện quy định nộp phiếu trong bao lâu sau khi phát hiện? Có được báo cáo ẩn danh không?
- Sau khi báo cáo, anh/chị có nhận được phản hồi không, qua kênh nào, sau bao lâu?
- Một tháng khoa có khoảng bao nhiêu báo cáo sự cố / near-miss? Loại nào hay gặp nhất?
