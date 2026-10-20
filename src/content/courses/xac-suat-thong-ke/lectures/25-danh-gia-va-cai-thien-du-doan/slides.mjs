export const slides = [
  {
    "note": "25-danh-gia-va-cai-thien-du-doan",
    "title": "Phân rã tổng bình phương biến thiên",
    "bullets": [
      "Tổng bình phương toàn phần SST phân rã thành tổng bình phương mô hình SSM và phần dư SSE.",
      "Đẳng thức phân rã bảo toàn nhờ tính trực giao giữa giá trị dự báo và phần dư.",
      "Là nền tảng định lượng để đánh giá hiệu quả giải thích của mô hình."
    ],
    "formula": "$$\n\\text{SST} = \\text{SSM} + \\text{SSE}\n$$",
    "example": "Tổng biến thiên toàn phần SST = 32,0 được phân rã thành SSM = 25,6 và SSE = 6,4."
  },
  {
    "note": "25-danh-gia-va-cai-thien-du-doan",
    "title": "Đo lường sai số dự báo bằng RMSE",
    "bullets": [
      "RMSE là căn bậc hai của trung bình bình phương các phần dư.",
      "Mang cùng đơn vị đo lường với biến phụ thuộc y, rất thuận tiện để diễn giải thực tế.",
      "Phản ánh độ lớn điển hình của sai số khi áp dụng mô hình để dự báo."
    ],
    "formula": "$$\n\\text{RMSE} = \\sqrt{\\frac{1}{n}\\sum_{i=1}^n e_i^2}\n$$",
    "example": "Mô hình đạt RMSE = 1,13 đơn vị, nghĩa là sai số dự báo trung bình vào khoảng 1,13 đơn vị."
  },
  {
    "note": "25-danh-gia-va-cai-thien-du-doan",
    "title": "Hệ số xác định R bình phương",
    "bullets": [
      "Đo lường tỷ lệ phần trăm biến thiên của y được giải thích bởi đường hồi quy.",
      "Trong mô hình tuyến tính đơn, R^2 bằng đúng bình phương của hệ số tương quan r.",
      "Giá trị nằm trong đoạn [0, 1], càng gần 1 thì mức độ khớp dữ liệu càng hoàn hảo."
    ],
    "formula": "$$\n\\begin{aligned}R^2&=\\mathrm{SSM}/\\mathrm{SST}\\\\&=1-\\mathrm{SSE}/\\mathrm{SST}.\\end{aligned}\n$$",
    "example": "Với SSM = 25,6 và SST = 32,0, hệ số xác định đạt R^2 = 0,80 (giải thích được 80% biến thiên)."
  }
]
