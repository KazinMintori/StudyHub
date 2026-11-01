"""Crop Chapter 29 figures and application images from the source PDF.

Run from the StudyHub repository root with Python and PyMuPDF installed.
The crop rectangles are page coordinates in points, with a margin added by the
script so labels, arrowheads, and captions near each illustration remain visible.
"""
from pathlib import Path
import pymupdf as fitz
from PIL import Image, ImageChops, ImageDraw

SOURCE = Path("raw_materials/physics/source/young-freedman-15.pdf")
OUTPUT = Path("docs/vat-ly-2/bai-giang/img/young-29")
OUTPUT.mkdir(parents=True, exist_ok=True)

# Keys are output stems. Values are (one-based PDF page number, x0, y0, x1, y1)
# in the 648 x 783 point page coordinate system. Boxes include the full artwork
# while excluding adjacent prose where practical.
CROPS = {
    "ung-dung-kich-thich-tu-xuyen-so": (974, 0, 336, 193, 481),
    "hinh-29-01": (974, 75, 529, 574, 730),
    "hinh-29-02": (975, 475, 129, 598, 300),
    "hinh-29-03": (975, 453, 593, 616, 728),
    "hinh-29-04": (976, 78, 86, 574, 264),
    "hinh-29-05": (976, 324, 603, 572, 744),
    "hinh-29-06": (977, 85, 487, 418, 742),
    "hinh-29-07": (978, 335, 637, 548, 753),
    "hinh-29-08": (979, 78, 575, 568, 736),
    "hinh-29-09": (980, 351, 121, 531, 240),
    "hinh-29-10": (980, 171, 611, 563, 730),
    "hinh-29-11": (981, 394, 125, 569, 225),
    "hinh-29-12": (981, 393, 522, 569, 611),
    "hinh-tu-kiem29-2": (982, 35, 483, 194, 578),
    "hinh-29-13": (983, 424, 566, 556, 676),
    "hinh-29-14": (984, 83, 87, 578, 246),
    "hinh-29-15": (985, 454, 139, 616, 432),
    "hinh-29-16": (986, 34, 153, 199, 354),
    "hinh-29-17": (987, 88, 104, 328, 317),
}

MARGIN = 3
SCALE = 2.5

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Source PDF not found: {SOURCE}")
    doc = fitz.open(SOURCE)
    for stem, (page_number, x0, y0, x1, y1) in CROPS.items():
        page = doc[page_number - 1]
        rect = fitz.Rect(x0, y0, x1, y1) + (-MARGIN, -MARGIN, MARGIN, MARGIN)
        rect &= page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        pix.save(OUTPUT / f"{stem}.png")
        path=OUTPUT/f"{stem}.png"
        image=Image.open(path).convert('RGB')
        if stem == 'hinh-29-17':
            # The preceding caption ends in the top-left corner of this clip.
            # Remove only that prose; keep the y-axis label at PDF x=167.5.
            mask_right=round((146-rect.x0)*SCALE)
            mask_bottom=round((106-rect.y0)*SCALE)
            ImageDraw.Draw(image).rectangle((0,0,mask_right,mask_bottom),fill='white')
        bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
        if bounds:
            left,top,right,bottom=bounds
            image.crop((max(0,left-12),max(0,top-12),min(image.width,right+12),min(image.height,bottom+12))).save(path,optimize=True)
        print(f"{stem}: PDF p.{page_number}, crop={tuple(round(v, 1) for v in rect)}")
    print(f"Wrote {len(CROPS)} crops to {OUTPUT}")

if __name__ == "__main__":
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-29-16.png', 'pdfPage': 986, 'bounds': [31, 150, 202, 362], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-tu-kiem29-2.png', 'pdfPage': 982, 'bounds': [32, 480, 197, 588], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-29-08.png', 'pdfPage': 979, 'bounds': [75, 575, 571, 739], 'scale': 2.5, 'masks': []}]
if __name__ == "__main__":
    from pathlib import Path as _StudyHubPath
    import pymupdf as _studyhub_pdf
    from PIL import Image as _StudyHubImage, ImageDraw as _StudyHubImageDraw
    _studyhub_root = _StudyHubPath(__file__).resolve().parents[1]
    with _studyhub_pdf.open(_studyhub_root / 'raw_materials/physics/source/young-freedman-15.pdf') as _studyhub_document:
        for _studyhub_spec in _studyhub_final_frame_specs:
            _studyhub_box = _studyhub_spec['bounds']
            _studyhub_scale = _studyhub_spec['scale']
            _studyhub_pix = _studyhub_document[_studyhub_spec['pdfPage'] - 1].get_pixmap(matrix=_studyhub_pdf.Matrix(_studyhub_scale, _studyhub_scale), clip=_studyhub_pdf.Rect(_studyhub_box), alpha=False)
            _studyhub_image = _StudyHubImage.frombytes('RGB', (_studyhub_pix.width, _studyhub_pix.height), _studyhub_pix.samples)
            for _studyhub_mask in _studyhub_spec['masks']:
                _StudyHubImageDraw.Draw(_studyhub_image).rectangle([(_studyhub_mask[0] - _studyhub_box[0]) * _studyhub_scale, (_studyhub_mask[1] - _studyhub_box[1]) * _studyhub_scale, (_studyhub_mask[2] - _studyhub_box[0]) * _studyhub_scale, (_studyhub_mask[3] - _studyhub_box[1]) * _studyhub_scale], fill='white')
            _studyhub_destination = _studyhub_root / _studyhub_spec['file']
            _studyhub_destination.parent.mkdir(parents=True, exist_ok=True)
            _studyhub_image.save(_studyhub_destination)
