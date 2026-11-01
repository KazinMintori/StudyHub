"""Reproduce chapter 29 opening, summary illustrations and bridge diagram."""
from pathlib import Path
import pymupdf
from PIL import Image,ImageChops
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/vat-ly-2/bai-giang/img/young-29'
FIGURES={
    'mo-dau-29':(953,(0,0,430,246)),
    'tom-tat-faraday':(977,(488,91,615,178)),
    'tom-tat-lenz':(977,(488,192,578,265)),
    'tom-tat-chuyen-dong':(977,(484,276,592,337)),
    'tom-tat-dien-truong':(977,(487,385,590,442)),
    'hinh-bridge29-28':(978,(340,621,563,734)),
}
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    pdf=pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')
    for name,(printed,box) in FIGURES.items():
        page=pdf[printed+19]
        pix=page.get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(box),alpha=False)
        file=OUT/f'{name}.png';pix.save(file)
        if name!='mo-dau-29':
            image=Image.open(file).convert('RGB')
            bounds=ImageChops.difference(image,Image.new('RGB',image.size,'white')).getbbox()
            if bounds:
                x0,y0,x1,y1=bounds
                image.crop((max(0,x0-12),max(0,y0-12),min(image.width,x1+12),min(image.height,y1+12))).save(file,optimize=True)
    print(f'Prepared {len(FIGURES)} opening, summary and bridge assets.')
if __name__=='__main__':main()


# Final source frames verified against the original PDF, 2026-11-01.
_studyhub_final_frame_specs = [{'file': 'docs/vat-ly-2/bai-giang/img/young-29/tom-tat-faraday.png', 'pdfPage': 997, 'bounds': [488, 83, 615, 178], 'scale': 2.5, 'masks': []}]
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
