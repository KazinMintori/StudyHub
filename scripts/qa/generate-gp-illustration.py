"""Plot the same three-variable monomial equality in two coordinate systems."""
from math import cos, sin, log, pi
from pathlib import Path

ANGLES = (pi / 5, pi / 6)
SAMPLES = [.75, .875, 1, 1.125, 1.25, 1.375, 1.5]


def project(point, center, scale):
    x, y, z = point
    yaw, pitch = ANGLES
    horizontal = x * cos(yaw) - y * sin(yaw)
    depth = x * sin(yaw) + y * cos(yaw)
    return 180 + scale * horizontal, center - scale * (z * cos(pitch) - depth * sin(pitch))


def panel(logarithmic):
    center, scale = (398, 84) if logarithmic else (158, 90)

    def coordinates(x, y):
        z = 1 / (x * y)
        if logarithmic:
            return log(x), log(y), log(z)
        return x - 1.125, y - 1.125, z - 1

    paths = []
    for fixed in SAMPLES:
        varying = [.75 + .75 * step / 40 for step in range(41)]
        for pairs in ([(fixed, v) for v in varying], [(v, fixed) for v in varying]):
            points = [project(coordinates(x, y), center, scale) for x, y in pairs]
            path = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
            paths.append(f'<polyline points="{path}" fill="none" stroke="#7757b9" stroke-width="1.05"/>')
    curve = []
    for step in range(41):
        x = .75 * 2 ** (step / 40)
        y = 1.5 / 2 ** (step / 40)
        curve.append(project(coordinates(x, y), center, scale))
    points = ' '.join(f'{x:.2f},{y:.2f}' for x, y in curve)
    paths.append(f'<polyline points="{points}" fill="none" stroke="#19705a" stroke-width="2.3"/>')
    for x, y in (curve[0], curve[20], curve[-1]):
        paths.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="#19705a"/>')
    return '\n'.join(paths)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="495" viewBox="0 0 360 495" role="img">
<title>Mặt tích bằng 1 và mặt phẳng tổng logarit bằng 0</title>
<rect width="360" height="495" rx="12" fill="#fff"/>
<g fill="#242136" font-family="sans-serif" font-size="17">
<text x="22" y="32">Tọa độ gốc</text><text x="22" y="57">x₁x₂x₃ = 1</text>
<text x="22" y="276">Tọa độ logarit</text><text x="22" y="301">y₁ + y₂ + y₃ = 0</text>
</g>
<path d="M22 246H338" fill="none" stroke="#ded9e3"/>
{panel(False)}
{panel(True)}
</svg>'''

if __name__ == '__main__':
    target = Path('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02/gp-log-surface.svg')
    target.write_text(svg, encoding='utf-8')
