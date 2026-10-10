// Module bài tập phòng Lab: Lab 5: Phân khúc giá & host chuyên nghiệp (groupby, transform, merge)
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-05-series-dataframe-chuyen-sau",
  "title": "Lab 5: Phân khúc giá & host chuyên nghiệp (groupby, transform, merge)",
  "dataset": {
    "name": "Inside Airbnb Santiago (Bảng đa chiều 18.534 chỗ ở)",
    "type": "CSV (Pandas DataFrame có cấu trúc quan hệ)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "description": "Bảng dữ liệu 18.534 chỗ ở phân bố tại 34 quận và 4 loại phòng của thủ đô Santiago. Phục vụ phân tích phân khúc giá (Bình dân, Tầm trung, Cao cấp), nhận diện chủ nhà chuyên nghiệp (host_id sở hữu từ 2 chỗ ở trở lên), thực hiện kỹ thuật transform gắn quy mô quận vào từng dòng và ghép nối merge có kiểm định quan hệ validate='1:m'."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Phân biệt truy xuất loc theo nhãn và iloc theo vị trí",
      "prompt": "Cho DataFrame chỗ ở với chỉ mục đã bị xáo trộn hoặc đặt nhãn tùy ý. Hãy thực hiện hai thao tác cắt lát: (1) Dùng `.loc['10':'20']` để chọn theo nhãn chỉ mục; (2) Dùng `.iloc[10:20]` để chọn theo vị trí số nguyên từ dòng 10 đến 19. Nêu rõ sự khác biệt về việc bao gồm cận cuối (endpoint inclusion).",
      "prediction": "Phương thức `.loc` sẽ lấy cả hai đầu mút (bao gồm cả nhãn '20'), trong khi phương thức `.iloc` tuân thủ quy ước cắt lát tiêu chuẩn của Python (lấy từ chỉ số 10 đến 19, không bao gồm chỉ số 20).",
      "solutionBasic": "import pandas as pd\n\nurl = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv'\ndf = pd.read_csv(url)\n\n# Lấy theo vị trí số nguyên\nsub_iloc = df.iloc[0:5]\nprint('Số dòng iloc[0:5]:', len(sub_iloc)) # Trả về đúng 5 dòng",
      "solutionAdvanced": "# Đặt chỉ mục có ý nghĩa và so sánh hành vi\ndf_custom = df.set_index('id')\n# loc tra cứu theo nhãn khóa chính id\nsub_loc = df_custom.loc[df_custom.index[0]:df_custom.index[4]]\nprint('Số dòng loc theo khoảng nhãn:', len(sub_loc))\nassert len(sub_iloc) == 5",
      "explanation": "Quy tắc cốt lõi: `.loc` tra cứu theo nhãn (Labels) và luôn lấy cả hai cận đầu cuối vì nhãn có thể là chuỗi ký tự hoặc ngày tháng; `.iloc` tra cứu theo vị trí số nguyên (Integer positions) và không lấy cận cuối.",
      "verification": "assert len(sub_iloc) == 5\nassert sub_iloc.index[0] == df.index[0]"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Cơ chế tự động căn chỉnh nhãn (Index Alignment) khi tính toán",
      "prompt": "Khởi tạo hai Series giá phòng với tập chỉ mục khác nhau: `s1` có chỉ mục ['a', 'b', 'c'] và `s2` có chỉ mục ['b', 'c', 'd']. Thực hiện phép cộng `s1 + s2`. Giải thích tại sao nhãn 'a' và 'd' lại mang giá trị `NaN` và cách dùng `.add(fill_value=0)` để bảo toàn số liệu.",
      "prediction": "Khi thực hiện phép toán giữa hai đối tượng pandas, hệ thống sẽ tự động ghép nối theo nhãn chỉ mục (Index Alignment). Nhãn nào chỉ xuất hiện ở một phía sẽ không tìm thấy đối tác tương ứng ở phía kia, dẫn đến việc sinh ra giá trị thiếu NaN.",
      "solutionBasic": "s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])\ns2 = pd.Series([40, 50, 60], index=['b', 'c', 'd'])\ncong_tu_nhien = s1 + s2\nprint('Cộng tự nhiên (sinh NaN):\\n', cong_tu_nhien)",
      "solutionAdvanced": "# Sử dụng phương thức số học kèm tham số fill_value\ncong_bao_toan = s1.add(s2, fill_value=0)\nprint('Cộng bảo toàn bằng fill_value=0:\\n', cong_bao_toan)\nassert cong_bao_toan['a'] == 10 and cong_bao_toan['d'] == 60",
      "explanation": "Cơ chế Alignment là một trong những tính năng mạnh mẽ nhất của pandas giúp ngăn ngừa lỗi lệch dòng khi ghép nối dữ liệu không cùng thứ tự, nhưng cũng là nguồn sinh ra NaN nếu người phân tích không hiểu rõ tập nhãn của hai bên.",
      "verification": "assert pd.isna(cong_tu_nhien['a'])\nassert cong_bao_toan['b'] == 60"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Tạo cột phân khúc giá bằng map và hàm logic",
      "prompt": "Dựa trên mức giá mỗi đêm `price`, hãy phân chia toàn bộ 18.534 chỗ ở thành 3 phân khúc: 'Bình dân' (dưới 35.000 CLP), 'Tầm trung' (từ 35.000 đến dưới 100.000 CLP), và 'Cao cấp' (từ 100.000 CLP trở lên). Gắn kết quả vào cột mới `phan_khuc`.",
      "prediction": "Hàm `.map()` hoặc `.apply()` ánh xạ từng giá trị số của cột giá qua hàm phân loại logic. Đa số chỗ ở tại Santiago sẽ nằm ở phân khúc Bình dân và Tầm trung.",
      "solutionBasic": "def xep_phan_khuc(gia):\n    if pd.isna(gia) or gia <= 0:\n        return 'Không xác định'\n    elif gia < 35000:\n        return 'Bình dân'\n    elif gia < 100000:\n        return 'Tầm trung'\n    else:\n        return 'Cao cấp'\n\ndf['phan_khuc'] = df['price'].map(xep_phan_khuc)\nprint('Phân bổ các phân khúc:\\n', df['phan_khuc'].value_counts())",
      "solutionAdvanced": "# Sử dụng pd.cut để tối ưu hóa vector hóa với kiểu dữ liệu Category\nbins = [0, 35000, 100000, float('inf')]\nlabels = ['Bình dân', 'Tầm trung', 'Cao cấp']\ndf['phan_khuc_cut'] = pd.cut(df['price'], bins=bins, labels=labels, right=False)\nprint('Phân bổ bằng pd.cut:\\n', df['phan_khuc_cut'].value_counts())",
      "explanation": "Phương thức `pd.cut()` chạy trên mã nguồn C tối ưu hóa hiệu năng cao hơn việc gọi một hàm Python thuần qua `.map()`, đồng thời trả về kiểu dữ liệu Category giúp tiết kiệm 70% bộ nhớ RAM so với kiểu chuỗi Object.",
      "verification": "assert 'phan_khuc' in df.columns\nassert len(df['phan_khuc'].unique()) >= 3"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Tổng hợp dữ liệu nâng cao bằng agg với cú pháp đặt tên cột",
      "prompt": "Gom nhóm theo `phan_khuc` và sử dụng cú pháp Named Aggregation của pandas để tính toán đồng thời: số lượng chỗ ở (`so_cho_o = ('id', 'count')`), giá trung bình (`gia_tb = ('price', 'mean')`), giá trung vị (`gia_tv = ('price', 'median')`), và số đêm tối thiểu trung bình (`dem_tt_tb = ('minimum_nights', 'mean')`).",
      "prediction": "Named Aggregation cho phép định nghĩa trực tiếp tên cột mới ở đầu ra đi liền với hàm tổng hợp, loại bỏ hoàn toàn việc phải đổi tên MultiIndex phức tạp sau khi groupby.",
      "solutionBasic": "bang_thong_ke = df.groupby('phan_khuc').agg(\n    so_cho_o=('id', 'count'),\n    gia_tb=('price', 'mean'),\n    gia_tv=('price', 'median'),\n    dem_tt_tb=('minimum_nights', 'mean')\n).reset_index()\nprint('Bảng thống kê 3 phân khúc:\\n', bang_thong_ke)",
      "solutionAdvanced": "def thong_ke_phan_khuc_chuan(df_in: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Tổng hợp nhóm có kiểm soát kiểu và làm tròn tiền tệ.\"\"\"\n    res = df_in.groupby('phan_khuc', observed=False).agg(\n        so_cho_o=('id', 'count'),\n        gia_tb=('price', 'mean'),\n        gia_tv=('price', 'median')\n    )\n    res['gia_tb'] = res['gia_tb'].round(0)\n    res['ty_le'] = (res['so_cho_o'] / len(df_in) * 100).round(2)\n    return res.sort_values(by='gia_tv')\n\nprint(thong_ke_phan_khuc_chuan(df))",
      "explanation": "Cú pháp Named Aggregation `df.groupby().agg(ten_moi=('cot', 'ham'))` là chuẩn mực hiện đại của pandas (từ phiên bản 0.25 trở lên), giúp mã nguồn tường minh và không làm phát sinh MultiIndex ở cấp cột.",
      "verification": "assert 'so_cho_o' in bang_thong_ke.columns and 'gia_tb' in bang_thong_ke.columns\nassert len(bang_thong_ke) >= 3"
    },
    {
      "id": "task-5",
      "title": "Bài 5: Nhận diện host chuyên nghiệp và kỹ thuật transform gắn quy mô quận",
      "prompt": "Một chủ nhà (`host_id`) được xếp vào nhóm 'Chuyên nghiệp' nếu sở hữu từ 2 chỗ ở trở lên trong tập dữ liệu. Hãy tạo cột Boolean `la_host_chuyen_nghiep`. Tiếp theo, dùng phương thức `.transform('count')` để gắn trực tiếp quy mô tổng số chỗ ở của từng quận vào từng dòng tương ứng của bảng gốc.",
      "prediction": "Phương thức `.agg()` sẽ thu gọn số dòng bằng số lượng nhóm, trong khi `.transform()` sẽ trả về một Series có kích thước hoàn toàn bằng kích thước DataFrame gốc, giúp gắn kết quả tính toán nhóm vào từng bản ghi mà không cần merge.",
      "solutionBasic": "# 1. Nhận diện host chuyên nghiệp\nhost_counts = df['host_id'].value_counts()\ndf['la_host_chuyen_nghiep'] = df['host_id'].map(lambda hid: host_counts.get(hid, 0) >= 2)\n\n# 2. Gắn quy mô quận bằng transform\ndf['quy_mo_quan'] = df.groupby('neighbourhood')['id'].transform('count')\nprint(df[['id', 'neighbourhood', 'quy_mo_quan', 'la_host_chuyen_nghiep']].head())",
      "solutionAdvanced": "# Tối ưu hóa đếm số lượng bằng transform('size') ở tầng C\ndf['host_listings_count_tinh'] = df.groupby('host_id')['id'].transform('size')\ndf['la_host_chuyen_nghiep_nc'] = df['host_listings_count_tinh'] >= 2\nassert (df['la_host_chuyen_nghiep'] == df['la_host_chuyen_nghiep_nc']).all()",
      "explanation": "Kỹ thuật `.transform()` là công cụ đắc lực khi cần thực hiện các phép chuẩn hóa dữ liệu theo nhóm (Group Normalization), ví dụ: tính độ lệch của giá phòng so với mức giá trung bình của chính quận đó (`df['price'] - df.groupby('neighbourhood')['price'].transform('mean')`).",
      "verification": "assert len(df['quy_mo_quan']) == len(df)\nassert df['la_host_chuyen_nghiep'].dtype == bool"
    },
    {
      "id": "task-6",
      "title": "Bài 6: Tạo bảng chéo pivot_table và Ghép nối bảng merge có kiểm định quan hệ",
      "prompt": "Tạo một bảng chéo bằng `df.pivot_table()` thể hiện mức giá trung vị với chỉ mục hàng là `phan_khuc` và các cột là `la_host_chuyen_nghiep`. Sau đó, tạo một bảng tra cứu thông tin quận `df_quan_meta` và thực hiện ghép nối bằng `pd.merge()` kèm tham số `validate='m:1'` và `indicator=True` để kiểm tra độ tin cậy.",
      "prediction": "Tham số `validate='m:1'` sẽ lập tức ném ngoại lệ MergeError nếu bảng tra cứu bên phải có chứa khóa quận bị trùng lặp, giúp ngăn chặn sự cố bùng nổ số dòng (Row Explosion) trong cơ sở dữ liệu.",
      "solutionBasic": "# Bảng chéo phân khúc x host chuyên nghiệp\nbang_cheo = df.pivot_table(\n    index='phan_khuc',\n    columns='la_host_chuyen_nghiep',\n    values='price',\n    aggfunc='median'\n)\nprint('Bảng chéo giá trung vị:\\n', bang_cheo)",
      "solutionAdvanced": "# Ghép nối an toàn phòng thủ\ndf_meta = pd.DataFrame({\n    'neighbourhood': ['Providencia', 'Santiago', 'Las Condes'],\n    'vung_do_thi': ['Kinh doanh', 'Lịch sử', 'Tài chính cao cấp']\n})\n# Kiểm định quan hệ nhiều-một (Many-to-One)\ndf_merged = pd.merge(\n    df, df_meta,\n    on='neighbourhood',\n    how='left',\n    validate='m:1',\n    indicator=True\n)\nprint('Kiểm tra vết ghép nối:\\n', df_merged['_merge'].value_counts())",
      "explanation": "Trong quy trình kỹ thuật dữ liệu, luôn bật `indicator=True` khi thực hiện `how='left'` để kiểm tra tỷ lệ khớp (Merge Match Rate) và phát hiện các giá trị không khớp (left_only) nhằm truy tìm lỗi chính tả hoặc thiếu hụt dữ liệu danh mục.",
      "verification": "assert '_merge' in df_merged.columns\nassert len(df_merged) == len(df)"
    }
  ]
};
