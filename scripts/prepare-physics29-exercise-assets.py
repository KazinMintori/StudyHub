"""Reproduce complete chapter 29 exercise illustrations with unclipped labels."""
from pathlib import Path
import pymupdf
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-29'
# Printed page and PDF-point rectangle. Caption text is written in Vietnamese
# in the exercise statement, so only the diagram itself is extracted.
FIGURES={
 'hinh-e29-7':(980,(180,604,300,745)),
 'hinh-e29-8':(980,(474,76,575,143)),
 'hinh-e29-12':(980,(486,406,573,450)),
 'hinh-e29-14':(980,(487,550,574,633)),
 'hinh-e29-15':(980,(470,664,574,744)),
 'hinh-e29-16':(981,(125,147,306,269)),
 'hinh-e29-17':(981,(241,296,335,389)),
 'hinh-e29-18':(981,(164,430,242,496)),
 'hinh-e29-19':(981,(137,577,288,653)),
 'hinh-e29-20':(981,(423,60,542,153)),
 'hinh-e29-21':(981,(506,173,614,245)),
 'hinh-e29-22':(981,(522,271,615,360)),
 'hinh-e29-24':(981,(372,549,583,608)),
 'hinh-e29-25':(981,(519,642,614,698)),
 'hinh-e29-26':(982,(184,75,299,161)),
 'hinh-e29-27':(982,(34,321,298,395)),
 'hinh-e29-28':(982,(190,419,297,477)),
 'hinh-e29-29':(982,(175,551,299,611)),
 'hinh-e29-31':(982,(313,155,574,216)),
 'hinh-e29-32':(982,(313,398,574,455)),
 'hinh-e29-33':(982,(313,570,574,636)),
 'hinh-p29-44':(983,(354,381,585,433)),
 'hinh-p29-45':(983,(495,470,614,550)),
 'hinh-p29-48':(984,(181,154,297,233)),
 'hinh-p29-49':(984,(177,260,298,373)),
 'hinh-p29-51':(984,(165,569,298,650)),
 'hinh-p29-53':(984,(445,78,574,158)),
 'hinh-p29-54':(984,(450,187,575,279)),
 'hinh-p29-55':(984,(334,423,575,539)),
 'hinh-p29-56':(984,(475,570,575,657)),
 'hinh-p29-59':(985,(215,243,335,315)),
 'hinh-p29-60':(985,(84,541,285,618)),
 'hinh-p29-61':(985,(240,640,335,738)),
 'hinh-p29-62':(985,(506,79,615,158)),
 'hinh-p29-64':(985,(353,466,616,557)),
 'hinh-p29-65':(985,(502,585,615,648)),
 'hinh-p29-66':(986,(109,256,216,323)),
 'hinh-p29-67':(986,(170,490,298,624)),
 'hinh-p29-68':(986,(482,75,580,208)),
 'hinh-p29-69':(986,(340,452,585,553)),
 'hinh-p29-73':(987,(354,195,620,270)),
 'hinh-p29-74':(987,(354,344,620,506)),
 'mcat29-tms':(987,(85,319,340,430)),
}
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 pdf=pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
 for name,(printed,box) in FIGURES.items():
  pdf[printed+19].get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(box),alpha=False).save(OUT/f'{name}.png')
  path=OUT/f'{name}.png';image=Image.open(path).convert('RGB')
  bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
  if bounds:
   left,top,right,bottom=bounds
   image.crop((max(0,left-12),max(0,top-12),min(image.width,right+12),min(image.height,bottom+12))).save(path,optimize=True)
 print('Prepared',len(FIGURES),'chapter 29 end-of-chapter images.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-15.png', 'pdfPage': 1000, 'bounds': [470, 664, 574, 758], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-16.png', 'pdfPage': 1001, 'bounds': [105, 147, 306, 277], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-17.png', 'pdfPage': 1001, 'bounds': [241, 296, 347, 389], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-18.png', 'pdfPage': 1001, 'bounds': [164, 430, 242, 501], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-19.png', 'pdfPage': 1001, 'bounds': [129, 577, 288, 653], 'scale': 2.5, 'masks': [[129, 577, 135, 588]]}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-20.png', 'pdfPage': 1001, 'bounds': [423, 60, 542, 158], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-21.png', 'pdfPage': 1001, 'bounds': [506, 173, 614, 251], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-24.png', 'pdfPage': 1001, 'bounds': [372, 549, 583, 618], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-28.png', 'pdfPage': 1002, 'bounds': [190, 419, 297, 485], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-29.png', 'pdfPage': 1002, 'bounds': [175, 551, 299, 625], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-e29-33.png', 'pdfPage': 1002, 'bounds': [313, 570, 574, 641], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-44.png', 'pdfPage': 1003, 'bounds': [354, 375, 585, 433], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-48.png', 'pdfPage': 1004, 'bounds': [181, 154, 297, 240], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-51.png', 'pdfPage': 1004, 'bounds': [165, 564, 298, 655], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-55.png', 'pdfPage': 1004, 'bounds': [334, 423, 575, 545], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-56.png', 'pdfPage': 1004, 'bounds': [475, 564, 575, 657], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-64.png', 'pdfPage': 1005, 'bounds': [353, 460, 616, 557], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-65.png', 'pdfPage': 1005, 'bounds': [502, 585, 615, 662], 'scale': 2.5, 'masks': []}, {'file': 'docs/vat-ly-2/bai-giang/img/young-29/hinh-p29-66.png', 'pdfPage': 1006, 'bounds': [100, 256, 221, 323], 'scale': 2.5, 'masks': []}]
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
