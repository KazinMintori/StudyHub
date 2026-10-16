"""Trích xuất hình ảnh tham chiếu và tạo các đồ thị giải pháp SVG cho bài tập Chapter 42 nhóm C."""
from pathlib import Path
import hashlib
import math
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-42'

# Crops for reference images from Young & Freedman 15th ed.
# Format: stem -> (1-based page, (x0, y0, x1, y1))
CROPS = {
    'hinh-tham-chieu-c-1': (1442, (34, 614, 188, 745)),  # Fig 42.23: Fermi-Dirac distribution curves at T > 0
    'hinh-tham-chieu-c-2': (1442, (34, 240, 194, 372)),  # Fig 42.22: Fermi-Dirac distribution at T = 0
    'hinh-tham-chieu-c-3': (1433, (460, 490, 602, 755)), # Fig 42.8: Vibration-rotation energy level diagram
    'hinh-tham-chieu-c-4': (1439, (76, 567, 474, 708)),  # Fig 42.19: Insulator, semiconductor, conductor bands
}


def generate_svg_01(out_path: Path):
    """Vẽ đường thế năng liên kết ion U(r) cho bài 42.1."""
    w, h = 600, 360
    ox, oy = 80, 240
    # Potential: U(r) = -A/r + B/r^9, normalized
    pts = []
    for i in range(120):
        r_val = 0.72 + (2.5 * i / 120)
        u_val = -1.0 / r_val + 0.12 / (r_val**9)
        px = ox + (r_val - 0.7) * 180.0
        py = oy + u_val * 160.0
        if 40 <= py <= 320:
            pts.append((px, py))
    path_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .grid {{ stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .text-title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .annot {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #b91c1c; font-weight: 500; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="text-title">Đường thế năng liên kết ion U(r) theo khoảng cách liên hạt nhân</text>
  <line x1="{ox}" y1="{oy}" x2="560" y2="{oy}" class="axis" />
  <line x1="{ox}" y1="40" x2="{ox}" y2="330" class="axis" />
  <path d="{path_d}" class="curve" />
  <line x1="210" y1="40" x2="210" y2="320" class="grid" />
  <circle cx="210" cy="112" r="4" fill="#b91c1c" />
  <text x="220" y="116" class="annot">Cực tiểu tại r₀ = 0,29 nm (U₀ ≈ -4,97 eV)</text>
  <text x="540" y="{oy - 10}" class="label">r</text>
  <text x="{ox + 10}" y="50" class="label">U(r)</text>
  <text x="{ox - 18}" y="{oy + 5}" class="label">0</text>
  <text x="210" y="{oy + 22}" class="label" text-anchor="middle">r₀</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_02(out_path: Path):
    """Vẽ giản đồ mức năng lượng quay El = l(l+1)hbar^2 / (2I) cho bài 42.3 và 42.4."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .level {{ stroke: #1e293b; stroke-width: 2; }}
    .trans-down {{ stroke: #dc2626; stroke-width: 2; stroke-dasharray: 4,3; marker-end: url(#arrow-down); }}
    .trans-up {{ stroke: #16a34a; stroke-width: 2; marker-end: url(#arrow-up); }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .tag {{ font-family: system-ui, sans-serif; font-size: 13px; font-weight: 600; fill: #4338ca; }}
  </style>
  <defs>
    <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626" />
    </marker>
    <marker id="arrow-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#16a34a" />
    </marker>
  </defs>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Các mức năng lượng quay của phân tử hai nguyên tử Eₗ = l(l+1)ħ²/(2I)</text>
  <!-- Levels l = 0, 1, 2, 3, 4 -->
  <line x1="120" y1="310" x2="480" y2="310" class="level" />
  <text x="80" y="315" class="label">l = 0</text>
  <text x="490" y="315" class="label">E₀ = 0</text>
  <line x1="120" y1="280" x2="480" y2="280" class="level" />
  <text x="80" y="285" class="label">l = 1</text>
  <text x="490" y="285" class="label">E₁ = 2ε₀</text>
  <line x1="120" y1="230" x2="480" y2="230" class="level" />
  <text x="80" y="235" class="label">l = 2</text>
  <text x="490" y="235" class="label">E₂ = 6ε₀</text>
  <line x1="120" y1="160" x2="480" y2="160" class="level" />
  <text x="80" y="165" class="label">l = 3</text>
  <text x="490" y="165" class="label">E₃ = 12ε₀</text>
  <line x1="120" y1="70" x2="480" y2="70" class="level" />
  <text x="80" y="75" class="label">l = 4</text>
  <text x="490" y="75" class="label">E₄ = 20ε₀</text>
  <!-- Transitions -->
  <line x1="220" y1="230" x2="220" y2="276" class="trans-down" />
  <text x="180" y="255" class="tag">Bài 42.3: Phát xạ l=2 → 1</text>
  <line x1="380" y1="160" x2="380" y2="76" class="trans-up" />
  <text x="390" y="115" class="tag">Bài 42.4: Hấp thụ l=3 → 4</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_03(out_path: Path):
    """Vẽ các nhánh chuyển mức dao động - quay P và R cho bài 42.8 và VP42.3.4."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .band-line {{ stroke: #475569; stroke-width: 1.5; }}
    .p-branch {{ stroke: #dc2626; stroke-width: 2; marker-end: url(#arrow-p); }}
    .r-branch {{ stroke: #2563eb; stroke-width: 2; marker-end: url(#arrow-r); }}
  </style>
  <defs>
    <marker id="arrow-p" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626" />
    </marker>
    <marker id="arrow-r" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>
  </defs>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Phổ dao động - quay: Nhánh P (Δl = -1) và Nhánh R (Δl = +1)</text>
  <!-- n = 1 upper manifold -->
  <text x="50" y="80" class="label" font-weight="bold">n = 1</text>
  <line x1="120" y1="60" x2="520" y2="60" class="band-line" />
  <text x="530" y="65" class="label">l = 3</text>
  <line x1="120" y1="80" x2="520" y2="80" class="band-line" />
  <text x="530" y="85" class="label">l = 2</text>
  <line x1="120" y1="100" x2="520" y2="100" class="band-line" />
  <text x="530" y="105" class="label">l = 1</text>
  <!-- n = 0 lower manifold -->
  <text x="50" y="270" class="label" font-weight="bold">n = 0</text>
  <line x1="120" y1="240" x2="520" y2="240" class="band-line" />
  <text x="530" y="245" class="label">l = 3</text>
  <line x1="120" y1="260" x2="520" y2="260" class="band-line" />
  <text x="530" y="265" class="label">l = 2</text>
  <line x1="120" y1="280" x2="520" y2="280" class="band-line" />
  <text x="530" y="285" class="label">l = 1</text>
  <line x1="120" y1="300" x2="520" y2="300" class="band-line" />
  <text x="530" y="305" class="label">l = 0</text>
  <!-- Transition arrows -->
  <line x1="220" y1="260" x2="220" y2="64" class="r-branch" />
  <text x="170" y="160" class="label" fill="#2563eb">Nhánh R (0,2 → 1,3)</text>
  <line x1="380" y1="240" x2="380" y2="84" class="p-branch" />
  <text x="390" y="160" class="label" fill="#dc2626">Nhánh P (0,3 → 1,2)</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_04(out_path: Path):
    """Vẽ mạng tinh thể lập phương kiểu NaCl / KBr với khoảng cách lân cận d cho bài 42.12 và 42.13."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .lattice-edge {{ stroke: #94a3b8; stroke-width: 1.5; }}
    .ion-pos {{ fill: #3b82f6; stroke: #1d4ed8; stroke-width: 1.5; }}
    .ion-neg {{ fill: #ef4444; stroke: #b91c1c; stroke-width: 1.5; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Cấu trúc mạng ion lập phương xen kẽ (NaCl / KBr)</text>
  <!-- Grid representation 3x3 front plane -->
  <g transform="translate(180, 80)">
    <line x1="0" y1="0" x2="200" y2="0" class="lattice-edge" />
    <line x1="0" y1="100" x2="200" y2="100" class="lattice-edge" />
    <line x1="0" y1="200" x2="200" y2="200" class="lattice-edge" />
    <line x1="0" y1="0" x2="0" y2="200" class="lattice-edge" />
    <line x1="100" y1="0" x2="100" y2="200" class="lattice-edge" />
    <line x1="200" y1="0" x2="200" y2="200" class="lattice-edge" />
    <!-- Row 0 -->
    <circle cx="0" cy="0" r="10" class="ion-pos" />
    <circle cx="100" cy="0" r="14" class="ion-neg" />
    <circle cx="200" cy="0" r="10" class="ion-pos" />
    <!-- Row 1 -->
    <circle cx="0" cy="100" r="14" class="ion-neg" />
    <circle cx="100" cy="100" r="10" class="ion-pos" />
    <circle cx="200" cy="100" r="14" class="ion-neg" />
    <!-- Row 2 -->
    <circle cx="0" cy="200" r="10" class="ion-pos" />
    <circle cx="100" cy="200" r="14" class="ion-neg" />
    <circle cx="200" cy="200" r="10" class="ion-pos" />
    <!-- Spacing marker d -->
    <line x1="0" y1="225" x2="100" y2="225" stroke="#0f172a" stroke-width="1.5" />
    <text x="50" y="245" class="label" text-anchor="middle" font-weight="bold">d</text>
  </g>
  <!-- Legend -->
  <circle cx="440" cy="140" r="8" class="ion-pos" />
  <text x="460" y="145" class="label">Ion dương (K⁺ hoặc Na⁺)</text>
  <circle cx="440" cy="180" r="12" class="ion-neg" />
  <text x="460" y="185" class="label">Ion âm (Br⁻ hoặc Cl⁻)</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_05(out_path: Path):
    """Vẽ khe năng lượng Eg và chuyển mức hấp thụ photon cho bài 42.14, 42.15, 42.16."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .band-c {{ fill: #eff6ff; stroke: #3b82f6; stroke-width: 2; }}
    .band-v {{ fill: #f8fafc; stroke: #64748b; stroke-width: 2; }}
    .photon {{ stroke: #ea580c; stroke-width: 2; stroke-dasharray: 4,3; marker-end: url(#arrow-phot); }}
  </style>
  <defs>
    <marker id="arrow-phot" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ea580c" />
    </marker>
  </defs>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Kích thích electron qua vùng cấm năng lượng E_g bằng photon</text>
  <!-- Conduction Band -->
  <rect x="150" y="60" width="300" height="70" class="band-c" rx="4" />
  <text x="300" y="100" class="label" text-anchor="middle" font-weight="bold" fill="#1e40af">Vùng dẫn (Conduction Band - Trống tại 0 K)</text>
  <!-- Valence Band -->
  <rect x="150" y="220" width="300" height="70" class="band-v" rx="4" />
  <text x="300" y="260" class="label" text-anchor="middle" font-weight="bold" fill="#334155">Vùng hóa trị (Valence Band - Đầy tại 0 K)</text>
  <!-- Band gap Eg -->
  <line x1="470" y1="130" x2="470" y2="220" stroke="#0f172a" stroke-width="2" />
  <text x="490" y="180" class="label" font-weight="bold">Khe cấm E_g</text>
  <!-- Excitation arrow -->
  <line x1="250" y1="220" x2="250" y2="134" class="photon" />
  <text x="180" y="175" class="label" fill="#ea580c" font-weight="bold">Photon hf ≥ E_g</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_06(out_path: Path):
    """Vẽ mật độ trạng thái g(E) ~ sqrt(E) trong mô hình electron tự do cho bài 42.17, 42.18, 42.19."""
    w, h = 600, 360
    ox, oy = 80, 290
    pts = []
    for i in range(100):
        e_val = i / 100.0 * 8.0
        g_val = math.sqrt(e_val) * 65.0
        px = ox + e_val * 55.0
        py = oy - g_val
        pts.append((px, py))
    path_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)

    ef_x = ox + 5.5 * 55.0
    pts_fill = [p for p in pts if p[0] <= ef_x]
    fill_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts_fill) + f" L {ef_x},{oy} L {ox},{oy} Z"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .filled {{ fill: rgba(37, 99, 235, 0.18); }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .annot {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #b91c1c; font-weight: 500; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Mật độ trạng thái g(E) ∝ √E và các mức bị chiếm đến E_F tại 0 K</text>
  <path d="{fill_d}" class="filled" />
  <path d="{path_d}" class="curve" />
  <line x1="{ox}" y1="{oy}" x2="550" y2="{oy}" class="axis" />
  <line x1="{ox}" y1="40" x2="{ox}" y2="{oy}" class="axis" />
  <line x1="{ef_x}" y1="{oy}" x2="{ef_x}" y2="{oy - math.sqrt(5.5)*65.0}" stroke="#b91c1c" stroke-width="2" stroke-dasharray="4,3" />
  <text x="{ef_x}" y="{oy + 22}" class="annot" text-anchor="middle">E_F</text>
  <text x="540" y="{oy - 10}" class="label">E</text>
  <text x="{ox + 10}" y="50" class="label">g(E)</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_07(out_path: Path):
    """Vẽ hàm phân bố Fermi-Dirac f(E) tại kT = 0,25 EF cho bài 42.20."""
    w, h = 600, 360
    ox, oy = 80, 270
    # E / EF from 0 to 2.5
    pts = []
    for i in range(120):
        x = i / 120.0 * 2.5
        f_val = 1.0 / (math.exp((x - 1.0) / 0.25) + 1.0)
        px = ox + x * 180.0
        py = oy - f_val * 200.0
        pts.append((px, py))
    path_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)

    px_05 = ox + 0.5 * 180.0
    py_05 = oy - (1.0 / (math.exp(-2.0) + 1.0)) * 200.0
    px_15 = ox + 1.5 * 180.0
    py_15 = oy - (1.0 / (math.exp(2.0) + 1.0)) * 200.0

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .grid {{ stroke: #cbd5e1; stroke-width: 1; stroke-dasharray: 4,4; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .annot {{ font-family: system-ui, sans-serif; font-size: 13px; fill: #b91c1c; font-weight: 600; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Hàm phân bố Fermi–Dirac f(E) tại kT = 0,25 E_F</text>
  <line x1="{ox}" y1="{oy}" x2="560" y2="{oy}" class="axis" />
  <line x1="{ox}" y1="40" x2="{ox}" y2="{oy}" class="axis" />
  <path d="{path_d}" class="curve" />
  <!-- Points at E = 0.5 EF and E = 1.5 EF -->
  <line x1="{px_05}" y1="{oy}" x2="{px_05}" y2="{py_05}" class="grid" />
  <circle cx="{px_05}" cy="{py_05}" r="5" fill="#b91c1c" />
  <text x="{px_05 - 10}" y="{py_05 - 10}" class="annot">f(0,5 E_F) = 0,881</text>
  <line x1="{px_15}" y1="{oy}" x2="{px_15}" y2="{py_15}" class="grid" />
  <circle cx="{px_15}" cy="{py_15}" r="5" fill="#b91c1c" />
  <text x="{px_15 + 10}" y="{py_15 - 10}" class="annot">f(1,5 E_F) = 0,119</text>
  <text x="{ox + 180.0}" y="{oy + 22}" class="label" text-anchor="middle" font-weight="bold">E_F</text>
  <text x="{ox - 18}" y="{oy - 200}" class="label">1</text>
  <text x="{ox - 24}" y="{oy - 100}" class="label">0,5</text>
  <text x="540" y="{oy - 10}" class="label">E</text>
  <text x="{ox + 10}" y="50" class="label">f(E)</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_08(out_path: Path):
    """Vẽ nhiệt dung mol của electron Cv,el ∝ T so với giới hạn Dulong-Petit 3R cho bài 42.21."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .limit {{ stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 5,4; }}
    .curve-tot {{ fill: none; stroke: #0f172a; stroke-width: 2.5; }}
    .curve-el {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Đóng góp của electron vào nhiệt dung kim loại C_V so với mạng tinh thể</text>
  <line x1="80" y1="280" x2="540" y2="280" class="axis" />
  <line x1="80" y1="50" x2="80" y2="280" class="axis" />
  <line x1="80" y1="90" x2="540" y2="90" class="limit" />
  <text x="90" y="85" class="label" fill="#64748b">Giới hạn mạng tinh thể 3R ≈ 24,9 J/(mol·K)</text>
  <!-- Total Cv approaching 3R -->
  <path d="M 80,280 Q 180,260 250,130 T 520,95" class="curve-tot" />
  <text x="440" y="125" class="label" font-weight="bold">C_V tổng cộng</text>
  <!-- Electron Cv linear with T, small slope -->
  <line x1="80" y1="280" x2="520" y2="265" class="curve-el" />
  <text x="360" y="255" class="label" fill="#2563eb" font-weight="bold">C_V,el = (π²/2)(kT/E_F)R (&lt; 1% ở 300 K)</text>
  <text x="520" y="305" class="label">T (K)</text>
  <text x="90" y="60" class="label">C_V</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_09(out_path: Path):
    """Vẽ giản đồ pha tạp bán dẫn loại n (mức donor) và loại p (mức acceptor) cho Q42.18, Q42.22."""
    w, h = 600, 360
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .band-c {{ fill: #eff6ff; stroke: #3b82f6; stroke-width: 1.5; }}
    .band-v {{ fill: #f8fafc; stroke: #64748b; stroke-width: 1.5; }}
    .d-level {{ stroke: #d97706; stroke-width: 2; stroke-dasharray: 5,4; }}
    .a-level {{ stroke: #9333ea; stroke-width: 2; stroke-dasharray: 5,4; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Các mức tạp chất donor (loại n) và acceptor (loại p) trong vùng cấm</text>
  <!-- Panel Left: n-type -->
  <g transform="translate(60, 60)">
    <text x="100" y="0" class="label" font-weight="bold" text-anchor="middle">Bán dẫn loại n (Donor)</text>
    <rect x="0" y="20" width="200" height="50" class="band-c" rx="4" />
    <text x="100" y="50" class="label" text-anchor="middle">Vùng dẫn E_c</text>
    <line x1="0" y1="90" x2="200" y2="90" class="d-level" />
    <text x="100" y="85" class="label" fill="#d97706" text-anchor="middle" font-weight="600">Mức donor E_D</text>
    <rect x="0" y="160" width="200" height="50" class="band-v" rx="4" />
    <text x="100" y="190" class="label" text-anchor="middle">Vùng hóa trị E_v</text>
  </g>
  <!-- Panel Right: p-type -->
  <g transform="translate(340, 60)">
    <text x="100" y="0" class="label" font-weight="bold" text-anchor="middle">Bán dẫn loại p (Acceptor)</text>
    <rect x="0" y="20" width="200" height="50" class="band-c" rx="4" />
    <text x="100" y="50" class="label" text-anchor="middle">Vùng dẫn E_c</text>
    <line x1="0" y1="140" x2="200" y2="140" class="a-level" />
    <text x="100" y="135" class="label" fill="#9333ea" text-anchor="middle" font-weight="600">Mức acceptor E_A</text>
    <rect x="0" y="160" width="200" height="50" class="band-v" rx="4" />
    <text x="100" y="190" class="label" text-anchor="middle">Vùng hóa trị E_v</text>
  </g>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def generate_svg_10(out_path: Path):
    """Vẽ đặc tuyến V-I của điốt tiếp giáp p-n I = Is(exp(eV/kT) - 1) cho Q42.23 và Section 42.7."""
    w, h = 600, 360
    ox, oy = 250, 260
    # Forward curve V > 0
    pts_f = []
    for i in range(80):
        v_val = i / 80.0 * 0.35
        # Scale for visualization
        i_val = 5.0 * (math.exp(v_val / 0.08) - 1.0)
        px = ox + v_val * 600.0
        py = oy - i_val * 0.45
        if 40 <= py <= oy:
            pts_f.append((px, py))
    path_f = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts_f)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .title {{ font-family: system-ui, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .rev-curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .label {{ font-family: system-ui, sans-serif; font-size: 14px; fill: #334155; }}
    .annot {{ font-family: system-ui, sans-serif; font-size: 13px; fill: #b91c1c; font-weight: 500; }}
  </style>
  <rect width="{w}" height="{h}" class="bg" rx="8" />
  <text x="{w/2}" y="28" class="title">Đặc tuyến V–I của tiếp giáp p–n: I = I_S(e^{{eV/kT}} - 1)</text>
  <line x1="40" y1="{oy}" x2="550" y2="{oy}" class="axis" />
  <line x1="{ox}" y1="40" x2="{ox}" y2="320" class="axis" />
  <!-- Forward branch -->
  <path d="{path_f}" class="curve" />
  <!-- Reverse branch approaching -Is -->
  <line x1="50" y1="{oy + 15}" x2="{ox}" y2="{oy}" class="rev-curve" />
  <text x="530" y="{oy - 10}" class="label">V</text>
  <text x="{ox + 10}" y="50" class="label">I</text>
  <text x="60" y="{oy + 32}" class="annot">Dòng bão hòa nghịch -I_S</text>
  <text x="360" y="100" class="annot">Phân cực thuận: Dòng tăng hàm mũ</text>
</svg>"""
    out_path.write_text(svg, encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))

    # Generate SVGs
    svg_generators = [
        ('loi-giai-c-01.svg', generate_svg_01),
        ('loi-giai-c-02.svg', generate_svg_02),
        ('loi-giai-c-03.svg', generate_svg_03),
        ('loi-giai-c-04.svg', generate_svg_04),
        ('loi-giai-c-05.svg', generate_svg_05),
        ('loi-giai-c-06.svg', generate_svg_06),
        ('loi-giai-c-07.svg', generate_svg_07),
        ('loi-giai-c-08.svg', generate_svg_08),
        ('loi-giai-c-09.svg', generate_svg_09),
        ('loi-giai-c-10.svg', generate_svg_10),
    ]
    for filename, gen in svg_generators:
        path = OUT / filename
        gen(path)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(dict(stem=filename[:-4], type='svg', sha256=sha, size=(600, 360)))

    print(f'Prepared {len(rows)} assets successfully:')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
