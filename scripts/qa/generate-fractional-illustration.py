"""Exact labels for the fractional map's reweighted midpoint."""
from pathlib import Path
from lxml import etree
import pymupdf

out=Path('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02')
out.mkdir(parents=True,exist_ok=True)
qa=Path('qa/math-ai-visuals/fractional-illustration');qa.mkdir(parents=True,exist_ok=True)
body='''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="354" viewBox="0 0 360 354" role="img">
<title>Trung điểm trước chuẩn hóa trở thành tổ hợp một phần ba ảnh A và hai phần ba ảnh B</title>
<rect width="360" height="354" rx="12" fill="#ffffff"/>
<g font-family="sans-serif" font-size="17" fill="#242136">
<text x="180" y="30" text-anchor="middle">Trước phép đổi biến</text>
<line x1="42" y1="78" x2="318" y2="78" stroke="#81798e" stroke-width="1.3"/>
<g fill="#7757b9"><circle cx="42" cy="78" r="5"/><circle cx="180" cy="78" r="5"/><circle cx="318" cy="78" r="5"/></g>
<text x="42" y="61" text-anchor="middle">A</text><text x="180" y="61" text-anchor="middle">M</text><text x="318" y="61" text-anchor="middle">B</text>
<text x="42" y="111" text-anchor="middle">(1, 0)</text><text x="180" y="111" text-anchor="middle">(1, 2)</text><text x="318" y="111" text-anchor="middle">(1, 4)</text>
<text x="42" y="141" text-anchor="middle">D = 2</text><text x="180" y="141" text-anchor="middle">D = 3</text><text x="318" y="141" text-anchor="middle">D = 4</text>
<text x="180" y="190" text-anchor="middle">Sau phép đổi biến</text>
<line x1="42" y1="238" x2="318" y2="238" stroke="#81798e" stroke-width="1.3"/>
<g fill="#19705a"><circle cx="42" cy="238" r="5"/><circle cx="226" cy="238" r="5"/><circle cx="318" cy="238" r="5"/></g>
<text x="42" y="220" text-anchor="middle">A′</text><text x="226" y="220" text-anchor="middle">M′</text><text x="318" y="220" text-anchor="middle">B′</text>
<text x="42" y="275" text-anchor="middle">f = 3/2</text><text x="226" y="275" text-anchor="middle">f = 7/3</text><text x="318" y="275" text-anchor="middle">f = 11/4</text>
<text x="180" y="320" text-anchor="middle">M′ = (1/3)A′ + (2/3)B′</text>
<text x="180" y="344" text-anchor="middle" font-size="15">Hai đoạn dùng cùng thang tham số từ A đến B.</text>
</g></svg>'''
target=out/'fractional-reweighted-midpoint.svg';target.write_text(body,encoding='utf-8')
root=etree.fromstring(body.encode());root.set('width','294');root.set('height',str(294*354/360))
document=pymupdf.open(stream=etree.tostring(root),filetype='svg')
document[0].get_pixmap().save(qa/'fractional-reweighted-midpoint.png')
print(target)
