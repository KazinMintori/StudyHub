"""Trích xuất hình ảnh và tạo các đồ thị giải pháp SVG cho nhóm bài tập Chapter 40 nhóm C."""
from pathlib import Path
import hashlib
import math
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'hinh-e40-28': (1375, (220, 362, 336, 492)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-40'


def generate_svg_40_08(out_path: Path):
    """Vẽ đồ thị hàm sóng psi(x) = A * exp(-b|x|) cho bài 40.8."""
    w, h = 600, 360
    ox, oy = 300, 290
    scale_x = 140.0
    scale_y = 150.0
    b = 2.0
    A = math.sqrt(b)

    n_points = 160
    pts = []
    for i in range(n_points + 1):
        x = -1.6 + (3.2 * i / n_points)
        y = A * math.exp(-b * abs(x))
        px = ox + x * scale_x
        py = oy - y * scale_y
        pts.append((px, py))

    path_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    area_d = path_d + f" L {pts[-1][0]:.1f},{oy} L {pts[0][0]:.1f},{oy} Z"

    peak_x = ox
    peak_y = oy - A * scale_y

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .grid {{ stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .axis-arrow {{ fill: #334155; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; stroke-linejoin: round; }}
    .area {{ fill: rgba(37, 99, 235, 0.12); }}
    .tick-text {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #475569; text-anchor: middle; }}
    .tick-text-y {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #475569; text-anchor: end; }}
    .label {{ font-family: system-ui, -apple-system, sans-serif; font-size: 14px; font-weight: 600; fill: #1e293b; }}
    .title {{ font-family: system-ui, -apple-system, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .annot {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #b91c1c; font-weight: 500; }}
  </style>

  <!-- Background -->
  <rect width="{w}" height="{h}" class="bg" rx="8" />

  <!-- Title -->
  <text x="{w/2}" y="28" class="title">Đồ thị hàm sóng ψ(x) = A·exp(-b|x|) (b = 2,00 m⁻¹)</text>

  <!-- Grid lines -->
  <line x1="{ox - 1.5*scale_x}" y1="{oy}" x2="{ox + 1.5*scale_x}" y2="{oy}" class="grid" />
  <line x1="{ox - 1.0*scale_x}" y1="45" x2="{ox - 1.0*scale_x}" y2="{oy}" class="grid" />
  <line x1="{ox - 0.5*scale_x}" y1="45" x2="{ox - 0.5*scale_x}" y2="{oy}" class="grid" />
  <line x1="{ox + 0.5*scale_x}" y1="45" x2="{ox + 0.5*scale_x}" y2="{oy}" class="grid" />
  <line x1="{ox + 1.0*scale_x}" y1="45" x2="{ox + 1.0*scale_x}" y2="{oy}" class="grid" />
  <line x1="50" y1="{oy - 1.0*scale_y}" x2="{w - 40}" y2="{oy - 1.0*scale_y}" class="grid" />
  <line x1="50" y1="{peak_y:.1f}" x2="{w - 40}" y2="{peak_y:.1f}" class="grid" />

  <!-- Shaded Area Under Curve -->
  <path d="{area_d}" class="area" />

  <!-- Axes -->
  <!-- X axis -->
  <line x1="40" y1="{oy}" x2="{w - 30}" y2="{oy}" class="axis" />
  <polygon points="{w - 25},{oy} {w - 35},{oy - 4} {w - 35},{oy + 4}" class="axis-arrow" />
  <text x="{w - 20}" y="{oy + 18}" class="label">x (m)</text>

  <!-- Y axis -->
  <line x1="{ox}" y1="{h - 30}" x2="{ox}" y2="40" class="axis" />
  <polygon points="{ox},35 {ox - 4},45 {ox + 4},45" class="axis-arrow" />
  <text x="{ox + 12}" y="45" class="label">ψ(x) (m⁻¹/²)</text>

  <!-- Ticks X -->
  <line x1="{ox - 1.0*scale_x}" y1="{oy}" x2="{ox - 1.0*scale_x}" y2="{oy + 5}" class="axis" />
  <text x="{ox - 1.0*scale_x}" y="{oy + 20}" class="tick-text">-1,0</text>

  <line x1="{ox - 0.5*scale_x}" y1="{oy}" x2="{ox - 0.5*scale_x}" y2="{oy + 5}" class="axis" />
  <text x="{ox - 0.5*scale_x}" y="{oy + 20}" class="tick-text">-0,5</text>

  <text x="{ox - 10}" y="{oy + 20}" class="tick-text">0</text>

  <line x1="{ox + 0.5*scale_x}" y1="{oy}" x2="{ox + 0.5*scale_x}" y2="{oy + 5}" class="axis" />
  <text x="{ox + 0.5*scale_x}" y="{oy + 20}" class="tick-text">0,5</text>

  <line x1="{ox + 1.0*scale_x}" y1="{oy}" x2="{ox + 1.0*scale_x}" y2="{oy + 5}" class="axis" />
  <text x="{ox + 1.0*scale_x}" y="{oy + 20}" class="tick-text">1,0</text>

  <!-- Ticks Y -->
  <line x1="{ox - 5}" y1="{oy - 1.0*scale_y}" x2="{ox}" y2="{oy - 1.0*scale_y}" class="axis" />
  <text x="{ox - 8}" y="{oy - 1.0*scale_y + 4}" class="tick-text-y">1,0</text>

  <line x1="{ox - 5}" y1="{peak_y:.1f}" x2="{ox}" y2="{peak_y:.1f}" class="axis" />
  <text x="{ox - 8}" y="{peak_y + 4:.1f}" class="tick-text-y">A ≈ 1,414</text>

  <!-- Curve -->
  <path d="{path_d}" class="curve" />

  <!-- Cusp indicator -->
  <circle cx="{peak_x}" cy="{peak_y:.1f}" r="4" fill="#b91c1c" />
  <text x="{peak_x + 10}" y="{peak_y - 8:.1f}" class="annot">Đỉnh nhọn cực đại (x = 0, ψ = A)</text>
</svg>"""

    out_path.write_text(svg, encoding='utf-8')


def generate_svg_40_16(out_path: Path):
    """Vẽ đồ thị mật độ xác suất trạng thái cơ bản |psi_1(x)|^2 cho bài 40.16."""
    w, h = 600, 360
    left_wall = 140
    right_wall = 460
    well_w = right_wall - left_wall
    oy = 290
    peak_h = 180.0

    n_points = 100
    pts = []
    for i in range(n_points + 1):
        frac = i / n_points
        px = left_wall + frac * well_w
        val = math.sin(math.pi * frac) ** 2
        py = oy - val * peak_h
        pts.append((px, py))

    path_d = "M " + " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    area_d = path_d + f" L {right_wall},{oy} L {left_wall},{oy} Z"

    peak_x = left_wall + 0.5 * well_w
    peak_y = oy - peak_h

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <style>
    .bg {{ fill: #ffffff; }}
    .wall-shade {{ fill: #f1f5f9; }}
    .wall-line {{ stroke: #334155; stroke-width: 3.5; stroke-linecap: round; }}
    .grid {{ stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }}
    .axis {{ stroke: #334155; stroke-width: 1.5; }}
    .axis-arrow {{ fill: #334155; }}
    .curve {{ fill: none; stroke: #2563eb; stroke-width: 2.5; }}
    .area {{ fill: rgba(37, 99, 235, 0.15); }}
    .tick-text {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #475569; text-anchor: middle; }}
    .tick-text-y {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #475569; text-anchor: end; }}
    .label {{ font-family: system-ui, -apple-system, sans-serif; font-size: 14px; font-weight: 600; fill: #1e293b; }}
    .title {{ font-family: system-ui, -apple-system, sans-serif; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
    .annot {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #b91c1c; font-weight: 500; }}
    .wall-text {{ font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #64748b; font-style: italic; text-anchor: middle; }}
  </style>

  <!-- Background -->
  <rect width="{w}" height="{h}" class="bg" rx="8" />

  <!-- Title -->
  <text x="{w/2}" y="28" class="title">Mật độ xác suất trạng thái cơ bản |ψ₁(x)|² = (2/L) sin²(πx/L)</text>

  <!-- Wall Shading Outside Well -->
  <rect x="30" y="50" width="{left_wall - 30}" height="{oy - 50}" class="wall-shade" />
  <rect x="{right_wall}" y="50" width="{w - 30 - right_wall}" height="{oy - 50}" class="wall-shade" />

  <text x="85" y="160" class="wall-text">Vùng cấm (U = ∞)</text>
  <text x="85" y="180" class="wall-text">|ψ₁|² = 0</text>

  <text x="515" y="160" class="wall-text">Vùng cấm (U = ∞)</text>
  <text x="515" y="180" class="wall-text">|ψ₁|² = 0</text>

  <!-- Grid / Guides -->
  <line x1="{left_wall}" y1="{peak_y}" x2="{right_wall}" y2="{peak_y}" class="grid" />
  <line x1="{peak_x}" y1="{peak_y}" x2="{peak_x}" y2="{oy}" class="grid" stroke="#b91c1c" stroke-width="1.2" />

  <!-- Shaded Area Under Probability Density Curve -->
  <path d="{area_d}" class="area" />

  <!-- Probability Density Curve -->
  <path d="{path_d}" class="curve" />

  <!-- Well Walls -->
  <line x1="{left_wall}" y1="50" x2="{left_wall}" y2="{oy}" class="wall-line" />
  <line x1="{right_wall}" y1="50" x2="{right_wall}" y2="{oy}" class="wall-line" />

  <!-- X axis -->
  <line x1="30" y1="{oy}" x2="{w - 25}" y2="{oy}" class="axis" />
  <polygon points="{w - 20},{oy} {w - 30},{oy - 4} {w - 30},{oy + 4}" class="axis-arrow" />
  <text x="{w - 15}" y="{oy + 18}" class="label">x</text>

  <!-- Y axis at left wall -->
  <line x1="{left_wall}" y1="{oy}" x2="{left_wall}" y2="45" class="axis" />
  <polygon points="{left_wall},40 {left_wall - 4},50 {left_wall + 4},50" class="axis-arrow" />
  <text x="{left_wall - 10}" y="45" class="tick-text-y">|ψ₁(x)|²</text>

  <!-- Peak Indicator -->
  <circle cx="{peak_x}" cy="{peak_y}" r="4" fill="#b91c1c" />
  <text x="{peak_x}" y="{peak_y - 12}" class="annot" text-anchor="middle">Cực đại tại x = L/2 (|ψ₁|² = 2/L)</text>

  <!-- Ticks on X axis -->
  <line x1="{left_wall}" y1="{oy}" x2="{left_wall}" y2="{oy + 6}" class="axis" />
  <text x="{left_wall}" y="{oy + 22}" class="tick-text">0</text>

  <line x1="{left_wall + 0.25*well_w}" y1="{oy}" x2="{left_wall + 0.25*well_w}" y2="{oy + 5}" class="axis" />
  <text x="{left_wall + 0.25*well_w}" y="{oy + 22}" class="tick-text">L/4</text>

  <line x1="{peak_x}" y1="{oy}" x2="{peak_x}" y2="{oy + 6}" class="axis" />
  <text x="{peak_x}" y="{oy + 22}" class="tick-text" font-weight="bold">L/2</text>

  <line x1="{left_wall + 0.75*well_w}" y1="{oy}" x2="{left_wall + 0.75*well_w}" y2="{oy + 5}" class="axis" />
  <text x="{left_wall + 0.75*well_w}" y="{oy + 22}" class="tick-text">3L/4</text>

  <line x1="{right_wall}" y1="{oy}" x2="{right_wall}" y2="{oy + 6}" class="axis" />
  <text x="{right_wall}" y="{oy + 22}" class="tick-text">L</text>

  <!-- Ticks on Y axis -->
  <line x1="{left_wall - 5}" y1="{peak_y}" x2="{left_wall}" y2="{peak_y}" class="axis" />
  <text x="{left_wall - 8}" y="{peak_y + 4}" class="tick-text-y">2/L</text>
</svg>"""

    out_path.write_text(svg, encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))

    # Generate solution SVGs
    svg_08_path = OUT / 'loi-giai-40-08.svg'
    generate_svg_40_08(svg_08_path)
    sha_08 = hashlib.sha256(svg_08_path.read_bytes()).hexdigest()
    rows.append(dict(stem='loi-giai-40-08', type='svg', sha256=sha_08, size=(600, 360)))

    svg_16_path = OUT / 'loi-giai-40-16.svg'
    generate_svg_40_16(svg_16_path)
    sha_16 = hashlib.sha256(svg_16_path.read_bytes()).hexdigest()
    rows.append(dict(stem='loi-giai-40-16', type='svg', sha256=sha_16, size=(600, 360)))

    print(f'Prepared {len(rows)} assets successfully:')
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
