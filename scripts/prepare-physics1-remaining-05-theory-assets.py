"""Reproducible original-PDF crops for Chapter 5 theory."""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
OUT = ROOT / 'docs/vat-ly-1/bai-giang/img/young-05'
SCALE = 2.5

# Map of crop key to (page_1_indexed, (x0, y0, x1, y1))
CROPS = {
    'r-theory-mo-dau': (149, (0, 0, 442, 245)),
    'r-theory-hinh-05-01': (150, (312, 608, 595, 755)),
    'r-theory-hinh-05-02': (151, (354, 385, 615, 553)),
    'r-theory-hinh-05-03': (152, (142, 445, 470, 614)),
    'r-theory-hinh-05-04': (153, (78, 75, 338, 212)),
    'r-theory-hinh-05-05': (154, (138, 76, 470, 247)),
    'r-theory-hinh-05-06': (154, (36, 439, 195, 746)),
    'r-theory-hinh-05-07': (155, (354, 485, 615, 650)),
    'r-theory-hinh-05-08': (156, (312, 320, 560, 450)),
    'r-theory-hinh-05-09': (156, (312, 585, 595, 755)),
    'r-theory-hinh-05-10': (157, (354, 322, 615, 500)),
    'r-theory-hinh-05-11': (158, (36, 125, 195, 290)),
    'r-theory-hinh-05-12': (158, (311, 370, 585, 520)),
    'r-theory-hinh-05-13': (159, (142, 76, 550, 213)),
    'r-theory-hinh-05-14': (159, (95, 495, 590, 720)),
    'r-theory-hinh-05-15': (160, (36, 580, 296, 755)),
    'r-theory-hinh-05-16': (161, (456, 613, 615, 755)),
    'r-theory-hinh-05-17': (162, (36, 95, 195, 260)),
    'r-theory-hinh-05-18': (162, (36, 288, 195, 470)),
    'r-theory-hinh-05-19': (163, (78, 88, 580, 395)),
    'r-theory-hinh-05-20': (164, (36, 296, 296, 445)),
    'r-theory-hinh-05-21': (165, (78, 152, 338, 295)),
    'r-theory-hinh-05-22': (165, (354, 348, 615, 490)),
    'r-theory-hinh-05-23': (166, (36, 76, 302, 210)),
    'r-theory-hinh-05-24': (167, (456, 75, 615, 255)),
    'r-theory-hinh-05-25': (167, (78, 622, 615, 755)),
    'r-theory-hinh-05-26': (168, (36, 125, 195, 445)),
    'r-theory-hinh-05-27': (168, (36, 515, 197, 619)),
    'r-theory-hinh-05-28': (169, (456, 283, 615, 480)),
    'r-theory-hinh-05-29': (169, (456, 521, 615, 747)),
    'r-theory-hinh-05-30': (170, (36, 84, 195, 315)),
    'r-theory-hinh-05-31': (170, (36, 583, 296, 740)),
    'r-theory-hinh-05-32': (171, (78, 318, 338, 480)),
    'r-theory-hinh-05-33': (171, (354, 544, 615, 712)),
    'r-theory-hinh-05-34': (172, (142, 583, 464, 734)),
    'r-theory-hinh-05-35': (173, (490, 140, 612, 295)),
    'r-theory-hinh-05-36': (173, (354, 426, 615, 580)),
    'r-theory-hinh-05-37': (174, (36, 166, 195, 335)),
    'r-theory-hinh-05-38': (175, (85, 60, 435, 430)),
    'r-theory-tom-tat-01': (176, (445, 253, 575, 356)),
    'r-theory-tom-tat-02': (176, (445, 413, 575, 513)),
    'r-theory-tom-tat-03': (176, (445, 538, 576, 619)),
    'r-theory-tom-tat-04': (177, (500, 60, 610, 142)),
    'r-theory-app-centrifuge': (174, (0, 550, 194, 695)),
    'r-theory-app-pollen': (167, (456, 421, 648, 564)),
    'r-theory-app-wipers': (163, (456, 567, 648, 710)),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(PDF) as pdf:
        for name, (page, box) in CROPS.items():
            rect = pymupdf.Rect(box)
            pix = pdf[page - 1].get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
            pix.save(str(OUT / f'{name}.png'))
    print(f'Successfully saved {len(CROPS)} original source crops to {OUT}.')


if __name__ == '__main__':
    main()
