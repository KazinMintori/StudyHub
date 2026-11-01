"""Rebuild Chapter 28.1–28.4 theory figures from Young & Freedman pages 918–927."""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-28"
SCALE = 2.5

# name: (printed page, (left, top, right, bottom)); page index = printed + 19.
FIGURES = {
    "mo-chuong": (918, (210, 0, 648, 240)),
    "hinh-28-01": (919, (450, 135, 640, 540)),
    "hinh-28-02": (920, (380, 420, 610, 580)),
    "hinh-28-03": (921, (450, 365, 640, 750)),
    "hinh-28-04": (923, (75, 185, 320, 275)),
    "hinh-28-05": (924, (30, 100, 195, 260)),
    "hinh-28-06": (924, (30, 345, 195, 510)),
    "hinh-28-07": (925, (35, 435, 305, 725)),
    "hinh-28-08": (925, (425, 560, 585, 620)),
    "hinh-28-09": (926, (30, 290, 210, 465)),
    "hinh-28-10": (927, (450, 270, 620, 305)),
    "ung-dung-tu-truong-hanh-tinh": (922, (38, 238, 190, 340)),
    "tu-kiem-tra-28-03": (926, (30, 45, 205, 165)),
    "tu-kiem-tra-28-04": (927, (510, 420, 620, 475)),
}

MASKS = {
    # The blue page rule is below Figure 28.7 and outside its field-line map.
    "hinh-28-07": [(35, 720, 305, 725)],
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    document = pymupdf.open(PDF)
    for name, (printed_page, box) in FIGURES.items():
        page = document[printed_page + 19]
        rect = pymupdf.Rect(box)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop outside printed page {printed_page}: {name} {rect}")
        pixmap = page.get_pixmap(
            matrix=pymupdf.Matrix(SCALE, SCALE),
            clip=rect,
            alpha=False,
        )
        output = OUT / f"{name}.png"
        pixmap.save(output)
        if name in MASKS:
            with Image.open(output) as source:
                image = source.convert("RGB")
                draw = ImageDraw.Draw(image)
                for left, top, right, bottom in MASKS[name]:
                    draw.rectangle(
                        (
                            round((left - rect.x0) * SCALE),
                            round((top - rect.y0) * SCALE),
                            round((right - rect.x0) * SCALE),
                            round((bottom - rect.y0) * SCALE),
                        ),
                        fill="white",
                    )
                image.save(output, optimize=True)
        with Image.open(output) as source:
            image = source.convert("RGB")
            delta = ImageChops.difference(image, Image.new("RGB", image.size, "white"))
            bounds = delta.getbbox()
            if bounds:
                padding = round(5 * SCALE)
                left, top, right, bottom = bounds
                bounds = (
                    max(0, left - padding),
                    max(0, top - padding),
                    min(image.width, right + padding),
                    min(image.height, bottom + padding),
                )
                image.crop(bounds).save(output, optimize=True)
    print(f"Prepared {len(FIGURES)} Chapter 28.1–28.4 theory assets at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-28-02.png', 'pdfPage': 940, 'bounds': [380, 412, 610, 590], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-28-04.png', 'pdfPage': 943, 'bounds': [75, 170, 320, 275], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-28-08.png', 'pdfPage': 945, 'bounds': [425, 560, 585, 642], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-28-09.png', 'pdfPage': 946, 'bounds': [30, 290, 210, 487], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/tu-kiem-tra-28-04.png', 'pdfPage': 947, 'bounds': [498, 420, 620, 475], 'scale': 2.5, 'masks': []}]
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
