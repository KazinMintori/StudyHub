// Module bài tập phòng Lab: Lab 7: Chuỗi và biểu thức chính quy trên 690 nghìn đánh giá
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-07-xu-ly-chuoi",
  "title": "Lab 7: Chuỗi và biểu thức chính quy trên 690 nghìn đánh giá",
  "dataset": {
    "name": "Tập bình luận du khách Santiago (690.112 đánh giá đầy đủ)",
    "type": "CSV nén Gzip (Văn bản tự do đa ngôn ngữ)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/reviews.csv.gz",
    "description": "690.112 phản hồi bằng văn bản của du khách bằng tiếng Tây Ban Nha, tiếng Anh, tiếng Bồ Đào Nha, chứa thẻ HTML thô (<br/>), số điện thoại, địa chỉ và biểu cảm, phục vụ làm sạch chuỗi và biểu thức chính quy (Regex)."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Chuẩn hóa chuỗi trước khi đếm và bẫy NaN của str.contains",
      "prompt": "Xét cột văn bản đánh giá `comments`. Hãy tìm các bình luận có chứa từ 'metro' (tàu điện ngầm). Thử nghiệm và giải thích tại sao gọi `comments.str.contains('metro')` mà không khai báo `na=False` sẽ tạo ra mặt nạ Boolean chứa giá trị `NaN`, khiến phép lọc bị lỗi.",
      "prediction": "Phương thức `.str.contains()` khi gặp ô dữ liệu bị thiếu (`NaN`) sẽ trả về kết quả là `NaN` thay vì `False`. Khi đưa mảng chứa NaN này vào dấu ngoặc vuông `df[mask]`, pandas sẽ báo lỗi không thể lọc bằng mảng Boolean không xác định.",
      "solutionBasic": "import pandas as pd\n\nurl_reviews = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv'\nrv = pd.read_csv(url_reviews, nrows=10000)\n\n# Bắt buộc đặt na=False để biến NaN thành False\nmat_na_metro = rv['comments'].str.lower().str.contains('metro', na=False)\nso_review_metro = mat_na_metro.sum()\nprint(f'Số bình luận nhắc tới Metro: {so_review_metro:,}')",
      "solutionAdvanced": "def tim_kiem_tu_khoa_phong_thu(series_van_ban: pd.Series, tu_khoa: str) -> pd.Series:\n    \"\"\"Chuẩn hóa chuỗi và lọc an toàn với bẫy NaN.\"\"\"\n    # 1. Điền tạm giá trị thiếu thành chuỗi rỗng\n    s_clean = series_van_ban.fillna('').astype(str).str.strip().str.lower()\n    # 2. Tìm kiếm chính xác từ độc lập bằng regex r'\\b...\\b'\n    pattern = rf'\\b{re.escape(tu_khoa.lower())}\\b'\n    return s_clean.str.contains(pattern, regex=True)",
      "explanation": "Luôn luôn truyền tham số `na=False` khi sử dụng các phương thức kiểm tra chuỗi của pandas như `.str.contains()`, `.str.startswith()`, `.str.endswith()` để đảm bảo kết quả trả về là một mảng thuần Boolean.",
      "verification": "assert mat_na_metro.dtype == bool\nassert not mat_na_metro.isna().any()"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Loại bỏ thẻ HTML bằng biểu thức chính quy Regex",
      "prompt": "Các đánh giá trích xuất từ web thường chứa thẻ ngắt dòng `<br/>` hoặc các thẻ HTML khác như `<p>`, `</p>`. Hãy sử dụng phương thức `str.replace()` với mẫu Regex `r'<br\\s*/?>'` để chuẩn hóa toàn bộ các thẻ ngắt dòng này thành một dấu khoảng trắng.",
      "prediction": "Thẻ ngắt dòng HTML có thể xuất hiện dưới nhiều biến thể: `<br>`, `<br/>`, `<br />`. Biểu thức chính quy `r'<br\\s*/?>'` sẽ bắt trọn vẹn tất cả các biến thể này.",
      "solutionBasic": "rv['comments_clean'] = rv['comments'].astype(str).str.replace(r'<br\\s*/?>', ' ', regex=True)",
      "solutionAdvanced": "def loai_bo_html_chuan_muc(s: pd.Series) -> pd.Series:\n    \"\"\"Xóa toàn bộ thẻ HTML và thu gọn khoảng trắng thừa.\"\"\"\n    # 1. Xóa mọi thẻ HTML bất kỳ <...>\n    khong_html = s.astype(str).str.replace(r'<[^>]+>', ' ', regex=True)\n    # 2. Thu gọn nhiều khoảng trắng liên tiếp thành 1 khoảng trắng\n    return khong_html.str.split().str.join(' ')\n\nrv['comments_sach'] = loai_bo_html_chuan_muc(rv['comments'])\nprint(rv['comments_sach'].head(2))",
      "explanation": "Kỹ thuật `s.str.split().str.join(' ')` là một mẹo kinh điển trong xử lý ngôn ngữ tự nhiên: việc split tách từ theo khoảng trắng bất kỳ (khoảng trắng, tab, xuống dòng) rồi join lại bằng một dấu cách đơn sẽ dọn sạch toàn bộ khoảng trắng rác.",
      "verification": "assert not rv['comments_sach'].str.contains('<br').any()"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Trích xuất thông tin có cấu trúc bằng str.extract và Nhóm bắt (Capture Groups)",
      "prompt": "Trong một số bình luận, du khách ghi lại số ngày lưu trú theo cấu trúc như: 'stayed 3 days', 'spent 5 nights', 'quedamos 4 dias'. Hãy viết biểu thức chính quy kèm nhóm bắt (Capture Group) để trích xuất số ngày lưu trú từ văn bản.",
      "prediction": "Phương thức `.str.extract(r'(\\d+)\\s*(?:days|nights|dias)')` sử dụng cặp ngoặc đơn `()` để định nghĩa nhóm bắt, pandas sẽ tự động lấy chuỗi số khớp bên trong ngoặc đơn và trả về dưới dạng cột riêng biệt.",
      "solutionBasic": "pattern = r'(\\d+)\\s*(?:days|nights|dias)'\ns_so_ngay = rv['comments_sach'].str.extract(pattern, expand=False)\nprint('Số ngày lưu trú trích xuất được:\\n', s_so_ngay.dropna().head())",
      "solutionAdvanced": "def trich_xuat_so_ngay_luu_tru(s: pd.Series) -> pd.Series:\n    \"\"\"Trích xuất số nguyên và ép kiểu an toàn.\"\"\"\n    pat = r'(\\d+)\\s*(?:days?|nights?|días?|dias?)'\n    extracted = s.str.extract(pat, flags=re.IGNORECASE, expand=False)\n    return pd.to_numeric(extracted, errors='coerce')\n\nrv['so_ngay_o'] = trich_xuat_so_ngay_luu_tru(rv['comments_sach'])\nprint('Thống kê số ngày lưu trú:\\n', rv['so_ngay_o'].describe())",
      "explanation": "Sử dụng cờ `flags=re.IGNORECASE` giúp mẫu Regex khớp được cả chữ hoa lẫn chữ thường mà không cần phải chuyển đổi toàn bộ văn bản sang chữ thường trước khi quét.",
      "verification": "test_txt = pd.Series(['I stayed 4 nights here', 'Great place', 'Quedamos 10 dias'])\nextr = trich_xuat_so_ngay_luu_tru(test_txt)\nassert extr.iloc[0] == 4 and extr.iloc[2] == 10 and pd.isna(extr.iloc[1])"
    }
  ]
};
