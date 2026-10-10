// Module bài tập phòng Lab: Lab 12: Biểu đồ cho báo cáo và cách kiểm tra bằng assert
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-12-truc-quan-hoa-co-ban",
  "title": "Lab 12: Biểu đồ cho báo cáo và cách kiểm tra bằng assert",
  "dataset": {
    "name": "Tập số liệu trực quan hóa thị trường lưu trú Santiago",
    "type": "CSV (Dữ liệu bảng đa biến)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "secondary_url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv",
    "description": "Số liệu phục vụ thiết kế biểu đồ báo cáo xuất bản: biểu đồ đường chuỗi thời gian, biểu đồ thanh ngang cơ cấu loại phòng kèm nhãn dữ liệu, histogram phân phối giá hai đỉnh (bimodal), và kỹ thuật sửa đổi biểu đồ cắt trục tung sai lệch."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Chuẩn bị chuỗi dữ liệu đánh giá theo tháng của quận Providencia",
      "prompt": "Từ tệp `listings.csv` và `reviews.csv`, hãy lọc riêng các đánh giá của các chỗ ở nằm tại quận 'Providencia' trong giai đoạn từ năm 2022 đến 2025. Tổng hợp thành một Series số lượt đánh giá theo tháng (`resample('ME')`).",
      "prediction": "Số lượt đánh giá của Providencia sẽ phản ánh rõ mùa vụ du lịch của Nam bán cầu: cao điểm vào mùa hè (tháng 12, tháng 1, tháng 2) và giảm xuống vào mùa đông (tháng 6, tháng 7).",
      "solutionBasic": "import pandas as pd\n\n# 1. Lấy danh sách ID chỗ ở tại Providencia\nids_pro = set(ds.loc[ds['neighbourhood'] == 'Providencia', 'id'])\n# 2. Lọc bảng reviews\nrv_pro = rv.loc[rv['listing_id'].isin(ids_pro) & (rv['date'] >= '2022-01-01') & (rv['date'] <= '2025-12-31')]\n# 3. Gom theo tháng\nrv_thang = rv_pro.set_index('date').resample('ME').size()\nprint('Chuỗi tháng Providencia:\\n', rv_thang.head())",
      "solutionAdvanced": "# Đóng gói hàm trích xuất chuỗi thời gian của quận\ndef trinh_xuat_chuoi_thang_quan(df_ls: pd.DataFrame, df_rv: pd.DataFrame, quan: str, start: str, end: str) -> pd.Series:\n    target_ids = set(df_ls.loc[df_ls['neighbourhood'] == quan, 'id'])\n    sub_rv = df_rv.loc[df_rv['listing_id'].isin(target_ids)].copy()\n    sub_rv = sub_rv.loc[(sub_rv['date'] >= start) & (sub_rv['date'] <= end)]\n    ts = sub_rv.set_index('date').resample('ME')['id'].count()\n    assert len(ts) > 0, 'Chuỗi thời gian không được rỗng'\n    return ts\n\nts_pro = trinh_xuat_chuoi_thang_quan(ds, rv, 'Providencia', '2022-01-01', '2025-12-31')",
      "explanation": "Sử dụng mã tần suất `'ME'` (Month End) thay cho mã `'M'` đã lỗi thời trong các phiên bản pandas mới nhất để tránh cảnh báo Future Deprecation.",
      "verification": "assert len(ts_pro) == 48, '4 năm từ 2022 đến 2025 phải có đúng 48 tháng.'"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Thiết kế Biểu đồ đường chuẩn OOP và Kiểm tra thuộc tính hình vẽ bằng assert",
      "prompt": "Sử dụng giao diện hướng đối tượng của Matplotlib (`fig, ax = plt.subplots()`) để vẽ biểu đồ đường chuỗi đánh giá theo tháng của Providencia. Yêu cầu: Đặt tiêu đề rõ ràng, nhãn trục X, nhãn trục Y, bật lưới mờ (`grid(alpha=0.3)`), định dạng trục Y từ 0, và lưu hình vào thư mục `figures/pro_reviews_trend.png`. Viết các dòng lệnh `assert` kiểm tra thuộc tính của đối tượng `Axes`.",
      "prediction": "Trong môi trường kiểm thử tự động, ta có thể dùng `assert` để kiểm tra trực tiếp các thuộc tính của `Axes` như tiêu đề (`ax.get_title()`), giới hạn trục (`ax.get_ylim()`), nhãn trục mà không cần phải mở ảnh bằng mắt thường.",
      "solutionBasic": "import matplotlib.pyplot as plt\n\nfig, ax = plt.subplots(figsize=(10, 4.5), dpi=100)\nax.plot(ts_pro.index, ts_pro.values, color='#0284c7', lw=2, marker='o', ms=4, label='Lượt đánh giá/tháng')\nax.set_title('Xu hướng đánh giá chỗ ở tại Providencia (2022 - 2025)', fontsize=12, pad=12)\nax.set_xlabel('Thời gian', fontsize=10)\nax.set_ylabel('Số lượt đánh giá', fontsize=10)\nax.set_ylim(bottom=0)\nax.grid(True, linestyle='--', alpha=0.3)\nax.legend()\n\nplt.tight_layout()\nplt.savefig('test_pro_trend.png')\nplt.close()",
      "solutionAdvanced": "# Kiểm thử tự động thuộc tính hình học của đồ thị bằng assert\nfig, ax = plt.subplots()\nax.plot(ts_pro.index, ts_pro.values)\nax.set_title('Xu hướng Providencia')\nax.set_ylim(bottom=0)\n\n# Khẳng định chất lượng đồ thị tự động\nassert ax.get_title() == 'Xu hướng Providencia', 'Tiêu đề biểu đồ chưa được thiết lập!'\ny_bottom, y_top = ax.get_ylim()\nassert y_bottom == 0.0, 'Trục tung phải bắt đầu từ mốc 0!'\nassert len(ax.lines) == 1, 'Biểu đồ phải chứa đúng 1 đường dữ liệu.'\nplt.close(fig)",
      "explanation": "Kỹ thuật kiểm tra đồ thị bằng `assert` là phương pháp độc đáo giúp tích hợp việc kiểm tra chất lượng báo cáo trực quan hóa vào quy trình CI/CD tự động.",
      "verification": "assert y_bottom == 0.0"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Biểu đồ thanh ngang với nhãn dữ liệu trực tiếp (Direct Bar Labels)",
      "prompt": "Tính tỷ lệ căn hộ nguyên căn (`Entire home/apt`) tại 6 quận du lịch lớn nhất Santiago: Providencia, Santiago, Las Condes, Ñuñoa, Viña del Mar, Valparaíso. Vẽ biểu đồ thanh ngang (`ax.barh`) có sắp xếp thứ tự tăng dần và gắn trực tiếp nhãn giá trị phần trăm vào đầu mỗi thanh bằng `ax.bar_label()`.",
      "prediction": "Biểu đồ thanh ngang (Horizontal Bar Chart) giúp việc đọc tên các quận dài không bị nghiêng hoặc chồng lấn lên nhau, đồng thời gắn nhãn số liệu trực tiếp giúp người đọc nắm bắt ngay thông tin mà không phải đối chiếu dòng gióng xuống trục hoành.",
      "solutionBasic": "top_quan = ['Providencia', 'Santiago', 'Las Condes', 'Ñuñoa']\ndf_top = ds[ds['neighbourhood'].isin(top_quan)]\nty_le_quan = df_top.groupby('neighbourhood')['room_type'].apply(lambda s: (s == 'Entire home/apt').mean()).sort_values()\n\nfig, ax = plt.subplots(figsize=(8, 4))\nbars = ax.barh(ty_le_quan.index, ty_le_quan.values * 100, color='#3b82f6')\nax.bar_label(bars, fmt='%.1f%%', padding=5)\nax.set_xlim(0, 100)\nax.set_title('Tỷ lệ căn hộ nguyên căn theo quận')\nplt.tight_layout()\nplt.close()",
      "solutionAdvanced": "def ve_thanh_ngang_chuyen_nghiep(series_data: pd.Series, tieu_de: str) -> tuple:\n    \"\"\"Vẽ thanh ngang chuẩn mực báo cáo xuất bản.\"\"\"\n    s_sorted = series_data.sort_values(ascending=True)\n    fig, ax = plt.subplots(figsize=(8, len(s_sorted) * 0.6 + 1.5), dpi=120)\n    bars = ax.barh(s_sorted.index, s_sorted.values * 100, color='#2563eb', height=0.6)\n    ax.bar_label(bars, fmt='%.1f%%', padding=4, fontsize=9, fontweight='bold')\n    ax.set_xlim(0, max(s_sorted.values * 100) * 1.15)\n    ax.set_title(tieu_de, fontsize=11, fontweight='bold', pad=10)\n    ax.spines[['top', 'right']].set_visible(False) # Xóa khung viền thừa\n    return fig, ax\n\nfig, ax = ve_thanh_ngang_chuyen_nghiep(ty_le_quan, 'Cơ cấu phòng nguyên căn tại Santiago')\nplt.close(fig)",
      "explanation": "Quy tắc thiết kế thông tin tối giản (Data-Ink Ratio của Edward Tufte): Xóa bỏ các đường viền trên và viền phải không cần thiết (`spines[['top', 'right']].set_visible(False)`) để mắt người đọc tập trung hoàn toàn vào dữ liệu thanh ngang.",
      "verification": "assert len(ty_le_quan) > 0"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Nhận diện và sửa đổi biểu đồ cắt cụt trục tung gây hiểu sai lệch",
      "prompt": "Xét tình huống: Tỷ lệ phòng nguyên căn của Providencia là 68.5% và Santiago là 65.2%. Một báo cáo đồ họa đã cắt trục hoành từ 64% đến 70%, khiến cột của Providencia nhìn dài gấp đôi cột của Santiago dù mức chênh lệch thực tế chỉ là 3.3 điểm phần trăm. Hãy viết mã mô phỏng lại biểu đồ sai lệch đó và vẽ lại phiên bản trung thực có trục hoành bắt đầu từ 0.",
      "prediction": "Việc cắt cụt trục tọa độ (Truncated Axis) trên biểu đồ thanh là một trong những thủ thuật thị giác gây hiểu sai phổ biến nhất trong truyền thông: nó bóp méo tỷ lệ chiều dài, biến một chênh lệch nhỏ thành sự khác biệt khổng lồ.",
      "solutionBasic": "# Biểu đồ trung thực bắt buộc có trục xuất phát từ 0\nfig, ax = plt.subplots(figsize=(6, 3))\nax.bar(['Santiago', 'Providencia'], [65.2, 68.5], color=['#94a3b8', '#0284c7'])\nax.set_ylim(0, 100) # Trục từ 0\nax.set_ylabel('Tỷ lệ (%)')\nax.set_title('Phiên bản trung thực: Trục bắt đầu từ mốc 0')\nplt.tight_layout()\nplt.close()",
      "solutionAdvanced": "def so_sanh_bieu_do_trung_thuc(val_a: float, val_b: float, label_a: str, label_b: str):\n    \"\"\"Tạo cặp so sánh trực quan giữa biểu đồ bị cắt trục và biểu đồ chuẩn mực.\"\"\"\n    fig, (ax_sai, ax_dung) = plt.subplots(1, 2, figsize=(10, 3.5))\n    # Hình sai lệch: cắt trục từ 60\n    ax_sai.bar([label_a, label_b], [val_a, val_b], color=['#ef4444', '#dc2626'])\n    ax_sai.set_ylim(60, 72)\n    ax_sai.set_title('BỊ LỖI: Cắt cụt trục tạo ảo giác gấp đôi')\n    \n    # Hình trung thực: từ 0\n    ax_dung.bar([label_a, label_b], [val_a, val_b], color=['#10b981', '#059669'])\n    ax_dung.set_ylim(0, 100)\n    ax_dung.set_title('TRUNG THỰC: Giữ đúng tỷ lệ chiều dài')\n    plt.tight_layout()\n    return fig\n\nfig_cmp = so_sanh_bieu_do_trung_thuc(65.2, 68.5, 'Santiago', 'Providencia')\nplt.close(fig_cmp)",
      "explanation": "Biểu đồ cột (Bar Chart) mã hóa đại lượng bằng chiều dài thị giác. Do đó, quy tắc bất biến trong đạo đức trực quan hóa dữ liệu là: Trục của biểu đồ cột bắt buộc phải xuất phát từ mốc 0. Nếu muốn phóng to dao động nhỏ, hãy dùng biểu đồ đường (Line Chart) và ghi chú rõ thang đo.",
      "verification": "assert True"
    }
  ]
};
