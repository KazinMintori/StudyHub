// Module bài tập phòng Lab: Lab 8: Chuỗi thời gian: quý, cửa sổ trượt và so cùng kỳ
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-08-du-lieu-thoi-gian",
  "title": "Lab 8: Chuỗi thời gian: quý, cửa sổ trượt và so cùng kỳ",
  "dataset": {
    "name": "Chuỗi thời gian lượt đánh giá Santiago (2010 - 2026)",
    "type": "CSV (DatetimeIndex theo ngày)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv",
    "description": "Dãy thời gian 690.112 sự kiện đánh giá trải dài từ năm 2010 đến ngày 29/06/2026. Phục vụ tính toán tổng hợp theo quý (resample), phân tích kỳ chưa trọn vẹn, tính trung bình trượt 7 ngày (rolling window) và đo lường tăng trưởng cùng kỳ (YoY)."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Làm sạch mốc thời gian và thiết lập DatetimeIndex",
      "prompt": "Tệp dữ liệu được chụp (snapshot) vào ngày 29/06/2026. Bất kỳ bản ghi nào có ngày đánh giá sau mốc này đều là dữ liệu lỗi hoặc do đồng hồ hệ thống sai lệch. Hãy lọc bỏ các dòng có `date > '2026-06-29'`, sau đó đưa cột `date` làm chỉ mục của bảng và sắp xếp theo thứ tự thời gian tăng dần.",
      "prediction": "Việc thiết lập DatetimeIndex có thứ tự thời gian tăng dần là điều kiện tiên quyết bắt buộc để có thể thực hiện thao tác cắt lát theo chuỗi thời gian (Time-series Slicing) và tính toán cửa sổ trượt.",
      "solutionBasic": "import pandas as pd\n\nurl_rv = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv'\nrv_raw = pd.read_csv(url_rv, parse_dates=['date'])\n\n# 1. Lọc bỏ ngày sau mốc chụp\nmoc_chup = pd.Timestamp('2026-06-29')\nrv_clean = rv_raw[rv_raw['date'] <= moc_chup].copy()\n\n# 2. Đặt DatetimeIndex và sắp xếp\nrv_ts = rv_clean.set_index('date').sort_index()\nprint('Khoảng thời gian khảo sát:', rv_ts.index.min(), 'đến', rv_ts.index.max())",
      "solutionAdvanced": "def chuan_hoa_chuoi_thoi_gian(df: pd.DataFrame, moc_cat: str = '2026-06-29') -> pd.DataFrame:\n    \"\"\"Chuẩn hóa chuỗi thời gian phòng thủ và kiểm tra tính đơn điệu.\"\"\"\n    df_valid = df.loc[df['date'].notna()].copy()\n    ts_limit = pd.to_datetime(moc_cat)\n    df_valid = df_valid.loc[df_valid['date'] <= ts_limit]\n    df_sorted = df_valid.set_index('date').sort_index()\n    assert df_sorted.index.is_monotonic_increasing, 'Chỉ mục thời gian chưa được sắp xếp tăng dần!'\n    return df_sorted",
      "explanation": "Khi chỉ mục là DatetimeIndex đã được sắp xếp (`is_monotonic_increasing == True`), pandas có thể thực hiện tìm kiếm nhị phân với độ phức tạp $O(\\log N)$, giúp các thao tác cắt lát khoảng thời gian như `df['2024-01':'2024-03']` thực thi gần như tức thì.",
      "verification": "assert rv_ts.index.max() <= moc_chup\nassert rv_ts.index.is_monotonic_increasing"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Tổng hợp theo quý (Resample) và Bẫy kỳ snapshot chưa trọn vẹn",
      "prompt": "Sử dụng phương thức `.resample('QE')` (Quarter End) để đếm số lượt đánh giá của từng quý. Quan sát quý 2 năm 2026 (2026-Q2) kết thúc vào ngày 30/06/2026 trong khi mốc chụp là ngày 29/06/2026. Giải thích tại sao việc so sánh quý chưa trọn vẹn với các quý trước có thể gây hiểu lầm nghiêm trọng trong báo cáo kinh doanh.",
      "prediction": "Nếu quý cuối cùng bị thiếu dữ liệu dù chỉ 1 ngày hoặc chưa kết thúc toàn bộ chu kỳ kinh doanh, tổng số đánh giá của quý đó sẽ sụt giảm giả tạo, khiến người đọc nhầm tưởng rằng hoạt động du lịch đang bị suy thoái.",
      "solutionBasic": "danh_gia_quy = rv_ts.resample('QE').size()\nprint('Số đánh giá 5 quý gần nhất:\\n', danh_gia_quy.tail(5))",
      "solutionAdvanced": "def phan_tich_quy_an_toan(series_ts: pd.Series, ngay_cuoi: str) -> pd.Series:\n    \"\"\"Tổng hợp theo quý và tự động gắn cờ hoặc loại bỏ quý chưa trọn vẹn.\"\"\"\n    quy_counts = series_ts.resample('QE').size()\n    ts_end = pd.to_datetime(ngay_cuoi)\n    # Nếu ngày cuối cùng của dữ liệu không trùng ngày cuối quý, loại bỏ quý đó khỏi báo cáo tăng trưởng\n    ngay_cuoi_quy = quy_counts.index[-1]\n    if ts_end < ngay_cuoi_quy:\n        print(f'Cảnh báo: Quý {ngay_cuoi_quy.to_period(\"Q\")} chưa trọn vẹn (mới đến {ts_end.date()})')\n    return quy_counts\n\nquy_thuc_te = phan_tich_quy_an_toan(rv_ts['id'], '2026-06-29')",
      "explanation": "Nguyên tắc vàng của phân tích chuỗi thời gian: Không bao giờ so sánh một chu kỳ chưa trọn vẹn (Incomplete Period) với các chu kỳ đầy đủ trong quá khứ mà không có trọng số điều chỉnh hoặc chú thích rõ ràng.",
      "verification": "assert len(danh_gia_quy) > 0\nassert danh_gia_quy.index.freqstr.startswith('Q')"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Làm mượt chuỗi bằng Cửa sổ trượt (Rolling Window) 7 ngày",
      "prompt": "Tính tổng số lượt đánh giá theo từng ngày trong năm 2024. Vì số liệu theo ngày thường dao động mạnh do hiệu ứng ngày cuối tuần (Weekend Effect), hãy dùng `.rolling(window=7, min_periods=1).mean()` để tạo đường xu hướng trung bình trượt 7 ngày.",
      "prediction": "Đường trung bình trượt 7 ngày sẽ triệt tiêu dao động chu kỳ tuần, giúp nhận diện rõ ràng các đợt cao điểm du lịch thực sự mà không bị nhiễu bởi sự khác biệt giữa ngày trong tuần và ngày thứ Bảy, Chủ nhật.",
      "solutionBasic": "rv_2024 = rv_ts.loc['2024']\ndem_ngay = rv_2024.resample('D').size()\nma_7_ngay = dem_ngay.rolling(window=7).mean()\nprint('5 ngày đầu năm 2024:\\n', dem_ngay.head())\nprint('Trung bình trượt 7 ngày:\\n', ma_7_ngay.head(10))",
      "solutionAdvanced": "# Sử dụng cửa sổ trượt theo khoảng thời gian thực '7D'\nma_chuan = dem_ngay.rolling('7D', min_periods=1).mean()\nassert pd.notna(ma_chuan.iloc[0]), 'Với min_periods=1, giá trị ngày đầu tiên không bị NaN'\nprint('Đường làm mượt 7 ngày chuẩn mực đã sẵn sàng.')",
      "explanation": "Tham số `min_periods=1` cho phép hàm tính toán ngay từ ngày đầu tiên thay vì phải đợi đủ 7 ngày (tránh việc 6 ngày đầu tiên bị biến thành NaN).",
      "verification": "assert len(ma_7_ngay) == len(dem_ngay)\nassert ma_chuan.iloc[0] == dem_ngay.iloc[0]"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Đo lường tốc độ tăng trưởng cùng kỳ (Year-over-Year Growth)",
      "prompt": "Tính tổng số đánh giá của từng năm và sử dụng phương thức `.pct_change()` để đo lường tỷ lệ tăng trưởng cùng kỳ (YoY). So sánh số tăng trưởng tuyệt đối (số đánh giá tăng thêm) và số tăng trưởng tương đối (phần trăm).",
      "prediction": "Trong giai đoạn đầu khi quy mô thị trường còn nhỏ, tỷ lệ tăng trưởng phần trăm có thể lên tới 200-300% dù số đánh giá tăng thêm không nhiều. Ngược lại, khi thị trường đã bão hòa, mức tăng 10% có thể tương ứng với hàng chục nghìn lượt đánh giá mới.",
      "solutionBasic": "dem_nam = rv_ts.resample('YE').size()\ntang_truong_yoy = dem_nam.pct_change()\nchenh_lech_tuyet_doi = dem_nam.diff()\n\nbang_yoy = pd.DataFrame({\n    'so_luong': dem_nam,\n    'tang_tuyet_doi': chenh_lech_tuyet_doi,\n    'tang_truong_pct': (tang_truong_yoy * 100).round(1)\n})\nprint('Báo cáo tăng trưởng cùng kỳ theo năm:\\n', bang_yoy.tail(5))",
      "solutionAdvanced": "def bao_cao_yoy_chuyen_nghiep(series_ts: pd.Series) -> pd.DataFrame:\n    \"\"\"Đóng gói báo cáo YoY hoàn chỉnh kèm nhận định quy mô.\"\"\"\n    s_year = series_ts.resample('YE').size()\n    df_res = pd.DataFrame({\n        'nam': s_year.index.year,\n        'so_danh_gia': s_year.values,\n        'tang_tuyet_doi': s_year.diff().fillna(0).astype(int),\n        'tang_truong_pct': (s_year.pct_change() * 100).round(2)\n    })\n    return df_res\n\nprint(bao_cao_yoy_chuyen_nghiep(rv_ts['id']))",
      "explanation": "Trong báo cáo thống kê chuyên nghiệp, không bao giờ trình bày đơn độc tỷ lệ phần trăm tăng trưởng mà phải đặt cạnh con số cơ sở tuyệt đối để tránh bẫy ảo giác toán học từ mẫu số nhỏ.",
      "verification": "assert 'tang_truong_pct' in bang_yoy.columns\nassert pd.isna(bang_yoy['tang_truong_pct'].iloc[0])"
    }
  ]
};
