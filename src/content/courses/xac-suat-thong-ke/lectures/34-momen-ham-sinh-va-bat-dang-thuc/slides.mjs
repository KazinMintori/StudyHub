export const slides = [
  {
    "note": "34-momen-ham-sinh-va-bat-dang-thuc",
    "title": "Mômen bổ sung thông tin về phân phối",
    "bullets": [
      "Mômen gốc bậc $k$ là $\\mu_k=\\mathbb E[X^k]$, hữu hạn khi $\\mathbb E[|X|^k]<\\infty$.",
      "Mômen trung tâm đo lũy thừa độ lệch quanh trung bình. Bậc hai là phương sai.",
      "Đối xứng và mômen bậc ba hữu hạn kéo theo độ lệch bằng 0. Độ lệch bằng 0 chưa đủ kết luận đối xứng."
    ],
    "formula": "$$\n\\mu'_k=\\mathbb E[(X-\\mu)^k]\n$$",
    "example": "Biến Chuẩn chuẩn tắc có mômen bậc bốn bằng $3$, nên độ nhọn chuẩn hóa bằng $3$ và độ nhọn dư bằng $0$."
  },
  {
    "note": "34-momen-ham-sinh-va-bat-dang-thuc",
    "title": "MGF sinh mômen khi hữu hạn quanh 0",
    "bullets": [
      "Giả sử $M_X(t)=\\mathbb E[e^{tX}]$ hữu hạn trên một khoảng mở quanh 0.",
      "Đạo hàm bậc $k$ tại 0 bằng mômen gốc bậc $k$.",
      "MGF bằng nhau trên một lân cận 0 xác định cùng phân phối. Với tổng độc lập, MGF bằng tích các MGF."
    ],
    "formula": "$$\nM_X^{(k)}(0)=\\mathbb E[X^k]\n$$",
    "example": "MGF của Chuẩn chuẩn tắc là $e^{t^2/2}$, cho kỳ vọng $0$, mômen bậc hai $1$ và mômen bậc bốn $3$."
  },
  {
    "note": "34-momen-ham-sinh-va-bat-dang-thuc",
    "title": "Markov và Chebyshev cho các cận hữu hạn mẫu",
    "bullets": [
      "Markov áp dụng cho biến không âm có kỳ vọng hữu hạn với ngưỡng $a>0$.",
      "Chebyshev áp dụng cho độ lệch khỏi trung bình. Ở dạng dùng $k\\sigma$, cần $0<\\sigma^2<\\infty$ và $k>0$.",
      "Các cận không yêu cầu một họ phân phối cụ thể, nhưng có thể lỏng."
    ],
    "formula": "$$\nP(X\\ge a)\\le\\frac{\\mathbb E[X]}a\n$$",
    "example": "Với trung bình $70$ và độ lệch chuẩn $10$, Markov chặn xác suất điểm từ $90$ trở lên bởi $7/9$, còn Chebyshev cho cận $1/4$."
  },
  {
    "note": "34-momen-ham-sinh-va-bat-dang-thuc",
    "title": "Jensen so sánh kỳ vọng qua hàm lồi",
    "bullets": [
      "Với hàm lồi $g$ trên một khoảng chứa giá trị của $X$, giả sử $X$ và $g(X)$ khả tích.",
      "Nếu hàm lồi ngặt, dấu bằng đòi hỏi $X$ là hằng số hầu chắc chắn.",
      "Cauchy–Schwarz áp dụng cho hai biến có mômen bậc hai hữu hạn và cho giới hạn trị tuyệt đối của tương quan."
    ],
    "formula": "$$\n\\mathbb E[g(X)]\\ge g(\\mathbb E[X])\n$$",
    "example": "Biến $X$ nhận $1$ và $7$ với xác suất bằng nhau có kỳ vọng $4$, nhưng kỳ vọng nghịch đảo là $4/7>1/4$."
  }
]
