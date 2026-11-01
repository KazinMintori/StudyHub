"""Crop Chapter 28 end-of-chapter figures from Young–Freedman 15e.

Coordinates are PDF points on printed pages. The zero-based PDF page index is
the printed page number plus 19. Crops are rendered at 2.5x and trimmed to a
small white border so labels, arrows, and graph axes remain legible.
"""

from pathlib import Path

import pymupdf
from PIL import Image, ImageChops, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw_materials/physics/source/young-freedman-15.pdf"
OUT = ROOT / "docs/vat-ly-2/bai-giang/img/young-28"
SCALE = 2.5

# stem: (printed page, (left, top, right, bottom))
FIGURES = {
    "hinh-bridge28-30": (944, (360, 295, 520, 415)),
    "hinh-q28-13": (945, (255, 350, 335, 395)),
    "hinh-e28-3": (945, (542, 245, 612, 325)),
    "hinh-e28-4": (945, (420, 370, 550, 425)),
    "hinh-e28-6": (945, (510, 505, 620, 590)),
    "hinh-e28-8": (946, (220, 73, 310, 155)),
    "hinh-e28-9": (946, (180, 198, 290, 260)),
    "hinh-e28-12": (946, (45, 460, 165, 540)),
    "hinh-e28-13": (946, (160, 442, 285, 530)),
    "hinh-e28-19": (946, (460, 350, 570, 440)),
    "hinh-e28-21": (946, (480, 580, 575, 615)),
    "hinh-e28-23": (947, (100, 130, 310, 190)),
    "hinh-e28-24": (947, (215, 220, 345, 300)),
    "hinh-e28-25": (947, (115, 365, 270, 495)),
    "hinh-e28-27": (947, (215, 610, 330, 685)),
    "hinh-e28-28": (947, (490, 75, 630, 148)),
    "hinh-e28-29": (947, (480, 165, 610, 230)),
    "hinh-e28-32": (947, (495, 425, 610, 480)),
    "hinh-e28-33": (947, (495, 500, 612, 575)),
    "hinh-e28-38": (948, (185, 140, 300, 240)),
    "hinh-e28-39": (948, (185, 315, 300, 390)),
    "hinh-p28-49": (948, (460, 300, 595, 410)),
    # Include both wires at y=+a and y=-a; the lower wire's into-page symbol
    # sits below the x-axis and was clipped by the previous y=485 boundary.
    "hinh-p28-58": (949, (225, 405, 330, 515)),
    "hinh-p28-59": (949, (75, 650, 310, 770)),
    "hinh-p28-60": (949, (400, 125, 545, 220)),
    # Retain the lower conductor as well as the two hanging cords.
    "hinh-p28-61": (949, (420, 300, 560, 400)),
    "hinh-p28-62": (949, (520, 415, 612, 485)),
    "hinh-p28-64": (950, (180, 75, 310, 225)),
    "hinh-p28-66": (950, (195, 340, 295, 385)),
    "hinh-p28-68": (950, (180, 595, 280, 675)),
    "hinh-p28-69": (950, (395, 110, 500, 170)),
    # Include the full right ends of both infinite-sheet rows with a clear margin.
    "hinh-p28-70": (950, (465, 190, 580, 270)),
    "hinh-p28-71": (950, (450, 345, 590, 455)),
    "hinh-p28-72": (951, (75, 75, 285, 175)),
    "hinh-p28-74": (951, (265, 380, 335, 430)),
    "hinh-p28-76": (951, (490, 90, 630, 220)),
    "hinh-p28-77": (951, (490, 365, 630, 510)),
    "hinh-p28-79": (952, (180, 75, 300, 175)),
}

# Remove the caption that shares the top edge with the E28.13 diagram.
MASKS = {
    "hinh-e28-3": [(542, 245, 560, 275)],
    "hinh-e28-13": [(160, 442, 225, 460)],
    "hinh-e28-25": [(115, 365, 180, 372)],
    "hinh-e28-6": [(510, 515, 530, 540)],
    "hinh-e28-33": [(495, 500, 510, 520)],
    "hinh-p28-49": [(460, 400, 595, 410)],
}


def trim_white(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    bounds = ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()
    if bounds:
        left, top, right, bottom = bounds
        pad = 5
        image.crop((max(0, left - pad), max(0, top - pad),
                    min(image.width, right + pad), min(image.height, bottom + pad))) \
             .save(path, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for stem, (printed_page, coordinates) in FIGURES.items():
        page = doc[printed_page + 19]
        rect = pymupdf.Rect(coordinates)
        if not page.rect.contains(rect):
            raise ValueError(f"Crop outside printed page {printed_page}: {stem} {rect}")
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect, alpha=False)
        out = OUT / f"{stem}.png"
        pix.save(out)
        if stem in MASKS:
            image = Image.open(out).convert("RGB")
            draw = ImageDraw.Draw(image)
            for left, top, right, bottom in MASKS[stem]:
                draw.rectangle((round((left - rect.x0) * SCALE), round((top - rect.y0) * SCALE),
                                round((right - rect.x0) * SCALE), round((bottom - rect.y0) * SCALE)),
                               fill="white")
            image.save(out, optimize=True)
        trim_white(out)
    print(f"Prepared {len(FIGURES)} Chapter 28 exercise figures at {SCALE:g}x in {OUT}")


if __name__ == "__main__":
    main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-13.png', 'pdfPage': 966, 'bounds': [160, 442, 285, 544], 'scale': 2.5, 'masks': [[160, 442, 225, 460]]}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-19.png', 'pdfPage': 966, 'bounds': [460, 350, 578, 485], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-24.png', 'pdfPage': 967, 'bounds': [215, 220, 345, 318], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-25.png', 'pdfPage': 967, 'bounds': [115, 365, 270, 500], 'scale': 2.5, 'masks': [[115, 365, 180, 372]]}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-27.png', 'pdfPage': 967, 'bounds': [215, 610, 338, 685], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-3.png', 'pdfPage': 965, 'bounds': [542, 245, 622, 325], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-38.png', 'pdfPage': 968, 'bounds': [185, 140, 300, 254], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-39.png', 'pdfPage': 968, 'bounds': [185, 315, 300, 402], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-e28-9.png', 'pdfPage': 966, 'bounds': [180, 198, 298, 260], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-58.png', 'pdfPage': 969, 'bounds': [225, 405, 338, 523], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-61.png', 'pdfPage': 969, 'bounds': [400, 300, 568, 400], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-64.png', 'pdfPage': 970, 'bounds': [180, 75, 310, 237], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-66.png', 'pdfPage': 970, 'bounds': [195, 340, 303, 393], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-68.png', 'pdfPage': 970, 'bounds': [180, 595, 298, 675], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-69.png', 'pdfPage': 970, 'bounds': [383, 110, 500, 170], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-70.png', 'pdfPage': 970, 'bounds': [465, 190, 580, 282], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-71.png', 'pdfPage': 970, 'bounds': [450, 345, 590, 469], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-74.png', 'pdfPage': 971, 'bounds': [265, 380, 335, 437], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-p28-79.png', 'pdfPage': 972, 'bounds': [180, 75, 300, 187], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-28/hinh-q28-13.png', 'pdfPage': 965, 'bounds': [255, 350, 335, 410], 'scale': 2.5, 'masks': []}]
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
