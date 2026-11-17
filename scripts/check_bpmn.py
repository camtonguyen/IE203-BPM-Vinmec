"""Kiểm tra các file .bpmn theo rubric IE203.

- XML hợp lệ, có thẻ definitions của BPMN 2.0
- Đếm cổng điều kiện (exclusive/inclusive/event-based/complex) và parallel gateway
- Kiểm tra có split & join song song
- Cảnh báo gateway rẽ nhánh chưa đặt tên / nhánh ra chưa ghi điều kiện
Mức điểm rubric: >7 cổng = 1đ; >=5 = 0.75đ; >=3 = 0.5đ.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}
COND = ["exclusiveGateway", "inclusiveGateway", "eventBasedGateway", "complexGateway"]


def score(n):
    return 1.0 if n > 7 else 0.75 if n >= 5 else 0.5 if n >= 3 else 0.0


def check(path):
    errors, warns = [], []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return [f"XML lỗi: {e}"], [], None
    if not root.tag.endswith("definitions"):
        return ["Không phải file BPMN 2.0 (thiếu definitions)"], [], None

    flows = {f.get("id"): f for f in root.iter(f"{{{NS['bpmn']}}}sequenceFlow")}
    cond = []
    for t in COND:
        cond += list(root.iter(f"{{{NS['bpmn']}}}{t}"))
    par = list(root.iter(f"{{{NS['bpmn']}}}parallelGateway"))

    for g in cond:
        outs = g.findall("bpmn:outgoing", NS)
        if len(outs) > 1:
            if not (g.get("name") or "").strip():
                warns.append(f"Gateway {g.get('id')} rẽ nhánh nhưng chưa đặt tên câu hỏi")
            for o in outs:
                f = flows.get(o.text)
                if f is not None and not (f.get("name") or "").strip() \
                        and f.find("bpmn:conditionExpression", NS) is None \
                        and g.get("default") != f.get("id"):
                    warns.append(f"Nhánh {f.get('id')} từ {g.get('id')} chưa ghi điều kiện")

    splits = [g for g in par if len(g.findall("bpmn:outgoing", NS)) > 1]
    joins = [g for g in par if len(g.findall("bpmn:incoming", NS)) > 1]
    if not splits or not joins:
        warns.append("Chưa có cặp parallel split & join (rubric yêu cầu Split & Join)")
    return errors, warns, (len(cond), len(splits), len(joins))


def main(folder):
    files = sorted(Path(folder).rglob("*.bpmn"))
    if not files:
        print("Chưa có file .bpmn nào.")
        return 0
    failed = False
    for f in files:
        errors, warns, stats = check(f)
        print(f"\n== {f}")
        for e in errors:
            print("  LỖI:", e)
        if stats:
            n, s, j = stats
            print(f"  Cổng điều kiện: {n}  | parallel split: {s}, join: {j}  | điểm độ phức tạp ước tính: {score(n)}")
        for w in warns:
            print("  Cảnh báo:", w)
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "bpmn"))
