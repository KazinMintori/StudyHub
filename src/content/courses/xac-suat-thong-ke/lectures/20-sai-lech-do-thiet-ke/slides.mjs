export const slides = [
  {
    "note": "20-sai-lech-do-thiet-ke",
    "title": "Sai lầm loại I, Sai lầm loại II và Mức kiểm định",
    "bullets": [
      "Sai lầm loại I là bác bỏ H0 khi H0 đúng; kiểm định mức alpha chặn xác suất này bởi alpha.",
      "Sai lầm loại II là không bác bỏ H0 khi H0 sai, có xác suất ký hiệu là beta.",
      "Kích thước kiểm định thực tế có thể nhỏ hơn alpha trong mô hình rời rạc hoặc giả thuyết phức.",
      "R là miền bác bỏ. Θ₀ và Θ₁ lần lượt là tập tham số thuộc giả thuyết không và đối thuyết."
    ],
    "formula": "$$\n\\begin{aligned}P_\\theta(R)&\\le\\alpha\\quad(\\theta\\in\\Theta_0),\\\\\\beta(\\theta)&=P_\\theta(R^c)\\quad(\\theta\\in\\Theta_1).\\end{aligned}\n$$",
    "example": "Tuyên án một người vô tội là sai lầm loại I; bỏ lọt tội phạm nguy hiểm là sai lầm loại II."
  },
  {
    "note": "20-sai-lech-do-thiet-ke",
    "title": "Lực kiểm định và các biện pháp nâng cao",
    "bullets": [
      "Lực kiểm định là xác suất bác bỏ chính xác H0 khi H0 thực sự sai, bằng 1 trừ beta.",
      "Trong một họ miền bác bỏ lồng nhau cố định, siết chặt alpha làm giảm lực kiểm định.",
      "Tăng cỡ mẫu, giảm sai số đo lường, thiết kế bắt cặp và dùng thống kê tối ưu giúp cải thiện cả hai loại sai lầm."
    ],
    "formula": "$$\n\\pi(\\theta)=1-\\beta(\\theta).\n$$",
    "example": "Thử nghiệm lâm sàng được thiết kế cỡ mẫu đủ lớn để đạt lực kiểm định tối thiểu 80% tại mức ý nghĩa 5%."
  },
  {
    "note": "20-sai-lech-do-thiet-ke",
    "title": "Vấn đề kiểm định nhiều lần và hiệu chỉnh",
    "bullets": [
      "Khi thực hiện đồng thời nhiều kiểm định độc lập, xác suất mắc ít nhất một sai lầm loại I tăng vọt.",
      "Hiệu chỉnh Bonferroni chia mức ý nghĩa alpha cho tổng số phép kiểm định m cần thực hiện.",
      "Kiểm soát tỷ lệ phát hiện sai FDR là cách tiếp cận hiện đại trong phân tích dữ liệu lớn."
    ],
    "formula": "$$\n\\alpha_{\\text{Bonferroni}} = \\frac{\\alpha}{m}\n$$",
    "example": "Thực hiện 100 phép thử với $\\alpha = 0{,}05$, ngưỡng kiểm định Bonferroni cho mỗi phép thử là 0,0005."
  }
]
