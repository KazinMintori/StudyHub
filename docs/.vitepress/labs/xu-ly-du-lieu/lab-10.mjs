// Module bài tập phòng Lab: Lab 10: Đảm bảo chất lượng chéo bảng
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-10-lam-sach-du-lieu",
  "title": "Lab 10: Đảm bảo chất lượng chéo bảng",
  "dataset": {
    "name": "Cặp bảng Chỗ ở & Đánh giá (Listings - Reviews Santiago)",
    "type": "CSV quan hệ (Relational CSVs)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "secondary_url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv",
    "description": "Kiểm định chất lượng dữ liệu chéo bảng: xác thực miền thời gian, phát hiện khóa ngoại mồ côi (foreign key orphans), đối chiếu cột dẫn xuất number_of_reviews với số dòng đếm thực tế, và đóng gói báo cáo QA chuẩn mực."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Xác định miền thời gian và ngày bất thường trong bảng đánh giá",
      "prompt": "Đọc tệp `reviews.csv` và xác định ngày đánh giá sớm nhất (`min_date`) và muộn nhất (`max_date`). Kiểm tra xem có bản ghi nào mang ngày vượt quá mốc chụp dữ liệu '2026-06-29' hay không. Đếm số dòng vi phạm nếu có.",
      "prediction": "Các hệ thống phân tán thường gặp lỗi trôi thời gian (Clock Drift) hoặc do múi giờ GMT khiến một số đánh giá vào ban đêm bị ghi nhận sang ngày hôm sau.",
      "solutionBasic": "import pandas as pd\n\nurl_rv = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv'\nrv = pd.read_csv(url_rv, parse_dates=['date'])\n\nmin_date = rv['date'].min()\nmax_date = rv['date'].max()\nso_dong_sau_moc = (rv['date'] > '2026-06-29').sum()\nprint(f'Miền thời gian: từ {min_date.date()} đến {max_date.date()}')\nprint(f'Số bản ghi sau mốc chụp: {so_dong_sau_moc}')",
      "solutionAdvanced": "def kiem_dinh_mien_thoi_gian(df_rv: pd.DataFrame, moc_chup: str) -> dict:\n    \"\"\"Kiểm định miền thời gian của bảng sự kiện.\"\"\"\n    s_date = df_rv['date'].dropna()\n    ts_moc = pd.to_datetime(moc_chup)\n    vi_pham = (s_date > ts_moc).sum()\n    return {\n        'tong_so': len(df_rv),\n        'ngay_dau': str(s_date.min().date()),\n        'ngay_cuoi': str(s_date.max().date()),\n        'so_vi_pham_tuong_lai': int(vi_pham),\n        'ty_le_vi_pham': float(vi_pham / len(df_rv))\n    }\n\nprint(kiem_dinh_mien_thoi_gian(rv, '2026-06-29'))",
      "explanation": "Kiểm tra tính hợp lệ của miền thời gian (Temporal Domain Validation) là bước phòng thủ đầu tiên trước khi xây dựng các mô hình dự báo chuỗi thời gian.",
      "verification": "assert min_date <= max_date"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Phát hiện khóa ngoại mồ côi (Foreign Key Orphan Records)",
      "prompt": "Trong mô hình quan hệ, mỗi đánh giá trong bảng `reviews` phải tham chiếu đến một chỗ ở hợp lệ trong bảng `listings` qua cột `listing_id`. Hãy tìm số lượng đánh giá bị 'mồ côi' (Orphan reviews - có `listing_id` nhưng không tồn tại trong danh sách `id` của bảng `listings`).",
      "prediction": "Các chỗ ở đã bị chủ nhà gỡ bỏ hoặc bị hệ thống khóa tài khoản có thể đã biến mất khỏi bảng listings hiện hành, nhưng lịch sử đánh giá trong quá khứ vẫn còn lưu lại trong bảng reviews.",
      "solutionBasic": "url_ls = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv'\nds = pd.read_csv(url_ls, usecols=['id'])\n\ntap_id_cho_o = set(ds['id'])\nmat_na_mo_coi = ~rv['listing_id'].isin(tap_id_cho_o)\nso_review_mo_coi = mat_na_mo_coi.sum()\nprint(f'Số lượng đánh giá mồ côi: {so_review_mo_coi:,} ({so_review_mo_coi/len(rv):.2%})')",
      "solutionAdvanced": "def tim_khoa_ngoai_mo_coi(df_con: pd.DataFrame, df_cha: pd.DataFrame, cot_khoa_con: str, cot_khoa_cha: str) -> dict:\n    \"\"\"Kiểm định toàn vẹn tham chiếu quan hệ giữa hai bảng.\"\"\"\n    set_cha = set(df_cha[cot_khoa_cha].dropna())\n    s_khoa_con = df_con[cot_khoa_con]\n    orphans = s_khoa_con[~s_khoa_con.isin(set_cha)]\n    return {\n        'tong_so_con': len(df_con),\n        'so_mo_coi': len(orphans),\n        'so_khoa_cha_thieu': orphans.nunique(),\n        'toan_ven': len(orphans) == 0\n    }\n\nprint(tim_khoa_ngoai_mo_coi(rv, ds, 'listing_id', 'id'))",
      "explanation": "Đưa các khóa của bảng cha về cấu trúc `set` trong Python giúp thao tác `.isin()` thực thi với độ phức tạp $O(1)$ thay vì phải quét tuyến tính $O(N)$ nếu để dạng danh sách.",
      "verification": "assert so_review_mo_coi >= 0"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Đối chiếu cột dẫn xuất number_of_reviews với số dòng thực tế",
      "prompt": "Cột `number_of_reviews` trong bảng chỗ ở là một cột dẫn xuất (Derived Column). Hãy đếm số lượt đánh giá thực tế của từng chỗ ở từ bảng `reviews.csv`, ghép nối với bảng `listings.csv` và kiểm tra mức độ chênh lệch giữa con số được công bố và con số thực đếm.",
      "prediction": "Số đánh giá thực đếm trong bảng reviews rút gọn có thể nhỏ hơn cột number_of_reviews trong bảng listings do chính sách bảo mật quyền riêng tư của nền tảng đã ẩn đi một số đánh giá cũ hoặc tài khoản bị xóa.",
      "solutionBasic": "dem_thuc_te = rv.groupby('listing_id').size().rename('so_dem_thuc')\nds_kiem_tra = ds.merge(dem_thuc_te, left_on='id', right_index=True, how='left')\nds_kiem_tra['so_dem_thuc'] = ds_kiem_tra['so_dem_thuc'].fillna(0).astype(int)\n\nds_kiem_tra['lech'] = ds_kiem_tra['number_of_reviews'] - ds_kiem_tra['so_dem_thuc']\nso_dong_lech = (ds_kiem_tra['lech'] != 0).sum()\nprint(f'Số chỗ ở có số đánh giá bị lệch: {so_dong_lech:,}/{len(ds)}')",
      "solutionAdvanced": "def doi_chieu_cot_dan_xuat(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Đối chiếu tính nhất quán giữa cột tổng hợp sẵn và sự kiện nguyên tử.\"\"\"\n    rv_counts = df_reviews.groupby('listing_id')['id'].count()\n    merged = df_listings[['id', 'number_of_reviews']].copy()\n    merged['so_thuc_te'] = merged['id'].map(rv_counts).fillna(0).astype(int)\n    merged['do_lech'] = merged['number_of_reviews'] - merged['so_thuc_te']\n    return merged\n\nbao_cao_lech = doi_chieu_cot_dan_xuat(ds, rv)\nprint('Phân phối độ lệch:\\n', bao_cao_lech['do_lech'].describe())",
      "explanation": "Trong kho dữ liệu, các cột dẫn xuất luôn tiềm ẩn nguy cơ mất đồng bộ (Stale Data). Quy trình kiểm tra chéo (Cross-table Reconciliation) giúp kỹ sư phát hiện sự cố đường ống dữ liệu cập nhật không trọn vẹn.",
      "verification": "assert 'so_thuc_te' in bao_cao_lech.columns"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Đóng gói báo cáo kiểm định chất lượng qa_report chuẩn mực",
      "prompt": "Viết hàm `qa_report(metrics: dict, notes: dict, out_csv: str)` đóng gói toàn bộ các chỉ số kiểm tra chất lượng từ Bài 1 đến Bài 3 vào một bảng CSV có cấu trúc chuẩn mực: `['chi_so', 'gia_tri', 'danh_gia', 'ghi_chu']`.",
      "prediction": "Báo cáo chất lượng dữ liệu tự động đóng vai trò là chứng chỉ đảm bảo dữ liệu (Data Quality Certificate) trước khi đưa các bảng vào kho lưu trữ sản xuất.",
      "solutionBasic": "def qa_report_cb(so_lieu: dict, ghi_chu: dict, out_path: str):\n    rows = []\n    for k, v in so_lieu.items():\n        rows.append({\n            'chi_so': k,\n            'gia_tri': v,\n            'danh_gia': 'ĐẠT' if v == 0 else 'CẦN XEM XÉT',\n            'ghi_chu': ghi_chu.get(k, '')\n        })\n    df_qa = pd.DataFrame(rows)\n    df_qa.to_csv(out_path, index=False)\n    return df_qa",
      "solutionAdvanced": "def qa_report_nc(metrics: dict, notes: dict, out_csv: str = 'qa_report.csv') -> pd.DataFrame:\n    \"\"\"Đóng gói báo cáo QA theo chuẩn kiểm toán kỹ thuật dữ liệu.\"\"\"\n    records = []\n    for k, val in metrics.items():\n        status = 'DAT' if val == 0 else ('CANH_BAO' if 'lech' in k else 'NGHI_VAN')\n        records.append({\n            'ma_chi_so': k,\n            'gia_tri_quan_sat': val,\n            'trang_thai_kiem_dinh': status,\n            'giai_thich_nghiep_vu': notes.get(k, 'Không có ghi chú bổ sung')\n        })\n    df_rep = pd.DataFrame(records)\n    df_rep.to_csv(out_csv, index=False, encoding='utf-8')\n    return df_rep",
      "explanation": "Một quy trình dữ liệu chuyên nghiệp luôn đi kèm với báo cáo kiểm toán có thể đọc được bằng mắt và tự động phân tích được bằng máy móc.",
      "verification": "test_m = {'orphan_reviews': 5, 'future_dates': 0}\ntest_n = {'orphan_reviews': 'Chỗ ở đã bị xóa', 'future_dates': 'Không có'}\nrep = qa_report_nc(test_m, test_n, 'test_qa.csv')\nassert os.path.exists('test_qa.csv')\nos.remove('test_qa.csv')"
    }
  ]
};
