# Hướng dẫn ghi thời gian thực tế (event log)

Dùng cho T27 (ghi ≥ 3 lượt khám) và T44 (phân tích PM4Py). Kết quả lưu ở `data/event_log.csv`,
**đúng định dạng** `data/event_log_template.csv`. Các dòng trong template là **ví dụ định dạng, không phải số liệu thật**.

> `data/event_log.csv` hiện là **bản mô phỏng** (mọi dòng có `note` bắt đầu bằng `mô phỏng`), xem [README](README.md).
> Khi có số đo thật thì **thay toàn bộ file**, không trộn dòng thật với dòng mô phỏng.

## 1. Định dạng file

- Mã hóa **UTF-8**, dấu phân cách **dấu phẩy**, dòng đầu là tiêu đề. Ô có dấu phẩy thì bọc trong `"..."`.
- Mỗi dòng = **một hoạt động** của **một lượt khám**. Sắp xếp theo `case_id`, rồi theo `start_time`.

| Cột | Bắt buộc | Định dạng | Ý nghĩa |
|---|---|---|---|
| `case_id` | Có | `L01`, `L02`… | Mã lượt khám **ẩn danh**, đánh số theo thứ tự quan sát. Không dùng tên, mã hồ sơ, số điện thoại |
| `activity` | Có | Chọn từ **danh mục ở mục 3** | Tên hoạt động, viết đúng chính tả để PM4Py gộp đúng |
| `start_time` | Có | `YYYY-MM-DD HH:MM` (24h) | Thời điểm bắt đầu |
| `end_time` | Có | `YYYY-MM-DD HH:MM` (24h) | Thời điểm kết thúc; phải ≥ `start_time` |
| `resource` | Không | Vai trò, **không ghi tên người** | `Lễ tân`, `Điều dưỡng`, `Bác sĩ`, `Thu ngân`, `Kỹ thuật viên XN`, `Kỹ thuật viên CĐHA`, `Dược sĩ`, `Nhân viên bảo hiểm`. Để trống với hoạt động *Chờ…* |
| `note` | Không | Văn bản ngắn | Bối cảnh: có lịch hẹn, BHYT/bảo hiểm tư nhân, loại cận lâm sàng, vì sao chờ lâu… Không ghi chẩn đoán |

## 2. Quy tắc ghi

1. **Ghi theo giờ đồng hồ điện thoại**, chính xác đến phút. Ghi ngay tại chỗ, không ước lượng lại sau.
2. **Ghi cả thời gian chờ** thành hoạt động riêng (`Chờ khám`, `Chờ kết quả`…). Thời gian chờ là dữ liệu quan trọng nhất
   để tìm lãng phí (T42) và tính thời gian chu kỳ (T44).
3. Khoảng trống giữa hai hoạt động ≤ 3 phút (đi bộ giữa các phòng) **không cần** ghi riêng; > 3 phút thì ghi
   `Di chuyển` hoặc `Chờ …` tùy tình huống.
4. Hoạt động lặp lại (vd *Thanh toán* hai lần: tạm ứng và quyết toán) thì ghi **hai dòng**, phân biệt ở `note`.
5. Hai hoạt động **song song** (vd lấy máu và chờ siêu âm) thì ghi hai dòng có khoảng thời gian chồng nhau — đúng thực tế,
   không cần tách.
6. Không quan sát được điểm bắt đầu/kết thúc thì vẫn ghi dòng đó, ghi `note: ước lượng` để loại khi phân tích.
7. Lượt khám bị bỏ dở (người bệnh về trước, chuyển nhập viện) → ghi đến hoạt động cuối cùng, `note` ghi lý do.
8. **Được dùng mẫu quan sát từ cơ sở ngoài Vinmec cho C1.** `note` ghi `ngoài Vinmec (loại cơ sở)`, không ghi tên cơ sở.
   Báo cáo dùng các mẫu này phải nêu rõ đó không phải số liệu đo tại Vinmec.

## 3. Danh mục hoạt động (C1 Khám ngoại trú)

Dùng đúng tên dưới đây. Cần thêm hoạt động mới thì bổ sung vào bảng này trong cùng PR.

| Hoạt động | Thuộc quy trình | Ghi chú |
|---|---|---|
| Tiếp đón - mở hồ sơ | C1 / C4 | Check-in lịch hẹn hoặc mở hồ sơ khách mới |
| Chờ đo sinh hiệu | C1 | |
| Đo sinh hiệu | C1 | Mạch, huyết áp, cân nặng… |
| Chờ khám | C1 | Từ lúc ngồi chờ (sau đo sinh hiệu) đến lúc được gọi vào phòng khám. KPI *Thời gian chờ khám* của M2 tính rộng hơn: hết *Tiếp đón - mở hồ sơ* → bắt đầu *Khám lần 1* |
| Khám lần 1 | C1 | Bác sĩ khám, chỉ định |
| Chờ thanh toán | C3 | Từ lúc có chỉ định hoặc kết luận đến lúc bắt đầu thanh toán |
| Thanh toán | C3 | Tạm ứng / quyết toán / bảo lãnh – ghi ở `note` |
| Chờ bảo lãnh | C3 | Chờ công ty bảo hiểm phản hồi |
| Xét nghiệm - lấy mẫu | C2 | |
| Chẩn đoán hình ảnh | C2 | Ghi loại (X-quang, siêu âm, CT…) ở `note` |
| Thăm dò chức năng | C2 | Điện tim, nội soi… |
| Chờ cận lâm sàng | C2 | Chờ đến lượt làm xét nghiệm/CĐHA |
| Chờ kết quả | C2 | Từ lúc làm xong đến lúc có kết quả / quay lại phòng khám |
| Khám lần 2 - đọc kết quả | C1 | |
| Lĩnh thuốc | S1 | Gồm cả thời gian chờ ở nhà thuốc nếu không tách được |
| Di chuyển | – | Chỉ ghi khi > 3 phút |

## 4. Bảo mật

- **Không** ghi tên, tuổi, chẩn đoán, số hồ sơ, biển số xe, ảnh của người bệnh. Không ghi tên nhân viên.
- Chỉ quan sát/ghi khi có sự đồng ý của người bệnh (thường là chính thành viên nhóm hoặc người thân đi khám).
- Ghi chép tay gốc giữ ngoài repo.

## 5. Kiểm tra trước khi mở PR

```bash
python scripts/check_event_log.py data/event_log.csv
```

Script báo lỗi khi thiếu cột, sai định dạng thời gian, `end_time` < `start_time`, hoặc `activity` không có trong danh mục.

## 6. Đọc bằng PM4Py (dùng ở T44)

```python
import pandas as pd
import pm4py

df = pd.read_csv("data/event_log.csv", parse_dates=["start_time", "end_time"])
df = df[~df["note"].fillna("").str.contains("ước lượng")]        # quy tắc 6: loại dòng không đủ bắt đầu/kết thúc
df = pm4py.format_dataframe(df, case_id="case_id", activity_key="activity", timestamp_key="end_time",
                            start_timestamp_key="start_time")
log = pm4py.convert_to_event_log(df)
print(pm4py.get_variants(log))                                   # các biến thể đường đi
dfg, start, end = pm4py.discover_performance_dfg(log)            # thời gian trung bình giữa các bước
```
