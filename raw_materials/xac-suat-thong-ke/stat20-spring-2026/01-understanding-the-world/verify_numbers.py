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
source = Path(__file__).with_name('notes.html').read_text(encoding='utf-8')
for value in ['70%', '99%', '1.2%']:
    assert value in source
examples = body.split('## 1. Các loại phát biểu từ dữ liệu', 1)[1].split('## 2.', 1)[0]
assert examples.count('70%') == 2
assert 'hơn 99%' in examples and 'Uber' in examples and '1,2%' in examples
assert 'sinh viên UET' not in examples
assert Fraction('1.2') / 100 == Fraction(3, 250)
print('Ví dụ chính giữ tỷ lệ 70%, hơn 99% và Uber tăng 1,2%; ví dụ tính tỷ lệ là giả định riêng.')
print('Các tỷ lệ đúng; nguồn và giấy phép chỉ xuất hiện trong phần tham khảo.')
