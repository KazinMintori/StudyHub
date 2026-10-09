"""Lập danh mục từng trang nguyên tác, không biến OCR thành công thức đã xác minh.

python -I raw_materials/physics/audit_full_source.py
Đầu ra cục bộ dưới qa/physics/full-source (gitignored).
"""
from pathlib import Path
import hashlib
import json
import re
import sys
import pymupdf

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'raw_materials/physics/source/young-freedman-15.pdf'
OUT = ROOT/'qa/physics/full-source'
OUT.mkdir(parents=True, exist_ok=True)
old = json.loads((ROOT/'qa/physics/source/manifest.json').read_text(encoding='utf-8'))
document = pymupdf.open(SOURCE)
assert len(document) == 1587
assert 'APPENDIX A' in document[1544].get_text()
assert '44.56' in document[1543].get_text()
chapters = []
pages = []
for index, chapter in enumerate(old):
    start = chapter['start']
    end = old[index+1]['start']-1 if index+1 < len(old) else 1524
    entries = []
    for printed in range(start, end+1):
        pdf_number = printed+20
        page = document[pdf_number-1]
        text = page.get_text()
        filename = f'pdf-{pdf_number:04}.txt'
        (OUT/filename).write_text(text,encoding='utf-8')
        markers = sorted(set(re.findall(
            r'EXAMPLE\s+\d+\.\d+|CONCEPTUAL EXAMPLE\s+\d+\.\d+|'
            r'PROBLEM.SOLVING STRATEGY|TEST YOUR UNDERSTANDING|'
            r'GUIDED PRACTICE|DISCUSSION QUESTIONS|EXERCISES|'
            r'CHALLENGE PROBLEMS|MCAT.STYLE PASSAGE PROBLEMS|APPLICATION',
            text,re.I)))
        entry = dict(chapter=chapter['chapter'],printedPage=printed,pdfPage=pdf_number,
                     sourceText=filename,textSha256=hashlib.sha256(text.encode()).hexdigest(),
                     imageObjects=len(page.get_images()),markers=markers,
                     translationStatus='pending',visualComparisonStatus='pending')
        entries.append(entry)
        pages.append(entry)
    chapters.append(dict(chapter=chapter['chapter'],course='vat-ly-1' if index<20 else 'vat-ly-2',
                         printedStart=start,printedEnd=end,pdfStart=start+20,pdfEnd=end+20,
                         pageCount=len(entries),sections=chapter['sections']))
assert [p['printedPage'] for p in pages] == list(range(1,1525))
assert sum(c['pageCount'] for c in chapters[:20]) == 677
assert sum(c['pageCount'] for c in chapters[20:]) == 847
record=dict(sourceSha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),totalPdfPages=len(document),
            chapterPrintedPages=1524,frontMatterPdfPages=[1,20],
            appendicesAnswersCreditsIndexPdfPages=[1545,1587],chapters=chapters,pages=pages)
(OUT/'manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
for printed in [1,25,33,677,678,1521,1524]:
    document[printed+19].get_pixmap(matrix=pymupdf.Matrix(1,1)).save(OUT/f'printed-{printed:04}.png')
print(f'Đã lập danh mục {len(chapters)} chương, {len(pages)} trang nội dung và bài tập.')
print('Vật lý 1: 677 trang; Vật lý 2: 847 trang. Mọi trang liên tục, không có khoảng trống.')
print('Chưa xác nhận dịch hoặc đối chiếu trực quan toàn bộ: các trạng thái đều pending.')
