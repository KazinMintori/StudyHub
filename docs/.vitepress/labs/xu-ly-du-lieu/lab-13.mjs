// Module bài tập phòng Lab: Lab 13: seaborn, bản đồ số chỗ ở và phản biện cách chọn mốc
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-13-truc-quan-hoa-nang-cao",
  "title": "Lab 13: seaborn, bản đồ số chỗ ở và phản biện cách chọn mốc",
  "dataset": {
    "name": "Inside Airbnb Santiago & Bản đồ địa lý Quận (GeoJSON)",
    "type": "CSV & GeoJSON (Không gian địa lý GIS)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "secondary_url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/neighbourhoods.geojson",
    "description": "Bao gồm bảng thuộc tính chỗ ở và file ranh giới hành chính 34 quận của Santiago (neighbourhoods.geojson), dùng cho trực quan hóa nâng cao với seaborn (Boxplot, Hue) và bản đồ nhiệt không gian GeoPandas."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Khảo sát phân phối giá bằng Boxplot và Hue phân loại chủ nhà",
      "prompt": "Sử dụng thư viện `seaborn` để vẽ biểu đồ hộp (Boxplot) thể hiện mức giá của 4 quận hàng đầu, đồng thời phân rã theo tham số `hue='la_host_chuyen_nghiep'`. Do giá có ngoại lai cực lớn, hãy sử dụng thang logarit trên trục tung (`ax.set_yscale('log')`) để hiển thị trọn vẹn phân phối.",
      "prediction": "Các chủ nhà chuyên nghiệp (sở hữu từ 2 chỗ ở trở lên) thường quản lý các căn hộ có mức giá trung vị đồng đều hơn và ít xuất hiện các mức giá siêu rẻ của phòng ở chia sẻ gia đình.",
      "solutionBasic": "import seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Lọc 4 quận lớn và giá dương\ntop_4 = ['Providencia', 'Santiago', 'Las Condes', 'Ñuñoa']\ndf_sub = df[(df['neighbourhood'].isin(top_4)) & (df['price'] > 0)].copy()\n\nfig, ax = plt.subplots(figsize=(9, 5))\nsns.boxplot(data=df_sub, x='neighbourhood', y='price', hue='la_host_chuyen_nghiep', ax=ax, palette='Set2')\nax.set_yscale('log')\nax.set_title('Phân phối giá theo quận và loại hình chủ nhà (Thang Log)')\nplt.tight_layout()\nplt.close()",
      "solutionAdvanced": "def ve_boxplot_nang_cao(data: pd.DataFrame, quan_list: list[str]) -> plt.Figure:\n    \"\"\"Vẽ boxplot kết hợp stripplot hiển thị mật độ điểm dữ liệu thật.\"\"\"\n    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=100)\n    sub = data[data['neighbourhood'].isin(quan_list) & (data['price'] > 0)]\n    sns.boxplot(data=sub, x='neighbourhood', y='price', hue='la_host_chuyen_nghiep',\n                ax=ax, showfliers=False, palette=['#93c5fd', '#1d4ed8'])\n    ax.set_title('So sánh phân phối giá giữa chủ nhà cá nhân và chuyên nghiệp')\n    ax.set_ylabel('Giá mỗi đêm (CLP)')\n    return fig\n\nfig_box = ve_boxplot_nang_cao(df, top_4)\nplt.close(fig_box)",
      "explanation": "Tham số `showfliers=False` giúp ẩn các điểm ngoại lai quá xa để tập trung nhìn rõ khoảng tứ phân vị IQR và trung vị của các nhóm trong biểu đồ báo cáo.",
      "verification": "assert len(df_sub) > 0"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Ghép nối dữ liệu không gian GeoPandas và Trực quan hóa bản đồ nhiệt",
      "prompt": "Đọc tệp ranh giới quận `neighbourhoods.geojson` bằng GeoPandas. Tính số lượng chỗ ở và giá trung vị của từng quận từ `listings.csv`, sau đó ghép nối với bảng hình học không gian qua tên quận `neighbourhood`. Vẽ bản đồ thể hiện mật độ chỗ ở toàn thành phố.",
      "prediction": "Các quận trung tâm Providencia, Santiago Centro và Las Condes sẽ có màu sắc đậm nhất trên bản đồ nhiệt, phản ánh sự tập trung dày đặc của hoạt động du lịch và căn hộ cho thuê ngắn hạn.",
      "solutionBasic": "import geopandas as gpd\n\n# Bước đọc và ghép dữ liệu địa lý\ngeo_url = 'https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/neighbourhoods.geojson'\ngdf_quan = gpd.read_file(geo_url)\n\nthong_ke_quan = df.groupby('neighbourhood').agg(\n    so_cho_o=('id', 'count'),\n    gia_tv=('price', 'median')\n).reset_index()\n\ngdf_merged = gdf_quan.merge(thong_ke_quan, left_on='neighbourhood', right_on='neighbourhood', how='left')\nprint('Đã ghép nối dữ liệu bản đồ thành công:', gdf_merged.shape)",
      "solutionAdvanced": "def ve_ban_do_mat_do(gdf_in: gpd.GeoDataFrame) -> plt.Figure:\n    \"\"\"Vẽ bản đồ phân bố chỗ ở với thanh chỉ báo màu sắc (Colorbar).\"\"\"\n    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)\n    gdf_in.plot(column='so_cho_o', cmap='OrRd', linewidth=0.8, edgecolor='0.5',\n                legend=True, ax=ax, legend_kwds={'label': 'Số lượng chỗ ở'})\n    ax.set_title('Phân bố không gian chỗ ở tại Santiago (Chile)', fontsize=12)\n    ax.set_axis_off() # Tắt tọa độ kinh vĩ độ để bản đồ thẩm mỹ hơn\n    return fig\n\n# Bản đồ không gian hoàn thành\nprint('Mô hình dữ liệu GIS sẵn sàng.')",
      "explanation": "Trong GeoPandas, phương thức `.plot(column='...')` tự động ánh xạ đại lượng số thành dải màu liên tục (Choropleth Map). Luôn tắt trục tọa độ (`ax.set_axis_off()`) khi trình bày bản đồ hành chính đô thị.",
      "verification": "assert 'geometry' in gdf_quan.columns"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Phản biện lỗi chọn mốc so sánh thiên lệch (Cherry-picking Baseline)",
      "prompt": "Xét tình huống: Một báo cáo công bố rằng 'Năm 2023 du lịch Santiago bùng nổ tăng trưởng 180%'. Khi kiểm tra dữ liệu, mốc so sánh được chọn là năm 2020 (năm đại dịch COVID-19 thị trường đóng băng). Hãy viết mã so sánh năm 2023 với: (1) Năm đáy 2020; (2) Năm bình thường trước dịch 2019. Viết lời nhận định phản biện trung thực.",
      "prediction": "So với đáy khủng hoảng 2020, con số tăng trưởng sẽ bị thổi phồng cực lớn (+180%). Tuy nhiên nếu so với mức đỉnh bình thường 2019, năm 2023 có thể chỉ mới hồi phục nhẹ hoặc thậm chí vẫn thấp hơn giai đoạn trước dịch.",
      "solutionBasic": "# Tính số đánh giá theo năm\nrv_years = rv.set_index('date').resample('YE').size()\nrv_years.index = rv_years.index.year\n\nso_2019 = rv_years.get(2019, 1)\nso_2020 = rv_years.get(2020, 1)\nso_2023 = rv_years.get(2023, 1)\n\ntang_so_2020 = (so_2023 - so_2020) / so_2020\ntang_so_2019 = (so_2023 - so_2019) / so_2019\n\nprint(f'Tăng trưởng so với đáy dịch 2020: {tang_so_2020:.1%}')\nprint(f'Tăng trưởng so với mốc bình thường 2019: {tang_so_2019:.1%}')",
      "solutionAdvanced": "def phan_bien_chon_moc_so_sanh(series_nam: pd.Series, nam_danh_gia: int, moc_day: int, moc_chuan: int) -> dict:\n    \"\"\"Vạch trần thiên lệch khi chọn mốc so sánh có lợi (Cherry-picking).\"\"\"\n    val_danh_gia = series_nam[nam_danh_gia]\n    val_day = series_nam[moc_day]\n    val_chuan = series_nam[moc_chuan]\n    \n    return {\n        'nam_xet': nam_danh_gia,\n        'tang_so_voi_day': round((val_danh_gia - val_day) / val_day * 100, 1),\n        'tang_so_voi_chuan': round((val_danh_gia - val_chuan) / val_chuan * 100, 1),\n        'nhan_xet': 'Tăng trưởng so với đáy chỉ phản ánh sự hồi phục kỹ thuật, không phải là bước nhảy vọt so với thời kỳ bình thường.'\n    }\n\nprint(phan_bien_chon_moc_so_sanh(rv_years, 2023, 2020, 2019))",
      "explanation": "Lỗi chọn mốc (Baseline Cherry-picking) là một hình thức ngụy biện thống kê tinh vi. Một nhà phân tích trung thực luôn phải so sánh số liệu với một năm cơ sở ổn định (Pre-crisis Baseline) thay vì chọn đáy khủng hoảng để phóng đại thành tích.",
      "verification": "assert tang_so_2020 > tang_so_2019"
    }
  ]
};
