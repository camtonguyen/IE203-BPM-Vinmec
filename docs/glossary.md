# Bảng Thuật Ngữ và Từ Viết Tắt (Glossary)

Tài liệu này chuẩn hóa toàn bộ các khái niệm, ký hiệu, chỉ số hiệu năng và từ viết tắt được sử dụng xuyên suốt trong đồ án **IE203 – Phân tích, mô hình hóa và cải tiến quy trình khám chữa bệnh ngoại trú tại Bệnh viện Đa khoa Quốc tế Vinmec Central Park**.

---

## 1. Thuật ngữ Quản trị Quy trình & BPMN 2.0 (Business Process Management & Notation)

| Thuật ngữ | Tiếng Anh / Viết tắt | Định nghĩa & Ý nghĩa trong đề tài Vinmec |
|---|---|---|
| **Quản trị quy trình nghiệp vụ** | BPM (*Business Process Management*) | Phương pháp tiếp cận có hệ thống nhằm nhận diện, thiết kế, thực thi, đo lường, giám sát và tối ưu hóa các quy trình khám chữa bệnh tại Vinmec. |
| **Ký hiệu mô hình hóa quy trình** | BPMN 2.0 (*Business Process Model and Notation 2.0*) | Chuẩn quốc tế (OMG / ISO 19510) dùng để trực quan hóa quy trình bằng biểu đồ luồng nghiệp vụ chuẩn xác, cho phép cả nhà quản lý y tế và kỹ sư CNTT cùng hiểu được. |
| **Quy trình hiện trạng** | As-Is Process | Mô hình phản ánh chân thực cách thức quy trình khám ngoại trú đang vận hành trên thực tế tại Vinmec Central Park (ghi nhận qua phỏng vấn, khảo sát, quan sát thực tế). |
| **Quy trình tương lai / cải tiến** | To-Be Process | Mô hình quy trình sau khi đã tái thiết kế, áp dụng chuyển đổi số, loại bỏ lãng phí (Lean) và tối ưu hóa thời gian chờ cho người bệnh. |
| **Quy trình nghiệp vụ** | Business Process | Tập hợp các hoạt động hoặc nhiệm vụ có cấu trúc, được liên kết logic với nhau để tạo ra một kết quả cụ thể phục vụ người bệnh (ví dụ: Quy trình khám ngoại trú, Quy trình cấp phát thuốc). |
| **Sự kiện** | Event | Yếu tố xảy ra trong quá trình vận hành, có thể kích hoạt, làm gián đoạn hoặc kết thúc một luồng xử lý. Ký hiệu bằng hình tròn.<br>- **Start Event**: Sự kiện bắt đầu (viền đơn mảnh).<br>- **Intermediate Event**: Sự kiện trung gian (viền kép).<br>- **End Event**: Sự kiện kết thúc (viền đậm). |
| **Hoạt động / Công việc** | Activity / Task | Đơn vị công việc được thực hiện trong quy trình. Ký hiệu bằng hình chữ nhật bo góc tròn.<br>- **User Task**: Công việc do con người thực hiện với sự hỗ trợ của phần mềm.<br>- **Service Task**: Tác vụ tự động do hệ thống máy tính thực hiện (API, logic phần mềm).<br>- **Manual Task**: Tác vụ thủ công không can thiệp hệ thống. |
| **Cổng điều kiện / Rẽ nhánh** | Gateway | Điểm kiểm soát luồng điều khiển (rẽ nhánh, hội tụ hoặc kết hợp) dựa trên các điều kiện nghiệp vụ. Ký hiệu bằng hình thoi.<br>- **Exclusive Gateway (XOR)**: Rẽ đúng 1 nhánh duy nhất thỏa mãn điều kiện.<br>- **Parallel Gateway (AND)**: Tách luồng song song (Split) hoặc chờ tất cả các luồng hoàn thành (Join).<br>- **Inclusive Gateway (OR)**: Rẽ một hoặc nhiều nhánh đồng thời tùy theo điều kiện.<br>- **Event-based Gateway**: Rẽ nhánh theo sự kiện đầu tiên xảy ra. |
| **Bể chứa** | Pool | Đại diện cho một thực thể hoặc tổ chức độc lập (ví dụ: `Bệnh viện Vinmec Central Park`, `Người bệnh`). Ký hiệu bằng khung chữ nhật lớn nằm ngang/dọc bao bọc toàn bộ quy trình. |
| **Làn** | Lane | Phân chia bên trong một Pool để chỉ định trách nhiệm của từng vai trò, chức danh hoặc phòng ban cụ thể (ví dụ: `Bác sĩ khám`, `Điều dưỡng`, `Dược sĩ`, `Thu ngân`). |
| **Luồng tuần tự** | Sequence Flow | Mũi tên nét liền biểu thị thứ tự thực thi của các công việc, sự kiện và cổng điều kiện bên trong cùng một Pool. |
| **Luồng thông điệp** | Message Flow | Mũi tên nét đứt có hình tròn ở gốc và mũi tên rỗng ở đầu, biểu thị sự trao đổi thông tin hoặc tài liệu giữa hai Pool độc lập (ví dụ: Người bệnh gửi Đơn thuốc cho Nhà thuốc). |
| **Đối tượng dữ liệu** | Data Object | Tài liệu hoặc thông tin nghiệp vụ được tạo ra hoặc sử dụng bởi các hoạt động (ví dụ: Phiếu chỉ định cận lâm sàng, Đơn thuốc điện tử, Hóa đơn viện phí). |

---

## 2. Thuật ngữ Khai phá Quy trình & Mô phỏng (Process Mining & Simulation)

| Thuật ngữ | Tiếng Anh / Viết tắt | Định nghĩa & Ý nghĩa trong đề tài Vinmec |
|---|---|---|
| **Nhật ký sự kiện** | Event Log | Tập dữ liệu ghi lại lịch sử thực thi của các ca bệnh trong hệ thống bệnh viện. Mỗi dòng tối thiểu gồm 3 trường cốt lõi: Mã ca (*Case ID*), Tên hoạt động (*Activity*), Dấu thời gian (*Timestamp*). |
| **Mã ca bệnh** | Case ID | Định danh duy nhất cho một lượt khám bệnh của người bệnh (ví dụ: `L01`, `L02`... để đảm bảo nguyên tắc ẩn danh thông tin y tế). |
| **Khai phá quy trình** | Process Mining | Nhánh công nghệ kết nối giữa khoa học dữ liệu và quản trị quy trình, cho phép trích xuất tri thức từ Event Log thực tế để khám phá (*Process Discovery*), kiểm định sự tuân thủ (*Conformance Checking*) và tăng cường (*Enhancement*). |
| **Thư viện khai phá quy trình Python** | PM4Py (*Process Mining for Python*) | Thư viện mã nguồn mở chuyên dụng trong Python dùng để phân tích dữ liệu log, tạo đồ thị DFG, phát hiện nghẽn cổ chai và tính toán thời gian chu trình thực tế tại Vinmec. |
| **Thư viện mô phỏng rời rạc** | SimPy (*Simulation in Python*) | Thư viện Python dùng cho mô phỏng hướng sự kiện rời rạc (*Discrete-Event Simulation - DES*). Ứng dụng để lập mô hình dòng người bệnh di chuyển qua các hàng đợi (phòng khám, phòng cận lâm sàng, nhà thuốc) trước và sau khi cải tiến. |
| **Độ khớp mô hình** | Fitness | Thước đo trong Conformance Checking đánh giá tỷ lệ các ca khám trong Event Log thực tế có thể được tái hiện hoàn toàn trên mô hình BPMN. |
| **Độ chính xác** | Precision | Thước đo đánh giá liệu mô hình BPMN có cho phép các hành vi không từng xảy ra trong thực tế hay không (tránh mô hình quá lỏng lẻo). |

---

## 3. Các Chỉ số Đo lường Hiệu năng & Vận hành (Performance Metrics & Operations)

| Thuật ngữ | Tiếng Anh / Ký hiệu | Định nghĩa & Công thức áp dụng tại Vinmec |
|---|---|---|
| **Thời gian chu trình** | Cycle Time ($CT$) / Lead Time | Tổng thời gian từ khi người bệnh bước vào cửa tiếp đón bệnh viện Vinmec cho đến khi hoàn tất khám, lấy thuốc và rời đi: $$CT = T_{\text{kết thúc}} - T_{\text{bắt đầu}}$$ |
| **Thời gian phục vụ / Xử lý** | Processing Time / Service Time ($PT$) | Thời gian thực tế mà nhân viên y tế (bác sĩ, điều dưỡng, dược sĩ) trực tiếp làm việc để cung cấp dịch vụ cho người bệnh (ví dụ: thời gian bác sĩ thăm khám trong phòng). |
| **Thời gian chờ** | Waiting Time ($WT$) | Thời gian lãng phí mà người bệnh phải ngồi chờ giữa các khâu (chờ gọi số, chờ kết quả xét nghiệm, chờ phát thuốc): $$WT = CT - \sum PT$$ |
| **Thông lượng** | Throughput ($TH$) | Số lượng lượt người bệnh được phục vụ hoàn tất trong một đơn vị thời gian (ví dụ: số lượt khám/giờ hoặc số lượt/ngày của một phòng khám). |
| **Số lượng đang chờ / Đang xử lý** | Work in Progress ($WIP$) | Số lượng người bệnh đang có mặt đồng thời tại các khâu trong bệnh viện ở một thời điểm bất kỳ. |
| **Hiệu suất sử dụng nguồn lực** | Resource Utilization ($U$) | Tỷ lệ phần trăm thời gian nhân sự hoặc máy móc y tế thực tế bận rộn phục vụ người bệnh so với tổng thời gian làm việc khả dụng: $$U = \frac{\text{Thời gian bận}}{\text{Tổng thời gian ca}} \times 100\%$$ |
| **Định luật Little** | Little's Law | Định lý nền tảng của lý thuyết hàng đợi: $$WIP = TH \times CT$$. Áp dụng để tính toán sức chứa và giảm ùn ứ tại sảnh chờ Vinmec. |
| **Điểm nghẽn cổ chai** | Bottleneck | Khâu có công suất xử lý thấp nhất hoặc thời gian chờ tích lũy cao nhất làm giới hạn thông lượng của toàn bộ chuỗi khám bệnh (thường rơi vào khâu xét nghiệm hoặc thanh toán bảo hiểm). |
| **Thỏa thuận mức dịch vụ** | SLA (*Service Level Agreement*) | Cam kết tiêu chuẩn chất lượng dịch vụ của bệnh viện (ví dụ: thời gian chờ khám dưới 15 phút, trả kết quả xét nghiệm thường quy dưới 60 phút). |

---

## 4. Công nghệ Thông tin, Hạ tầng & Triển khai (DevOps & Systems)

| Thuật ngữ | Tiếng Anh / Viết tắt | Định nghĩa & Ứng dụng |
|---|---|---|
| **Tích hợp & Triển khai liên tục** | CI/CD (*Continuous Integration / Continuous Delivery*) | Quy trình tự động hóa kiểm thử mã nguồn, lint BPMN XML, đếm gateway và kiểm tra tiêu chuẩn trước khi hợp nhất mã nguồn vào nhánh chính của repository. |
| **GitHub Actions** | GitHub Actions | Nền tảng CI/CD tích hợp sẵn của GitHub thực thi các workflow kiểm tra file BPMN, chặn file ghi âm và kiểm tra tính toàn vẹn của mã nguồn. |
| **Công nghệ đóng gói container** | Docker & Docker Compose | Nền tảng ảo hóa mức hệ điều hành, cho phép đóng gói toàn bộ engine Camunda, database và môi trường demo thành các container có thể chạy đồng nhất trên mọi máy tính. |
| **Động cơ thực thi quy trình** | Camunda BPM (Camunda 7 Run) | Nền tảng mã nguồn mở quản lý và thực thi luồng công việc BPMN 2.0. Sử dụng Camunda 7 bản Run để chạy trực tiếp mô hình quy trình To-Be, cung cấp giao diện Tasklist cho nhân viên và Cockpit cho nhà quản lý. |
| **Giao diện lập trình ứng dụng REST** | REST API | Giao diện cho phép hệ thống bên ngoài gọi và tương tác với Camunda Engine (ví dụ: tự động deploy file `.bpmn`, khởi tạo tiến trình khám, cập nhật trạng thái nhiệm vụ). |

---

## 5. Thuật ngữ Y tế, Pháp lý & Nghiệp vụ Vinmec Central Park

| Thuật ngữ | Tiếng Anh / Viết tắt | Định nghĩa & Quy định liên quan |
|---|---|---|
| **Hệ thống Thông tin Bệnh viện** | HIS (*Hospital Information System*) | Hệ thống phần mềm lõi quản lý thông tin hành chính, viện phí, hồ sơ bệnh nhân và lịch hẹn tại Vinmec. |
| **Hệ thống Thông tin Phòng Xét nghiệm** | LIS (*Laboratory Information System*) | Hệ thống tiếp nhận chỉ định, kết nối trực tiếp với máy phân tích huyết học/sinh hóa và tự động trả kết quả về HIS. |
| **Hệ thống Lưu trữ & Truyền hình ảnh Y khoa** | RIS/PACS (*Radiology Information System / Picture Archiving and Communication System*) | Hệ thống quản lý chẩn đoán hình ảnh (X-quang, CT, MRI, Siêu âm) và lưu trữ ảnh số định dạng DICOM chuẩn quốc tế. |
| **Bệnh án Điện tử** | EMR / EHR (*Electronic Medical / Health Record*) | Bản ghi số hóa toàn bộ lịch sử y khoa, kết quả khám, chỉ định cận lâm sàng và đơn thuốc của người bệnh tại Vinmec. |
| **Bảo hiểm Y tế Xã hội** | BHYT | Bảo hiểm y tế bắt buộc theo quy định của Luật Bảo hiểm Y tế Việt Nam. Người bệnh tại Vinmec được hưởng mức chi trả theo diện trái tuyến hoặc đúng tuyến chuyển viện. |
| **Bảo hiểm Tư nhân / Bảo lãnh viện phí** | BHTN (*Private Health Insurance*) | Dịch vụ bảo lãnh thanh toán viện phí trực tiếp giữa Vinmec và các công ty bảo hiểm tư nhân/quốc tế (Bảo Việt, PTI, Manulife, Liberty, Prudential...). |
| **Tiêu chuẩn Quốc tế về Quản lý Y tế** | JCI (*Joint Commission International*) | Bộ tiêu chuẩn chất lượng y tế khắt khe nhất thế giới mà Vinmec Central Park đạt được, yêu cầu nghiêm ngặt về an toàn người bệnh, nhận diện người bệnh (2 định danh), quản lý thuốc và kiểm soát nhiễm khuẩn. |
| **Phân tích nguyên nhân gốc rễ** | RCA (*Root Cause Analysis*) | Phương pháp điều tra, phân tích có cấu trúc để tìm ra nguyên nhân sâu xa của các sự cố y khoa hoặc sự chậm trễ trong quy trình thay vì chỉ khắc phục triệu chứng bề mặt. |
| **Chỉ số sinh hiệu** | Vital Signs | Các dấu hiệu sinh tồn cơ bản của người bệnh được điều dưỡng đo đạc trước khi vào khám: Mạch (Pulse), Huyết áp (Blood Pressure), Thân nhiệt (Temperature), Nhịp thở (Respiration), SpO2. |
| **Cận lâm sàng** | Paraclinical | Các kỹ thuật chẩn đoán hỗ trợ bác sĩ lâm sàng, bao gồm xét nghiệm mẫu bệnh phẩm (máu, nước tiểu) và chẩn đoán hình ảnh (X-quang, siêu âm, nội soi, MRI, CT). |
| **Ứng dụng MyVinmec** | MyVinmec App | Ứng dụng di động của Hệ thống Y tế Vinmec cho phép người bệnh đặt lịch hẹn trước, chọn bác sĩ, thanh toán trực tuyến và tra cứu kết quả cận lâm sàng, đơn thuốc số hóa. |
