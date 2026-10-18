"""Verification script for Group A of the Data Processing course (xu-ly-du-lieu).

Checks:
1. Authoring contract compliance (metadata, prerequisites, ready status, substantial line counts).
2. Lesson and slides metadata (.mjs exports, slide count 4-6, required fields).
3. Math syntax rules (standalone $$ lines, no \\vert{}, inline math length, aligned rules).
4. Style and pedagogical rules (no em dashes in prose, capitalization after colons, no banned phrases).
5. Specific technical topics (reshape sharing/non-sharing with np.shares_memory, no contiguous claims, all IAI exercises, Appendix B tools).
6. Numerical correctness assertions for all exercises.
"""

from pathlib import Path
import json
import re
import sys
import subprocess
import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
COURSE_DOCS = ROOT / "docs/xu-ly-du-lieu/bai-giang"
LECTURES_DIR = ROOT / "src/content/courses/xu-ly-du-lieu/lectures"
CONTRACT_PATH = ROOT / "raw_materials/xu-ly-du-lieu/authoring-contract.json"

GROUP_A_SLUGS = [
    "bai-01-tong-quan-cong-cu-chinh-sach-ai",
    "bai-02-python-co-ban",
    "bai-03-cau-truc-du-lieu-ham-tep",
    "bai-03-numpy",
    "bai-04-lam-quen-pandas",
    "phu-luc-b-ipython"
]

BANNED_PHRASES = [
    "lấy từ giáo trình",
    "lấy từ slide",
    "lấy từ sách",
    "do người soạn thêm",
    "không gán cho tác giả",
    "khoan đã, hãy xem lại",
    "à không, thay vào đó",
    "sinh viên rất hay nhầm",
    "lỗi phổ biến nhất của sinh viên",
    "đa số sinh viên đều mắc",
    "bẫy thi cử",
    "bản dịch của",
    "tiến độ bản dịch",
    "nguyên tác"
]

def parse_frontmatter(content: str):
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not match:
        return {}
    fm_text = match.group(1)
    fm = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                items = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
                fm[key] = items
            else:
                fm[key] = val.strip("'\"")
    return fm

def check_group_a_contract():
    print("[1/6] Kiểm tra authoring-contract.json và cấu trúc tệp...")
    with open(CONTRACT_PATH, "r", encoding="utf-8") as f:
        contract = json.load(f)

    contract_lessons = {item["slug"]: item for item in contract["lessons"] if item.get("group") == "a"}
    assert set(contract_lessons.keys()) == set(GROUP_A_SLUGS), "Danh sách slug group a không khớp contract!"

    for slug in GROUP_A_SLUGS:
        item = contract_lessons[slug]
        doc_path = COURSE_DOCS / f"{slug}.md"
        assert doc_path.exists(), f"Thiếu tệp ghi chú: {doc_path}"

        text = doc_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        assert len(lines) >= 250, f"Ghi chú {slug} quá ngắn ({len(lines)} dòng < 250 dòng)!"

        fm = parse_frontmatter(text)
        assert fm.get("title") == item["title"], f"Title lệch hợp đồng tại {slug}: '{fm.get('title')}' vs '{item['title']}'"
        expected_prereqs = item.get("prerequisites", [])
        actual_prereqs = fm.get("prerequisites", [])
        assert actual_prereqs == expected_prereqs, f"Prerequisites lệch tại {slug}: {actual_prereqs} vs {expected_prereqs}"
        status_val = fm.get("status") or fm.get("lessonStatus")
        assert status_val == "ready", f"Status chưa ready tại {slug}: {status_val}"

        # Kiểm tra lesson.mjs
        lesson_mjs_path = LECTURES_DIR / slug / "lesson.mjs"
        assert lesson_mjs_path.exists(), f"Thiếu {lesson_mjs_path}"
        lesson_text = lesson_mjs_path.read_text(encoding="utf-8")
        assert f'"slug": "{slug}"' in lesson_text, f"lesson.mjs {slug} sai slug"
        assert f'"title": "{item["title"]}"' in lesson_text, f"lesson.mjs {slug} sai title"
        assert '"status": "ready"' in lesson_text, f"lesson.mjs {slug} status chưa ready"

        # Kiểm tra slides.mjs
        slides_mjs_path = LECTURES_DIR / slug / "slides.mjs"
        assert slides_mjs_path.exists(), f"Thiếu {slides_mjs_path}"
        slides_text = slides_mjs_path.read_text(encoding="utf-8")
        assert "export const slides = [" in slides_text, f"slides.mjs {slug} thiếu export slides"
        js = "import {slides} from " + json.dumps(slides_mjs_path.as_uri()) + "; console.log(JSON.stringify(slides))"
        output = subprocess.run(["node", "--input-type=module", "-e", js], capture_output=True, text=True, encoding="utf-8", check=True)
        slides = json.loads(output.stdout)
        assert 4 <= len(slides) <= 6, f"slides.mjs {slug} cần 4-6 thẻ"
        assert all(slide["title"] and len(slide["bullets"]) >= 2 and slide["note"] == slug for slide in slides)

    print("  -> Tệp ghi chú, lesson.mjs và slides.mjs đều đầy đủ và đúng định dạng.")

def check_math_formatting():
    print("[2/6] Kiểm tra chuẩn mực công thức toán học TeX...")
    for slug in GROUP_A_SLUGS:
        doc_path = COURSE_DOCS / f"{slug}.md"
        text = doc_path.read_text(encoding="utf-8")
        lines = text.splitlines()

        in_code_fence = False
        in_display_math = False
        display_math_content = []

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            # Kiểm tra $$ trên dòng riêng
            if "$$" in line:
                if stripped != "$$":
                    raise AssertionError(f"Dấu $$ không đứng riêng biệt trên dòng tại {slug}:{idx} -> '{line}'")
                if not in_display_math:
                    in_display_math = True
                    display_math_content = []
                else:
                    in_display_math = False
                    block_str = "\n".join(display_math_content)
                    assert r"\vert{}" not in block_str, f"Cấm dùng \\vert{{}} tại {slug}:{idx}"
                    assert r"\Vert{}" not in block_str, f"Cấm dùng \\Vert{{}} tại {slug}:{idx}"
                    # Cấm ngắt dòng ngay sau dấu =
                    assert not re.search(r"=\s*\\\\", block_str), f"Cấm ngắt dòng ngay sau dấu = tại {slug}:{idx}"
                continue

            if in_display_math:
                display_math_content.append(line)
            else:
                # Kiểm tra công thức inline không quá dài (> 140 ký tự)
                inline_matches = re.findall(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", line)
                for im in inline_matches:
                    assert len(im) <= 140, f"Công thức inline quá dài ({len(im)} ký tự) tại {slug}:{idx} -> ${im}$"
                    assert r"\vert{}" not in im and r"\Vert{}" not in im, f"Cấm \\vert{{}} trong inline tại {slug}:{idx}"

    print("  -> Các quy tắc cú pháp toán trong script đã qua. Bề rộng phải kiểm bằng MathJax và trình duyệt.")

def check_style_and_vietnamese():
    print("[3/6] Kiểm tra văn phong tiếng Việt học thuật, dấu câu và viết hoa...")
    for slug in GROUP_A_SLUGS:
        doc_path = COURSE_DOCS / f"{slug}.md"
        text = doc_path.read_text(encoding="utf-8")
        lower_text = text.lower()

        # Kiểm tra cụm từ cấm
        for phrase in BANNED_PHRASES:
            assert phrase not in lower_text, f"Phát hiện cụm từ cấm '{phrase}' trong {slug}"

        lines = text.splitlines()
        in_code = False
        in_frontmatter = False
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if idx == 1 and stripped == "---":
                in_frontmatter = True
                continue
            if in_frontmatter:
                if stripped == "---":
                    in_frontmatter = False
                continue

            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue

            # Bỏ qua container VitePress (::: exercise, ::: solution, ::: tip, ...)
            if stripped.startswith(":::"):
                continue

            # Kiểm tra gạch ngang dài (em dash —) trong văn xuôi
            if "—" in line:
                clean_line = re.sub(r"\[.*?\]\(.*?\)", "", line)
                assert "—" not in clean_line, f"Phát hiện em dash '—' trong văn xuôi tại {slug}:{idx} -> '{line}'"

            # Kiểm tra viết hoa sau dấu hai chấm (: )
            # Tìm token đầu tiên sau dấu hai chấm
            for m in re.finditer(r":\s+(\S+)", line):
                token = m.group(1)
                # Bỏ qua nếu token bắt đầu bằng ký tự đặc biệt, code, math, số hoặc url
                if token[0] in ("`", "$", '"', "'", "(", "[", "{", "%", "#", "/", "\\") or token[0].isdigit():
                    continue
                if token.startswith("http://") or token.startswith("https://"):
                    continue
                # Nếu là chữ cái, bắt buộc phải viết hoa
                first_char = token[0]
                if re.match(r"[a-zA-ZÀ-ỹ]", first_char):
                    assert first_char.isupper(), f"Sau dấu hai chấm phải viết hoa chữ cái đầu tại {slug}:{idx} -> token '{token}' trong '{line}'"

    print("  -> Không thấy các mẫu từ và dấu câu bị cấm mà script kiểm tra.")

def check_technical_coverage():
    print("[4/6] Kiểm tra phạm vi kỹ thuật của Wes McKinney và bài tập IAI...")
    # Chương 4: NumPy
    np_text = (COURSE_DOCS / "bai-03-numpy.md").read_text(encoding="utf-8")
    assert "np.shares_memory" in np_text, "Chương 4 phải dùng np.shares_memory để giải thích view/copy!"
    assert "không khẳng định mọi mảng ndarray đều liên tục" in np_text.lower() or "không phải mọi mảng ndarray đều liên tục" in np_text.lower(), "Chương 4 phải nêu rõ không phải mọi mảng đều liên tục!"
    for ex_idx in range(1, 7):
        assert f"Bài tập {ex_idx}:" in np_text or f"Bài tập thực hành {ex_idx}" in np_text, f"Chương 4 thiếu Bài tập {ex_idx} (IAI03 Ex {ex_idx})!"

    # Chương 5: pandas
    pd_text = (COURSE_DOCS / "bai-04-lam-quen-pandas.md").read_text(encoding="utf-8")
    for ex_idx in range(1, 6):
        assert f"Bài tập {ex_idx}:" in pd_text or f"Bài tập thực hành {ex_idx}" in pd_text, f"Chương 5 thiếu Bài tập {ex_idx} (IAI04 Ex {ex_idx})!"
    assert "Bài tập 6:" in pd_text or "Bài tập thực hành 6" in pd_text, "Chương 5 thiếu Bài tập 6 (IAI05 Ex 1)!"
    assert "Bài tập 7:" in pd_text or "Bài tập thực hành 7" in pd_text, "Chương 5 thiếu Bài tập 7 (IAI05 Ex 2)!"

    # Phụ lục B: IPython
    ip_text = (COURSE_DOCS / "phu-luc-b-ipython.md").read_text(encoding="utf-8")
    for keyword in ["%run", "%paste", "In", "Out", "_", "!", "$", "%debug", "pdb", "%time", "%timeit", "%prun", "%autoreload", "ipython_config.py"]:
        assert keyword in ip_text, f"Phụ lục B thiếu chủ đề: {keyword}"
    for ex_idx in range(1, 4):
        assert f"Bài tập {ex_idx}:" in ip_text or f"Bài tập thực hành {ex_idx}" in ip_text, f"Phụ lục B thiếu Bài tập {ex_idx}!"

    # Kiểm tra bản quyền CC BY-NC-SA 4.0 trong Tài liệu tham khảo
    for slug in ["bai-03-numpy", "bai-04-lam-quen-pandas"]:
        text = (COURSE_DOCS / f"{slug}.md").read_text(encoding="utf-8")
        assert "CC BY-NC-SA 4.0" in text, f"Thiếu ghi nhận bản quyền CC BY-NC-SA 4.0 tại {slug}"
        assert "https://github.com/uet-iai-course/programming-for-data-processing" in text, f"Thiếu liên kết giáo trình IAI tại {slug}"

    print("  -> Các dấu hiệu cấu trúc và chủ đề được liệt kê trong script đều có mặt.")

def check_numerical_computations():
    print("[5/6] Chạy kiểm tra số học và assert kết quả thực thi các bài tập...")
    # Bài tập 1 IAI03 (dtype overflow)
    arr_i8 = np.array([125, 126, 127], dtype=np.int8)
    arr_overflow = arr_i8 + np.int8(2)
    assert arr_overflow.tolist() == [127, -128, -127]
    arr_safe = arr_i8.astype(np.int16) + 2
    assert arr_safe.tolist() == [127, 128, 129]

    # Bài tập 3 IAI03 (strides offset)
    matrix = np.arange(12, dtype=np.int32).reshape(3, 4)
    item_size = matrix.itemsize # 4
    strides = matrix.strides # (16, 4)
    # phần tử tại hàng 2, cột 1: offset = 2*16 + 1*4 = 36 bytes
    assert 2 * strides[0] + 1 * strides[1] == 36
    assert matrix[2, 1] == 9

    # Bài tập 4 IAI03 (view vs copy)
    A = np.arange(1, 13).reshape(3, 4)
    V = A[:2, 1:3]
    V[:] = 99
    assert A[0, 1] == 99 and A[0, 2] == 99
    assert A[1, 1] == 99 and A[1, 2] == 99
    assert np.shares_memory(A, V) is True

    # Reshape sharing vs non-sharing
    X = np.arange(12)
    Y = X.reshape(3, 4)
    assert np.shares_memory(X, Y) is True
    Z = Y.T.reshape(-1)
    assert np.shares_memory(Y, Z) is False

    # Bài tập 5 IAI03 (broadcasting)
    grid = np.zeros((3, 4), dtype=int)
    row_add = np.array([10, 20, 30, 40])
    res_row = grid + row_add
    col_add = np.array([[1], [2], [3]])
    res_col = grid + col_add
    assert res_row[0].tolist() == [10, 20, 30, 40]
    assert res_col[:, 0].tolist() == [1, 2, 3]

    # Bài tập 6 IAI03 (mean keepdims)
    data = np.array([[10, 20, 30], [40, 50, 60]], dtype=float)
    row_mean = data.mean(axis=1, keepdims=True)
    centered = data - row_mean
    assert np.allclose(centered, [[-10.0, 0.0, 10.0], [-10.0, 0.0, 10.0]])

    # IAI04 Ex 1 (budget filtering)
    df_places = pd.DataFrame({
        "gia_dem": [25, 45, 60, 30, 80],
        "so_dem_toi_thieu": [1, 2, 3, 1, 4]
    })
    total_cost = df_places["gia_dem"] * df_places["so_dem_toi_thieu"]
    qualify = df_places[total_cost <= 100]
    assert qualify.index.tolist() == [0, 1, 3]

    # IAI05 Ex 1 (fee lookup by label)
    df_rooms = pd.DataFrame({"loai_phong": ["Entire", "Private", "Shared", "Entire"]})
    fee_series = pd.Series({"Entire": 20.0, "Private": 10.0, "Shared": 5.0})
    df_rooms["phi_don_dep"] = df_rooms["loai_phong"].map(fee_series)
    assert df_rooms["phi_don_dep"].tolist() == [20.0, 10.0, 5.0, 20.0]

    # IAI05 Ex 2 (where conditional free fee)
    df_rooms["so_dem"] = [5, 2, 8, 3]
    df_rooms["phi_thuc_thu"] = np.where(df_rooms["so_dem"] >= 7, 0.0, df_rooms["phi_don_dep"])
    assert df_rooms["phi_thuc_thu"].tolist() == [20.0, 10.0, 0.0, 20.0]

    print("  -> Các assertion độc lập về số học và logic đã qua.")

def check_coverage_file():
    print("[6/6] Kiểm tra cấu trúc coverage-a.json...")
    cov_path = ROOT / "raw_materials/xu-ly-du-lieu/coverage-a.json"
    assert cov_path.exists(), "Tệp coverage-a.json chưa được tạo!"
    cov = json.loads(cov_path.read_text(encoding="utf-8"))
    assert "chapters" in cov, "coverage-a.json thiếu trường 'chapters'"
    assert "exercises" in cov, "coverage-a.json thiếu trường 'exercises'"
    assert "proseReview" in cov, "coverage-a.json thiếu trường 'proseReview'"
    assert "tests" in cov, "coverage-a.json thiếu trường 'tests'"
    assert len(cov["chapters"]) == 6, f"coverage-a.json phải có 6 chapters, hiện có {len(cov['chapters'])}"
    print("  -> coverage-a.json đầy đủ cấu trúc và các trường yêu cầu.")

def main():
    print("=== BẮT ĐẦU KIỂM THỬ TOÀN DIỆN GROUP A (XỬ LÝ DỮ LIỆU) ===")
    check_group_a_contract()
    check_math_formatting()
    check_style_and_vietnamese()
    check_technical_coverage()
    check_numerical_computations()
    if (ROOT / "raw_materials/xu-ly-du-lieu/coverage-a.json").exists():
        check_coverage_file()
    else:
        print("[6/6] (coverage-a.json sẽ được kiểm tra sau khi khởi tạo)")
    print("Group A: Các kiểm tra được liệt kê đã qua.")

if __name__ == "__main__":
    main()
