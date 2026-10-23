from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
OUT_DIR = ROOT / 'docs/vat-ly-1/bai-giang/img/young-18'

# Format: basename -> (1-based PDF page, (x0, y0, x1, y1))
CROPS = {
    'e-table-16-2': (533, (75.0, 75.0, 402.0, 223.0)),
    'e-fig-p18-52': (628, (216.0, 404.5, 296.0, 503.0)),
    'e-fig-p18-61': (629, (220.0, 273.0, 336.0, 352.0)),
    'e-fig-p18-77': (630, (180.0, 474.0, 298.0, 603.0)),
    'e-fig-p18-80': (630, (308.0, 628.0, 546.0, 745.0)),
    'e-fig-p18-81': (631, (190.0, 195.0, 325.0, 305.0)),
    'e-fig-p18-83': (631, (350.0, 279.0, 607.0, 449.0)),
    'e-fig-18-24': (620, (210.0, 83.0, 575.0, 258.0)),
    'e-fig-18-08': (606, (35.0, 95.0, 195.0, 385.0)),
    'e-fig-18-18b': (615, (453.0, 440.0, 615.0, 596.0)),
    'e-fig-18-23': (618, (36.0, 192.0, 195.0, 452.0)),
}

SCALE = 3

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(PDF_PATH) as doc:
        for name, (page_1based, rect) in CROPS.items():
            page = doc[page_1based - 1]
            mat = pymupdf.Matrix(SCALE, SCALE)
            pix = page.get_pixmap(matrix=mat, clip=pymupdf.Rect(rect), alpha=False)
            target = OUT_DIR / f'{name}.png'
            pix.save(target)
            print(f'Saved {target.name} ({pix.width}x{pix.height})')

if __name__ == '__main__':
    main()
