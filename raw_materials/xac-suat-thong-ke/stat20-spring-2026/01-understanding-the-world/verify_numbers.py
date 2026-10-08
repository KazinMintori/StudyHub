"""Kiểm tra phép tính bổ sung, không xác minh các nhận định thực nghiệm của nguồn."""
from fractions import Fraction
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = Path(__file__).resolve().parents[4]
notes = (root / 'docs/xac-suat-thong-ke/bai-giang/00-hieu-the-gioi-bang-du-lieu.md').read_text(encoding='utf-8')
source = Path(__file__).with_name('notes.html').read_text(encoding='utf-8')
for numerator, denominator in [(7, 10), (14, 20)]:
    percentage = Fraction(numerator, denominator) * 100
    assert percentage == 70
    print(f'{numerator}/{denominator} * 100 = {percentage}%')

assert '70%' in source and '99%' in source and '1.2%' in source
translation = notes.split('## 2. Các loại phát biểu từ dữ liệu')[1].split('## 3.')[0]
assert translation.count('70%') == 2
assert 'hơn 99%' in translation and '1,2%' in translation
assert Fraction('1.2') / 100 == Fraction(3, 250)
print('Giữ nguyên hai ví dụ 70%, ngưỡng hơn 99% và mức tăng 1,2% của nguồn.')
