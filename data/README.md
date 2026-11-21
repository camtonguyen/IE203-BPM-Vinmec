# Dữ liệu

- `event_log.csv`: thời gian thực tế, cùng định dạng `event_log_template.csv`. **Chỉ dùng mã lượt ẩn danh.** Dòng mẫu trong template là ví dụ định dạng, không phải số liệu thật.
  Cách ghi, danh mục hoạt động và cách kiểm tra: [HUONG-DAN-GHI-THOI-GIAN.md](HUONG-DAN-GHI-THOI-GIAN.md)
  (`python scripts/check_event_log.py data/event_log.csv`).
- `cost_rates.csv`: đơn giá nhân công và giá dịch vụ, mỗi dòng **bắt buộc ghi nguồn + ngày truy cập**.
