"""Shared typography and colors for the classical XSTK scientific figures."""
from functools import lru_cache
from pathlib import Path
from io import BytesIO
import base64
import hashlib
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FONT_FAMILY = "StudyHub Figure Sans"
PALETTE = {
    "ink": "#1f1c2b", "muted": "#6b6580", "paper": "#ffffff",
    "canvas": "#f5f4f9", "rule": "#dcd8e8", "grid": "#e4e0f0",
    "primary": "#5a37a8", "teal": "#087f7a", "copper": "#8a5100", "alert": "#b42318",
}
COLOR_MAP = {
    "#0f172a": PALETTE["ink"], "#17212b": PALETTE["ink"], "#1e293b": PALETTE["ink"],
    "#334155": "#4f4a62", "#475569": PALETTE["muted"], "#4c5966": PALETTE["muted"],
    "#64748b": PALETTE["muted"], "#cbd5e1": PALETTE["rule"], "#e2e8f0": PALETTE["rule"],
    "#f8fafc": "#faf9fd", "#94a3b8": "#a29ab4",
    "#3b82f6": PALETTE["primary"], "#2563eb": PALETTE["primary"],
    "#2458a6": PALETTE["primary"], "#215eab": PALETTE["primary"], "#1e40af": "#46288a",
    "#10b981": PALETTE["teal"], "#059669": PALETTE["teal"], "#007c78": PALETTE["teal"],
    "#047857": "#075e5b", "#065f46": "#075e5b",
    "#f59e0b": PALETTE["copper"], "#f97316": PALETTE["copper"], "#eab308": PALETTE["copper"],
    "#9a4c11": PALETTE["copper"], "#b45309": PALETTE["copper"],
    "#ef4444": PALETTE["alert"], "#dc2626": PALETTE["alert"], "#b91c1c": PALETTE["alert"],
    "#b13b35": PALETTE["alert"], "#8b5cf6": "#a03b72",
    "#dbeafe": "#eee9fb", "#eff6ff": "#f4f0fc", "#e0f2fe": "#eee9fb",
    "#ecfdf5": "#edf7f5", "#d1fae5": "#e3f3f0",
    "#fef2f2": "#fcf0f2", "#fee2e2": "#f9e6ea", "#fef3c7": "#fbf1df",
    "#ffedd5": "#fbf1df", "#fff7ed": "#fcf5ea",
}


@lru_cache(maxsize=2)
def figure_font(weight=400):
    """Merge the installed Latin/Vietnamese subsets, preserving their metrics."""
    from fontTools.merge import Merger
    source = ROOT / "node_modules/@fontsource/be-vietnam-pro/files"
    files = [source / f"be-vietnam-pro-{subset}-{weight}-normal.woff2"
             for subset in ("latin", "vietnamese")]
    if not all(file.exists() for file in files):
        raise RuntimeError("Be Vietnam Pro is unavailable. Run npm ci in the repository.")
    key = hashlib.sha256(b"".join(file.read_bytes() for file in files)).hexdigest()[:16]
    cache = Path(tempfile.gettempdir()) / "studyhub-xstk-fonts"
    cache.mkdir(exist_ok=True)
    target = cache / f"StudyHubFigureSans-{weight}-{key}.ttf"
    if not target.exists():
        font = Merger().merge([str(file) for file in files])
        font.flavor = None
        font.recalcTimestamp = False
        style = "Regular" if weight == 400 else "SemiBold"
        names = {1: FONT_FAMILY, 4: f"{FONT_FAMILY} {style}",
                 6: f"StudyHubFigureSans-{style}", 16: FONT_FAMILY}
        for record in font["name"].names:
            if record.nameID in names:
                record.string = names[record.nameID].encode(record.getEncoding(), errors="replace")
        font.save(target)
    return target


@lru_cache(maxsize=128)
def _font_faces(characters):
    from fontTools import subset
    from fontTools.ttLib import TTFont
    css = []
    for weight in (400, 600):
        font = TTFont(figure_font(weight), recalcTimestamp=False)
        options = subset.Options()
        options.layout_features = ["*"]
        sub = subset.Subsetter(options=options)
        sub.populate(text=characters)
        sub.subset(font)
        font.flavor = "woff2"
        encoded = BytesIO()
        font.save(encoded)
        data = base64.b64encode(encoded.getvalue()).decode("ascii")
        css.append(f"@font-face{{font-family:'{FONT_FAMILY}';font-style:normal;"
                   f"font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return "".join(css)


def polish_svg(source):
    """Embed stable Vietnamese typography without external font requests."""
    tree = ET.fromstring(source)
    characters = "".join(sorted(set("".join(tree.itertext()) + "0123456789-+. ")))
    # Original generated color roles are mapped to the site's ink-on-paper palette.
    source = re.sub(r"#[0-9a-fA-F]{6}\b",
                    lambda match: COLOR_MAP.get(match.group().lower(), match.group()), source)
    # Promote small labels while preserving math superscripts inside tspans.
    def text_tag(match):
        tag = match.group()
        return re.sub(r'font-size=(["\'])([\d.]+)(?:px)?\1',
                      lambda size: f'font-size="{max(14, float(size[2])):g}"', tag)
    source = re.sub(r"<text\b[^>]*>", text_tag, source)
    source = re.sub(r"(font-size:\s*)([\d.]+)(px)",
                    lambda size: f"{size[1]}{max(14, float(size[2])):g}{size[3]}", source)
    css = _font_faces(characters)
    css += (f"text{{font-family:'{FONT_FAMILY}','Segoe UI',Arial,sans-serif!important}}"
            ".math-text{font-family:'Cambria Math','Times New Roman',serif!important}"
            "path,polyline,line{stroke-linecap:round;stroke-linejoin:round}")
    insertion = ("<!-- Typography derived from Be Vietnam Pro, SIL OFL 1.1. "
                 "See ../OFL-BeVietnamPro.txt. -->"
                 f"<defs><style>{css}</style></defs>")
    result = re.sub(r"<svg\b[^>]*>", lambda match: match.group() + insertion, source, count=1)
    return "\n".join(line.rstrip() for line in result.splitlines()) + "\n"


def configure_matplotlib():
    import matplotlib
    from matplotlib import font_manager
    for weight in (400, 600):
        font_manager.fontManager.addfont(str(figure_font(weight)))
    matplotlib.rcParams.update({
        "font.family": [FONT_FAMILY, "DejaVu Sans"], "font.size": 15, "axes.titlesize": 19,
        "axes.labelsize": 15, "xtick.labelsize": 14, "ytick.labelsize": 14,
        "axes.titleweight": 600, "axes.titlepad": 18, "axes.labelpad": 10,
        "legend.fontsize": 14, "legend.frameon": False,
        "xtick.major.pad": 9, "ytick.major.pad": 9,
        "figure.constrained_layout.w_pad": .16, "figure.constrained_layout.h_pad": .16,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": PALETTE["muted"], "text.color": PALETTE["ink"],
        "axes.labelcolor": PALETTE["ink"], "xtick.color": PALETTE["muted"],
        "ytick.color": PALETTE["muted"], "grid.color": PALETTE["grid"],
        "lines.linewidth": 2.4, "svg.fonttype": "none", "svg.hashsalt": "studyhub-xstk",
        "savefig.facecolor": PALETTE["paper"],
    })
