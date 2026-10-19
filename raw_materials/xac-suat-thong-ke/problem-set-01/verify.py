"""Kiểm số của Problem Set 01 và tạo ảnh từ bảng dữ liệu đã đọc."""

from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PUBLIC = ROOT / "docs/public/materials/xac-suat-thong-ke/problem-set-01"
IMAGE = ROOT / "docs/xac-suat-thong-ke/problem-set/img/problem-set-01/penguins-head.png"

# Bài 1: Đếm máy gặp sự cố, không đếm số lần xảy ra sự cố.
assert F(48, 2400) == F(1, 50)
assert F(21, 700) == F(3, 100)
assert [F(48, 2400) * 1000, F(21, 700) * 1000] == [20, 30]

# Bài 2: Trọng số là tỷ lệ số tác vụ của mỗi nhóm.
assert [F(9, 10), F(80, 100), F(20, 100), F(1, 10)] == [F(9, 10), F(4, 5), F(1, 5), F(1, 10)]
assert F(9 + 20, 10 + 100) == F(29, 110)
assert F(80 + 1, 100 + 10) == F(81, 110)
assert F(10, 110) * F(9, 10) + F(100, 110) * F(20, 100) == F(29, 110)
assert F(100, 110) * F(80, 100) + F(10, 110) * F(1, 10) == F(81, 110)

# Bài 3: Cho trọng số bằng nhau theo bộ pin hoặc theo phép đo.
pins = [[10, 14], [20, 20, 20, 20], [30]]
means = [F(sum(pin), len(pin)) for pin in pins]
assert means == [12, 20, 30]
assert sum(means) / 3 == F(62, 3)
assert F(sum(map(sum, pins)), sum(map(len, pins))) == F(134, 7)

# Bài 4: Mỗi cặp là mùa và lựa chọn của một người.
survey = [
    ("Spring", "Beach"), ("Spring", "Mountains"),
    ("Summer", "Beach"), ("Summer", "Beach"), ("Summer", "Mountains"),
    ("Fall", "Mountains"), ("Fall", "Mountains"),
    ("Winter", "Beach"), ("Winter", "Mountains"), ("Winter", "Beach"),
]
counts = Counter(survey)
seasons = ["Spring", "Summer", "Fall", "Winter"]
assert [[counts[(s, p)] for p in ["Mountains", "Beach"]] for s in seasons] == [[1, 1], [1, 2], [2, 0], [1, 2]]
assert sum(counts[(s, "Beach")] for s in seasons) == 5

# Bài 9: Giữ đúng bản CSV dùng để chạy và hiển thị.
data = pd.read_csv(HERE / "penguins.csv")
assert data.shape == (344, 8)
assert list(data.columns) == ["species", "island", "bill_length_mm", "bill_depth_mm",
                              "flipper_length_mm", "body_mass_g", "sex", "year"]
assert data.loc[0, "bill_length_mm"] == 39.1
assert pd.isna(data.loc[3, "body_mass_g"])
PUBLIC.mkdir(parents=True, exist_ok=True)
(PUBLIC / "penguins.csv").write_bytes((HERE / "penguins.csv").read_bytes())

# Ảnh đầu ra chia thành ba nhóm cột, giữ chỉ số hàng để ghép lại.
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, axes = plt.subplots(3, 1, figsize=(9.5, 8.2))
panels = [
    (["species", "island", "sex", "year"], "Nhóm cột phân loại và năm"),
    (["bill_length_mm", "bill_depth_mm"], "Kích thước mỏ (mm)"),
    (["flipper_length_mm", "body_mass_g"], "Chiều dài cánh (mm) và khối lượng (g)"),
]
for ax, (cols, title) in zip(axes, panels):
    ax.axis("off")
    ax.set_title(title, loc="left", fontsize=14, fontweight="bold", pad=12, color="#3d315b")
    rows = [[str(idx)] + ["NaN" if pd.isna(v) else str(v) for v in row]
            for idx, row in data.head()[cols].iterrows()]
    table = ax.table(cellText=rows, colLabels=["Hàng"] + cols, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.7)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#ded8e8")
        if row == 0:
            cell.set_facecolor("#eee9f5")
            cell.set_text_props(weight="bold")
        elif row % 2 == 0:
            cell.set_facecolor("#faf8fd")
fig.suptitle("Palmer Penguins: Năm hàng đầu", fontsize=18, fontweight="bold", color="#3d315b")
fig.text(0.04, 0.02, "Cùng chỉ số hàng là cùng một cá thể. NaN biểu thị giá trị bị thiếu.", fontsize=12)
fig.tight_layout(rect=(0.02, 0.05, 0.98, 0.95), h_pad=2)
IMAGE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(IMAGE, dpi=160, facecolor="white")
plt.close(fig)

report = {
    "pandas": pd.__version__,
    "csv_sha256": hashlib.sha256((HERE / "penguins.csv").read_bytes()).hexdigest(),
    "shape": list(data.shape),
    "dtypes": {col: str(dtype) for col, dtype in data.dtypes.items()},
    "percent_success_A": float(F(29, 110) * 100),
    "percent_success_B": float(F(81, 110) * 100),
    "mean_by_battery": str(F(62, 3)),
    "mean_by_measurement": str(F(134, 7)),
    "source_subquestions": [6, 8, 8, 7, 6, 6, 7, 6, 7, 9],
    "image": str(IMAGE.relative_to(ROOT)).replace("\\", "/"),
}
(HERE / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
