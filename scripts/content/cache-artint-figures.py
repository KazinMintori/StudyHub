"""Cache only figures actually referenced by the two published chapters."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import urlparse

import requests

root = Path(__file__).resolve().parents[2]
notes = root / "docs/ai-nen-tang-tac-tu/bai-giang"
manifest_path = root / "raw_materials/ai-nen-tang-tac-tu/review/figures.json"
records = {}
for chapter in ["05-menh-de-va-suy-dien", "15-ca-the-va-quan-he"]:
    directory = notes / chapter
    if not directory.exists():
        continue
    for page in directory.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        urls = set(re.findall(r"!\[[^\]]*\]\((https://artint\.info/3e/html/[^\s)]+)\)", text))
        for url in urls:
            filename = Path(urlparse(url).path).name
            if not re.fullmatch(r"[a-zA-Z0-9_.-]+\.(?:png|svg|jpe?g|gif|webp)", filename):
                raise ValueError(f"Unsupported image: {url}")
            target = directory / "figures" / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                response = requests.get(url, timeout=45)
                response.raise_for_status()
                if response.headers.get("content-type", "").startswith("text/html"):
                    raise ValueError(f"HTML returned for figure: {url}")
                target.write_bytes(response.content)
            data = target.read_bytes()
            relative = target.relative_to(root).as_posix()
            records[relative] = dict(source=url, sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
            image_link = Path(__import__('os').path.relpath(target, page.parent)).as_posix()
            text = text.replace("](" + url + ")", "](" + image_link + ")")
        page.write_text(text, encoding="utf-8")
manifest_path.parent.mkdir(parents=True, exist_ok=True)
existing = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
existing.update(records)
manifest_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Cached {len(records)} referenced chapter figures; retained {len(existing)} manifest entries.")
