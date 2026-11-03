"""Reproduce the SOCP illustration of common and independent uncertainty."""
from pathlib import Path
from math import sqrt

output = Path('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02/socp-uncertainty-growth.svg')

def curve(function):
    return ' '.join(f'{54+27*count:.2f},{292-22*function(count):.2f}'
                    for count in (index/8 for index in range(73)))

illustration = f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="350" viewBox="0 0 360 350" role="img">
<title>Hai tốc độ tăng của độ lệch chuẩn</title>
<rect width="360" height="350" rx="12" fill="#fff"/>
<path d="M54 70V292H316" fill="none" stroke="#81798e" stroke-width="1.2"/>
<path d="M54 226H297M54 94H297" fill="none" stroke="#d6d1de" stroke-width="1"/>
<polyline points="{curve(lambda count: count)}" fill="none" stroke="#7757b9" stroke-width="2"/>
<polyline points="{curve(sqrt)}" fill="none" stroke="#19705a" stroke-width="2"/>
<circle cx="297" cy="94" r="4" fill="#7757b9"/><circle cx="297" cy="226" r="4" fill="#19705a"/>
<g fill="#242136" font-family="sans-serif" font-size="16">
<text x="22" y="34">Độ lệch chuẩn của tổng</text><text x="179" y="82">Sai số dùng chung</text>
<text x="140" y="210">Sai số độc lập</text><text x="32" y="99">9</text><text x="32" y="231">3</text>
<text x="40" y="314">0</text><text x="292" y="314">9</text><text x="211" y="337">Số đơn vị n</text>
</g></svg>'''

if __name__ == '__main__':
    output.write_text(illustration, encoding='utf-8')
    print('Generated uncertainty scaling illustration.')
