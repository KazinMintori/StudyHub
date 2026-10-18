#!/usr/bin/env python3
"""
scripts/verify-data-lab-03.py
Bộ kiểm thử và kiểm định toàn diện cho Lab 03: NumPy và Tư Duy Vector Hóa.

Phạm vi kiểm tra:
1. Xác minh sự tồn tại và tính hợp lệ của các file sở hữu:
   - raw_materials/xu-ly-du-lieu/labs/lab-03.md
   - raw_materials/xu-ly-du-lieu/labs/coverage-03.json
2. Kiểm tra quy chuẩn Markdown và sư phạm trong lab-03.md:
   - Đủ 8 mã bài tập: data-lab-03-01 đến data-lab-03-08
   - Cặp khối ::: exercise và ::: solution hoàn chỉnh
   - Không chứa dấu gạch ngang dài (em dash '—' hoặc '--') trong văn xuôi
   - Không chứa dấu chấm phẩy (';') trong văn xuôi
   - Quy tắc viết hoa sau dấu hai chấm (':')
   - Không chứa các từ ngữ cảm tính hoặc cụm từ bị cấm
   - Khối công thức hiển thị $$ đứng trên dòng riêng, không chứa \\vert hay \\Vert
   - Bảng kết quả đúng chuẩn Markdown/HTML
3. Kiểm tra tính bao phủ trong coverage-03.json:
   - Bao phủ đầy đủ 40 cell của course/2627-1/notebooks/lab-03.ipynb
   - Bao phủ đầy đủ 45 cell của template/lab-03.ipynb
4. Thực thi và kiểm định kết quả số học của mọi hàm và lời giải:
   - Bài 1 (data-lab-03-01): Cấu trúc mảng, strides, byte offset, chuyển int32
   - Bài 2 (data-lab-03-02): Lát cắt bước nhảy, view chia sẻ bộ nhớ, offset
   - Bài 3 (data-lab-03-03): Đột biến trên View vs Fancy Indexing, copy an toàn
   - Bài 4 (data-lab-03-04): Boolean mask, fancy indexing tọa độ, np.ix_
   - Bài 5 (data-lab-03-05): Broadcasting cộng vector theo hàng và cột
   - Bài 6 (data-lab-03-06): Chuẩn hóa theo hàng, sửa lỗi trục axis, keepdims
   - Bài 7 (data-lab-03-07): Benchmark lặp Python vs NumPy vector hóa
   - Bài 8 (data-lab-03-08): Thống kê mô tả (mean, median, std, share) và lấy mẫu ngẫu nhiên
"""

import os
import re
import sys
import json
import traceback
from pathlib import Path

# Cấu hình UTF-8 cho stdout và stderr
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
LAB_MD_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "lab-03.md"
COVERAGE_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "coverage-03.json"

EXPECTED_EXERCISES = [
    "data-lab-03-01",
    "data-lab-03-02",
    "data-lab-03-03",
    "data-lab-03-04",
    "data-lab-03-05",
    "data-lab-03-06",
    "data-lab-03-07",
    "data-lab-03-08",
]

FORBIDDEN_WORDS = [
    "kỳ diệu",
    "vô cùng",
    "cực kỳ",
    "then chốt",
    "bẫy thi cử",
    "sinh viên rất hay nhầm",
    "hợp đồng",
    "Khoan đã",
    "À không",
    "Ý tôi là",
    "Nhầm rồi",
]


def test_file_existence():
    """Kiểm tra sự tồn tại của các tệp thuộc phạm vi lab-03."""
    print("--- [1] Kiểm tra sự tồn tại của các tệp sở hữu ---")
    assert LAB_MD_PATH.exists(), f"Không tìm thấy tệp {LAB_MD_PATH}"
    assert COVERAGE_PATH.exists(), f"Không tìm thấy tệp {COVERAGE_PATH}"
    assert LAB_MD_PATH.stat().st_size > 1000, "Tệp lab-03.md quá ngắn hoặc rỗng."
    assert COVERAGE_PATH.stat().st_size > 500, "Tệp coverage-03.json quá ngắn hoặc rỗng."
    print("  ✓ Tệp lab-03.md và coverage-03.json tồn tại và có nội dung đầy đủ.")


def test_markdown_pedagogical_rules():
    """Kiểm tra các quy chuẩn văn phong, định dạng và sư phạm trong Markdown."""
    print("--- [2] Kiểm tra quy chuẩn Markdown và văn phong tiếng Việt ---")
    with open(LAB_MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Kiểm tra đủ 8 exercise IDs
    for ex_id in EXPECTED_EXERCISES:
        assert f'id="{ex_id}"' in content, f"Thiếu mã bài tập {ex_id} trong lab-03.md"
    print(f"  ✓ Đã tìm thấy đầy đủ 8 mã bài tập: {', '.join(EXPECTED_EXERCISES)}")

    # 2. Kiểm tra container exercise và solution
    exercise_opens = len(re.findall(r"^::: exercise", content, re.MULTILINE))
    solution_opens = len(re.findall(r"^::: solution", content, re.MULTILINE))
    container_closes = len(re.findall(r"^:::\s*$", content, re.MULTILINE))
    assert exercise_opens == 8, f"Số lượng '::: exercise' là {exercise_opens}, kỳ vọng 8"
    assert solution_opens == 8, f"Số lượng '::: solution' là {solution_opens}, kỳ vọng 8"
    assert container_closes == 16, f"Số lượng ':::' đóng là {container_closes}, kỳ vọng 16"
    print("  ✓ Cấu trúc 8 khối ::: exercise và 8 khối ::: solution khớp hoàn hảo.")

    # 3. Phân tách dòng code fence và văn xuôi để kiểm tra quy chuẩn
    lines = content.splitlines()
    in_code_block = False
    in_table = False

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Kiểm tra không có thẻ H1 (# ) bên ngoài code fences
        if stripped.startswith("# "):
            raise AssertionError(f"Dòng {idx}: Tiêu đề H1 không được phép xuất hiện, bắt buộc dùng từ H2 trở xuống:\n{line}")

        # Kiểm tra toàn bộ khối công thức display $$ phải nằm trên một dòng riêng biệt
        if "$$" in line and stripped != "$$":
            raise AssertionError(f"Dòng {idx}: Ký hiệu $$ phải nằm trên một dòng riêng biệt, không dính liền nội dung:\n{line}")

        # Kiểm tra bảng markdown
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            continue
        else:
            in_table = False

        # Bỏ qua dòng trống, tiêu đề bảng hoặc dòng phân cách, container :::
        if not stripped or stripped.startswith("#") or stripped.startswith(">") or stripped.startswith(":::"):
            continue

        # Kiểm tra em dash trong văn xuôi (không cho phép '—' hoặc '--' trong văn xuôi)
        # Chỉ trừ trường hợp tên en-dash tác giả hoặc khoảng số (ví dụ: 357–362)
        if "—" in line:
            raise AssertionError(f"Dòng {idx} chứa dấu gạch ngang dài em dash ('—'):\n{line}")
        if "--" in line and not stripped.startswith("---"):
            raise AssertionError(f"Dòng {idx} chứa dấu '--' trong văn xuôi:\n{line}")

        # Kiểm tra dấu chấm phẩy ';' trong văn xuôi
        if ";" in line:
            raise AssertionError(f"Dòng {idx} chứa dấu chấm phẩy (';') trong văn xuôi:\n{line}")

        # Kiểm tra từ cấm
        for word in FORBIDDEN_WORDS:
            pattern = r"(?<!\w)" + re.escape(word) + r"(?!\w)"
            if re.search(pattern, line, re.IGNORECASE):
                raise AssertionError(f"Dòng {idx} chứa cụm từ không chuẩn mực ('{word}'):\n{line}")

        # Kiểm tra viết hoa sau dấu hai chấm (':')
        # Bỏ qua URL (http:), math, hoặc code
        if ":" in line and not in_table:
            matches = re.finditer(r":\s+(\S)", line)
            for m in matches:
                char = m.group(1)
                # Bỏ qua nếu nằm trong URL, đường dẫn, thẻ HTML, hoặc công thức toán
                prefix = line[:m.start()]
                if any(x in prefix for x in ["http", "https", "<span", "$", "`"]):
                    continue
                if char.islower():
                    raise AssertionError(
                        f"Dòng {idx} vi phạm quy tắc viết hoa sau dấu hai chấm (ký tự '{char}' viết thường):\n{line}"
                    )

        # Kiểm tra TeX trong heading
        if stripped.startswith("#") and "$" in stripped:
            raise AssertionError(f"Dòng {idx}: Tiêu đề không được chứa công thức TeX ($):\n{line}")

    print("  ✓ Cấu trúc Markdown chuẩn mực: Không H1 ngoài code fence, $$ đứng riêng dòng, không em-dash, không dấu ';', viết hoa sau ':'.")


def test_markdown_code_execution():
    """Thực thi độc lập toàn bộ các khối mã Python thực tế trong lab-03.md."""
    print("--- [3] Thực thi toàn bộ các khối mã Python trong lab-03.md ---")
    from contextlib import redirect_stdout, redirect_stderr
    from io import StringIO
    from tempfile import TemporaryDirectory
    import ast

    with open(LAB_MD_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", text, flags=re.M | re.S)
    assert len(blocks) >= 18, f"Kỳ vọng tối thiểu 18 khối mã Python, tìm thấy {len(blocks)}"

    namespace = {"__name__": "__lesson__", "display": lambda *objects, **kwargs: None}
    previous_cwd = Path.cwd()
    with TemporaryDirectory(prefix="studyhub-lab-03-verify-") as temporary:
        try:
            os.chdir(temporary)
            for index, code in enumerate(blocks, 1):
                tree = ast.parse(code, filename=f"lab-03.md:block-{index}")
                output, errors = StringIO(), StringIO()
                with redirect_stdout(output), redirect_stderr(errors):
                    exec(compile(tree, f"lab-03.md:block-{index}", "exec"), namespace)
            if "plt" in namespace:
                namespace["plt"].close("all")
        finally:
            os.chdir(previous_cwd)

    print(f"  ✓ Đã thực thi thành công 100% {len(blocks)} khối mã Python từ đầu đến cuối không lỗi.")


def test_coverage_mapping():
    """Kiểm tra tính bao phủ và toàn vẹn của tệp coverage-03.json."""
    print("--- [3] Kiểm tra độ phủ tế bào notebook trong coverage-03.json ---")
    with open(COVERAGE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["lab"] == "lab-03"
    assert data["total_exercises"] == 8
    assert set(data["exercise_ids"]) == set(EXPECTED_EXERCISES)

    cells_map = data["cells"]
    course_key = "course/2627-1/notebooks/lab-03.ipynb"
    template_key = "template/lab-03.ipynb"

    assert course_key in cells_map, f"Thiếu nguồn {course_key}"
    assert template_key in cells_map, f"Thiếu nguồn {template_key}"

    course_cells = cells_map[course_key]
    template_cells = cells_map[template_key]

    assert len(course_cells) == 40, f"Nguồn course có 40 cell, tìm thấy {len(course_cells)}"
    assert len(template_cells) == 45, f"Nguồn template có 45 cell, tìm thấy {len(template_cells)}"

    # Kiểm tra tính tuần tự của chỉ mục cell
    assert [c["cell_index"] for c in course_cells] == list(range(40))
    assert [c["cell_index"] for c in template_cells] == list(range(45))

    # Mọi cell đều có lý do hợp lệ
    for c in course_cells + template_cells:
        assert "reason" in c and len(c["reason"].strip()) > 5, f"Cell {c['cell_index']} thiếu lý do phân loại"
        assert c["status"] in ("mapped", "merged", "excluded", "preamble", "summary")

    print(f"  ✓ 100% bao phủ: 40/40 cell từ course và 45/45 cell từ template được đối chiếu.")


def test_exercise_solutions():
    """Kiểm định độc lập kết quả tính toán số học của từng bài tập."""
    print("--- [4] Kiểm định số học và thuật toán các bài tập ---")
    import numpy as np

    # Khởi tạo dữ liệu gốc
    A = np.array([
        [10, 12, 11],
        [20, 21, 24],
        [30, 33, 31],
        [40, 44, 42]
    ], dtype=np.int64)

    # ==========================================
    # BÀI 1: Cấu trúc mảng, strides và byte offset
    # ==========================================
    print("  * Kiểm thử Bài 1 (data-lab-03-01)...")
    # Cách 1
    assert A.shape == (4, 3)
    assert A.itemsize == 8
    assert A.nbytes == 96
    assert A.strides == (24, 8)
    offset_3_1 = 3 * A.strides[0] + 1 * A.strides[1]
    assert offset_3_1 == 80

    A32 = A.astype(np.int32)
    assert A32.dtype == np.dtype("int32")
    assert A32.nbytes == 48
    assert A32.strides == (12, 4)
    np.testing.assert_array_equal(A32, A)

    # Cách 2: array_layout
    def array_layout(matrix: np.ndarray, row: int, col: int) -> dict:
        if matrix.ndim != 2:
            raise ValueError("Yêu cầu ma trận đầu vào phải có đúng 2 chiều.")
        if not (0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]):
            raise IndexError(f"Chỉ số ({row}, {col}) vượt quá kích thước ma trận {matrix.shape}.")
        strides = matrix.strides
        offset = int(row * strides[0] + col * strides[1])
        return {
            "shape": matrix.shape,
            "itemsize": matrix.itemsize,
            "nbytes": matrix.nbytes,
            "strides": strides,
            "offset": offset,
            "int32_array": matrix.astype(np.int32)
        }

    res_q1 = array_layout(A, 3, 1)
    assert res_q1["shape"] == (4, 3)
    assert res_q1["itemsize"] == 8
    assert res_q1["nbytes"] == 96
    assert res_q1["strides"] == (24, 8)
    assert res_q1["offset"] == 80
    assert res_q1["int32_array"].dtype == np.int32
    assert res_q1["int32_array"].nbytes == 48
    np.testing.assert_array_equal(res_q1["int32_array"], A)

    # Trường hợp biên
    single = np.array([[7]], dtype=np.int64)
    res_single = array_layout(single, 0, 0)
    assert res_single["offset"] == 0 and res_single["nbytes"] == 8

    try:
        array_layout(A, 4, 0)
        assert False, "Cần báo lỗi IndexError khi chỉ số ngoài phạm vi"
    except IndexError:
        pass

    # ==========================================
    # BÀI 2: Lát cắt và view chia sẻ bộ nhớ
    # ==========================================
    print("  * Kiểm thử Bài 2 (data-lab-03-02)...")
    # Cách 1
    V = A[1::2, 0::2]
    np.testing.assert_array_equal(V, [[20, 24], [40, 42]])
    assert V.shape == (2, 2)
    assert V.strides == (48, 16)
    offset_v11 = (1 + 1 * 2) * A.strides[0] + (0 + 1 * 2) * A.strides[1]
    assert offset_v11 == 88
    assert np.shares_memory(A, V)

    # Cách 2: slice_view
    def slice_view(matrix: np.ndarray) -> dict:
        if matrix.ndim != 2:
            raise ValueError("Yêu cầu ma trận đầu vào phải có 2 chiều.")
        if matrix.shape[0] < 4 or matrix.shape[1] < 3:
            raise ValueError("Kích thước ma trận không đủ.")
        view = matrix[1::2, 0::2]
        orig_row = 1 + 1 * 2
        orig_col = 0 + 1 * 2
        offset_val = orig_row * matrix.strides[0] + orig_col * matrix.strides[1]
        return {
            "view": view,
            "shape": view.shape,
            "strides": view.strides,
            "offset_v11": offset_val,
            "shares_memory": bool(np.shares_memory(matrix, view))
        }

    res_q2 = slice_view(A)
    np.testing.assert_array_equal(res_q2["view"], [[20, 24], [40, 42]])
    assert res_q2["shape"] == (2, 2)
    assert res_q2["strides"] == (48, 16)
    assert res_q2["offset_v11"] == 88
    assert res_q2["shares_memory"] is True

    # ==========================================
    # BÀI 3: Phân biệt View và Bản sao độc lập
    # ==========================================
    print("  * Kiểm thử Bài 3 (data-lab-03-03)...")
    B = A.copy()
    V_test = B[:, 1:3]
    C_test = B[:, [1, 2]]

    # Sửa C không đổi B
    C_test[0, 0] = -9
    np.testing.assert_array_equal(B[0], [10, 12, 11])

    # Sửa V làm đổi B
    V_test[0, 0] = -1
    np.testing.assert_array_equal(B[0], [10, -1, 11])

    # Cách 2: copy_columns
    def copy_columns(matrix: np.ndarray) -> np.ndarray:
        if matrix.ndim != 2:
            raise ValueError("Yêu cầu ma trận 2 chiều.")
        if matrix.shape[1] < 3:
            raise ValueError("Ma trận cần có ít nhất 3 cột.")
        result = matrix[:, 1:3].copy()
        if np.shares_memory(result, matrix):
            raise RuntimeError("Lỗi chia sẻ bộ nhớ.")
        return result

    D = copy_columns(B)
    np.testing.assert_array_equal(D, B[:, 1:3])
    assert not np.shares_memory(D, B)
    D[0, 0] = 999
    # B không đổi khi D đổi
    np.testing.assert_array_equal(B[0], [10, -1, 11])
    # A ban đầu không bị tác động
    np.testing.assert_array_equal(A[0], [10, 12, 11])

    # ==========================================
    # BÀI 4: Chọn phần tử nâng cao
    # ==========================================
    print("  * Kiểm thử Bài 4 (data-lab-03-04)...")
    so_chan = A[A % 2 == 0]
    hai_o = A[[0, 2], [1, 2]]
    bon_o = A[np.ix_([0, 2], [1, 2])]

    np.testing.assert_array_equal(so_chan, [10, 12, 20, 24, 30, 40, 44, 42])
    assert so_chan.shape == (8,)
    np.testing.assert_array_equal(hai_o, [12, 31])
    assert hai_o.shape == (2,)
    np.testing.assert_array_equal(bon_o, [[12, 11], [33, 31]])
    assert bon_o.shape == (2, 2)

    for arr in [so_chan, hai_o, bon_o]:
        assert not np.shares_memory(A, arr)
        assert arr.dtype == A.dtype

    # Cách 2: select_elements
    def select_elements(matrix: np.ndarray) -> dict:
        if matrix.ndim != 2:
            raise ValueError("Yêu cầu ma trận 2 chiều.")
        if matrix.shape[0] < 3 or matrix.shape[1] < 3:
            raise ValueError("Ma trận cần tối thiểu 3x3.")
        rows = np.array([0, 2])[:, np.newaxis]
        cols = np.array([1, 2])[np.newaxis, :]
        return {
            "so_chan": matrix[matrix % 2 == 0],
            "hai_o": matrix[[0, 2], [1, 2]],
            "bon_o": matrix[rows, cols]
        }

    res_q4 = select_elements(A)
    np.testing.assert_array_equal(res_q4["so_chan"], so_chan)
    np.testing.assert_array_equal(res_q4["hai_o"], hai_o)
    np.testing.assert_array_equal(res_q4["bon_o"], bon_o)

    # Biên: Ma trận toàn số lẻ
    odd_mat = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])
    res_odd = select_elements(odd_mat)
    assert res_odd["so_chan"].size == 0
    assert res_odd["so_chan"].shape == (0,)

    # ==========================================
    # BÀI 5: Broadcasting cộng theo hàng và cột
    # ==========================================
    print("  * Kiểm thử Bài 5 (data-lab-03-05)...")
    b = np.array([1, 2, 3])
    d = np.array([10, 20, 30, 40])
    K = A + b + d[:, np.newaxis]
    expected_K = np.array([
        [21, 24, 24],
        [41, 43, 47],
        [61, 65, 64],
        [81, 86, 85]
    ])
    np.testing.assert_array_equal(K, expected_K)
    np.testing.assert_array_equal(A[1], [20, 21, 24])  # A không đổi

    # Cách 2: broadcast_add
    def broadcast_add(matrix: np.ndarray, column_add: np.ndarray, row_add: np.ndarray) -> np.ndarray:
        if matrix.ndim != 2:
            raise ValueError("Yêu cầu ma trận 2 chiều.")
        nrows, ncols = matrix.shape
        col_vec = np.asarray(column_add)
        row_vec = np.asarray(row_add)
        if col_vec.ndim != 1 or col_vec.size != ncols:
            raise ValueError("Độ dài column_add không khớp số cột.")
        if row_vec.ndim != 1 or row_vec.size != nrows:
            raise ValueError("Độ dài row_add không khớp số hàng.")
        return matrix + col_vec + row_vec[:, np.newaxis]

    res_k = broadcast_add(A, b, d)
    np.testing.assert_array_equal(res_k, expected_K)

    # Biên: Ma trận số thực 2x4
    mat_real = np.zeros((2, 4), dtype=np.float64)
    res_real = broadcast_add(mat_real, np.array([1, 2, 3, 4]), np.array([10, 20]))
    np.testing.assert_array_equal(res_real, [[11, 12, 13, 14], [21, 22, 23, 24]])

    # ==========================================
    # BÀI 6: Chuẩn hóa theo hàng (Row Centering)
    # ==========================================
    print("  * Kiểm thử Bài 6 (data-lab-03-06)...")
    gia = np.array([
        [40, 50, 60],
        [60, 60, 60],
        [30, 60, 90]
    ], dtype=np.float64)

    trung_binh_hang = gia.mean(axis=1, keepdims=True)
    chenh_lech = gia - trung_binh_hang
    assert trung_binh_hang.shape == (3, 1)
    np.testing.assert_allclose(trung_binh_hang, [[50.0], [60.0], [60.0]])
    expected_deviations = np.array([
        [-10.0, 0.0, 10.0],
        [0.0, 0.0, 0.0],
        [-30.0, 0.0, 30.0]
    ])
    np.testing.assert_allclose(chenh_lech, expected_deviations)
    np.testing.assert_allclose(chenh_lech.mean(axis=1), 0.0, atol=1e-12)

    # Cách 2: center_rows
    def center_rows(prices: np.ndarray) -> tuple:
        arr = np.asarray(prices, dtype=np.float64)
        if arr.ndim != 2 or arr.size == 0:
            raise ValueError("Yêu cầu ma trận 2 chiều không rỗng.")
        means = arr.mean(axis=1)[:, np.newaxis]
        deviations = arr - means
        return means, deviations

    m, dev = center_rows(gia)
    np.testing.assert_allclose(m, [[50.0], [60.0], [60.0]])
    np.testing.assert_allclose(dev, expected_deviations)

    # Biên: Ma trận chỉ có 1 cột
    one_col = np.array([[10.0], [25.0], [40.0]])
    m1, dev1 = center_rows(one_col)
    np.testing.assert_allclose(dev1, [[0.0], [0.0], [0.0]])

    # ==========================================
    # BÀI 7: Phân tích hiệu năng vector hóa
    # ==========================================
    print("  * Kiểm thử Bài 7 (data-lab-03-07)...")
    def nhan_list(xs):
        return [v * 2 for v in xs]

    def nhan_for_array(x):
        return [v * 2 for v in x]

    def nhan_array(x):
        return x * 2

    # Kiểm tra tính tương đương số học trên quy mô nhỏ và lớn
    for n in (10, 1000):
        x = np.arange(n, dtype=np.int64)
        xs = x.tolist()
        np.testing.assert_array_equal(nhan_list(xs), nhan_array(x))
        np.testing.assert_array_equal(nhan_for_array(x), nhan_array(x))

    # Thực thi đo thời gian để xác nhận script chạy thật
    from timeit import repeat
    x_test = np.arange(100, dtype=np.int64)
    xs_test = x_test.tolist()
    t1 = min(repeat(lambda: nhan_list(xs_test), number=10, repeat=3))
    t2 = min(repeat(lambda: nhan_for_array(x_test), number=10, repeat=3))
    t3 = min(repeat(lambda: nhan_array(x_test), number=10, repeat=3))
    assert t1 > 0 and t2 > 0 and t3 > 0

    # ==========================================
    # BÀI 8: Thống kê mô tả và lấy mẫu ngẫu nhiên
    # ==========================================
    print("  * Kiểm thử Bài 8 (data-lab-03-08)...")
    gia_dem = np.array([40, 50, 60, 70, 380], dtype=np.float64)

    assert np.mean(gia_dem) == 120.0
    assert np.median(gia_dem) == 60.0
    np.testing.assert_allclose(np.std(gia_dem, ddof=0), np.sqrt(17000))
    assert np.mean(gia_dem <= 70.0) == 0.8

    rng = np.random.default_rng(42)
    indices = rng.choice(len(gia_dem), size=3, replace=False)
    np.testing.assert_array_equal(indices, [4, 0, 3])
    sample = gia_dem[indices]
    np.testing.assert_array_equal(sample, [380.0, 40.0, 70.0])
    np.testing.assert_allclose(np.mean(sample), 490.0 / 3)

    # Cách 2: price_statistics
    def price_statistics(prices: np.ndarray, threshold: float = 70.0, sample_size: int = 3, seed: int = 42) -> dict:
        arr = np.asarray(prices, dtype=np.float64)
        if arr.ndim != 1 or arr.size == 0:
            raise ValueError("Mảng 1 chiều không rỗng.")
        if not (1 <= sample_size <= arr.size):
            raise ValueError("Kích thước mẫu không hợp lệ.")
        mean_val = float(np.mean(arr))
        median_val = float(np.median(arr))
        std_val = float(np.std(arr, ddof=0))
        share_val = float(np.mean(arr <= threshold))
        rng_local = np.random.default_rng(seed)
        idx = rng_local.choice(len(arr), size=sample_size, replace=False)
        spl = arr[idx]
        return {
            "mean": mean_val,
            "median": median_val,
            "std": std_val,
            "share": share_val,
            "indices": idx,
            "sample": spl,
            "sample_mean": float(np.mean(spl))
        }

    res_q8 = price_statistics(gia_dem)
    assert res_q8["mean"] == 120.0
    assert res_q8["median"] == 60.0
    np.testing.assert_allclose(res_q8["std"], np.sqrt(17000))
    assert res_q8["share"] == 0.8
    np.testing.assert_array_equal(res_q8["indices"], [4, 0, 3])
    np.testing.assert_array_equal(res_q8["sample"], [380.0, 40.0, 70.0])
    np.testing.assert_allclose(res_q8["sample_mean"], 490.0 / 3)

    # Biên: Rút toàn bộ mẫu
    res_full = price_statistics(gia_dem, sample_size=5, seed=123)
    assert len(res_full["indices"]) == 5
    assert len(set(res_full["indices"])) == 5
    assert res_full["sample_mean"] == 120.0

    print("  ✓ Tất cả 8 bài tập đã vượt qua 100% các bài kiểm tra số học và trường hợp biên.")


def main():
    print("=" * 65)
    print("  StudyHub: Kiểm Tra Tự Động Toàn Diện Cho Lab 03 (NumPy)")
    print("=" * 65)
    try:
        test_file_existence()
        test_markdown_pedagogical_rules()
        test_coverage_mapping()
        test_exercise_solutions()
        print("=" * 65)
        print(">>> KẾT QUẢ: TẤT CẢ PHÉP KIỂM TRA ĐỀU ĐẠT CHUẨN 100% <<<")
        print("=" * 65)
        return 0
    except Exception as exc:
        print("\n" + "!" * 65)
        print("LỖI KIỂM ĐỊNH:")
        traceback.print_exc()
        print("!" * 65)
        return 1


if __name__ == "__main__":
    sys.exit(main())
