# Vietnamese glyphs for MathJax SVG

MathJax 3's TeX font lacks several Vietnamese characters. Its server-side fallback
estimates their widths, then draws them in the browser's serif font. This splits
words such as “một chuỗi” and can detach their tone marks.

`vietnamese.mjs` adds outlines and actual advances for missing characters only.
The existing TeX symbols and supported characters stay unchanged. Normal, italic,
bold and bold italic variants are generated from the already installed Source
Serif 4 font dependency. No browser font fetch or runtime MathJax is introduced.

Regenerate the checked-in data from the repository root with:

```sh
python scripts/maintenance/generate-vietnamese-math-font.py
```

The generator requires `fonttools[woff]`. CI consumes the generated JSON directly
and does not need Python font tools. The derived outlines retain the accompanying
SIL Open Font License in `LICENSE`.
