"""Sinh data/event_log.csv bản MÔ PHỎNG (không phải số liệu đo thật).

Dùng: python scripts/sinh_event_log_mau.py
Nguồn của từng khoảng thời gian: xem data/README.md. Cùng SEED thì ra cùng file.
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 27
CASES = 30
OUT = Path(__file__).resolve().parent.parent / "data" / "event_log.csv"

# Khoảng thời gian (phút), phân phối đều.
VINMEC = {  # theo trang Vinmec công bố
    "Khám lần 1": (20, 40),       # trung bình khoảng 30 phút/lượt
    "Trả xét nghiệm": (60, 120),  # xét nghiệm đơn giản 1–2 giờ, tính từ lúc lấy mẫu xong
    "Chờ bảo lãnh": (15, 45),
}
ASSUMED = {  # nhóm giả định, chưa có nguồn: thay bằng số đo/phỏng vấn khi có
    "Tiếp đón - mở hồ sơ": (3, 10),
    "Chờ đo sinh hiệu": (1, 15),
    "Đo sinh hiệu": (3, 6),
    "Chờ khám": (5, 30),
    "Chờ thêm do đến trực tiếp/muộn": (5, 20),
    "Thanh toán": (3, 10),
    "Chờ cận lâm sàng": (4, 25),
    "Xét nghiệm - lấy mẫu": (5, 10),
    "Chẩn đoán hình ảnh": (10, 30),
    "Trả kết quả hình ảnh": (15, 45),
    "Khám lần 2 - đọc kết quả": (5, 15),
    "Lĩnh thuốc": (5, 20),
}
# Số lượt mỗi nhánh trong CASES lượt (giả định), được xáo ngẫu nhiên. "muộn" = có lịch hẹn nhưng đến muộn.
ARRIVAL = {"có lịch hẹn": 13, "muộn": 2, "đến trực tiếp": 15}
CLS = {(): 12, ("xn",): 6, ("cdha",): 6, ("xn", "cdha"): 6}
INSURED = {True: 9, False: 21}
DRUG = {True: 21, False: 9}
# Điểm nghẽn: hướng tác động lấy từ nguồn công khai (data/README.md), mức độ là giả định.
PEAK_FACTOR = 1.5  # thứ Bảy: tiếp đón và các bước chờ chưa có số Vinmec dài thêm
ROLES = {
    "Tiếp đón - mở hồ sơ": "Lễ tân", "Đo sinh hiệu": "Điều dưỡng", "Khám lần 1": "Bác sĩ",
    "Thanh toán": "Thu ngân", "Xét nghiệm - lấy mẫu": "Kỹ thuật viên XN",
    "Chẩn đoán hình ảnh": "Kỹ thuật viên CĐHA", "Thăm dò chức năng": "Kỹ thuật viên CĐHA", "Khám lần 2 - đọc kết quả": "Bác sĩ", "Lĩnh thuốc": "Dược sĩ",
}
# Giờ khám ngoại trú Central Park theo Vinmec: (giờ mở, giờ đóng, khoảng phút đến sau giờ mở)
SESSIONS = [((7, 30), (12, 0), 90), ((13, 0), (16, 30), 45)]
DAYS = [datetime(2026, 11, d) for d in range(23, 29)]  # thứ Hai – thứ Bảy

# 3 lượt NGOÀI Vinmec (L31–L33) dựng quanh mốc giờ in trên chứng từ. Ngày đã đổi; không ghi tên, cơ sở, chẩn đoán,
# chi trả. Chỉ các giờ có ghi "chứng từ" là lấy từ phiếu; thứ tự bước và mọi giờ khác là giả định.
# Mỗi dòng: (hoạt động, bắt đầu, kết thúc, ghi chú)
DOC_VISITS = [
    (datetime(2026, 11, 16), "bệnh viện công", [
        ("Tiếp đón - mở hồ sơ", "07:00", "07:08", "giả định"),
        ("Chờ khám", "07:08", "07:40", "giả định"),
        ("Khám lần 1", "07:40", "07:53", "kết thúc đặt theo giờ in đơn thuốc trên chứng từ"),
        ("Lĩnh thuốc", "07:53", "08:15", "giả định; bắt đầu đặt theo giờ in đơn thuốc trên chứng từ"),
    ]),
    (datetime(2026, 11, 17), "bệnh viện công", [
        ("Tiếp đón - mở hồ sơ", "05:00", "05:08", "giả định"),
        ("Chờ khám", "05:08", "05:30", "giả định"),
        ("Khám lần 1", "05:30", "05:43", "kết thúc đặt theo giờ chỉ định trên chứng từ"),
        ("Chờ thanh toán", "05:43", "06:35", "từ giờ chỉ định đến giờ in phiếu chỉ định trên chứng từ"),
        ("Thanh toán", "06:35", "06:38", "từ giờ in phiếu chỉ định đến giờ in phiếu thu trên chứng từ; tạm ứng"),
        ("Chờ cận lâm sàng", "06:38", "07:05", "giả định"),
        ("Chẩn đoán hình ảnh", "07:05", "07:20", "giả định"),
        ("Chờ cận lâm sàng", "07:20", "07:50", "giả định"),
        ("Thăm dò chức năng", "07:50", "08:05", "giả định"),
        ("Chờ kết quả", "08:05", "09:10", "giả định"),
        ("Khám lần 2 - đọc kết quả", "09:10", "09:20", "giả định"),
        ("Thanh toán", "09:20", "09:30", "giả định; quyết toán"),
    ]),
    (datetime(2026, 11, 18), "phòng khám tư", [
        ("Tiếp đón - mở hồ sơ", "07:26", "07:32", "kết thúc đặt theo giờ in nhãn xét nghiệm trên chứng từ"),
        ("Thanh toán", "07:32", "07:36", "giả định"),
        ("Chờ cận lâm sàng", "07:36", "07:50", "giả định"),
        ("Xét nghiệm - lấy mẫu", "07:50", "07:56", "giả định"),
        ("Chờ kết quả", "07:56", "09:20", "giả định"),
    ]),
]


def visit(rng, start, arrival, kinds, insured, drug):
    """Một lượt khám bắt đầu từ start; trả về (các dòng theo giờ bắt đầu, giờ kết thúc)."""
    rows, now = [], start

    weekend = start.weekday() == 5

    def minutes(key):
        value = rng.randint(*{**VINMEC, **ASSUMED}[key])
        if weekend and key in ASSUMED and (key.startswith("Chờ ") or key == "Tiếp đón - mở hồ sơ"):
            value = round(value * PEAK_FACTOR)
        return timedelta(minutes=value)

    def step(activity, note="giả định", length=None):
        nonlocal now
        end = now + (length or minutes(activity))
        if weekend and activity.startswith("Chờ ") and activity not in ("Chờ kết quả", "Chờ bảo lãnh"):
            note += "; cuối tuần đông khách"
        rows.append([activity, now, end, ROLES.get(activity, ""), f"mô phỏng; {note}"])
        now = end

    booked = "đến trực tiếp" if arrival == "đến trực tiếp" else "có lịch hẹn"
    step("Tiếp đón - mở hồ sơ", f"giả định; {booked}; " + ("bảo hiểm tư nhân" if insured else "tự chi trả"))
    step("Chờ đo sinh hiệu")
    step("Đo sinh hiệu")
    reason = {"đến trực tiếp": "đến trực tiếp", "muộn": "đến muộn so với giờ hẹn"}.get(arrival)
    if reason:
        step("Chờ khám", f"giả định; {reason}, chờ xếp lượt",
             minutes("Chờ khám") + minutes("Chờ thêm do đến trực tiếp/muộn"))
    else:
        step("Chờ khám")
    step("Khám lần 1", "Vinmec: mỗi lượt khám khoảng 30 phút")
    if kinds:
        step("Thanh toán", "giả định; tạm ứng cận lâm sàng")
        split, sampled = now, None
        if "xn" in kinds:
            step("Chờ cận lâm sàng", "giả định; xét nghiệm")
            step("Xét nghiệm - lấy mẫu")
            sampled = now
        if "cdha" in kinds:
            # Song song (quy tắc 5): xếp hàng CĐHA từ lúc tách nhánh, nhưng chỉ vào chụp sau khi lấy mẫu xong.
            free, now = now, split
            step("Chờ cận lâm sàng", "giả định; chẩn đoán hình ảnh", max(minutes("Chờ cận lâm sàng"), free - split))
            step("Chẩn đoán hình ảnh", "giả định; " + rng.choice(["siêu âm", "X-quang"]))
        ready, note = now, "giả định; kết quả hình ảnh"
        if "cdha" in kinds:
            ready = now + minutes("Trả kết quả hình ảnh")
        if sampled and (lab := sampled + minutes("Trả xét nghiệm")) > ready:
            ready, note = lab, "Vinmec: xét nghiệm đơn giản 1–2 giờ tính từ lúc lấy mẫu"
        step("Chờ kết quả", note, ready - now)
        step("Khám lần 2 - đọc kết quả")
    if insured:
        step("Chờ bảo lãnh", "Vinmec: xử lý bảo lãnh 15–45 phút")
        step("Thanh toán", "giả định; bảo lãnh")
    elif not kinds:
        step("Thanh toán", "giả định; sau khám")
    if drug:
        step("Lĩnh thuốc")
    rows.sort(key=lambda row: row[1])
    return rows, now


def generate():
    rng = random.Random(SEED)
    plan = []
    for counts in (ARRIVAL, CLS, INSURED, DRUG):
        column = [value for value, count in counts.items() for _ in range(count)]
        assert len(column) == CASES
        rng.shuffle(column)
        plan.append(column)
    visits = []
    for n, branches in enumerate(zip(*plan)):
        day = DAYS[n * len(DAYS) // CASES]
        while True:  # lượt kéo quá giờ đóng cửa thì chọn lại buổi và thời lượng, giữ nguyên nhánh
            opening, closing, spread = rng.choice(SESSIONS)
            start = day.replace(hour=opening[0], minute=opening[1]) + timedelta(minutes=rng.randint(0, spread))
            rows, end = visit(rng, start, *branches)
            if end <= day.replace(hour=closing[0], minute=closing[1]):
                break
        visits.append(rows)
    visits.sort(key=lambda rows: rows[0][1])  # mã lượt đánh theo thứ tự thời gian
    for day, place, steps in DOC_VISITS:
        at = lambda clock: datetime.combine(day, datetime.strptime(clock, "%H:%M").time())
        visits.append([[a, at(s), at(e), ROLES.get(a, ""), f"mô phỏng; ngoài Vinmec ({place}); {note}"]
                       for a, s, e, note in steps])
    return [[f"L{n:02d}", a, s.strftime("%Y-%m-%d %H:%M"), e.strftime("%Y-%m-%d %H:%M"), r, note]
            for n, rows in enumerate(visits, start=1) for a, s, e, r, note in rows]


if __name__ == "__main__":
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["case_id", "activity", "start_time", "end_time", "resource", "note"])
        writer.writerows(generate())
    print("Đã ghi", OUT)
