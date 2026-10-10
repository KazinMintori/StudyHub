// Module bài tập phòng Lab: Lab 6: Dữ liệu ngoài: file lớn, API lịch sử & DuckDB
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-06-ket-noi-truy-xuat-du-lieu",
  "title": "Lab 6: Dữ liệu ngoài: file lớn, API lịch sử & DuckDB",
  "dataset": {
    "name": "Inside Airbnb Santiago GZ (90 cột) & Open-Meteo Weather API",
    "type": "CSV nén (Gzip), Parquet & REST API JSON",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/listings.csv.gz",
    "secondary_url": "https://archive-api.open-meteo.com/v1/archive?latitude=-33.45&longitude=-70.67&start_date=2024-01-01&end_date=2024-01-31&daily=temperature_2m_max,precipitation_sum&timezone=America/Santiago",
    "description": "Bảng đầy đủ 90 cột nén Gzip (listings.csv.gz), tệp đánh giá 690 nghìn dòng (reviews.csv), và API thời tiết lịch sử Open-Meteo của trạm Santiago (-33.45, -70.67) để thực hành DuckDB, Parquet và ghép nối nguồn ngoài."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Đọc có chọn lọc trên tệp lớn bằng usecols và parse_dates",
      "prompt": "Tệp `listings.csv.gz` có tới 90 cột thông tin chi tiết. Nếu nạp toàn bộ sẽ tiêu tốn hàng Gigabyte bộ nhớ RAM. Hãy sử dụng tham số `usecols` để chỉ đọc 5 cột: `['id', 'name', 'room_type', 'price', 'last_review']` và tự động chuyển đổi ngày tháng bằng `parse_dates=['last_review']`. Đối chiếu mức tiết kiệm RAM.",
      "prediction": "Chỉ đọc 5 cột thay vì 90 cột sẽ giảm hơn 90% dung lượng RAM cần thiết để lưu trữ DataFrame và tăng tốc độ đọc tệp gấp 5-10 lần.",
      "solutionBasic": "import pandas as pd\n\n# Đọc có chọn lọc\ncot_can_doc = ['id', 'name', 'room_type', 'price', 'last_review']\nurl_full = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/listings.csv.gz'\ndf_selective = pd.read_csv(url_full, usecols=cot_can_doc, parse_dates=['last_review'])\nprint('Kích thước DataFrame chọn lọc:', df_selective.shape)\nprint('Kiểu dữ liệu:\\n', df_selective.dtypes)",
      "solutionAdvanced": "def doc_du_lieu_phong_thu(url_or_path: str, columns: list[str]) -> pd.DataFrame:\n    \"\"\"Đọc tệp nén lớn phòng thủ với bộ nhớ tối thiểu.\"\"\"\n    df = pd.read_csv(\n        url_or_path,\n        usecols=columns,\n        parse_dates=[c for c in columns if 'date' in c or 'review' in c],\n        low_memory=False\n    )\n    # Ép kiểu số để tiết kiệm RAM tối đa\n    if 'id' in df.columns:\n        df['id'] = pd.to_numeric(df['id'], downcast='integer')\n    return df\n\n# Kiểm tra mức sử dụng RAM thực tế\nram_usage = df_selective.memory_usage(deep=True).sum() / (1024 * 1024)\nprint(f'RAM sử dụng cho 5 cột: {ram_usage:.2f} MB')",
      "explanation": "Đọc cả bảng lớn rồi mới lọc bỏ cột (`df = pd.read_csv(...)[cols]`) là sai lầm phổ biến: nó vẫn buộc hệ thống phải cấp phát RAM tối đa để chứa toàn bộ 90 cột trong lúc đọc, dễ gây lỗi tràn bộ nhớ Out of Memory (OOM).",
      "verification": "assert df_selective.shape[1] == 5\nassert pd.api.types.is_datetime64_any_dtype(df_selective['last_review'])"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Làm sạch cột giá chứa ký tự tiền tệ và dấu phẩy ngăn nghìn",
      "prompt": "Trong bảng chi tiết 90 cột, cột `price` được lưu dưới dạng chuỗi có chứa ký hiệu tiền tệ và dấu phẩy, ví dụ `'$45,000.00'`. Hãy viết hàm chuẩn hóa chuỗi này thành số thực `float`. Xử lý phòng thủ các trường hợp giá trị rỗng hoặc `NaN`.",
      "prediction": "Nếu không loại bỏ ký tự `$` và dấu phẩy `,` trước khi gọi `astype(float)`, Python sẽ ném lỗi ValueError không thể chuyển đổi chuỗi chứa ký tự phi số.",
      "solutionBasic": "def lam_sach_gia_cb(gia_series: pd.Series) -> pd.Series:\n    return (\n        gia_series.astype(str)\n        .str.replace('$', '', regex=False)\n        .str.replace(',', '', regex=False)\n        .astype(float)\n    )",
      "solutionAdvanced": "def lam_sach_gia_nc(gia_series: pd.Series) -> pd.Series:\n    \"\"\"Làm sạch tiền tệ đa dạng bằng biểu thức chính quy và coerce lỗi.\"\"\"\n    # 1. Thay thế mọi ký tự không phải số hoặc dấu chấm thập phân\n    chuoi_sach = gia_series.astype(str).str.replace(r'[^0-9.]', '', regex=True)\n    # 2. Ép kiểu an toàn chuyển chuỗi rỗng thành NaN\n    return pd.to_numeric(chuoi_sach, errors='coerce')",
      "explanation": "Sử dụng `regex=False` khi thay thế các chuỗi cố định đơn giản giúp tăng tốc độ xử lý; đối với định dạng tiền tệ phức tạp, `regex=True` kết hợp `pd.to_numeric(..., errors='coerce')` đảm bảo mã nguồn không bao giờ bị dừng đột ngột.",
      "verification": "test_s = pd.Series(['$45,000.00', '$1,200.50', None, 'invalid'])\ncleaned = lam_sach_gia_nc(test_s)\nassert cleaned.iloc[0] == 45000.0 and cleaned.iloc[1] == 1200.50\nassert pd.isna(cleaned.iloc[2]) and pd.isna(cleaned.iloc[3])"
    },
    {
      "id": "task-3",
      "title": "Bài 3: So sánh hiệu năng lưu trữ và đọc: CSV phẳng vs Parquet dạng cột",
      "prompt": "Lưu DataFrame 18.534 dòng ra hai định dạng: `listings.csv` và `listings.parquet` (sử dụng thuật toán nén `snappy`). So sánh dung lượng tệp trên ổ đĩa và đo thời gian đọc lại dữ liệu của hai định dạng.",
      "prediction": "Định dạng Parquet lưu trữ theo hướng cột (Columnar Storage) và tích hợp nén từ điển, dự đoán kích thước tệp sẽ giảm 60-80% so với CSV và thời gian đọc lại sẽ nhanh hơn từ 3 đến 5 lần, đồng thời giữ nguyên kiểu dữ liệu ban đầu.",
      "solutionBasic": "import time\nimport os\n\n# 1. Xuất file\ndf_selective.to_csv('temp_listings.csv', index=False)\ndf_selective.to_parquet('temp_listings.parquet', index=False)\n\n# 2. So sánh dung lượng đĩa\nsz_csv = os.path.getsize('temp_listings.csv') / 1024\nsz_parquet = os.path.getsize('temp_listings.parquet') / 1024\nprint(f'Kích thước CSV: {sz_csv:.1f} KB vs Parquet: {sz_parquet:.1f} KB')",
      "solutionAdvanced": "# Đo lường thời gian đọc thực tế\nt0 = time.perf_counter()\npd.read_csv('temp_listings.csv')\nt_csv = time.perf_counter() - t0\n\nt0 = time.perf_counter()\npd.read_parquet('temp_listings.parquet')\nt_parquet = time.perf_counter() - t0\n\nprint(f'Thời gian đọc CSV: {t_csv*1000:.1f} ms vs Parquet: {t_parquet*1000:.1f} ms')\n# Dọn dẹp tệp tạm\nos.remove('temp_listings.csv')\nos.remove('temp_listings.parquet')",
      "explanation": "Tệp CSV không lưu thông tin kiểu dữ liệu (Schema Metadata), vì vậy mỗi khi đọc lại, pandas phải duyệt qua các dòng để phán đoán kiểu cột (Type Inference), gây chậm trễ nghiêm trọng trong quy trình Big Data.",
      "verification": "assert sz_parquet < sz_csv, 'Parquet phải có kích thước nhỏ hơn đáng kể so với CSV.'"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Thu thập dữ liệu API lịch sử và chuyển đổi JSON thành bảng phẳng",
      "prompt": "Gọi API thời tiết mở Open-Meteo để lấy dữ liệu nhiệt độ tối đa và lượng mưa hàng ngày tại Santiago trong tháng 01/2024. Áp dụng nguyên tắc kỹ thuật dữ liệu: luôn lưu phản hồi JSON thô (Raw JSON) trước khi chuyển đổi sang DataFrame phẳng.",
      "prediction": "Phản hồi API thời tiết có cấu trúc lồng nhau dạng từ điển chứa danh sách thời gian (`daily.time`) và danh sách nhiệt độ (`daily.temperature_2m_max`). Việc tạo DataFrame từ từ điển con này sẽ làm phẳng dữ liệu thành bảng theo ngày.",
      "solutionBasic": "import urllib.request\nimport json\n\napi_url = 'https://archive-api.open-meteo.com/v1/archive?latitude=-33.45&longitude=-70.67&start_date=2024-01-01&end_date=2024-01-31&daily=temperature_2m_max,precipitation_sum&timezone=America/Santiago'\n\nwith urllib.request.urlopen(api_url) as resp:\n    raw_json = json.loads(resp.read().decode('utf-8'))\n\ndf_weather = pd.DataFrame(raw_json['daily'])\nprint(df_weather.head())",
      "solutionAdvanced": "def lay_thoi_tiet_lich_su(lat: float, lon: float, start: str, end: str) -> pd.DataFrame:\n    \"\"\"Gọi API có kiểm soát lỗi mạng và lưu dấu vết thô.\"\"\"\n    url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start}&end_date={end}&daily=temperature_2m_max,precipitation_sum&timezone=America/Santiago'\n    req = urllib.request.Request(url, headers={'User-Agent': 'StudyHub-DataBot/1.0'})\n    with urllib.request.urlopen(req, timeout=10) as response:\n        data = json.loads(response.read().decode('utf-8'))\n    \n    assert 'daily' in data, 'Phản hồi API không có trường dữ liệu daily'\n    df_res = pd.DataFrame(data['daily'])\n    df_res['time'] = pd.to_datetime(df_res['time'])\n    return df_res\n\ndf_w = lay_thoi_tiet_lich_su(-33.45, -70.67, '2024-01-01', '2024-01-31')",
      "explanation": "Nguyên tắc kiến trúc dữ liệu: Luôn giữ nguyên dữ liệu gốc (Bronze Layer / Raw Data). Nếu quy tắc biến đổi bảng bị lỗi trong tương lai, kỹ sư có thể chạy lại mã nguồn từ tệp thô mà không phải gọi lại API (tránh tốn quota hoặc phụ thuộc mạng).",
      "verification": "assert len(df_w) == 31, 'Tháng 1 phải có đúng 31 ngày dữ liệu.'\nassert 'temperature_2m_max' in df_w.columns"
    },
    {
      "id": "task-5",
      "title": "Bài 5: Truy vấn trực tiếp tệp CSV bằng DuckDB mà không cần nạp vào RAM",
      "prompt": "Sử dụng công cụ OLAP nhúng DuckDB để thực thi truy vấn SQL trực tiếp trên tệp `reviews.csv` (690 nghìn dòng) trên đĩa mà không cần gọi `pd.read_csv()`. Thực hiện đếm số lượt đánh giá của từng loại phòng bằng cách JOIN hai tệp CSV trực tiếp trong câu lệnh SQL.",
      "prediction": "DuckDB sử dụng công cụ thực thi vector hóa (Vectorized Engine) và đọc dữ liệu theo khối trực tiếp từ đĩa, cho phép thực thi câu lệnh SQL tổng hợp trên tệp nửa triệu dòng chỉ trong vài chục mili-giây với mức tiêu thụ RAM cực kỳ thấp.",
      "solutionBasic": "import duckdb\n\n# DuckDB cho phép truy vấn trực tiếp cú pháp FROM 'duong_dan.csv'\nsql = '''\nSELECT room_type, COUNT(*) as so_luong, AVG(price) as gia_tb\nFROM 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv'\nGROUP BY room_type\nORDER BY so_luong DESC\n'''\nres_df = duckdb.query(sql).to_df()\nprint('Kết quả truy vấn trực tiếp bằng DuckDB:\\n', res_df)",
      "solutionAdvanced": "def truy_van_duckdb_nang_cao(url_listings: str, url_reviews: str) -> pd.DataFrame:\n    \"\"\"Truy vấn SQL JOIN trực tiếp 2 tệp CSV trên mạng.\"\"\"\n    conn = duckdb.connect(database=':memory:')\n    query = f'''\n    SELECT \n        l.neighbourhood,\n        l.room_type,\n        COUNT(r.date) as tong_review_2024\n    FROM '{url_listings}' l\n    LEFT JOIN '{url_reviews}' r ON l.id = r.listing_id\n    WHERE r.date >= '2024-01-01' AND r.date <= '2024-01-31'\n    GROUP BY l.neighbourhood, l.room_type\n    HAVING tong_review_2024 > 50\n    ORDER BY tong_review_2024 DESC\n    '''\n    return conn.execute(query).df()\n\n# DuckDB thực thi phân tích SQL cực nhanh\nprint('DuckDB sẵn sàng phục vụ phân tích quy mô lớn.')",
      "explanation": "DuckDB là giải pháp cách mạng cho khoa học dữ liệu hiện đại: nó giải quyết nút thắt cổ chai về RAM của pandas khi làm việc với các bảng dữ liệu từ vài Gigabyte đến hàng chục Gigabyte ngay trên máy trạm cá nhân.",
      "verification": "assert res_df.shape[0] > 0\nassert 'room_type' in res_df.columns"
    }
  ]
};
