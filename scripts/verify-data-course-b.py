#!/usr/bin/env python3
"""
scripts/verify-data-course-b.py
Comprehensive verification script for Group B (Chapters 6-10) of course xu-ly-du-lieu:
1. Verifies authoring contract adherence (slugs, titles, prerequisites, status).
2. Verifies module files (lesson.mjs, slides.mjs) syntax and content.
3. Verifies Markdown frontmatter and pedagogical formatting rules:
   - Standalone display math delimiters ($$)
   - No \\vert or \\Vert syntax
   - Inline math <= 38ex
   - Capitalization after colons
   - Absence of forbidden phrases (thinking aloud, unsubstantiated error rates, em-dashes)
   - Proper reference section with CC BY-NC-SA 4.0 attribution
4. Extracts and executes all Python code blocks to ensure runnable examples and passing assertions.
"""

import os
import re
import sys
import json
import subprocess
import traceback
from pathlib import Path

# Configure matplotlib for headless test execution
os.environ["MPLBACKEND"] = "Agg"
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent

GROUP_B_SLUGS = [
    {
        "chapter": "6",
        "slug": "bai-06-ket-noi-truy-xuat-du-lieu",
        "title": "Nạp, lưu trữ và truy xuất dữ liệu",
        "prerequisites": ["dataframe", "ham-lap-trinh"],
    },
    {
        "chapter": "7",
        "slug": "bai-10-lam-sach-du-lieu",
        "title": "Làm sạch, chuẩn bị và xử lý chuỗi",
        "prerequisites": ["dataframe"],
    },
    {
        "chapter": "8",
        "slug": "bai-08-ghep-bang-chuyen-dang",
        "title": "Chỉ mục phân cấp, ghép bảng và chuyển dạng",
        "prerequisites": ["dataframe", "chi-muc"],
    },
    {
        "chapter": "9",
        "slug": "bai-12-truc-quan-hoa-co-ban",
        "title": "Trực quan hóa dữ liệu và đọc biểu đồ",
        "prerequisites": ["dataframe", "thong-ke-mo-ta"],
    },
    {
        "chapter": "10",
        "slug": "bai-10-tong-hop-theo-nhom",
        "title": "Tổng hợp dữ liệu và phép toán theo nhóm",
        "prerequisites": ["dataframe", "gia-tri-thieu"],
    },
]

FORBIDDEN_PROSE_PHRASES = [
    "Khoan đã",
    "À không",
    "Ý tôi là",
    "Thử lại nào",
    "Nhầm rồi",
    "Sinh viên rất hay nhầm",
    "Lỗi phổ biến nhất của sinh viên",
    "Đa số sinh viên đều mắc bẫy",
    "Bẫy thi cử cực kỳ phổ biến",
]


def parse_frontmatter(md_content: str):
    """Parses simple YAML frontmatter from markdown content."""
    if not md_content.startswith("---"):
        return {}, md_content
    parts = md_content.split("---", 2)
    if len(parts) < 3:
        return {}, md_content
    fm_raw = parts[1].strip()
    body = parts[2].strip()

    fm = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            # Basic json array parsing if applicable
            if val.startswith("[") and val.endswith("]"):
                try:
                    val = json.loads(val)
                except Exception:
                    pass
            elif val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[key] = val
    return fm, body


def verify_markdown_rules(slug: str, md_path: Path):
    """Verifies pedagogical, math, and typography rules in markdown."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    lines = content.splitlines()

    # 1. Check length
    if len(lines) < 200:
        errors.append(f"Markdown is too short ({len(lines)} lines < 200).")

    # 2. Check frontmatter
    fm, body = parse_frontmatter(content)
    expected = next(item for item in GROUP_B_SLUGS if item["slug"] == slug)
    if fm.get("lecture") != slug:
        errors.append(f"Frontmatter lecture mismatch: '{fm.get('lecture')}' != '{slug}'")
    if fm.get("title") != expected["title"]:
        errors.append(f"Frontmatter title mismatch: '{fm.get('title')}' != '{expected['title']}'")
    if fm.get("prerequisites") != expected["prerequisites"]:
        errors.append(f"Frontmatter prerequisites mismatch: '{fm.get('prerequisites')}' != '{expected['prerequisites']}'")
    if fm.get("lessonStatus") != "ready":
        errors.append(f"Frontmatter lessonStatus is not 'ready': '{fm.get('lessonStatus')}'")

    # 3. Check forbidden phrases
    for phrase in FORBIDDEN_PROSE_PHRASES:
        if phrase in body:
            errors.append(f"Found forbidden thinking-aloud / speculative error phrase: '{phrase}'")

    # 4. Check references section & CC BY-NC-SA 4.0
    if "## Tài liệu tham khảo" not in body:
        errors.append("Missing required ending section '## Tài liệu tham khảo'")
    if "CC BY-NC-SA 4.0" not in body and "Creative Commons" not in body:
        errors.append("Missing required CC BY-NC-SA 4.0 attribution in references section")

    # 5. Check math formatting and forbidden LaTeX commands
    in_code_block = False
    in_display_math = False
    in_frontmatter = content.startswith("---")
    frontmatter_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if in_frontmatter:
            if stripped == "---":
                frontmatter_count += 1
                if frontmatter_count >= 2:
                    in_frontmatter = False
            continue

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Display math delimiters check
        if stripped == "$$":
            in_display_math = not in_display_math
            continue
        elif "$$" in stripped:
            errors.append(f"Line {idx}: Display math delimiter $$ is not on its own line: '{line}'")

        if in_display_math:
            # Check forbidden vert commands
            if r"\vert" in stripped or r"\Vert" in stripped:
                errors.append(f"Line {idx}: Forbidden \\vert or \\Vert in math block: '{line}'")
        else:
            # Check inline math
            inline_math_matches = re.findall(r"\$([^\$]+)\$", line)
            for m in inline_math_matches:
                if len(m) > 75:  # Approx 38ex threshold in text characters
                    errors.append(f"Line {idx}: Inline math expression too long ({len(m)} chars > 75): '${m}$'")
                if r"\vert" in m or r"\Vert" in m:
                    errors.append(f"Line {idx}: Forbidden \\vert or \\Vert in inline math: '${m}$'")

            # Check capitalization after colon in prose
            # Exclude lines starting with ::: (admonitions), html tags, tables (|), or comments
            if not stripped.startswith(":::") and not stripped.startswith("<") and not stripped.startswith("|"):
                # Find all occurrences of ": "
                for match in re.finditer(r":\s+", line):
                    after = line[match.end():]
                    # Skip markdown formatting like **, *, [, `, "
                    after_clean = re.sub(r"^[\*\_\[\`\"\'\(]+", "", after)
                    if after_clean:
                        first_char = after_clean[0]
                        if first_char.isalpha() and first_char.islower():
                            errors.append(f"Line {idx}: Lowercase letter '{first_char}' found immediately after colon: '{line.strip()}'")

            # Check for em-dashes (—) in prose
            if "—" in stripped and not stripped.startswith("<!--") and not stripped.startswith("```"):
                clean_line = re.sub(r"`[^`]+`", "", line)
                if "—" in clean_line:
                    errors.append(f"Line {idx}: Long em-dash '—' found in prose; use commas, parentheses, colons or natural connectives.")

    return errors


def verify_js_modules(slug: str):
    """Verifies that lesson.mjs and slides.mjs exist, pass node check, and have valid schema."""
    errors = []
    expected = next(item for item in GROUP_B_SLUGS if item["slug"] == slug)
    base_dir = REPO_ROOT / "src" / "content" / "courses" / "xu-ly-du-lieu" / "lectures" / slug

    lesson_file = base_dir / "lesson.mjs"
    slides_file = base_dir / "slides.mjs"

    if not lesson_file.exists():
        return [f"Missing {lesson_file}"]
    if not slides_file.exists():
        return [f"Missing {slides_file}"]

    # Run node --check
    for f in [lesson_file, slides_file]:
        res = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True)
        if res.returncode != 0:
            errors.append(f"Node syntax check failed for {f.name}: {res.stderr}")

    # Inspect content via node eval through stdin to avoid shell escaping issues on Windows
    eval_script = f"""import {{ lesson }} from '{lesson_file.resolve().as_uri()}';
import {{ slides }} from '{slides_file.resolve().as_uri()}';
console.log(JSON.stringify({{ lesson, slides }}));
"""
    res = subprocess.run(
        ["node", "--input-type=module"],
        input=eval_script,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    if res.returncode != 0:
        errors.append(f"Failed to evaluate modules for {slug}: {res.stderr}")
    else:
        try:
            data = json.loads(res.stdout)
            lesson = data.get("lesson", {})
            slides = data.get("slides", [])

            if lesson.get("slug") != slug:
                errors.append(f"lesson.slug mismatch: {lesson.get('slug')} != {slug}")
            if lesson.get("title") != expected["title"]:
                errors.append(f"lesson.title mismatch: {lesson.get('title')} != {expected['title']}")
            if lesson.get("prerequisites") != expected["prerequisites"]:
                errors.append(f"lesson.prerequisites mismatch: {lesson.get('prerequisites')} != {expected['prerequisites']}")
            if lesson.get("status") != "ready":
                errors.append(f"lesson.status is not ready: {lesson.get('status')}")

            if not (4 <= len(slides) <= 6):
                errors.append(f"slides count must be between 4 and 6, got {len(slides)}")

            for i, slide in enumerate(slides):
                if not slide.get("title"):
                    errors.append(f"Slide {i} missing title")
                if not slide.get("bullets") or len(slide.get("bullets")) < 2:
                    errors.append(f"Slide {i} bullets must have at least 2 items")
                if slide.get("note") != slug:
                    errors.append(f"Slide {i} note must match slug '{slug}', got '{slide.get('note')}'")
        except Exception as e:
            errors.append(f"Error parsing module evaluation output: {e}\nRaw output: {res.stdout}")

    return errors


def execute_python_code_blocks(slug: str, md_path: Path):
    """Extracts and executes all Python code blocks from markdown in a clean context and temporary directory."""
    import textwrap
    import tempfile
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    code_blocks = re.findall(r"```python\n(.*?)```", content, re.DOTALL)
    print(f"[{slug}] Found {len(code_blocks)} Python code blocks to execute.")

    # Execute all code blocks collectively in a shared namespace per lesson
    # so earlier setup/imports carry over naturally to later examples and exercises.
    namespace = {}
    errors = []

    orig_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.chdir(tmp_dir)
        try:
            for idx, block in enumerate(code_blocks, start=1):
                try:
                    # Dedent block in case it was inside a list item
                    dedented_block = textwrap.dedent(block)
                    compiled = compile(dedented_block, f"{slug}_block_{idx}.py", "exec")
                    exec(compiled, namespace)
                except Exception as e:
                    tb = traceback.format_exc()
                    errors.append(f"Code block #{idx} execution failed:\n{block}\nError: {e}\nTraceback:\n{tb}")
        finally:
            os.chdir(orig_cwd)
            try:
                import matplotlib.pyplot as plt
                plt.close("all")
            except Exception:
                pass

    return errors


def main():
    print("=" * 70)
    print("VERIFICATION SUITE: GROUP B (Chapters 6-10) - Course xu-ly-du-lieu")
    print("=" * 70)

    all_passed = True
    total_blocks_executed = 0

    for item in GROUP_B_SLUGS:
        slug = item["slug"]
        md_path = REPO_ROOT / "docs" / "xu-ly-du-lieu" / "bai-giang" / f"{slug}.md"
        print(f"\n--- Verifying Chapter {item['chapter']}: {slug} ---")

        if not md_path.exists():
            print(f"[FAIL] Markdown note does not exist: {md_path}")
            all_passed = False
            continue

        # 1. Verify markdown rules
        md_errors = verify_markdown_rules(slug, md_path)
        if md_errors:
            print(f"[FAIL] Markdown rules violations in {slug}:")
            for err in md_errors:
                print(f"  - {err}")
            all_passed = False
        else:
            print(f"[PASS] Markdown formatting and pedagogical rules verified.")

        # 2. Verify JS modules
        js_errors = verify_js_modules(slug)
        if js_errors:
            print(f"[FAIL] JS module issues in {slug}:")
            for err in js_errors:
                print(f"  - {err}")
            all_passed = False
        else:
            print(f"[PASS] lesson.mjs and slides.mjs syntax and schema verified.")

        # 3. Execute python code blocks
        code_errors = execute_python_code_blocks(slug, md_path)
        if code_errors:
            print(f"[FAIL] Python code block execution errors in {slug}:")
            for err in code_errors:
                print(f"  - {err}")
            all_passed = False
        else:
            print(f"[PASS] All Python code blocks executed cleanly with passing assertions.")

    print("\n" + "=" * 70)
    if all_passed:
        print("[SUCCESS] ALL GROUP B VERIFICATIONS PASSED!")
        print("=" * 70)
        sys.exit(0)
    else:
        print("[FAILED] SOME VERIFICATIONS FAILED. Please review the errors above.")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()
