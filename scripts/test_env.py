#!/usr/bin/env python3
"""Script kiểm tra toàn diện môi trường phân tích quy trình & mô phỏng IE203 (Task T30).

Kiểm tra:
1. Phiên bản Python (>= 3.10)
2. Thư viện mô phỏng SimPy (khởi tạo Environment, chạy tiến trình mẫu)
3. Thư viện xử lý dữ liệu Pandas & Numpy (đọc event_log.csv / event_log_template.csv)
4. Thư viện trực quan hóa Matplotlib (backend headless Agg, xuất biểu đồ test)
5. Thư viện khai phá quy trình PM4Py (format_dataframe, discover_dfg)
6. Khả năng đọc file BPMN 2.0 XML bằng PM4Py (read_bpmn)
7. Kiểm tra kết nối Camunda Docker local (tùy chọn, không làm lỗi CI)
"""

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_python_version():
    """Kiểm tra phiên bản Python."""
    print("1. Kiểm tra phiên bản Python...")
    v = sys.version_info
    print(f"   -> Python {v.major}.{v.minor}.{v.micro}")
    assert (v.major, v.minor) >= (3, 10), "Yêu cầu Python >= 3.10"
    return True


def test_simpy():
    """Kiểm tra thư viện SimPy."""
    print("2. Kiểm tra SimPy (Mô phỏng hướng sự kiện rời rạc)...")
    import simpy

    print(f"   -> SimPy version: {simpy.__version__}")
    env = simpy.Environment()
    results = []

    def patient_process(env, name, delay):
        yield env.timeout(delay)
        results.append((name, env.now))

    env.process(patient_process(env, "Bệnh nhân L01", 5))
    env.process(patient_process(env, "Bệnh nhân L02", 12))
    env.run(until=20)

    assert len(results) == 2, "Lỗi chạy tiến trình SimPy"
    assert results[0] == ("Bệnh nhân L01", 5), "Sai lệch thời gian mô phỏng L01"
    assert results[1] == ("Bệnh nhân L02", 12), "Sai lệch thời gian mô phỏng L02"
    print("   -> SimPy chạy kiểm thử thành công: 2 tiến trình hoàn tất đúng thời gian.")
    return True


def test_pandas_numpy():
    """Kiểm tra Pandas, Numpy và đọc event_log.csv / event_log_template.csv."""
    print("3. Kiểm tra Pandas & Numpy...")
    import numpy as np
    import pandas as pd

    print(f"   -> Pandas version: {pd.__version__}")
    print(f"   -> Numpy version: {np.__version__}")

    log_path = event_log_path()
    df = pd.read_csv(log_path)
    required_cols = {"case_id", "activity", "start_time", "end_time"}
    assert required_cols.issubset(df.columns), f"Thiếu cột chuẩn trong {log_path}"
    print(f"   -> Đọc thành công {log_path}: {len(df)} dòng, đầy đủ cột chuẩn.")
    return True


def event_log_path():
    for filename in ("event_log.csv", "event_log_template.csv"):
        path = ROOT / "data" / filename
        if path.is_file():
            return path
    raise FileNotFoundError("Chưa tìm thấy data/event_log.csv hoặc data/event_log_template.csv")


def test_matplotlib():
    """Kiểm tra Matplotlib ở chế độ headless (Agg)."""
    print("4. Kiểm tra Matplotlib...")
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print(f"   -> Matplotlib version: {matplotlib.__version__}")

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.bar(["Chờ khám", "Bác sĩ khám", "Lấy thuốc"], [25, 15, 10], color=["#e74c3c", "#2ecc71", "#3498db"])
    ax.set_title("Kiểm thử biểu đồ thời gian Vinmec")
    plt.tight_layout()

    out_test = ROOT / "analysis/test_plot.png"
    out_test.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_test)
    plt.close(fig)

    assert out_test.exists() and out_test.stat().st_size > 0, "Lỗi xuất file ảnh Matplotlib"
    out_test.unlink()
    print("   -> Matplotlib xuất biểu đồ thành công (Headless mode).")
    return True


def test_pm4py_event_log():
    """Kiểm tra PM4Py và khám phá DFG từ Event Log."""
    print("5. Kiểm tra PM4Py (Process Mining trên Event Log)...")
    import pandas as pd
    import pm4py

    print(f"   -> PM4Py version: {pm4py.__version__}")

    df = pd.read_csv(event_log_path())

    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    event_log = pm4py.format_dataframe(
        df,
        case_id="case_id",
        activity_key="activity",
        timestamp_key="end_time",
    )
    dfg, _, _ = pm4py.discover_dfg(event_log)
    assert len(dfg) > 0, "Không trích xuất được DFG từ Event Log"
    print(f"   -> PM4Py trích xuất DFG thành công ({len(dfg)} quan hệ trực tiếp).")
    return True


def test_pm4py_bpmn():
    """Kiểm tra khả năng đọc file BPMN 2.0 XML bằng PM4Py."""
    print("6. Kiểm tra đọc mô hình BPMN 2.0 (PM4Py)...")
    import pm4py

    bpmn_files = sorted((ROOT / "bpmn").rglob("*.bpmn"))
    if bpmn_files:
        bpmn_graph = pm4py.read_bpmn(str(bpmn_files[0]))
        nodes = bpmn_graph.get_nodes()
        assert len(nodes) > 0, f"File BPMN {bpmn_files[0]} không có node nào"
        print(f"   -> Đọc thành công {bpmn_files[0]} ({len(nodes)} nodes).")
        return True

    sample_bpmn = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
                  id="Definitions_Test" targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_Test" isExecutable="false">
    <bpmn:startEvent id="Start_1" name="Bắt đầu"/>
    <bpmn:task id="Task_1" name="Tiếp đón"/>
    <bpmn:endEvent id="End_1" name="Kết thúc"/>
    <bpmn:sequenceFlow id="Flow_1" sourceRef="Start_1" targetRef="Task_1"/>
    <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="End_1"/>
  </bpmn:process>
</bpmn:definitions>
"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_bpmn = Path(tmpdir) / "sample_test.bpmn"
        tmp_bpmn.write_text(sample_bpmn, encoding="utf-8")
        bpmn_graph = pm4py.read_bpmn(str(tmp_bpmn))
        nodes = bpmn_graph.get_nodes()
        assert len(nodes) == 3, f"Kỳ vọng 3 nodes trong BPMN mẫu, nhận được {len(nodes)}"
        print(f"   -> Đọc thành công BPMN 2.0 mẫu bằng PM4Py ({len(nodes)} nodes).")
    return True


def check_camunda_local():
    """Kiểm tra kết nối Camunda Docker local (thông tin tham khảo, không bắt buộc trong CI)."""
    print("7. Kiểm tra kết nối Camunda Engine local (http://localhost:8080)...")
    try:
        import requests

        resp = requests.get("http://localhost:8080/v2/topology", timeout=2)
        if resp.status_code == 200:
            print(f"   -> Camunda đang hoạt động: {resp.json()}")
        else:
            print(f"   -> [INFO] Camunda phản hồi mã {resp.status_code}.")
    except Exception:
        print("   -> [INFO] Camunda chưa chạy tại localhost:8080 (bỏ qua trong môi trường CI).")
    return True


def main():
    print("=" * 70)
    print("IE203 - BỆNH VIỆN VINMEC: KIỂM THỬ MÔI TRƯỜNG PYTHON & TOOLING (T30)")
    print("=" * 70)

    tests = [
        ("Python Version", test_python_version),
        ("SimPy Simulation", test_simpy),
        ("Pandas & Numpy", test_pandas_numpy),
        ("Matplotlib Visualization", test_matplotlib),
        ("PM4Py Event Log", test_pm4py_event_log),
        ("PM4Py BPMN Reader", test_pm4py_bpmn),
        ("Camunda Local Check", check_camunda_local),
    ]

    failed = False
    for _, func in tests:
        try:
            func()
        except Exception as e:
            print(f"   [FAIL] Lỗi: {e}")
            failed = True
        print("-" * 70)

    if failed:
        print("[FAIL] Môi trường có lỗi cấu hình. Vui lòng kiểm tra lại pip install -r requirements.txt.")
        return 1

    print("[OK] TẤT CẢ CÁC BÀI KIỂM THỬ ĐÃ VƯỢT QUA! MÔI TRƯỜNG SẴN SÀNG.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())

