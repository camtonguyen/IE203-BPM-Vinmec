"""Kiểm tra event log theo data/HUONG-DAN-GHI-THOI-GIAN.md.

Dùng: python scripts/check_event_log.py data/event_log.csv
Thoát mã 1 nếu có lỗi.
"""
import csv
import re
import sys
from datetime import datetime
from pathlib import Path

COLUMNS = ["case_id", "activity", "start_time", "end_time", "resource", "note"]
FMT = "%Y-%m-%d %H:%M"
GUIDE = Path(__file__).resolve().parent.parent / "data" / "HUONG-DAN-GHI-THOI-GIAN.md"


def allowed_activities():
    """Đọc danh mục hoạt động từ bảng mục 3 của file hướng dẫn."""
    text = GUIDE.read_text(encoding="utf-8")
    section = text.split("## 3.", 1)[1].split("\n## ", 1)[0]
    names = set()
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and cells[0] != "Hoạt động" and not set(cells[0]) <= set("-: "):
            names.add(cells[0])
    return names


def check(path):
    errors = []
    activities = allowed_activities()
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            return [f"Tiêu đề phải là: {','.join(COLUMNS)} (đang là {reader.fieldnames})"]
        for i, row in enumerate(reader, start=2):
            where = f"dòng {i}"
            if not re.fullmatch(r"L\d{2,}", row["case_id"] or ""):
                errors.append(f"{where}: case_id '{row['case_id']}' phải dạng L01, L02…")
            if row["activity"] not in activities:
                errors.append(f"{where}: activity '{row['activity']}' không có trong danh mục")
            try:
                start = datetime.strptime(row["start_time"], FMT)
                end = datetime.strptime(row["end_time"], FMT)
                if end < start:
                    errors.append(f"{where}: end_time trước start_time")
            except ValueError:
                errors.append(f"{where}: thời gian phải dạng YYYY-MM-DD HH:MM")
    return errors


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    errors = check(sys.argv[1])
    for e in errors:
        print("LỖI", e)
    print("OK" if not errors else f"{len(errors)} lỗi")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
