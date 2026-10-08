"""Kiểm tra các tỷ lệ giả định và vị trí tài liệu tham khảo của bài giảng."""
from fractions import Fraction
from pathlib import Path
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

root = Path(__file__).resolve().parents[4]
notes = (root / 'docs/xac-suat-thong-ke/bai-giang/00-hieu-the-gioi-bang-du-lieu.md').read_text(encoding='utf-8')
for numerator, denominator in [(7, 10), (14, 20)]:
    percentage = Fraction(numerator, denominator) * 100
    assert percentage == 70
    print(f'{numerator}/{denominator} * 100 = {percentage}%')

assert r'\frac{7}{10}\times 100\%=70\%' in notes
assert r'\frac{14}{20}\times 100\%=70\%' in notes
body, references = notes.split('## 4. Tài liệu tham khảo', 1)
assert not re.search(r'Stat[ -]?20|stat20|Berkeley|Edstem|CC BY', body, re.IGNORECASE)
assert 'Stat 20' in references and 'creativecommons.org/licenses/by/4.0/' in references
print('Các tỷ lệ đúng; nguồn và giấy phép chỉ xuất hiện trong phần tham khảo.')
