# Nhật ký đóng góp – Đinh Hoàng Phát (26410086)

- **Họ và tên:** Đinh Hoàng Phát
- **MSSV:** 26410086
- **Email GitHub:** `hoangphat310304@gmail.com`
- **Vai trò trong nhóm:** Phụ trách Quy trình Hỗ trợ (S1–S3), Hạ tầng CI/CD & Camunda Engine, Mô phỏng Hiệu năng SimPy.
- **Thời gian thực hiện:** 16/11/2026 – 14/12/2026.

---

## 1. Bảng Tổng hợp Nhiệm vụ theo Kế hoạch 4 Tuần

| Tuần | Mã Task | Tên Nhiệm vụ | Sản phẩm & File bàn giao | Trạng thái |
|:---:|:---:|---|---|:---:|
| **1** | **T01** | Hỗ trợ cấu trúc repository & tài liệu README | [README.md](../README.md), [members/26410086-hoang-phat.md](26410086-hoang-phat.md) | **Hoàn thành** |
| **1** | **T04** | Thiết lập CI GitHub Actions & Docker Camunda | [.github/workflows/check.yml](../.github/workflows/check.yml), [infra/docker-compose.yml](../infra/docker-compose.yml), [scripts/check_bpmn.py](../scripts/check_bpmn.py) | **Hoàn thành** |
| **1** | **T07** | Biên soạn Glossary và Bảng từ viết tắt | [docs/glossary.md](../docs/glossary.md) | **Hoàn thành** |
| **1** | **T16** | Mô tả chi tiết quy trình hỗ trợ S1, S2, S3 | [docs/processes/S1-cap-phat-thuoc.md](../docs/processes/S1-cap-phat-thuoc.md)<br>[docs/processes/S2-tuyen-dung-dao-tao.md](../docs/processes/S2-tuyen-dung-dao-tao.md)<br>[docs/processes/S3-khieu-nai.md](../docs/processes/S3-khieu-nai.md) | **Hoàn thành** |
| **2** | **T30** | Thiết lập môi trường Camunda, Python, PM4Py, SimPy | [requirements.txt](../requirements.txt), [scripts/test_env.py](../scripts/test_env.py), [analysis/test_environment.ipynb](../analysis/test_environment.ipynb) | **Hoàn thành** |
| **3** | **T37** | Xây dựng mô hình BPMN 2.0 chuẩn cho S1 và S3 | [bpmn/as-is/S1-cap-phat-thuoc.bpmn](../bpmn/as-is/S1-cap-phat-thuoc.bpmn)<br>[bpmn/as-is/S3-khieu-nai.bpmn](../bpmn/as-is/S3-khieu-nai.bpmn) | **Hoàn thành (1.0đ)** |
| **4** | **T49** | Mô phỏng SimPy As-Is vs To-Be & Đánh giá KPIs | [simulation/simulate_outpatient.py](../simulation/simulate_outpatient.py)<br>[simulation/README.md](../simulation/README.md)<br>[simulation/figures/as_is_vs_to_be_comparison.png](../simulation/figures/as_is_vs_to_be_comparison.png) | **Hoàn thành** |
| **4** | **T50** | Triển khai (Deploy) quy trình C1 To-Be lên Camunda | [bpmn/to-be/C1-kham-ngoai-tru.bpmn](../bpmn/to-be/C1-kham-ngoai-tru.bpmn)<br>[scripts/deploy_camunda.py](../scripts/deploy_camunda.py)<br>[scripts/camunda_worker.py](../scripts/camunda_worker.py) | **Hoàn thành** |
| **4** | **T59** | Đóng gói hạ tầng Demo One-Command & Hướng dẫn | [infra/DEMO_GUIDE.md](../infra/DEMO_GUIDE.md), [infra/camunda/README.md](../infra/camunda/README.md), [infra/camunda/deployments/](../infra/camunda/deployments/) | **Hoàn thành** |

---

## 2. Chi tiết Đóng góp theo Từng Tuần

### Tuần 1 (16/11/2026 – 22/11/2026): Khởi tạo Nền tảng, CI/CD, Thuật ngữ và Mô tả Quy trình
- **Task T04 (CI GitHub Actions + Docker Camunda):**
  + Tối ưu hóa workflow [.github/workflows/check.yml](../.github/workflows/check.yml) chạy tự động trên push/pull request. Tích hợp 3 jobs: Kiểm tra chuẩn BPMN XML và rubric chấm điểm; Kiểm tra bảo mật và quyền riêng tư thông tin y tế (chặn commit file ghi âm thô `.m4a`, `.mp3`); Kiểm tra môi trường Python và script mô phỏng.
  + Nâng cấp công cụ kiểm tra [scripts/check_bpmn.py](../scripts/check_bpmn.py) tự động quét cổng rẽ nhánh, cổng song song split/join, cảnh báo thiếu nhãn điều kiện và chấm điểm rubric tự động.
  + Chuẩn hóa [infra/docker-compose.yml](../infra/docker-compose.yml) sử dụng Camunda Run 7.22.0 với cơ chế tự động nạp file BPMN qua volume mount `./camunda/deployments` và healthcheck.
- **Task T07 (Glossary và Viết tắt):**
  + Biên soạn hoàn thiện [docs/glossary.md](../docs/glossary.md) bao gồm 5 nhóm thuật ngữ chuẩn hóa: BPMN 2.0, Khai phá & Mô phỏng quy trình (PM4Py, SimPy), Chỉ số hiệu năng vận hành (Cycle Time, Waiting Time, Throughput, Little's Law), Công nghệ triển khai (Docker, Camunda), và Nghiệp vụ y tế chuẩn JCI (BHYT, BHTN, HIS, LIS, RIS/PACS, EMR, RCA).
- **Task T16 (Mô tả quy trình S1, S2, S3):**
  + Biên soạn 3 tài liệu quy trình hỗ trợ hoàn chỉnh:
    * `S1-cap-phat-thuoc.md`: Cấp phát thuốc ngoại trú, đối chiếu 5 đúng theo JCI, liên kết bảo lãnh BHTN và trừ kho HIS.
    * `S2-tuyen-dung-dao-tao.md`: Tuyển dụng & đào tạo nhân sự y tế, thẩm tra văn bằng gốc (PSV - JCI), đào tạo an toàn IPSG/BLS.
    * `S3-khieu-nai.md`: Tiếp nhận & xử lý phản ánh người bệnh, phân tích nguyên nhân gốc rễ (RCA) và hành động khắc phục (CAPA).
  + Đảm bảo phân định rõ ràng giữa căn cứ bằng chứng pháp lý (Luật KCB 2023, Thông tư Bộ Y tế, Tiêu chuẩn JCI) và giả định nghiệp vụ khảo sát.
- **Task T01 (Hỗ trợ cấu trúc repository & README):**
  + Bổ sung tài liệu hướng dẫn chạy demo, kiểm tra liên kết chéo và hoàn thiện nhật ký thành viên.

### Tuần 2 (23/11/2026 – 29/11/2026): Thiết lập Môi trường Phân tích & Mô phỏng
- **Task T30 (Camunda + Python Environment):**
  + Chuẩn hóa [requirements.txt](../requirements.txt) với đầy đủ thư viện `pm4py`, `simpy`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl`, `requests`, `pytest`.
  + Xây dựng script kiểm thử tự động [scripts/test_env.py](../scripts/test_env.py) kiểm tra tính sẵn sàng của 5 thành phần: Python runtime, SimPy DES, Pandas/Numpy data handling, Matplotlib headless plotting và PM4Py DFG discovery. Chạy kiểm thử thành công 100%.
  + Xây dựng Jupyter Notebook mẫu [analysis/test_environment.ipynb](../analysis/test_environment.ipynb) phục vụ phân tích trực quan hóa dữ liệu ca khám.

### Tuần 3 (30/11/2026 – 06/12/2026): Xây dựng Mô hình BPMN S1 và S3
- **Task T37 (Mô hình hóa BPMN S1 & S3):**
  + Thiết kế file BPMN 2.0 chuẩn XML cho S1: [bpmn/as-is/S1-cap-phat-thuoc.bpmn](../bpmn/as-is/S1-cap-phat-thuoc.bpmn): 18 activities, 8 cổng điều kiện rẽ nhánh (> 7 cổng), 1 cặp Parallel Split & Join, đầy đủ nhãn điều kiện và sơ đồ BPMNDI. Đạt điểm Rubric: **1.0 / 1.0 (Xuất sắc)**.
  + Thiết kế file BPMN 2.0 chuẩn XML cho S3: [bpmn/as-is/S3-khieu-nai.bpmn](../bpmn/as-is/S3-khieu-nai.bpmn): 22 activities, 8 cổng điều kiện rẽ nhánh (> 7 cổng), 1 cặp Parallel Split & Join, sơ đồ trực quan đầy đủ 5 làn (Lanes). Đạt điểm Rubric: **1.0 / 1.0 (Xuất sắc)**.
  + Kiểm tra toàn bộ bằng `python scripts/check_bpmn.py bpmn`: 0 lỗi cú pháp, 0 cảnh báo.

### Tuần 4 (07/12/2026 – 14/12/2026): Mô phỏng Hiệu năng SimPy, Deploy Camunda & Đóng gói Demo
- **Task T49 (Mô phỏng SimPy As-Is vs To-Be):**
  + Lập trình công cụ mô phỏng [simulation/simulate_outpatient.py](../simulation/simulate_outpatient.py) mô phỏng 480 phút làm việc liên tục (1 ngày hành chính) tại Vinmec Central Park với phân phối đến Poisson giờ cao điểm và phân phối xử lý Triangular thực tế.
  + Kết quả định lượng chứng minh:
    * Throughput tăng **+82.5%** (80 ca lên 146 ca).
    * Thời gian chu trình trung bình (Cycle Time) giảm **44.5%** (195.3 phút xuống 108.3 phút).
    * Thời gian chờ trung bình giảm **46.4%** (124.2 phút xuống 66.6 phút).
    * Giải tỏa điểm nghẽn lễ tân tiếp đón (công suất giảm từ 97.1% quá tải xuống 16.7% an toàn nhờ Kiosk & App MyVinmec).
  + Kết xuất bộ 4 đồ thị chất lượng cao tại [simulation/figures/as_is_vs_to_be_comparison.png](../simulation/figures/as_is_vs_to_be_comparison.png) và bảng tóm tắt [simulation/simulation_results_summary.csv](../simulation/simulation_results_summary.csv).
  + Soạn thảo tài liệu phân tích chuyên sâu tại [simulation/README.md](../simulation/README.md).
- **Task T50 (Deploy C1 To-Be lên Camunda):**
  + Xây dựng quy trình thực thi [bpmn/to-be/C1-kham-ngoai-tru.bpmn](../bpmn/to-be/C1-kham-ngoai-tru.bpmn) (`isExecutable="true"`, 19 activities, 8 conditional gateways, 1 cặp parallel split & join, đạt **1.0đ Rubric**).
  + Viết công cụ deploy tự động qua REST API [scripts/deploy_camunda.py](../scripts/deploy_camunda.py) hỗ trợ khởi tạo phiên chạy ca khám mẫu.
  + Lập trình External Task Worker [scripts/camunda_worker.py](../scripts/camunda_worker.py) bằng Python tự động xử lý các tác vụ dịch vụ (đồng bộ hóa đơn kho dược, đặt lịch tái khám tự động qua App).
- **Task T59 (Đóng gói Docker Compose Demo):**
  + Thiết lập thư mục auto-deployment [infra/camunda/deployments/](../infra/camunda/deployments/) chứa sẵn cả 3 file BPMN (`C1-kham-ngoai-tru.bpmn`, `S1-cap-phat-thuoc.bpmn`, `S3-khieu-nai.bpmn`).
  + Soạn thảo kịch bản demo hoàn chỉnh [infra/DEMO_GUIDE.md](../infra/DEMO_GUIDE.md) và tài liệu vận hành [infra/camunda/README.md](../infra/camunda/README.md) hướng dẫn thầy cô và các thành viên chạy thử nghiệm hệ thống chỉ với một lệnh `docker compose up -d`.
