// Module bài tập phòng Lab: Lab 4: Lập hồ sơ một quận bằng pandas
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-04-lam-quen-pandas",
  "title": "Lab 4: Lập hồ sơ một quận bằng pandas",
  "dataset": {
    "name": "Hồ sơ quận Providencia (Santiago, Chile)",
    "type": "CSV (Pandas DataFrame có nhãn)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "description": "Tập con dữ liệu bao gồm 5.247 chỗ ở tại quận trung tâm Providencia, Santiago. Chứa các trường: id, name, neighbourhood, room_type, price, minimum_nights, number_of_reviews."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Cắt riêng một quận và thẩm định bảng bằng quy trình 5 bước",
      "prompt": "Đọc tệp `listings.csv`, lọc riêng các chỗ ở thuộc quận 'Providencia' và lưu thành DataFrame `df_pro`. Áp dụng thói quen 5 bước thẩm định: (1) `shape`, (2) `head()`, (3) `dtypes`, (4) kiểm tra ô thiếu `isna().sum()`, (5) thống kê phân phối `describe()`.",
      "prediction": "Providencia là quận trung tâm thương mại và tài chính của Santiago, chiếm khoảng 25-30% tổng số chỗ ở của toàn thành phố với tỷ lệ phòng nguyên căn cao.",
      "solutionBasic": "import pandas as pd\n\nurl = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv'\ndf = pd.read_csv(url)\ndf_pro = df[df['neighbourhood'] == 'Providencia'].copy()\n\nprint('Kích thước quận Providencia:', df_pro.shape)\nprint('Số lượng ô thiếu:\\n', df_pro.isna().sum())",
      "solutionAdvanced": "def tham_dinh_ho_so_quan(df_all: pd.DataFrame, ten_quan: str) -> pd.DataFrame:\n    \"\"\"Trích xuất và kiểm định hồ sơ quận với kiểm tra bất biến.\"\"\"\n    df_quan = df_all.loc[df_all['neighbourhood'] == ten_quan].copy()\n    assert not df_quan.empty, f'Không tìm thấy dữ liệu cho quận {ten_quan}'\n    \n    # Kiểm định tính duy nhất của khóa chính id\n    assert df_quan['id'].is_unique, 'Khóa chính id bị trùng lặp!'\n    return df_quan\n\ndf_pro = tham_dinh_ho_so_quan(df, 'Providencia')",
      "explanation": "Luôn dùng `.copy()` khi tạo DataFrame con từ một phép lọc. Nếu không dùng `.copy()`, các phép gán sau này sẽ kích hoạt cảnh báo SettingWithCopyWarning do pandas không xác định được đó là View hay Copy.",
      "verification": "assert len(df_pro) > 0\nassert (df_pro['neighbourhood'] == 'Providencia').all()"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Lọc kết hợp đa điều kiện và bẫy độ ưu tiên toán tử",
      "prompt": "Lọc các chỗ ở tại Providencia thỏa mãn đồng thời: (1) là căn hộ nguyên căn (`room_type == 'Entire home/apt'`); (2) giá mỗi đêm không vượt quá 60.000 CLP; (3) số đêm tối thiểu không quá 3 đêm. Đếm số lượng chỗ ở thỏa mãn.",
      "prediction": "Việc kết hợp nhiều điều kiện thực tế sẽ thu hẹp đáng kể tập dữ liệu, phục vụ nhóm khách du lịch cá nhân tìm kiếm chỗ ở bình dân và linh hoạt thời gian lưu trú.",
      "solutionBasic": "dieu_kien = (\n    (df_pro['room_type'] == 'Entire home/apt') &\n    (df_pro['price'] <= 60000) &\n    (df_pro['minimum_nights'] <= 3)\n)\nphong_phu_hop = df_pro[dieu_kien]\nprint('Số phòng thỏa mãn:', len(phong_phu_hop))",
      "solutionAdvanced": "# Sử dụng phương thức .query() giúp câu lệnh trực quan hơn\nphong_phu_hop_query = df_pro.query(\n    \"room_type == 'Entire home/apt' and price <= 60000 and minimum_nights <= 3\"\n)\nprint('Số lượng phòng (Query):', len(phong_phu_hop_query))\nassert len(phong_phu_hop) == len(phong_phu_hop_query)",
      "explanation": "Trong pandas, khi dùng toán tử bitwise `&`, bắt buộc phải bọc từng vế trong ngoặc đơn `()`. Nếu viết `df.col == a & df.col <= b`, Python sẽ đánh giá `a & df.col` trước gây lỗi TypeError.",
      "verification": "assert len(phong_phu_hop) <= len(df_pro)"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Sửa đổi giá trị bảng an toàn bằng .loc và tính lại cột phụ thuộc",
      "prompt": "Trong tệp dữ liệu có một số chỗ ở ghi nhận giá bằng 0 hoặc giá âm bất hợp lý do chủ nhà nhập thử nghiệm. Hãy dùng `.loc` để gán các giá trị `price <= 0` thành `np.nan`. Sau đó, tạo một cột mới `tong_chi_phi_toi_thieu = price * minimum_nights` và quan sát ảnh hưởng của giá trị thiếu.",
      "prediction": "Các phép toán số học thực hiện trên giá trị `NaN` sẽ tự động lan truyền thành `NaN` (`NaN * 3 == NaN`), giúp bảo vệ các chỉ số thống kê không bị sai lệch bởi các giá trị giả tạo.",
      "solutionBasic": "import numpy as np\n\ndf_pro.loc[df_pro['price'] <= 0, 'price'] = np.nan\ndf_pro['tong_chi_phi_toi_thieu'] = df_pro['price'] * df_pro['minimum_nights']\nprint('Số dòng bị gán NaN do giá không hợp lệ:', df_pro['price'].isna().sum())",
      "solutionAdvanced": "# Sửa đổi chuẩn mực và kiểm tra số quan sát hợp lệ\nso_dong_am = (df_pro['price'] <= 0).sum()\ndf_pro.loc[df_pro['price'] <= 0, 'price'] = np.nan\n\n# Đảm bảo phép nhân không tạo ra số âm\nassert (df_pro['price'].dropna() > 0).all(), 'Vẫn còn giá không dương sau khi làm sạch!'",
      "explanation": "Tuyệt đối không dùng cú pháp nối tiếp `df['price'][df['price'] <= 0] = np.nan` vì đây là cú pháp Chained Assignment, có thể chỉ sửa đổi trên một bản sao tạm thời mà không cập nhật vào DataFrame gốc.",
      "verification": "assert (df_pro.loc[df_pro['price'].isna(), 'tong_chi_phi_toi_thieu'].isna()).all()"
    },
    {
      "id": "task-4",
      "title": "Bài 4: So sánh chỉ số quận với toàn thành phố và xuất hồ sơ ra CSV",
      "prompt": "Tính mức giá trung vị và tỷ lệ căn hộ nguyên căn của quận Providencia và so sánh với mức bình quân chung của toàn thành phố Santiago. Xuất DataFrame hồ sơ quận Providencia ra tệp `ho_so_providencia.csv` và kiểm tra tệp vừa tạo.",
      "prediction": "Providencia là khu vực trung tâm hiện đại, dự đoán mức giá trung vị và tỷ lệ nguyên căn đều sẽ cao hơn mức trung bình toàn thành phố Santiago.",
      "solutionBasic": "med_quan = df_pro['price'].median()\nmed_tp = df['price'].median()\nprint(f'Giá trung vị Providencia: {med_quan:,.0f} CLP vs Toàn thành phố: {med_tp:,.0f} CLP')\n\n# Xuất tệp không mang theo chỉ mục số nguyên\ndf_pro.to_csv('ho_so_providencia.csv', index=False)",
      "solutionAdvanced": "def xuat_ho_so_va_doi_chieu(df_quan: pd.DataFrame, df_all: pd.DataFrame, file_out: str):\n    bao_cao_so_sanh = {\n        'quan': 'Providencia',\n        'gia_trung_vi_quan': float(df_quan['price'].median()),\n        'gia_trung_vi_toan_tp': float(df_all['price'].median()),\n        'chenh_lech_phan_tram': round((df_quan['price'].median() - df_all['price'].median()) / df_all['price'].median() * 100, 2)\n    }\n    df_quan.to_csv(file_out, index=False, encoding='utf-8')\n    return bao_cao_so_sanh\n\nso_sanh = xuat_ho_so_va_doi_chieu(df_pro, df, 'ho_so_providencia.csv')\nprint(so_sanh)",
      "explanation": "Khi xuất dữ liệu bằng `.to_csv()`, luôn đặt `index=False` trừ khi chỉ mục có ý nghĩa thời gian hoặc khóa nghiệp vụ, tránh việc khi đọc lại file sẽ bị sinh thêm cột thừa `Unnamed: 0`.",
      "verification": "assert os.path.exists('ho_so_providencia.csv')\nos.remove('ho_so_providencia.csv') if os.path.exists('ho_so_providencia.csv') else None"
    }
  ]
};
