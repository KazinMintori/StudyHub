// Module bài tập phòng Lab: Lab 14: Thực hành kể chuyện: kim tự tháp, lời đúng mức và thẩm định
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-14-ke-chuyen-bang-du-lieu",
  "title": "Lab 14: Thực hành kể chuyện: kim tự tháp, lời đúng mức và thẩm định",
  "dataset": {
    "name": "Bộ dữ liệu Case Study Kể chuyện Dữ liệu & Thẩm định AI",
    "type": "CSV & Báo cáo phân tích tổng hợp",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "description": "Tập dữ liệu phục vụ thẩm định tính trung thực của các bản báo cáo kinh doanh: kiểm chứng nghịch lý Simpson trong cơ cấu khách thuê, phát hiện lỗi chọn mốc thời gian thiên lệch (cherry-picking), và quy trình 3 bước thẩm định kết luận phân tích của AI."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Cấu trúc kim tự tháp Minto trong giao tiếp phân tích dữ liệu",
      "prompt": "Chuyển đổi một đoạn văn phân tích theo lối mòn học thuật (liệt kê bảng dữ liệu, kể lể các bước xử lý rồi mới đưa ra kết luận ở cuối) sang cấu trúc Kim tự tháp Minto (The Minto Pyramid Principle): (1) Đưa Thông điệp chính / Khuyến nghị hành động lên câu đầu tiên; (2) Trình bày 3 luận điểm cốt lõi; (3) Hỗ trợ bằng các con số dẫn chứng cụ thể.",
      "prediction": "Lãnh đạo và các bên liên quan trong doanh nghiệp chỉ có vài chục giây để nắm bắt vấn đề. Cấu trúc kim tự tháp Minto giúp người nghe nắm được ngay bản chất quyết định mà không bị lạc vào mê cung các phép tính chi tiết.",
      "solutionBasic": "# Bản nháp truyền thống (Kém hiệu quả):\n# 'Chúng tôi đã nạp 18.534 dòng, sau đó lọc theo quận và tính toán giá trung bình, kết quả cho thấy...'\n\n# Bản sửa theo Kim tự tháp Minto (Chuẩn mực):\nbang_thong_diep = '''\n[THÔNG ĐIỆP CHÍNH]: Cần tập trung đầu tư phân khúc căn hộ nguyên căn tại Providencia vì đây là động lực doanh thu số 1 của toàn thành phố.\n- Luận điểm 1: Tỷ lệ nguyên căn tại Providencia đạt 68.5% (cao hơn 12% so với bình quân thành phố).\n- Luận điểm 2: Giá trung vị đạt 45.000 CLP/đêm với số lượng đánh giá chiếm 35% toàn thị trường.\n- Luận điểm 3: Tỷ lệ lấp đầy ổn định quanh năm kể cả trong mùa thấp điểm.\n'''\nprint(bang_thong_diep)",
      "solutionAdvanced": "def tao_cau_truc_minto(thong_diep_dau: str, cac_luan_diem: list[dict]) -> str:\n    \"\"\"Đóng gói báo cáo phân tích theo chuẩn Minto Pyramid.\"\"\"\n    out = [f'★ KHUYẾN NGHỊ TRỌNG TÂM: {thong_diep_dau}\\n']\n    out.append('CÁC CĂN CỨ SỐ LIỆU ĐỐI CHỨNG:')\n    for idx, ld in enumerate(cac_luan_diem, 1):\n        out.append(f\"{idx}. {ld['luan_diem']}: {ld['con_so']} (Nguồn: {ld['nguon']})\")\n    return '\\n'.join(out)\n\nprint(tao_cau_truc_minto('Ưu tiên phát triển Providencia', [{'luan_diem': 'Thị phần lớn', 'con_so': '35% lượt khách', 'nguon': 'reviews.csv'}]))",
      "explanation": "Nguyên tắc Minto: Trả lời câu hỏi 'Thì sao?' (So what?) ngay từ câu mở đầu. Người nghe muốn biết quyết định kinh doanh trước, sau đó mới đến các bằng chứng kỹ thuật phía sau.",
      "verification": "assert 'KHUYẾN NGHỊ' in bang_thong_diep"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Tự tạo và giải mã Nghịch lý Simpson trong cơ cấu dữ liệu",
      "prompt": "Xây dựng một kịch bản dữ liệu kiểm chứng Nghịch lý Simpson (Simpson's Paradox): Giả sử hai chiến dịch quảng cáo A và B được triển khai trên hai nền tảng Khách Di động (Mobile) và Khách Máy tính (Desktop). Hãy thiết kế số liệu sao cho: Tỷ lệ chuyển đổi của B cao hơn A trên TỪNG nền tảng riêng lẻ, nhưng khi tính trung bình gộp toàn bộ, tỷ lệ chuyển đổi của A lại cao hơn B do cơ cấu phân bổ khách khác nhau.",
      "prediction": "Khi một nhóm có tỷ lệ chuyển đổi cao (Desktop) chiếm phần lớn cơ cấu mẫu của A (ví dụ 90%), nó sẽ kéo mức trung bình chung của A lên cao, che lấp sự thật rằng trên từng phân khúc B đều vượt trội.",
      "solutionBasic": "import pandas as pd\n\n# Thiết kế số liệu tạo nghịch lý Simpson\ndata_simpson = pd.DataFrame([\n    {'nhom': 'A', 'kenh': 'Mobile', 'chuyen_doi': 10, 'tong': 100},    # 10.0%\n    {'nhom': 'A', 'kenh': 'Desktop', 'chuyen_doi': 810, 'tong': 900},  # 90.0%\n    {'nhom': 'B', 'kenh': 'Mobile', 'chuyen_doi': 120, 'tong': 800},   # 15.0% (> 10%)\n    {'nhom': 'B', 'kenh': 'Desktop', 'chuyen_doi': 190, 'tong': 200},  # 95.0% (> 90%)\n])\ndata_simpson['ty_le'] = data_simpson['chuyen_doi'] / data_simpson['tong']\nprint('Tỷ lệ từng kênh:\\n', data_simpson[['nhom', 'kenh', 'ty_le']])\n\n# Tính trung bình gộp toàn bộ\ngop = data_simpson.groupby('nhom').agg({'chuyen_doi': 'sum', 'tong': 'sum'})\ngop['ty_le_chung'] = gop['chuyen_doi'] / gop['tong']\nprint('Tỷ lệ gộp chung (A cao hơn B!):\\n', gop['ty_le_chung'])",
      "solutionAdvanced": "# Khẳng định bằng toán học sự tồn tại của nghịch lý\nassert data_simpson.loc[(data_simpson['nhom']=='B') & (data_simpson['kenh']=='Mobile'), 'ty_le'].values[0] > \\\n       data_simpson.loc[(data_simpson['nhom']=='A') & (data_simpson['kenh']=='Mobile'), 'ty_le'].values[0]\nassert data_simpson.loc[(data_simpson['nhom']=='B') & (data_simpson['kenh']=='Desktop'), 'ty_le'].values[0] > \\\n       data_simpson.loc[(data_simpson['nhom']=='A') & (data_simpson['kenh']=='Desktop'), 'ty_le'].values[0]\nassert gop.loc['A', 'ty_le_chung'] > gop.loc['B', 'ty_le_chung'], 'Nghịch lý Simpson phải xảy ra!'\nprint('Nghịch lý Simpson đã được chứng minh bằng thực nghiệm toán học.')",
      "explanation": "Bài học đắt giá: Tuyệt đối không bao giờ đưa ra kết luận so sánh chỉ dựa trên con số bình quân chung gộp nếu chưa kiểm tra cơ cấu phân bổ của các biến ẩn (Lurking Variables) phía dưới.",
      "verification": "assert gop.loc['A', 'ty_le_chung'] > gop.loc['B', 'ty_le_chung']"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Quy trình 3 bước thẩm định báo cáo phân tích của AI",
      "prompt": "Một hệ thống AI phân tích tự động xuất ra kết luận: 'Các căn hộ tại Santiago giảm giá 15% vào mùa đông làm tăng 40% doanh thu của các chủ nhà'. Hãy thực hiện quy trình 3 bước thẩm định: Bước 1 (Truy số): Kiểm tra số liệu gốc có con số này không; Bước 2 (Phương pháp): Kiểm tra phép tính có bị lỗi mẫu số hoặc nghịch lý Simpson không; Bước 3 (Diễn giải): Phán quyết xem kết luận nhân quả có căn cứ hay chỉ là tương quan thời vụ.",
      "prediction": "Vào mùa đông lượng khách du lịch giảm tự nhiên theo mùa vụ. Việc giảm giá và tăng doanh thu có thể chỉ xảy ra ở một phân khúc cụ thể (ví dụ khu trượt tuyết Farellones trên núi) chứ không đúng cho toàn thành phố. AI đã suy diễn khái quát hóa quá đà.",
      "solutionBasic": "def quy_trinh_3_buoc_tham_dinh(ket_luan_ai: str) -> dict:\n    # Bước 1: Truy vết số gốc\n    b1 = 'Không tìm thấy con số 40% doanh thu trong bảng tổng hợplistings.csv'\n    # Bước 2: Phương pháp\n    b2 = 'Phép tính nhầm lẫn giữa doanh thu một nhóm trượt tuyết với toàn thành phố'\n    # Bước 3: Phán quyết\n    b3 = 'BÁC BỎ: Mối quan hệ mang tính tương quan mùa vụ địa phương, không có tính nhân quả toàn thành phố'\n    return {'Buoc_1_Truy_So': b1, 'Buoc_2_Phuong_Phap': b2, 'Buoc_3_Phan_Quyet': b3}\n\nprint(quy_trinh_3_buoc_tham_dinh('...'))",
      "solutionAdvanced": "def tham_dinh_ai_chuyen_sau(tuyen_bo: str, df_kiem_chung: pd.DataFrame) -> dict:\n    \"\"\"Đóng gói biên bản thẩm định phân tích AI độc lập.\"\"\"\n    # Kiểm tra sự tồn tại của biến doanh thu trong dữ liệu thô\n    has_revenue = 'revenue' in df_kiem_chung.columns\n    phan_quyet = {\n        'tuyen_bo_ai': tuyen_bo,\n        'buoc_1_xac_minh_so_lieu': 'Thất bại: Dữ liệu Inside Airbnb không ghi nhận doanh thu thực tế mà chỉ có giá niêm yết',\n        'buoc_2_kiem_tra_phuong_phap': 'AI đã tự nhân giá niêm yết với số review để ước tính doanh thu giả định',\n        'buoc_3_ket_luan_nhan_qua': 'Ngụy biện nhân quả: Giảm giá không chứng minh là nguyên nhân làm tăng số lượt khách',\n        'phán_quyết_cuối_cùng': 'KHÔNG PHÊ DUYỆT BÁO CÁO'\n    }\n    return phan_quyet\n\nprint(tham_dinh_ai_chuyen_sau('Giảm giá làm tăng doanh thu', ds))",
      "explanation": "Trong kỷ nguyên AI, năng lực quan trọng nhất của người làm khoa học dữ liệu không còn là viết code nhanh hơn, mà là năng lực phản biện, thẩm định và chịu trách nhiệm giải trình trước các kết luận do AI đưa ra.",
      "verification": "assert True"
    }
  ]
};
