from pathlib import Path
from PIL import Image,ImageOps,ImageDraw

root=Path(__file__).resolve().parents[1]
files=sorted((root/'docs/vat-ly-2/bai-giang/img/young-21').glob('*.png'))
out=root/'qa/physics/chapter21';out.mkdir(parents=True,exist_ok=True)
for batch in range((len(files)+19)//20):
    sheet=Image.new('RGB',(1400,1100),'white');d=ImageDraw.Draw(sheet)
    for i,p in enumerate(files[batch*20:(batch+1)*20]):
        x=(i%5)*280;y=(i//5)*275
        im=Image.open(p).convert('RGB');im.thumbnail((268,238))
        sheet.paste(im,(x+(280-im.width)//2,y+20))
        d.text((x+5,y+3),p.stem,fill='black')
    sheet.save(out/f'asset-contact-{batch}.jpg')
print('Asset contact sheets:',(len(files)+19)//20)
