"""Crop Chapter 1 Theory figures from Young & Freedman (15th ed.) pages 21-45.

Generates high-resolution PNG image assets for Sections 1.1-1.10, Chapter opening,
and Chapter summary.
Preserves original labels, panels, coordinate axes, and diagrams without cutting.
"""

from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"

OUT = ROOT / "docs/vat-ly-1/bai-giang/img/young-01"

SCALE = 2.5

# Dict format: basename -> (PDF1based_page, (x0, y0, x1, y1))
CROPS = {
    'mo-chuong-loc-xoay.png': (21, (0, 0, 439, 250)),
    'hinh-1-1a.png': (22, (35, 76, 195, 300)),
    'hinh-1-1b.png': (22, (35, 315, 195, 456)),
    'hinh-1-2.png': (23, (457, 398, 614, 586)),
    'hinh-1-3.png': (24, (37, 330, 195, 721)),
    'hinh-1-4.png': (25, (455, 147, 614, 344)),
    'hinh-1-5.png': (26, (37, 78, 545, 265)),
    'hinh-1-6.png': (26, (35, 363, 195, 508)),
    'hinh-1-7.png': (28, (35, 117, 195, 325)),
    'hinh-1-8.png': (28, (37, 592, 197, 748)),
    'ung-dung-nhiet-do-gio.png': (30, (0, 634, 192, 742)),
    'hinh-1-9.png': (31, (457, 86, 617, 368)),
    'hinh-1-10.png': (31, (457, 425, 615, 546)),
    'hinh-1-11.png': (32, (37, 76, 197, 358)),
    'hinh-1-12.png': (32, (37, 404, 195, 572)),
    'hinh-1-13.png': (32, (77, 615, 569, 722)),
    'hinh-1-14.png': (33, (78, 89, 549, 181)),
    'hinh-1-15.png': (33, (449, 221, 609, 405)),
    'hinh-1-16.png': (33, (393, 448, 572, 577)),
    'hinh-1-17.png': (34, (37, 338, 180, 452)),
    'hinh-1-18.png': (34, (37, 540, 185, 734)),
    'hinh-1-19.png': (35, (84, 341, 331, 481)),
    'hinh-1-20.png': (36, (37, 85, 194, 288)),
    'hinh-1-21.png': (36, (49, 349, 178, 521)),
    'hinh-1-22.png': (36, (58, 584, 168, 753)),
    'hinh-1-23.png': (37, (390, 434, 565, 628)),
    'hinh-1-24.png': (38, (37, 389, 197, 570)),
    'hinh-1-25.png': (38, (37, 626, 155, 744)),
    'hinh-1-26.png': (39, (455, 461, 614, 742)),
    'hinh-1-27.png': (40, (45, 105, 183, 339)),
    'hinh-1-28.png': (41, (95, 207, 315, 329)),
    'hinh-1-29.png': (41, (393, 413, 608, 576)),
    'hinh-1-30.png': (42, (37, 86, 195, 347)),
    'hinh-1-31.png': (42, (35, 510, 194, 721)),
    'hinh-1-32.png': (43, (458, 116, 583, 336)),
    'hinh-1-33.png': (44, (82, 215, 246, 331)),
    'tom-tat-chu-so.png': (45, (488, 152, 604, 214)),
    'tom-tat-cong-vector.png': (45, (488, 245, 601, 285)),
    'tom-tat-thanh-phan.png': (45, (488, 327, 566, 406)),
    'tom-tat-vector-don-vi.png': (45, (489, 423, 582, 478)),
    'tom-tat-tich-vo-huong.png': (45, (488, 486.2, 599, 558)),
    'tom-tat-tich-co-huong.png': (45, (489, 585, 616, 670)),
}


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found at {LOCAL_SOURCE} or {MAIN_SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(SOURCE) as pdf:
        for basename, (page_num, box) in CROPS.items():
            target = OUT / basename
            # Re-render reviewed exact rectangles, even when an older crop exists.
            page = pdf[page_num - 1]
            rect = pymupdf.Rect(box) & page.rect
            pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            pix.save(str(target))
            print(f"Saved {target.name}: page {page_num}, box={box}, size={pix.width}x{pix.height}")
    print(f"Verified / generated {len(CROPS)} images in {OUT}")


if __name__ == "__main__":
    main()
