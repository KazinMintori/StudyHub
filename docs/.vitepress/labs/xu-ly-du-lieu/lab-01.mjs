// Module bài tập phòng Lab: Lab 1: Làm quen Colab & Quy trình làm việc với AI
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-01-tong-quan-cong-cu-chinh-sach-ai",
  "title": "Lab 1: Làm quen Colab & Quy trình làm việc với AI",
  "dataset": {
    "name": "Inside Airbnb Santiago (Bản visualisations rút gọn)",
    "type": "CSV (Bảng dữ liệu phẳng)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "description": "Bảng tổng hợp 18.534 chỗ ở tại Santiago (Chile) snapshot 2026-06-29: Định danh, tên phòng, chủ nhà, khu vực, loại phòng, mức giá (CLP), số đêm tối thiểu, số đánh giá."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Khám phá bẫy trạng thái ẩn của IPython Kernel",
      "prompt": "Trong môi trường Jupyter Notebook, trạng thái bộ nhớ do hạt nhân (Kernel) quản lý độc lập với thứ tự hiển thị của các ô mã. Hãy thực hiện hai thí nghiệm: (1) Khởi tạo biến `so_phong = 4` ở ô A, in giá trị ở ô B, sau đó xóa ô A; (2) Khởi tạo `dem = 0` ở ô C, chạy ô D chứa `dem += 1` liên tiếp 3 lần. Giải thích tại sao việc này có thể gây sai lệch kết quả khi bàn giao mã nguồn.",
      "prediction": "Dù xóa ô A, ô B vẫn chạy được và in ra 4 vì biến vẫn tồn tại trong RAM của Kernel. Ô D chạy 3 lần sẽ khiến `dem` có giá trị bằng 3 thay vì 1. Điều này chứng minh thứ tự hiển thị trong notebook không cam kết thứ tự thực thi thực tế.",
      "solutionBasic": "# Thí nghiệm chạy tuần tự trực tiếp trong notebook\nso_phong = 4\nprint('Số phòng:', so_phong)\n\n# Thí nghiệm tăng biến đếm\ndem = 0\nfor _ in range(3):\n    dem += 1\nprint('Giá trị sau 3 lần tăng:', dem)",
      "solutionAdvanced": "# Đóng gói quy trình kiểm soát trạng thái bằng hàm thuần khiết (Pure Function)\ndef tinh_trang_thai_lap(so_lan_tang: int, gia_tri_dau: int = 0) -> int:\n    \"\"\"Hàm thuần khiết không phụ thuộc và không làm thay đổi biến toàn cục.\"\"\"\n    ket_qua = gia_tri_dau\n    for _ in range(so_lan_tang):\n        ket_qua += 1\n    return ket_qua\n\ndem_chuan = tinh_trang_thai_lap(3)\nprint('Biến đếm chuẩn mực:', dem_chuan)",
      "explanation": "Bẫy trạng thái ẩn (Hidden State Trap) là nguyên nhân hàng đầu khiến các mã nguồn phân tích dữ liệu không thể tái lập. Chuẩn mực chuyên nghiệp là luôn sử dụng thao tác 'Restart Kernel & Run All Cells' trước khi bàn giao báo cáo.",
      "verification": "assert dem_chuan == 3, 'Giá trị đếm phải bằng 3 sau 3 chu kỳ lặp.'\nassert tinh_trang_thai_lap(0) == 0, 'Giá trị cơ sở phải được bảo toàn.'"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Đọc cấu trúc bảng dữ liệu thực tế và nhận diện loại phòng phổ biến",
      "prompt": "Đọc tệp dữ liệu `listings.csv` từ Inside Airbnb Santiago bằng thư viện pandas. Hãy xác định tổng số dòng (số chỗ ở quan sát) và tìm loại phòng (`room_type`) chiếm số lượng áp đảo nhất trong toàn thành phố.",
      "prediction": "Santiago là đô thị du lịch lớn, dự đoán loại phòng nguyên căn (Entire home/apt) sẽ chiếm tỷ trọng cao nhất do xu hướng thương mại hóa căn hộ cho thuê ngắn hạn.",
      "solutionBasic": "import pandas as pd\n\nurl = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv'\nds = pd.read_csv(url)\n\nso_dong = ds.shape[0]\nloai_phong_counts = ds['room_type'].value_counts()\nloai_nhieu_nhat = loai_phong_counts.index[0]\n\nprint(f'Tổng số chỗ ở: {so_dong:,}')\nprint(f'Loại phòng phổ biến nhất: {loai_nhieu_nhat} ({loai_phong_counts.iloc[0]:,} chỗ ở)')",
      "solutionAdvanced": "import pandas as pd\n\ndef phan_tich_co_cau_phong(data_url: str) -> dict:\n    \"\"\"Đọc phòng thủ và phân tích cơ cấu loại chỗ ở.\"\"\"\n    df = pd.read_csv(data_url, usecols=['id', 'room_type'], low_memory=False)\n    assert not df.empty, 'Bảng dữ liệu không được rỗng'\n    \n    counts = df['room_type'].value_counts(dropna=False)\n    return {\n        'tong_so': len(df),\n        'loai_chu_dao': counts.index[0],\n        'so_luong_chu_dao': int(counts.iloc[0]),\n        'co_cau': (counts / len(df)).to_dict()\n    }\n\nket_qua = phan_tich_co_cau_phong(url)\nprint(ket_qua)",
      "explanation": "Việc chỉ tải các cột cần thiết (`usecols=['id', 'room_type']`) giúp giảm tải đáng kể dung lượng bộ nhớ RAM và tăng tốc độ đọc dữ liệu đối với các bảng có hàng chục nghìn dòng.",
      "verification": "assert so_dong == 18534 or so_dong > 0, 'Phải đọc được toàn bộ danh sách chỗ ở.'\nassert loai_nhieu_nhat == 'Entire home/apt', 'Toàn bộ căn hộ là loại hình phổ biến nhất.'"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Tính tỷ lệ căn hộ nguyên căn bằng thao tác Vector hóa",
      "prompt": "Tính tỷ lệ phần trăm chỗ ở thuộc loại 'Entire home/apt' trên tổng số chỗ ở toàn thành phố Santiago. So sánh hiệu năng giữa việc duyệt vòng lặp truyền thống và phép toán vector hóa trên Series Boolean của pandas.",
      "prediction": "Phép lấy trung bình của mảng Boolean (`(series == target).mean()`) tương đương trực tiếp với việc đếm số phần tử True rồi chia cho tổng số dòng, nhưng chạy nhanh hơn hàng chục lần so với vòng lặp Python thuần vì được tối ưu ở tầng mã C.",
      "solutionBasic": "tong_so = len(ds)\nso_nguyen_can = 0\nfor loai in ds['room_type']:\n    if loai == 'Entire home/apt':\n        so_nguyen_can += 1\nty_le_cb = so_nguyen_can / tong_so if tong_so > 0 else 0.0\nprint(f'Tỷ lệ nguyên căn (Cơ bản): {ty_le_cb:.2%}')",
      "solutionAdvanced": "# Vector hóa ở tầng C của NumPy/pandas\nmat_na_nguyen_can = (ds['room_type'] == 'Entire home/apt')\nty_le_nc = mat_na_nguyen_can.mean()\nprint(f'Tỷ lệ nguyên căn (Vector hóa): {ty_le_nc:.2%}')",
      "explanation": "Trong đại số máy tính, kiểu Boolean quy ước True bằng 1 và False bằng 0. Do đó, hàm `.mean()` tính trung bình cộng của các giá trị 1 và 0 chính là tỷ lệ phần trăm các dòng thỏa mãn điều kiện.",
      "verification": "assert abs(ty_le_nc - ty_le_cb) < 1e-9, 'Hai cách tiếp cận phải trả về kết quả số học hoàn toàn trùng khớp.'\nassert 0.5 < ty_le_nc < 0.8, 'Tỷ lệ căn hộ nguyên căn tại Santiago nằm trong khoảng 50% đến 80%.'"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Đóng gói hàm phân tích thị trường độc lập (Mở rộng E1)",
      "prompt": "Xây dựng hàm `dong_goi_bao_cao_thi_truong(data: pd.DataFrame) -> dict` nhận vào DataFrame chỗ ở và xuất ra từ điển báo cáo hoàn chỉnh gồm: số lượng chỗ ở, giá trung bình, giá trung vị, tỷ lệ nguyên căn, và nhận định sơ bộ về sự phân hóa của thị trường.",
      "prediction": "Thị trường lưu trú thường có phân phối giá lệch phải mạnh (Right-skewed) do có một nhóm nhỏ biệt thự hoặc penthouse giá rất cao, vì vậy giá trung bình sẽ cao hơn đáng kể so với giá trung vị.",
      "solutionBasic": "def dong_goi_bao_cao_cb(df: pd.DataFrame) -> dict:\n    gia = df['price'].dropna()\n    return {\n        'tong_so': len(df),\n        'gia_trung_binh': float(gia.mean()) if len(gia) > 0 else 0.0,\n        'gia_trung_vi': float(gia.median()) if len(gia) > 0 else 0.0,\n        'ty_le_nguyen_can': float((df['room_type'] == 'Entire home/apt').mean())\n    }",
      "solutionAdvanced": "def dong_goi_bao_cao_nc(df: pd.DataFrame) -> dict:\n    \"\"\"Đóng gói phân tích thị trường có xử lý ngoại lệ phòng thủ.\"\"\"\n    if df.empty:\n        return {'trang_thai': 'RONG', 'tong_so': 0}\n    \n    gia_clean = pd.to_numeric(df['price'], errors='coerce').dropna()\n    gia_mean = float(gia_clean.mean()) if not gia_clean.empty else 0.0\n    gia_median = float(gia_clean.median()) if not gia_clean.empty else 0.0\n    ty_le = float((df['room_type'] == 'Entire home/apt').mean())\n    \n    lech_chuan = ((gia_mean - gia_median) / gia_median) if gia_median > 0 else 0.0\n    \n    return {\n        'tong_so': len(df),\n        'gia_trung_binh': round(gia_mean, 2),\n        'gia_trung_vi': round(gia_median, 2),\n        'ty_le_nguyen_can': round(ty_le * 100, 2),\n        'phan_hoa_gia': 'Lệch phải cao' if lech_chuan > 0.15 else 'Tương đối đồng đều'\n    }",
      "explanation": "Hàm chuyên nghiệp luôn kiểm tra trường hợp bảng dữ liệu đầu vào bị rỗng và xử lý các giá trị không thể ép kiểu số (`errors='coerce'`) để tránh làm sập toàn bộ đường ống phân tích trong sản xuất.",
      "verification": "bao_cao = dong_goi_bao_cao_nc(ds)\nassert 'tong_so' in bao_cao and 'gia_trung_vi' in bao_cao\nassert bao_cao['tong_so'] > 0"
    }
  ]
};
