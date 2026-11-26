# Nhật ký đóng góp – Đinh Hoàng Phát (26410086)

- **Họ và tên:** Đinh Hoàng Phát
- **MSSV:** 26410086
- **Email GitHub:** `hoangphat310304@gmail.com`
- **Vai trò trong nhóm:** Phụ trách Quy trình Hỗ trợ (S1–S3), Hạ tầng CI/CD & Camunda Engine, Mô phỏng Hiệu năng SimPy.
- **Thời gian thực hiện:** 16/11/2026 – 14/12/2026.

---

## 1. Bảng Tổng hợp Nhiệm vụ Tuần 1

| Tuần | Mã Task | Tên Nhiệm vụ | Sản phẩm & File bàn giao | Trạng thái |
|:---:|:---:|---|---|:---:|
| **1** | **T01** | Hỗ trợ cấu trúc repository & tài liệu README | [README.md](../README.md), [members/26410086-hoang-phat.md](26410086-hoang-phat.md) | **Hoàn thành** |
| **1** | **T04** | Thiết lập CI GitHub Actions & Docker Camunda | [.github/workflows/check.yml](../.github/workflows/check.yml), [infra/docker-compose.yml](../infra/docker-compose.yml), [scripts/check_bpmn.py](../scripts/check_bpmn.py), [scripts/check_links.py](../scripts/check_links.py) | **Hoàn thành** |
| **1** | **T07** | Biên soạn Glossary và Bảng từ viết tắt | [docs/glossary.md](../docs/glossary.md) | **Hoàn thành** |
| **1** | **T16** | Mô tả chi tiết quy trình hỗ trợ S1, S2, S3 | [docs/processes/S1-cap-phat-thuoc.md](../docs/processes/S1-cap-phat-thuoc.md)<br>[docs/processes/S2-tuyen-dung-dao-tao.md](../docs/processes/S2-tuyen-dung-dao-tao.md)<br>[docs/processes/S3-khieu-nai.md](../docs/processes/S3-khieu-nai.md) | **Hoàn thành** |
| **2** | **T30** | Dựng Camunda local, môi trường Python (PM4Py, SimPy), notebook mẫu | [requirements.txt](../requirements.txt), [scripts/test_env.py](../scripts/test_env.py), [analysis/test_environment.ipynb](../analysis/test_environment.ipynb), [infra/docker-compose.yml](../infra/docker-compose.yml) | **Hoàn thành** |

---

## 2. Chi tiết Đóng góp Tuần 1 (16/11/2026 – 22/11/2026)

### Khởi tạo Nền tảng, CI/CD, Thuật ngữ và Mô tả Quy trình
- **Task T04 (CI GitHub Actions + Docker Camunda):**
  + Tối ưu hóa workflow [.github/workflows/check.yml](../.github/workflows/check.yml) chạy tự động trên push/pull request. Tích hợp các jobs: Kiểm tra chuẩn BPMN XML và rubric chấm điểm; Kiểm tra bảo mật và quyền riêng tư thông tin y tế (chặn commit file ghi âm thô `.m4a`, `.mp3`); Kiểm tra liên kết tài liệu Markdown ([scripts/check_links.py](../scripts/check_links.py)); Kiểm tra cú pháp công cụ Python.
  + Nâng cấp công cụ kiểm tra [scripts/check_bpmn.py](../scripts/check_bpmn.py) tự động quét cổng rẽ nhánh, cổng song song split/join, cảnh báo thiếu nhãn điều kiện và chấm điểm rubric tự động.
  + Bổ sung công cụ kiểm tra liên kết [scripts/check_links.py](../scripts/check_links.py) tự động quét toàn bộ liên kết nội bộ trong các file Markdown, đảm bảo tính nhất quán tài liệu đồ án.
  + Chuẩn hóa [infra/docker-compose.yml](../infra/docker-compose.yml) sử dụng Camunda Run 7.22.0 với volume mount và healthcheck phục vụ chạy thử nghiệm.
- **Task T07 (Glossary và Viết tắt):**
  + Biên soạn hoàn thiện [docs/glossary.md](../docs/glossary.md) bao gồm 5 nhóm thuật ngữ chuẩn hóa: BPMN 2.0, Khai phá & Mô phỏng quy trình (PM4Py, SimPy), Chỉ số hiệu năng vận hành (Cycle Time, Waiting Time, Throughput, Little's Law), Công nghệ triển khai (Docker, Camunda), và Nghiệp vụ y tế chuẩn JCI (BHYT, BHTN, HIS, LIS, RIS/PACS, EMR, RCA).
- **Task T16 (Mô tả quy trình S1, S2, S3):**
  + Biên soạn 3 tài liệu quy trình hỗ trợ hoàn chỉnh:
    * `S1-cap-phat-thuoc.md`: Cấp phát thuốc ngoại trú, đối chiếu 5 đúng theo JCI, liên kết bảo lãnh BHTN và trừ kho HIS.
    * `S2-tuyen-dung-dao-tao.md`: Tuyển dụng & đào tạo nhân sự y tế, thẩm tra văn bằng gốc (PSV - JCI), đào tạo an toàn IPSG/BLS.
    * `S3-khieu-nai.md`: Tiếp nhận & xử lý phản ánh người bệnh, phân tích nguyên nhân gốc rễ (RCA) và hành động khắc phục (CAPA).
  + Đảm bảo phân định rõ ràng giữa căn cứ bằng chứng pháp lý (Luật KCB 2023, Thông tư Bộ Y tế, Tiêu chuẩn JCI) và giả định nghiệp vụ khảo sát.
- **Task T01 (Hỗ trợ cấu trúc repository & README):**
  + Đóng góp rà soát cấu trúc thư mục, chuẩn hóa tài liệu và cập nhật nhật ký thành viên.

### Tuần 2 (23/11/2026 – 29/11/2026): Thiết lập Môi trường Phân tích & Mô phỏng
- **Task T30 (Camunda local + Python Environment + Notebook mẫu):**
  + Chuẩn hóa [requirements.txt](../requirements.txt) với các thư viện cốt lõi (`pm4py`, `simpy`, `pandas`, `numpy`, `matplotlib`, `openpyxl`, `requests`).
  + Xây dựng script kiểm thử tự động [scripts/test_env.py](../scripts/test_env.py) kiểm tra Python runtime, SimPy DES, đọc `data/event_log_template.csv` bằng Pandas, vẽ biểu đồ headless bằng Matplotlib, khám phá DFG và đọc BPMN 2.0 bằng PM4Py, cùng kiểm tra kết nối Camunda Docker local (`http://localhost:8080/engine-rest/version`).
  + Xây dựng notebook mẫu [analysis/test_environment.ipynb](../analysis/test_environment.ipynb) kiểm thử đầy đủ SimPy, PM4Py (Event Log + BPMN), Matplotlib và Camunda REST API.
  + Bổ sung thư mục auto-deployment `infra/camunda/deployments/` đồng bộ với [infra/docker-compose.yml](../infra/docker-compose.yml).
