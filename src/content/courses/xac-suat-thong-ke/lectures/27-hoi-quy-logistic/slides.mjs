export const slides = [
  {
    "note": "27-hoi-quy-logistic",
    "title": "Giới hạn của hồi quy tuyến tính trên biến nhị phân",
    "bullets": [
      "Hồi quy tuyến tính có thể cho ra giá trị dự báo vượt ra ngoài đoạn xác suất [0, 1].",
      "Phần dư vi phạm giả định phương sai không đổi do biến thiên phụ thuộc vào xác suất p.",
      "Cần một hàm phi tuyến để chuyển đổi kết hợp tuyến tính về miền xác suất hợp lệ."
    ],
    "formula": "$$\nY \\in \\{0, 1\\}, \\quad \\hat{y} \\notin [0, 1]\n$$",
    "example": "Mô hình tuyến tính đơn dự báo xác suất đỗ đại học đạt 120% hoặc -15% khi điểm đầu vào cực đoan."
  },
  {
    "note": "27-hoi-quy-logistic",
    "title": "Hàm Sigmoid và hàm Log-Odds",
    "bullets": [
      "Hàm sigmoid ánh xạ toàn bộ trục số thực về khoảng xác suất mở (0, 1).",
      "Hàm logit biểu diễn logarit của tỷ số chênh lệch odds theo dạng tuyến tính.",
      "Mô hình hóa xác suất thành công có điều kiện theo biến giải thích x."
    ],
    "formula": "$$\n\\begin{aligned}\\eta&=\\beta_0+\\beta_1x,\\\\p(x)&=\\frac1{1+e^{-\\eta}},\\\\\\log\\frac p{1-p}&=\\eta.\\end{aligned}\n$$",
    "example": "Tại điểm cắt $\\beta_0 + \\beta_1 x = 0$, xác suất thành công đạt đúng 50%."
  },
  {
    "note": "27-hoi-quy-logistic",
    "title": "Tỷ số chênh Odds Ratio và giải thích hệ số",
    "bullets": [
      "Tỷ số chênh odds bằng xác suất thành công chia cho xác suất thất bại.",
      "Khi x tăng thêm 1 đơn vị, tỷ số chênh odds được nhân lên với hệ số $e^{\\beta_1}$.",
      "Hệ số $\\beta_1$ dương làm tăng xác suất thành công, hệ số âm làm giảm xác suất."
    ],
    "formula": "$$\n\\begin{aligned}\\mathrm{Odds}&=p/(1-p),\\\\\\mathrm{OR}&=e^{\\beta_1}.\\end{aligned}\n$$",
    "example": "Hệ số $\\beta_1 = 0{,}693$ tương ứng với Odds Ratio = $e^{0{,}693} = 2$, nghĩa là nguy cơ tăng gấp đôi mỗi khi x tăng 1 đơn vị."
  }
]
