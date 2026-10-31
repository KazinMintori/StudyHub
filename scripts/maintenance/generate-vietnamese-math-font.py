"""Generate SVG glyphs/metrics for Vietnamese characters missing from MathJax TeX.

Uses the existing OFL Source Serif 4 dependency; requires fonttools[woff].
Run from the repository root. The generated data is used only at build time.
"""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

root = Path(__file__).resolve().parents[2]
fonts = root / 'node_modules/@fontsource-variable/source-serif-4'
characters = sorted(set(
    'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ'
    'ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ'
))
data = {}
for variant, style, weight in [('normal', 'normal', 400), ('italic', 'italic', 400),
                                ('bold', 'normal', 700), ('bold-italic', 'italic', 700)]:
    glyphs = {}
    for subset in ['latin', 'vietnamese']:
        font = TTFont(fonts / f'files/source-serif-4-{subset}-standard-{style}.woff2')
        font = instantiateVariableFont(font, {'wght': weight}, inplace=True)
        cmap, glyph_set = font.getBestCmap(), font.getGlyphSet()
        units = font['head'].unitsPerEm
        for char in characters:
            if ord(char) not in cmap:
                continue
            glyph = glyph_set[cmap[ord(char)]]
            pen = SVGPathPen(glyph_set, ntos=lambda n: str(round(n, 2)).rstrip('0').rstrip('.') if n % 1 else str(int(n)))
            glyph.draw(TransformPen(pen, (1000/units, 0, 0, 1000/units, 0, 0)))
            bounds = BoundsPen(glyph_set)
            glyph.draw(bounds)
            _, bottom, _, top = bounds.bounds
            path = pen.getCommands()
            assert path.startswith('M')
            # MathJax prefixes M and appends Z when emitting a glyph path.
            glyphs[str(ord(char))] = [round(top/units, 6), round(max(0, -bottom)/units, 6),
                                      round(glyph.width/units, 6), {'p': path[1:]}]
        font.close()
    assert len(glyphs) == len(characters), (variant, len(glyphs))
    data[variant] = glyphs
output = root / 'scripts/math-fonts'
output.mkdir(exist_ok=True)
(output / 'source-serif-vietnamese.json').write_text(json.dumps(data, separators=(',', ':'))+'\n', encoding='utf8')
(output / 'LICENSE').write_bytes((fonts / 'LICENSE').read_bytes())
print(f'Generated {len(characters)} characters in {len(data)} variants')
