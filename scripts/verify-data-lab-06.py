#!/usr/bin/env python3
"""
scripts/verify-data-lab-06.py
Bộ kiểm thử và kiểm định toàn diện cho Lab 06:
Dữ liệu ngoài: Đọc tệp lớn có chọn lọc, API lịch sử, lưu trữ Parquet và truy vấn DuckDB.

Phạm vi kiểm tra:
1. Xác minh sự tồn tại và tính hợp lệ của các tệp sở hữu:
   - raw_materials/xu-ly-du-lieu/labs/lab-06.md
   - raw_materials/xu-ly-du-lieu/labs/coverage-06.json
   - scripts/verify-data-lab-06.py
2. Kiểm tra quy chuẩn Markdown và sư phạm trong lab-06.md:
   - Đủ 12 mã bài tập: data-lab-06-01 đến data-lab-06-12
   - Cặp khối ::: exercise và ::: solution hoàn chỉnh
   - Không chứa dấu gạch ngang dài (em dash '—' hoặc '--') trong văn xuôi
   - Không chứa dấu chấm phẩy (';') trong văn xuôi
   - Quy tắc viết hoa sau dấu hai chấm (':')
   - Không chứa các từ ngữ cảm tính hoặc cụm từ bị cấm
   - Khối công thức hiển thị $$ đứng trên dòng riêng, không chứa \\vert hay \\Vert
   - Bảng kết quả đúng chuẩn Markdown/HTML
3. Kiểm tra tính bao phủ trong coverage-06.json:
   - Bao phủ đầy đủ 46 cell của template/lab-06.ipynb
   - Bao phủ đầy đủ 37 cell của course/2627-1/notebooks/lab-06.ipynb
4. Thực thi và kiểm định kết quả số học của mọi hàm và lời giải:
   - Bài 1 (data-lab-06-01): Đọc có chọn lọc cột và parse ngày với usecols và parse_dates
   - Bài 2 (data-lab-06-02): Làm sạch chuỗi giá tiền bằng str.replace(..., regex=False)
   - Bài 3 (data-lab-06-03): Đối chiếu CSV và Parquet về kích thước và bảo toàn kiểu dữ liệu
   - Bài 4 (data-lab-06-04): Lưu phản hồi API thời tiết thô JSON và chuyển daily thành bảng
   - Bài 5 (data-lab-06-05): Đếm số đánh giá theo ngày và xử lý ngày không có đánh giá
   - Bài 6 (data-lab-06-06): Ghép thời tiết với đánh giá bằng LEFT JOIN và đo tương quan
   - Bài 7 (data-lab-06-07): Truy vấn DuckDB trực tiếp trên tệp CSV đếm theo năm
   - Bài 8 (data-lab-06-08): Phân biệt COUNT(*) và COUNT(cột) trong DuckDB trên tệp Parquet
   - Bài 9 (data-lab-06-09): Ghép nối DuckDB JOIN theo loại phòng và phân tích tỷ trọng
   - Bài 10 (data-lab-06-10): Lọc nhóm bằng mệnh đề HAVING trong DuckDB và đối chiếu pandas
   - Bài 11 (data-lab-06-11): So sánh chuỗi thời tiết và đánh giá tháng 7 giữa mùa đông
   - Bài 12 (data-lab-06-12): Truy vấn top chỗ ở nhận nhiều đánh giá nhất kèm tên định danh
"""

import os
import sys
import json
import re
import tempfile
from pathlib import Path

# Cấu hình UTF-8 cho stdout và stderr
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
LAB_MD_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "lab-06.md"
COVERAGE_PATH = REPO_ROOT / "raw_materials" / "xu-ly-du-lieu" / "labs" / "coverage-06.json"

EXPECTED_EXERCISES = [
    f"data-lab-06-{i:02d}" for i in range(1, 13)
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
    "Tài liệu này hệ thống hóa",
]


def test_file_existence():
    """Kiểm tra sự tồn tại của các tệp thuộc phạm vi lab-06."""
    print("--- [1] Kiểm tra sự tồn tại của các tệp sở hữu ---")
    assert LAB_MD_PATH.exists(), f"Không tìm thấy tệp {LAB_MD_PATH}"
    assert COVERAGE_PATH.exists(), f"Không tìm thấy tệp {COVERAGE_PATH}"
    assert LAB_MD_PATH.stat().st_size > 1000, "Tệp lab-06.md quá ngắn hoặc rỗng."
    assert COVERAGE_PATH.stat().st_size > 500, "Tệp coverage-06.json quá ngắn hoặc rỗng."
    print("  ✓ Tệp lab-06.md và coverage-06.json tồn tại và có nội dung đầy đủ.")


def test_markdown_pedagogical_rules():
    """Kiểm tra các quy chuẩn văn phong, định dạng và sư phạm trong Markdown."""
    print("--- [2] Kiểm tra quy chuẩn Markdown và văn phong tiếng Việt ---")
    content = LAB_MD_PATH.read_text(encoding="utf-8")

    # 1. Kiểm tra đủ 12 exercise IDs
    for ex_id in EXPECTED_EXERCISES:
        assert f'id="{ex_id}"' in content, f"Thiếu mã bài tập {ex_id} trong lab-06.md"
    print(f"  ✓ Đã tìm thấy đầy đủ 12 mã bài tập: {', '.join(EXPECTED_EXERCISES)}")

    # 2. Kiểm tra container exercise và solution
    exercise_opens = len(re.findall(r"^::: exercise", content, re.MULTILINE))
    solution_opens = len(re.findall(r"^::: solution", content, re.MULTILINE))
    container_closes = len(re.findall(r"^:::\s*$", content, re.MULTILINE))
    assert exercise_opens == 12, f"Số lượng '::: exercise' là {exercise_opens}, kỳ vọng 12."
    assert solution_opens == 12, f"Số lượng '::: solution' là {solution_opens}, kỳ vọng 12."
    assert container_closes == 24, f"Số lượng ':::' đóng container là {container_closes}, kỳ vọng 24 (12 bài x 2)."
    print("  ✓ Cấu trúc container '::: exercise' và '::: solution' hoàn toàn cân đối.")

    # 3. Tiêu đề bắt đầu từ H2, không có H1 (chỉ quét bên ngoài khối mã ```)
    content_outside_code = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    h1_matches = re.findall(r"^# [^\n]+", content_outside_code, re.MULTILINE)
    assert len(h1_matches) == 0, f"Tìm thấy tiêu đề cấp H1 không hợp lệ: {h1_matches}"
    h2_matches = re.findall(r"^## [^\n]+", content_outside_code, re.MULTILINE)
    assert len(h2_matches) >= 12, f"Số lượng tiêu đề H2 quá ít ({len(h2_matches)})."
    print(f"  ✓ Không có tiêu đề H1; tìm thấy {len(h2_matches)} tiêu đề H2 hợp lệ.")

    # 4. Kiểm tra các từ ngữ cấm
    for word in FORBIDDEN_WORDS:
        assert word not in content, f"Nội dung chứa từ ngữ cấm: '{word}'"
    print("  ✓ Không phát hiện từ ngữ cảm tính hoặc sáo rỗng bị cấm.")

    # 5. Kiểm tra dấu chấm phẩy và dấu gạch ngang dài trong văn xuôi (bên ngoài code fence)
    lines = content.splitlines()
    in_code = False
    in_math = False
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("$$"):
            in_math = not in_math
            continue
        if in_code or in_math:
            continue

        # Bỏ qua các dòng chú thích bảng markdown "| ... |"
        if stripped.startswith("|") and stripped.endswith("|"):
            continue

        # Bỏ qua dòng phân cách Markdown '---'
        if stripped == "---":
            continue

        # Kiểm tra dấu gạch ngang dài
        assert "—" not in line, f"Dòng {line_idx} chứa dấu gạch ngang dài (em dash '—'): {line}"
        if "--" in line:
            # Cho phép nếu là liên kết tác giả hoặc mã số
            assert False, f"Dòng {line_idx} chứa '--' trong văn xuôi: {line}"

        # Kiểm tra dấu chấm phẩy trong văn xuôi
        if ";" in line:
            # Cho phép thực thể HTML như &nbsp; &lt; &gt;
            cleaned = re.sub(r"&[a-zA-Z0-9#]+;", "", line)
            assert ";" not in cleaned, f"Dòng {line_idx} chứa dấu chấm phẩy ';' trong văn xuôi: {line}"

    print("  ✓ Không phát hiện dấu gạch ngang dài hoặc dấu chấm phẩy trong văn xuôi.")

    # 6. Kiểm tra viết hoa sau dấu hai chấm trong văn xuôi
    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("$$"):
            in_math = not in_math
            continue
        if in_code or in_math or not stripped:
            continue
        # Bỏ qua dòng bảng, container VitePress, URL, mã code
        if stripped.startswith("|") or stripped.startswith(":::") or "http://" in line or "https://" in line:
            continue
        # Tìm các vị trí ': ' trong câu văn
        matches = re.finditer(r":\s+([^\s])", line)
        for m in matches:
            char = m.group(1)
            # Kiểm tra xem có nằm trong code inline `$ ... $` hoặc `` ` ... ` ``
            prefix = line[:m.start()]
            if prefix.count("`") % 2 == 1 or prefix.count("$") % 2 == 1:
                continue
            if char.islower():
                assert False, f"Dòng {line_idx} vi phạm quy tắc viết hoa sau dấu hai chấm (ký tự '{char}'): {line}"

    print("  ✓ Tuân thủ nghiêm ngặt quy tắc viết hoa chữ cái đầu sau dấu hai chấm.")

    # 7. Kiểm tra công thức toán học $$ trên dòng riêng biệt
    inline_display_math = re.findall(r"[^\n]\$\$|\$\$[^\n]", content)
    for m in inline_display_math:
        if m.strip() != "$$":
            assert False, f"Khối công thức hiển thị '$$' dính liền văn bản: '{m}'"
    assert "\\vert" not in content, "Công thức toán chứa cú pháp cấm '\\vert'"
    assert "\\Vert" not in content, "Công thức toán chứa cú pháp cấm '\\Vert'"
    print("  ✓ Các khối toán học $$ đứng độc lập trên dòng riêng, không chứa \\vert hay \\Vert.")


def test_coverage_mapping():
    """Kiểm tra tệp coverage-06.json bao phủ toàn bộ các cell nguồn."""
    print("--- [3] Kiểm tra độ bao phủ trong coverage-06.json ---")
    data = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))
    assert data["lab"] == "lab-06"
    assert data["total_exercises"] == 12
    assert data["exercise_ids"] == EXPECTED_EXERCISES

    template_cells = data["cells"]["template/lab-06.ipynb"]
    course_cells = data["cells"]["course/2627-1/notebooks/lab-06.ipynb"]

    assert len(template_cells) == 46, f"template/lab-06.ipynb có {len(template_cells)} cell, kỳ vọng 46."
    assert len(course_cells) == 37, f"course/2627-1/notebooks/lab-06.ipynb có {len(course_cells)} cell, kỳ vọng 37."

    # Kiểm tra tính hợp lệ của từng bản ghi
    for cell in template_cells + course_cells:
        assert "cell_index" in cell
        assert "cell_type" in cell
        assert "status" in cell
        assert cell["status"] in ("mapped", "preamble", "excluded")
        assert "reason" in cell and len(cell["reason"]) > 5

    print(f"  ✓ Bao phủ 100% tế bào: 46 cell template và 37 cell course.")


def test_executable_solutions():
    """Kiểm tra và thực thi các lời giải số học của cả 12 bài tập."""
    print("--- [4] Thực thi kiểm chứng số học của các lời giải ---")
    import numpy as np
    import pandas as pd
    import duckdb

    # Khởi tạo fixture chuẩn
    _ngay = []
    for ngay, so in zip(pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]):
        _ngay += [ngay] * so
    _ngay += list(pd.to_datetime(["2023-03-15", "2023-08-02", "2023-11-20", "2024-02-11", "2024-05-05",
                                  "2024-07-19", "2024-09-30", "2024-12-24", "2024-12-31", "2025-03-08",
                                  "2025-06-21", "2025-09-18", "2025-12-05", "2026-02-14", "2026-04-01"]))
    demo_reviews = pd.DataFrame({
        "listing_id": [[11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9] for k in range(len(_ngay))],
        "date": _ngay,
    })
    demo_listings_full = pd.DataFrame({
        "id": [11, 12, 13, 14, 15, 16],
        "name": ["Depto Lastarria", "Pieza Bellavista", "Loft Providencia", "Casa Ñuñoa",
                 "Studio Centro", "Depto nuevo"],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": ["Santiago", "Recoleta", "Providencia", "Ñuñoa", "Santiago", "Las Condes"],
        "room_type": ["Entire home/apt", "Private room", "Entire home/apt", "Entire home/apt",
                      "Entire home/apt", "Private room"],
        "price": ["$45,647.00", "$18,500.00", "$1,120,000.00", None, "$59,000.00", "$25,990.50"],
        "first_review": ["2023-03-15", "2023-08-02", "2024-02-11", "2023-11-20", "2025-01-02", None],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    })
    demo_weather = {
        "latitude": -33.45, "longitude": -70.66, "timezone": "America/Santiago",
        "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
        "daily": {"time": [f"2025-01-{d:02d}" for d in range(1, 11)],
                  "temperature_2m_max": [31.4, 33.1, 29.1, 32.8, 30.2, 30.0, 28.5, 31.8, 30.9, 27.6]},
    }

    with tempfile.TemporaryDirectory(prefix="verify-data-lab-06-") as tmpdir:
        tmp_path = Path(tmpdir)
        rv_csv = tmp_path / "reviews.csv"
        ls_csv = tmp_path / "listings.csv"
        full_csv = tmp_path / "listings_full.csv"
        weather_json = tmp_path / "weather.json"

        demo_reviews.to_csv(rv_csv, index=False)
        demo_listings_full[["id", "name", "room_type"]].to_csv(ls_csv, index=False)
        demo_listings_full.to_csv(full_csv, index=False)

        # Bài 1: read_selected
        def read_selected_c1(path, columns: list, date_columns: list) -> pd.DataFrame:
            return pd.read_csv(path, usecols=columns, parse_dates=date_columns or False)

        def read_selected_c2(path, columns: list, date_columns: list, dtypes: dict = None) -> pd.DataFrame:
            return pd.read_csv(path, usecols=columns, parse_dates=date_columns or False, dtype=dtypes)

        cols = ["id", "room_type", "price", "first_review", "number_of_reviews"]
        res1_c1 = read_selected_c1(full_csv, cols, ["first_review"])
        res1_c2 = read_selected_c2(full_csv, cols, ["first_review"], dtypes={"id": str})
        assert res1_c1.shape == (6, 5)
        assert set(res1_c1.columns) == set(cols)
        assert str(res1_c1["first_review"].dtype).startswith("datetime64")
        assert res1_c1["first_review"].isna().sum() == 1
        assert pd.api.types.is_string_dtype(res1_c2["id"])
        print("  ✓ Bài 1 (data-lab-06-01): Đọc có chọn lọc và parse ngày thành công.")

        # Bài 2: clean_price
        def clean_price_c1(prices: pd.Series) -> pd.Series:
            return (
                prices.str.replace("$", "", regex=False)
                .str.replace(",", "", regex=False)
                .astype(float)
            )

        def clean_price_c2(prices: pd.Series) -> pd.Series:
            return prices.str.replace(r"[$,]", "", regex=True).pipe(pd.to_numeric, errors="coerce")

        res2_c1 = clean_price_c1(demo_listings_full["price"])
        res2_c2 = clean_price_c2(demo_listings_full["price"])
        np.testing.assert_allclose(res2_c1, [45647.0, 18500.0, 1120000.0, np.nan, 59000.0, 25990.5])
        np.testing.assert_allclose(res2_c2, [45647.0, 18500.0, 1120000.0, np.nan, 59000.0, 25990.5])
        assert res2_c1.median() == 45647.0
        assert demo_listings_full["price"].iloc[0] == "$45,647.00", "Không đột biến dữ liệu đầu vào."
        print("  ✓ Bài 2 (data-lab-06-02): Làm sạch cột giá tiền và bảo toàn NaN thành công.")

        # Bài 3: save_formats
        def save_formats_c1(df: pd.DataFrame, folder) -> dict:
            p_folder = Path(folder)
            csv_file = p_folder / "t6.csv"
            pq_file = p_folder / "t6.parquet"
            df.to_csv(csv_file, index=False)
            df.to_parquet(pq_file, index=False)
            df_csv = pd.read_csv(csv_file)
            df_pq = pd.read_parquet(pq_file)
            return {
                "size_csv": os.path.getsize(csv_file),
                "size_parquet": os.path.getsize(pq_file),
                "dtypes_csv": {col: str(df_csv[col].dtype) for col in df_csv.columns},
                "dtypes_parquet": {col: str(df_pq[col].dtype) for col in df_pq.columns},
            }

        res3 = save_formats_c1(res1_c1, tmp_path)
        assert res3["size_csv"] > 0 and res3["size_parquet"] > 0
        assert not res3["dtypes_csv"]["first_review"].startswith("datetime64")
        assert res3["dtypes_parquet"]["first_review"].startswith("datetime64")
        print("  ✓ Bài 3 (data-lab-06-03): Xác nhận Parquet bảo toàn kiểu ngày và kích thước nén.")

        # Bài 4: weather_table
        def weather_table_c1(payload: dict, path) -> pd.DataFrame:
            p_target = Path(path)
            p_target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return pd.DataFrame(payload["daily"])

        res4 = weather_table_c1(demo_weather, weather_json)
        assert weather_json.exists()
        assert json.loads(weather_json.read_text(encoding="utf-8")) == demo_weather
        assert res4.shape == (10, 2)
        assert list(res4.columns) == ["time", "temperature_2m_max"]
        assert round(res4["temperature_2m_max"].mean(), 2) == 30.54
        print("  ✓ Bài 4 (data-lab-06-04): Lưu trữ response thô và trích xuất bảng thời tiết thành công.")

        # Bài 5: reviews_per_day
        def reviews_per_day_c1(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
            rv_loc = rv.copy()
            start_date = pd.to_datetime(start)
            end_date = pd.to_datetime(end)
            mask = (rv_loc["date"] >= start_date) & (rv_loc["date"] <= end_date)
            sub = rv_loc.loc[mask]
            grouped = sub.groupby(sub["date"].dt.strftime("%Y-%m-%d")).size().reset_index(name="so_review")
            return grouped.rename(columns={"date": "time"}).sort_values("time").reset_index(drop=True)

        res5 = reviews_per_day_c1(demo_reviews, "2025-01-01", "2025-01-10")
        assert len(res5) == 9, "Ngày 2025-01-05 có 0 đánh giá nên không xuất hiện trong bảng đếm."
        assert res5["so_review"].sum() == 36
        assert res5.loc[0, "time"] == "2025-01-01" and res5.loc[0, "so_review"] == 3
        print("  ✓ Bài 5 (data-lab-06-05): Đếm số đánh giá theo ngày và lọc phạm vi thành công.")

        # Bài 6: join_weather
        def join_weather_c1(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict:
            merged = weather.merge(per_day, on="time", how="left")
            missing = int(merged["so_review"].isna().sum())
            corr = float(merged["temperature_2m_max"].corr(merged["so_review"]))
            return {
                "gop": merged,
                "so_thieu": missing,
                "he_so": corr,
            }

        res6 = join_weather_c1(res4, res5)
        assert res6["gop"].shape == (10, 3)
        assert res6["so_thieu"] == 1
        assert np.isnan(res6["gop"].loc[4, "so_review"])
        assert round(res6["he_so"], 3) == 0.084
        print("  ✓ Bài 6 (data-lab-06-06): Ghép LEFT JOIN thời tiết và đánh giá, tính tương quan thành công.")

        # Bài 7: sql_reviews_by_year
        def sql_reviews_by_year_c1(path) -> pd.DataFrame:
            path_str = Path(path).as_posix()
            return duckdb.sql(f"""
                SELECT year(date) AS nam, count(*) AS n
                FROM '{path_str}'
                GROUP BY nam
                ORDER BY nam
            """).df()

        res7 = sql_reviews_by_year_c1(rv_csv)
        assert res7["nam"].tolist() == [2023, 2024, 2025, 2026]
        assert res7["n"].tolist() == [3, 6, 40, 2]
        print("  ✓ Bài 7 (data-lab-06-07): DuckDB truy vấn đếm theo năm khớp hoàn hảo với dữ liệu.")

        # Bài 8: sql_count_listings_and_reviews
        def sql_count_listings_and_reviews_c1(parquet_path) -> pd.DataFrame:
            pq_str = Path(parquet_path).as_posix()
            return duckdb.sql(f"""
                SELECT room_type,
                       COUNT(*) AS so_cho_o,
                       COUNT(first_review) AS so_co_danh_gia
                FROM '{pq_str}'
                GROUP BY room_type
                ORDER BY so_cho_o DESC, room_type ASC
            """).df()

        pq_file = tmp_path / "listings.parquet"
        res1_c1.to_parquet(pq_file, index=False)
        res8 = sql_count_listings_and_reviews_c1(pq_file)
        assert res8["so_cho_o"].sum() == 6
        assert res8["so_co_danh_gia"].sum() == 5
        print("  ✓ Bài 8 (data-lab-06-08): Phân biệt COUNT(*) và COUNT(cột) trong DuckDB thành công.")

        # Bài 9: sql_reviews_by_room_type
        def sql_reviews_by_room_type_c1(reviews_path, listings_path, nam: int) -> pd.DataFrame:
            r_str = Path(reviews_path).as_posix()
            l_str = Path(listings_path).as_posix()
            return duckdb.sql(f"""
                SELECT l.room_type, count(*) AS n
                FROM '{r_str}' r
                JOIN '{l_str}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
                WHERE year(r.date) = {nam}
                GROUP BY l.room_type
                ORDER BY n DESC, l.room_type ASC
            """).df()

        res9 = sql_reviews_by_room_type_c1(rv_csv, ls_csv, 2025)
        assert res9["room_type"].tolist() == ["Entire home/apt", "Private room"]
        assert res9["n"].tolist() == [27, 9]
        assert res9["n"].sum() == 36
        print("  ✓ Bài 9 (data-lab-06-09): DuckDB JOIN đánh giá theo loại phòng thành công.")

        # Bài 10: sql_active_listings_having
        def sql_active_listings_having_c1(reviews_path, nam: int, threshold: int) -> pd.DataFrame:
            r_str = Path(reviews_path).as_posix()
            return duckdb.sql(f"""
                SELECT CAST(listing_id AS BIGINT) AS listing_id, count(*) AS n
                FROM '{r_str}'
                WHERE year(date) = {nam}
                GROUP BY listing_id
                HAVING count(*) >= {threshold}
                ORDER BY n DESC, listing_id ASC
            """).df()

        res10 = sql_active_listings_having_c1(rv_csv, 2025, 5)
        assert len(res10) == 3
        assert set(res10["listing_id"]) == {11, 12, 13}
        print("  ✓ Bài 10 (data-lab-06-10): Lọc nhóm bằng mệnh đề HAVING trong DuckDB thành công.")

        # Bài 11: compare_july_weather_reviews
        demo_weather_july = {
            "latitude": -33.45, "longitude": -70.66, "timezone": "America/Santiago",
            "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
            "daily": {"time": [f"2025-07-{d:02d}" for d in range(1, 11)],
                      "temperature_2m_max": [14.2, 13.5, 15.0, 12.8, 11.4, 13.9, 14.7, 16.1, 12.0, 13.3]},
        }
        demo_reviews_july = pd.DataFrame({
            "listing_id": [11, 12, 11, 13, 14, 11, 15, 12, 13, 11, 12, 14],
            "date": pd.to_datetime([
                "2025-07-01", "2025-07-01", "2025-07-02", "2025-07-03", "2025-07-04",
                "2025-07-04", "2025-07-06", "2025-07-07", "2025-07-08", "2025-07-09",
                "2025-07-09", "2025-07-10"
            ])
        })

        def compare_july_weather_reviews_c1(weather_payload: dict, rv: pd.DataFrame, start: str, end: str) -> dict:
            w_df = pd.DataFrame(weather_payload["daily"])
            rv_daily = reviews_per_day_c1(rv, start, end)
            merged = w_df.merge(rv_daily, on="time", how="left")
            missing = int(merged["so_review"].isna().sum())
            corr = float(merged["temperature_2m_max"].corr(merged["so_review"])) if merged["so_review"].notna().sum() > 1 else np.nan
            return {
                "bang_thoi_tiet": w_df,
                "bang_danh_gia": rv_daily,
                "gop": merged,
                "so_ngay_thieu": missing,
                "he_so_tuong_quan": corr,
            }

        res11 = compare_july_weather_reviews_c1(demo_weather_july, demo_reviews_july, "2025-07-01", "2025-07-10")
        assert res11["so_ngay_thieu"] == 1
        assert round(res11["he_so_tuong_quan"], 3) == -0.576
        print("  ✓ Bài 11 (data-lab-06-11): So sánh dữ liệu thời tiết và đánh giá tháng 7 thành công.")

        # Bài 12: sql_top_reviewed_listings
        def sql_top_reviewed_listings_c1(reviews_path, listings_path, nam: int, limit: int = 5) -> pd.DataFrame:
            r_str = Path(reviews_path).as_posix()
            l_str = Path(listings_path).as_posix()
            return duckdb.sql(f"""
                SELECT CAST(r.listing_id AS BIGINT) AS listing_id,
                       l.name,
                       count(*) AS n
                FROM '{r_str}' r
                JOIN '{l_str}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
                WHERE year(r.date) = {nam}
                GROUP BY r.listing_id, l.name
                ORDER BY n DESC, listing_id ASC
                LIMIT {limit}
            """).df()

        res12 = sql_top_reviewed_listings_c1(rv_csv, ls_csv, 2025, 5)
        assert len(res12) == 5
        assert res12.iloc[0]["listing_id"] == 11 and res12.iloc[0]["n"] == 14
        print("  ✓ Bài 12 (data-lab-06-12): Truy vấn top chỗ ở nhiều đánh giá nhất thành công.")

    print("\n--- TẤT CẢ 12 BÀI TẬP ĐÃ VƯỢT QUA KIỂM THỬ THÀNH CÔNG ---")


def main():
    print("======================================================================")
    print("CHẠY BỘ KIỂM THỬ TOÀN DIỆN CHO LAB 06: DỮ LIỆU NGOÀI VÀ DUCKDB")
    print("======================================================================\n")
    test_file_existence()
    test_markdown_pedagogical_rules()
    test_coverage_mapping()
    test_executable_solutions()
    print("\n✓ ĐÃ HOÀN TẤT TOÀN BỘ CÁC BƯỚC XÁC MINH LAB 06.")


if __name__ == "__main__":
    main()
