"""Put related, deduplicated lab sets in the existing chapter exercise tab."""
from pathlib import Path
import argparse
import json
import re

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--available", action="store_true", help="Preview only completed fragments locally; final integration requires all files.")
args = parser.parse_args()
placements = {
    "bai-01-tong-quan-cong-cu-chinh-sach-ai": ["lab-01.md"],
    "bai-03-cau-truc-du-lieu-ham-tep": ["lab-02.md"],
    "bai-03-numpy": ["lab-03.md"],
    "bai-04-lam-quen-pandas": ["lab-04.md", "lab-05-pandas.md"],
    "bai-06-ket-noi-truy-xuat-du-lieu": ["lab-06.md"],
    "bai-10-lam-sach-du-lieu": ["lab-07.md", "lab-07-regex.md", "lab-10.md", "lab-11.md"],
    "bai-08-ghep-bang-chuyen-dang": ["lab-05-merge.md"],
    "bai-12-truc-quan-hoa-co-ban": ["lab-12.md", "lab-13.md"],
    "bai-10-tong-hop-theo-nhom": ["lab-05-groupby.md"],
    "bai-08-du-lieu-thoi-gian": ["lab-08.md"],
    "bai-14-ke-chuyen-bang-du-lieu": ["lab-14.md"],
}

if args.available:
    placements = {slug: [name for name in names if (root / "raw_materials/xu-ly-du-lieu/labs" / name).is_file()] for slug, names in placements.items()}
    placements = {slug: names for slug, names in placements.items() if names}

for slug, names in placements.items():
    for name in names:
        assert (root / "raw_materials/xu-ly-du-lieu/labs" / name).is_file(), f"Not ready: {name}"

for slug, names in placements.items():
    file = root / "docs/xu-ly-du-lieu/bai-giang" / f"{slug}.md"
    text = file.read_text(encoding="utf-8")
    # These earlier notebook fragments are superseded by the full dual-solution sets.
    text = re.sub(r"\n<!--@include: [^\n]*raw_materials/xu-ly-du-lieu/practice/(?:iai-[^\n]*|regex\.md)[^\n]*-->\n", "\n", text)
    text = re.sub(r"\n<!-- data-labs:start -->.*?<!-- data-labs:end -->\n", "\n", text, flags=re.S)
    split = text.index('<div class="lecture-exercises-content"')
    reference = text.index("## Tài liệu tham khảo", split)
    sections = ["<!-- data-labs:start -->"]
    for name in names:
        identifier = name.removesuffix(".md")
        sections += [f'<section class="data-lab-set" data-lab="{identifier}">', "", f'<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/{name}-->', "", "</section>", ""]
    sections += ["<!-- data-labs:end -->", ""]
    text = text[:reference] + "\n".join(sections) + "\n" + text[reference:]
    # Credit belongs in the existing references, not inside each exercise prompt.
    credit = "- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).\n"
    if "[Notebook thực hành]" not in text:
        end = text.rfind("</div>")
        text = text[:end].rstrip() + "\n\n" + credit + "\n" + text[end:]
    file.write_text(text, encoding="utf-8")

manifest = [{"slug": slug, "files": names} for slug, names in placements.items()]
(root / "raw_materials/xu-ly-du-lieu/lab-placement.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Integrated {sum(map(len, placements.values()))} lab sets in {len(placements)} existing chapter tabs.")
