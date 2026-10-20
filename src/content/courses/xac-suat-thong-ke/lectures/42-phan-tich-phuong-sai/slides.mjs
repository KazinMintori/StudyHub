export const slides = [
  {
    "title": "ANOVA kiểm tra một giả thuyết tổng thể",
    "bullets": [
      "Giả thuyết không yêu cầu mọi kỳ vọng nhóm bằng nhau.",
      "Bác bỏ cho biết ít nhất hai kỳ vọng khác nhau, chưa chỉ ra tất cả cặp khác nhau.",
      "Công thức FWER dưới đây chỉ đúng khi các phép thử độc lập và mọi giả thuyết không đúng."
    ],
    "formula": "$$\n\\mathrm{FWER}=1-(1-\\alpha)^m\n$$",
    "example": "Sáu phép thử độc lập mức $5\\%$ cho FWER $26{,}49\\%$. Các cặp dùng chung nhóm thường phụ thuộc.",
    "note": "42-phan-tich-phuong-sai"
  },
  {
    "title": "So biến thiên giữa nhóm với biến thiên nội bộ",
    "bullets": [
      "Phân rã tổng bình phương là một đẳng thức đại số.",
      "Sai số chuẩn độc lập, cùng phương sai cho phân phối Fisher chính xác dưới giả thuyết không.",
      "SSB chia cho $k-1$, còn SSW chia cho $N-k$ để tạo các trung bình bình phương."
    ],
    "formula": "$$\nF=\\frac{\\mathrm{MSB}}{\\mathrm{MSW}}\n$$",
    "example": "Ba nhóm phân bón có SSB $32$, SSW $6$ và $F=24$, với $p\\approx0{,}000247$.",
    "note": "42-phan-tich-phuong-sai"
  },
  {
    "title": "So sánh từng cặp vẫn cần kiểm soát toàn họ",
    "bullets": [
      "Bonferroni dùng mức mỗi phép thử bằng $\\alpha/m$, không cần độc lập giữa các phép thử.",
      "Tukey HSD cho họ tất cả cặp trong mô hình chuẩn, cùng phương sai và cỡ nhóm bằng nhau.",
      "Họ so sánh phải bao trùm các phép thử đã cân nhắc, không chỉ những kết quả được chọn báo cáo."
    ],
    "formula": "$$\n\\mathrm{HSD}=q_{\\alpha,k,N-k}\\sqrt{\\frac{\\mathrm{MSW}}n}\n$$",
    "example": "Ngưỡng HSD $1{,}6119$ nhỏ hơn các chênh lệch $2$, $2$, $4$ của ba cặp trong ví dụ.",
    "note": "42-phan-tich-phuong-sai"
  },
  {
    "title": "Tương tác làm hiệu ứng phụ thuộc nhân tố còn lại",
    "bullets": [
      "Thiết kế hai nhân tố cân bằng với lặp độc lập cho phép tách tương tác và sai số.",
      "Đường kỳ vọng không song song biểu thị tương tác. Đường trung bình mẫu còn có nhiễu.",
      "Khi có tương tác, phải xét hiệu ứng tại từng mức cụ thể trước khi đưa kết luận tổng quát."
    ],
    "formula": "$$\nY_{ijk}=\\mu_{ij}+\\varepsilon_{ijk}\n$$",
    "example": "Thiết kế $3\\times4$ với năm lần lặp mỗi ô có bậc tự do sai số $48$.",
    "note": "42-phan-tich-phuong-sai"
  }
]
