export const slides = [
  {
    "title": "Thống kê biến thiên qua các lần lấy mẫu",
    "bullets": [
      "Mẫu i.i.d. gồm các quan sát độc lập, cùng phân phối.",
      "Thống kê là hàm của mẫu, không chứa tham số chưa biết.",
      "Phân phối mẫu mô tả thống kê qua các lần lặp lại phép lấy mẫu."
    ],
    "formula": "$$\n\\bar X=\\frac{X_1+\\dots+X_n}{n}\n$$",
    "example": "Phân phối của $\\bar X$ khác với phân phối của một quan sát $X_i$.",
    "note": "36-phan-phoi-mau-chinh-xac"
  },
  {
    "title": "Hiệu chỉnh Bessel cần phương sai hữu hạn",
    "bullets": [
      "Với mẫu i.i.d., $n\\ge2$ và phương sai hữu hạn, tổng bình phương sai lệch có kỳ vọng $(n-1)\\sigma^2$.",
      "Chia cho $n-1$ tạo ước lượng phương sai không chệch.",
      "Tính không chệch này không đòi hỏi tổng thể chuẩn."
    ],
    "formula": "$$\nS^2=\\frac{1}{n-1}\\sum_{i=1}^n(X_i-\\bar X)^2\n$$",
    "example": "Năm số đo có tổng bình phương sai lệch $30$ cho $s^2=7{,}5$.",
    "note": "36-phan-phoi-mau-chinh-xac"
  },
  {
    "title": "Mẫu chuẩn cho tính độc lập và Chi bình phương",
    "bullets": [
      "Với mẫu i.i.d. chuẩn, trung bình mẫu có phương sai $\\sigma^2/n$.",
      "Trung bình mẫu và phương sai mẫu độc lập.",
      "Không được suy tính độc lập chỉ từ hiệp phương sai bằng không."
    ],
    "formula": "$$\n\\frac{(n-1)S^2}{\\sigma^2}\\sim\\chi^2(n-1)\n$$",
    "example": "Giả thiết chuẩn tạo phân phối chính xác cho thống kê trên, kể cả mẫu nhỏ.",
    "note": "36-phan-phoi-mau-chinh-xac"
  },
  {
    "title": "Student và Fisher cần các thành phần độc lập",
    "bullets": [
      "Mẫu chuẩn i.i.d. cho thống kê Student khi thay độ lệch chuẩn tổng thể bằng $S$.",
      "Tỷ số hai biến Chi bình phương độc lập, mỗi biến chia cho bậc tự do, có phân phối Fisher.",
      "Giá trị tới hạn đuôi phải mức $\\alpha$ là phân vị tích lũy mức $1-\\alpha$."
    ],
    "formula": "$$\nT=\\frac{\\bar X-\\mu}{S/\\sqrt n}\\sim t(n-1)\n$$",
    "example": "Với hai mẫu chuẩn độc lập cùng phương sai, $S_1^2/S_2^2$ có phân phối Fisher.",
    "note": "36-phan-phoi-mau-chinh-xac"
  }
]
