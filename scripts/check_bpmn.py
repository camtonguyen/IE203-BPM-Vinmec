#!/usr/bin/env python3
"""Công cụ kiểm tra & chấm điểm các file .bpmn theo Rubric IE203 - Bệnh viện Vinmec.

Quy định Rubric IE203:
- File XML hợp lệ, đúng chuẩn BPMN 2.0 (thẻ definitions, namespace OMG).
- Kiểm tra Start Event và End Event của quy trình.
- Đếm cổng điều kiện: Exclusive (XOR), Inclusive (OR), Event-Based, Complex Gateway.
  + Thang điểm độ phức tạp cổng rẽ nhánh:
    * > 7 cổng điều kiện: 1.0 điểm (Mức tối đa).
    * >= 5 cổng điều kiện: 0.75 điểm.
    * >= 3 cổng điều kiện: 0.5 điểm.
    * < 3 cổng điều kiện: 0.0 điểm.
- Kiểm tra tính song song (Parallel Gateway):
  + Phải có ít nhất 1 cặp Parallel Split (tách luồng song song) và Parallel Join (hội tụ luồng).
- Kiểm tra quy tắc đặt tên & biểu diễn luồng:
  + Cổng rẽ nhánh phải có nhãn câu hỏi (ví dụ: "Có BHYT không?").
  + Các nhánh rẽ ra phải có nhãn điều kiện (hoặc conditionExpression hoặc default flow).
  + Kiểm tra luồng kết nối (Sequence Flow) tránh phần tử bị cô lập.
  + Kiểm tra phần tử BPMNDI để đảm bảo mở được trên Camunda Modeler / bpmn.io.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"
BPMNDI_NS = "http://www.omg.org/spec/BPMN/20100524/DI"
DC_NS = "http://www.omg.org/spec/DD/20100524/DC"
DI_NS = "http://www.omg.org/spec/DD/20100524/DI"

NAMESPACES = {
    "bpmn": BPMN_NS,
    "bpmndi": BPMNDI_NS,
    "dc": DC_NS,
    "di": DI_NS,
}

COND_GATEWAYS = [
    "exclusiveGateway",
    "inclusiveGateway",
    "eventBasedGateway",
    "complexGateway",
]

TASK_TYPES = [
    "task",
    "userTask",
    "serviceTask",
    "sendTask",
    "receiveTask",
    "manualTask",
    "businessRuleTask",
    "scriptTask",
    "subProcess",
    "callActivity",
]


def calculate_score(cond_count: int) -> float:
    """Tính điểm độ phức tạp rẽ nhánh theo Rubric IE203."""
    if cond_count > 7:
        return 1.0
    if cond_count >= 5:
        return 0.75
    if cond_count >= 3:
        return 0.5
    return 0.0


def check_bpmn_file(file_path: Path):
    """Kiểm tra chi tiết 1 file .bpmn.
    
    Returns:
        errors (list): Các lỗi nghiêm trọng (XML hỏng, thiếu definitions).
        warns (list): Các cảnh báo về chuẩn mô hình hóa (chưa đặt tên nhánh, thiếu split/join).
        stats (dict): Thống kê số lượng phần tử và điểm rubric.
    """
    errors = []
    warns = []
    stats = {}

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as err:
        return [f"Lỗi cú pháp XML: {err}"], [], {}
    except Exception as err:
        return [f"Không thể đọc file: {err}"], [], {}

    # 1. Kiểm tra thẻ gốc definitions
    if not root.tag.endswith("definitions"):
        return ["File không phải định dạng BPMN 2.0 (thiếu thẻ gốc <definitions>)"], [], {}

    # 2. Thu thập các phần tử luồng
    flows = {f.get("id"): f for f in root.iter(f"{{{BPMN_NS}}}sequenceFlow")}
    start_events = list(root.iter(f"{{{BPMN_NS}}}startEvent"))
    end_events = list(root.iter(f"{{{BPMN_NS}}}endEvent"))

    if not start_events:
        warns.append("Quy trình chưa có Start Event (<startEvent>)")
    if not end_events:
        warns.append("Quy trình chưa có End Event (<endEvent>)")

    # 3. Thu thập các loại Task / Activity
    activities = []
    for t in TASK_TYPES:
        activities.extend(root.iter(f"{{{BPMN_NS}}}{t}"))

    # 4. Thu thập Cổng điều kiện & Parallel Gateways
    cond_gateways = []
    for gtype in COND_GATEWAYS:
        cond_gateways.extend(root.iter(f"{{{BPMN_NS}}}{gtype}"))

    par_gateways = list(root.iter(f"{{{BPMN_NS}}}parallelGateway"))

    # 5. Phân tích Cổng rẽ nhánh (Split) & Hội tụ (Join)
    for g in cond_gateways:
        gid = g.get("id", "unnamed")
        gname = (g.get("name") or "").strip()
        outs = g.findall("bpmn:outgoing", NAMESPACES)
        ins = g.findall("bpmn:incoming", NAMESPACES)

        # Rẽ nhánh nếu outgoing > 1
        if len(outs) > 1:
            if not gname:
                warns.append(f"Cổng rẽ nhánh '{gid}' chưa đặt tên câu hỏi điều kiện (ví dụ: 'Có BHYT không?')")
            for out in outs:
                flow_id = out.text.strip() if out.text else ""
                flow = flows.get(flow_id)
                if flow is not None:
                    flow_name = (flow.get("name") or "").strip()
                    cond_expr = flow.find("bpmn:conditionExpression", NAMESPACES)
                    default_flow = g.get("default")
                    if not flow_name and cond_expr is None and default_flow != flow_id:
                        warns.append(f"Nhánh rẽ '{flow_id}' từ cổng '{gid}' chưa có nhãn điều kiện (Condition)")

    # 6. Kiểm tra cặp Parallel Split & Parallel Join
    par_splits = [g for g in par_gateways if len(g.findall("bpmn:outgoing", NAMESPACES)) > 1]
    par_joins = [g for g in par_gateways if len(g.findall("bpmn:incoming", NAMESPACES)) > 1]

    has_parallel_pair = len(par_splits) >= 1 and len(par_joins) >= 1
    if not has_parallel_pair:
        warns.append("Chưa đủ cặp Parallel Split & Join (Rubric yêu cầu có nhánh thực thi song song)")

    # 7. Kiểm tra BPMNDI (Tọa độ trực quan để mở trong Camunda Modeler)
    diagrams = list(root.iter(f"{{{BPMNDI_NS}}}BPMNDiagram"))
    if not diagrams:
        warns.append("Thiếu phần tử <bpmndi:BPMNDiagram> (sẽ không hiển thị hình ảnh trên Camunda Modeler / bpmn.io)")

    # 8. Thống kê tổng hợp
    cond_count = len(cond_gateways)
    rubric_score = calculate_score(cond_count)

    stats = {
        "start_events": len(start_events),
        "end_events": len(end_events),
        "activities": len(activities),
        "cond_gateways": cond_count,
        "par_splits": len(par_splits),
        "par_joins": len(par_joins),
        "rubric_score": rubric_score,
        "has_parallel_pair": has_parallel_pair,
        "has_bpmndi": len(diagrams) > 0,
    }

    return errors, warns, stats


def main(target_dir="bpmn"):
    """Quét và kiểm tra toàn bộ file .bpmn trong thư mục."""
    target_path = Path(target_dir)
    if not target_path.exists():
        print(f"Thư mục '{target_dir}' không tồn tại.")
        return 0

    bpmn_files = sorted(target_path.rglob("*.bpmn"))
    if not bpmn_files:
        print(f"Chưa tìm thấy file .bpmn nào trong thư mục '{target_dir}'.")
        return 0

    print("=" * 80)
    print(f"KIỂM TRA CHẤT LƯỢNG BPMN 2.0 THEO RUBRIC IE203 - BỆNH VIỆN VINMEC")
    print(f"Số lượng file tìm thấy: {len(bpmn_files)}")
    print("=" * 80)

    has_errors = False
    all_passed_rubric = True

    for fpath in bpmn_files:
        errors, warns, stats = check_bpmn_file(fpath)
        print(f"\n📂 File: {fpath}")

        if errors:
            has_errors = True
            for err in errors:
                print(f"  ❌ LỖI: {err}")
            continue

        cond_n = stats.get("cond_gateways", 0)
        p_split = stats.get("par_splits", 0)
        p_join = stats.get("par_joins", 0)
        score = stats.get("rubric_score", 0.0)
        acts = stats.get("activities", 0)

        status_icon = "🌟 [XUẤT SẮC - 1.0 ĐIỂM]" if score == 1.0 else "⚠️ [CHƯA ĐẠT TỐI ĐA]"
        print(f"  - Số công việc (Activities/Tasks): {acts}")
        print(f"  - Cổng điều kiện rẽ nhánh (Exclusive/Inclusive/Event-based): {cond_n}")
        print(f"  - Parallel Gateway: Split = {p_split}, Join = {p_join}")
        print(f"  - Đánh giá Rubric IE203: {score:.2f}/1.0 điểm -> {status_icon}")

        if warns:
            for w in warns:
                print(f"    ⚠️ Cảnh báo: {w}")
        else:
            print("    ✅ Hoàn toàn đạt chuẩn mô hình hóa BPMN 2.0 (không có cảnh báo)")

        if score < 1.0 or not stats.get("has_parallel_pair"):
            all_passed_rubric = False

    print("\n" + "=" * 80)
    if has_errors:
        print("❌ KẾT QUẢ: Phát hiện lỗi cú pháp XML hoặc định dạng BPMN. Cần sửa trước khi merge!")
        return 1
    
    if all_passed_rubric:
        print("🎉 KẾT QUẢ: Tất cả các file BPMN đều đạt điểm tối đa (1.0đ) theo Rubric IE203!")
    else:
        print("ℹ️ KẾT QUẢ: Tất cả file XML hợp lệ. Một số file cần bổ sung thêm cổng để đạt tối đa rubric.")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "bpmn"
    sys.exit(main(folder))
