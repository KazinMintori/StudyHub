"""Cache the authorized ArtInt 3e HTML and readable source, without a site build.

Uses the already installed requests and BeautifulSoup packages. Re-running reuses
HTML snapshots. Source files and hashes are evidence, not generated translations.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

BASE = "https://artint.info/3e/html/"
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "raw_materials/ai-nen-tang-tac-tu/source"
CHAPTERS = [
    ("01-tri-tue-nhan-tao-va-tac-tu", "Trí tuệ nhân tạo và tác tử", "a"),
    ("02-kien-truc-tac-tu-va-dieu-khien-phan-cap", "Kiến trúc tác tử và điều khiển phân cấp", "a"),
    ("03-tim-kiem-loi-giai", "Tìm kiếm lời giải", "a"),
    ("04-suy-luan-voi-rang-buoc", "Suy luận với ràng buộc", "a"),
    ("05-menh-de-va-suy-dien", "Mệnh đề và suy diễn", "a"),
    ("06-lap-ke-hoach-tat-dinh", "Lập kế hoạch tất định", "a"),
    ("07-hoc-may-co-giam-sat", "Học máy có giám sát", "b"),
    ("08-mang-no-ron-va-hoc-sau", "Mạng nơron và học sâu", "b"),
    ("09-suy-luan-voi-su-khong-chac-chan", "Suy luận với sự không chắc chắn", "b"),
    ("10-hoc-voi-su-khong-chac-chan", "Học với sự không chắc chắn", "b"),
    ("11-quan-he-nhan-qua", "Quan hệ nhân quả", "b"),
    ("12-lap-ke-hoach-trong-dieu-kien-khong-chac-chan", "Lập kế hoạch trong điều kiện không chắc chắn", "b"),
    ("13-hoc-tang-cuong", "Học tăng cường", "b"),
    ("14-he-da-tac-tu", "Hệ đa tác tử", "b"),
    ("15-ca-the-va-quan-he", "Cá thể và quan hệ", "c"),
    ("16-do-thi-tri-thuc-va-ban-the-hoc", "Đồ thị tri thức và bản thể học", "c"),
    ("17-hoc-quan-he-va-suy-luan-xac-suat", "Học quan hệ và suy luận xác suất", "c"),
    ("18-tac-dong-xa-hoi-cua-tri-tue-nhan-tao", "Tác động xã hội của trí tuệ nhân tạo", "c"),
    ("19-nhin-lai-va-trien-vong", "Nhìn lại và triển vọng", "c"),
    ("20-kien-thuc-toan", "Kiến thức toán học và ký hiệu", "c"),
    ("21-goi-ma-nguon-mo", "Đối chiếu với các gói mã nguồn mở", "c"),
]


def fetch(filename: str) -> tuple[str, str]:
    path = DEST / "html" / filename
    if path.exists():
        return filename, path.read_text(encoding="utf-8")
    response = requests.get(BASE + filename, timeout=45,
                            headers={"User-Agent": "StudyHub-authorized-translation-source/1.0"})
    response.raise_for_status()
    response.encoding = "utf-8"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(response.text, encoding="utf-8")
    return filename, response.text


def render(node: Tag | NavigableString, page_url: str) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if node.name in {"script", "style", "nav", "annotation", "annotation-xml"}:
        return ""
    if node.name == "math":
        tex = node.get("alttext", "").strip()
        if not tex:
            tex = node.get_text(" ", strip=True)
        return "\n\n$$\n" + tex + "\n$$\n\n" if node.get("display") == "block" else "$" + tex + "$"
    if node.name == "img":
        return "![" + node.get("alt", "Figure") + "](" + urljoin(page_url, node.get("src", "")) + ")"
    inner = "".join(render(child, page_url) for child in node.children)
    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return "\n\n" + "#" * min(int(node.name[1]), 6) + " " + inner.strip() + "\n\n"
    if node.name == "a" and node.get("href"):
        return "[" + inner.strip() + "](" + urljoin(page_url, node["href"]) + ")"
    if node.name == "li":
        return "\n- " + inner.strip() + "\n"
    if node.name == "pre":
        return "\n\n```\n" + node.get_text() + "\n```\n\n"
    if node.name in {"em", "i"}:
        return "*" + inner + "*"
    if node.name in {"strong", "b"}:
        return "**" + inner + "**"
    if node.name in {"td", "th"}:
        return inner.strip() + " | "
    if node.name == "tr":
        return "\n| " + inner.strip() + "\n"
    if node.name == "br":
        return "\n"
    if node.name in {"p", "div", "section", "figure", "figcaption", "blockquote", "table", "ul", "ol", "article"}:
        return "\n\n" + inner.strip() + "\n\n"
    return inner


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", type=int, action="append", help="Fetch only these numbered chapters; default: All.")
    args = parser.parse_args()
    _, root_html = fetch("ArtInt3e.html")
    root_soup = BeautifulSoup(root_html, "html.parser")
    chapter_links = []
    for anchor in root_soup.select("a[href]"):
        filename = urlparse(urljoin(BASE, anchor["href"])).path.rsplit("/", 1)[-1]
        if re.fullmatch(r"ArtInt3e\.(?:Ch\d+|A\d+)\.html", filename) and filename not in chapter_links:
            chapter_links.append(filename)
    if len(chapter_links) != 21:
        raise RuntimeError(f"Expected 19 chapters and 2 appendices, found {chapter_links}")
    chapters = [dict(number=i+1, slug=slug, title=title, part=part, filename=chapter_links[i],
                     url=BASE+chapter_links[i], pages=[]) for i, (slug, title, part) in enumerate(CHAPTERS)]
    selected = [c for c in chapters if not args.chapter or c["number"] in args.chapter]
    prefixes = {c["filename"][:-5]: c for c in selected}
    queue = set(c["filename"] for c in selected)
    visited = set()
    with ThreadPoolExecutor(max_workers=4) as pool:
        while queue:
            batch = sorted(queue - visited)
            queue.clear()
            if len(visited) + len(batch) > 1000:
                raise RuntimeError("Unexpected source expansion")
            for filename, html in pool.map(fetch, batch):
                visited.add(filename)
                soup = BeautifulSoup(html, "html.parser")
                article = soup.select_one("article.ltx_document") or soup.select_one(".ltx_page_content")
                if article is None:
                    raise RuntimeError(f"No article: {filename}")
                for anchor in article.select("a[href]"):
                    target_url = urljoin(BASE, anchor["href"])
                    parsed = urlparse(target_url)
                    target = parsed.path.rsplit("/", 1)[-1]
                    if parsed.netloc == "artint.info" and any(target == prefix + ".html" or target.startswith(prefix + ".") for prefix in prefixes):
                        if target.endswith(".html") and target not in visited:
                            queue.add(target)
                content = re.sub(r"\n[ \t]+", "\n", render(article, BASE + filename))
                content = re.sub(r"\n{3,}", "\n\n", content).strip()
                md_path = DEST / "text" / filename.replace(".html", ".md")
                md_path.parent.mkdir(parents=True, exist_ok=True)
                md_path.write_text("Source: " + BASE + filename + "\n\n" + content + "\n", encoding="utf-8")
                chapter = next(c for prefix, c in prefixes.items() if filename == prefix + ".html" or filename.startswith(prefix + "."))
                chapter["pages"].append(dict(filename=filename, title=(article.find(re.compile("^h[1-6]$")).get_text(" ", strip=True) if article.find(re.compile("^h[1-6]$")) else filename),
                                             source=BASE + filename, words=len(article.get_text(" ", strip=True).split()),
                                             sha256=hashlib.sha256(html.encode("utf-8")).hexdigest(),
                                             text=str(md_path.relative_to(ROOT)).replace("\\", "/")))
            print(f"Cached {len(visited)} source pages; pending {len(queue - visited)}", flush=True)
    manifest = dict(source=BASE + "ArtInt3e.html", fetched_at=datetime.now(timezone.utc).isoformat(),
                    permission="User confirmed translation and republication rights on 2026-11-02; no public relicensing asserted.",
                    chapters=selected, page_count=len(visited))
    path = DEST / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(pages=len(visited), words=sum(p["words"] for c in selected for p in c["pages"]), manifest=str(path)), ensure_ascii=False))


if __name__ == "__main__":
    main()
