export const slides = [
  {
    "note": "32-hiep-phuong-sai-va-ky-vong-co-dieu-kien",
    "title": "Tương quan cần hai phương sai dương hữu hạn",
    "bullets": [
      "Hiệp phương sai được xác định hữu hạn khi cả hai biến có mômen bậc hai hữu hạn.",
      "Nếu cả hai phương sai dương, hệ số tương quan là hiệp phương sai chia tích độ lệch chuẩn.",
      "Độc lập kéo theo hiệp phương sai bằng 0. Chiều ngược lại không đúng."
    ],
    "formula": "$$\n\\rho_{X,Y}=\\frac{\\mathrm{Cov}(X,Y)}{\\sigma_X\\sigma_Y}\n$$",
    "example": "Với $X\\sim U(-1,1)$ và $Y=X^2$, cả hai phương sai dương nhưng tương quan bằng 0 và hai biến phụ thuộc."
  },
  {
    "note": "32-hiep-phuong-sai-va-ky-vong-co-dieu-kien",
    "title": "Hiệp phương sai tham gia phương sai của tổng",
    "bullets": [
      "Giả sử các biến có mômen bậc hai hữu hạn.",
      "Đặt $S=\\sum_{i=1}^nX_i$, $\\sigma_i^2=\\mathrm{Var}(X_i)$ và $\\sigma_{ij}=\\mathrm{Cov}(X_i,X_j)$.",
      "Không tương quan từng đôi là điều kiện đủ để phương sai tổng bằng tổng phương sai."
    ],
    "formula": "$$\n\\mathrm{Var}(S)=\\sum_{i=1}^n\\sigma_i^2+2\\sum_{i<j}\\sigma_{ij}\n$$",
    "example": "Ba biến có phương sai $4$ và hiệp phương sai từng đôi bằng $1$ cho phương sai tổng bằng $18$."
  },
  {
    "note": "32-hiep-phuong-sai-va-ky-vong-co-dieu-kien",
    "title": "Kỳ vọng và phương sai toàn phần",
    "bullets": [
      "Với $X$ khả tích, đặt $M=\\mathbb E[X\\mid Y]$. Kỳ vọng của $M$ bằng kỳ vọng của $X$.",
      "Nếu $X$ có mômen bậc hai hữu hạn, đặt thêm $V=\\mathrm{Var}(X\\mid Y)$.",
      "Phương sai toàn phần cộng phần biến thiên trong nhóm với phần biến thiên giữa các trung bình nhóm."
    ],
    "formula": "$$\n\\mathrm{Var}(X)=\\mathbb E[V]+\\mathrm{Var}(M)\n$$",
    "example": "Trong ví dụ tổng Poisson, giả thiết các lượng yêu cầu độc lập với số đợt cho kỳ vọng tổng $50$ và phương sai $290$."
  },
  {
    "note": "32-hiep-phuong-sai-va-ky-vong-co-dieu-kien",
    "title": "Kỳ vọng có điều kiện tối thiểu hóa MSE",
    "bullets": [
      "Giả sử $X$ có mômen bậc hai hữu hạn và xét hàm dự báo $g(Y)$ cũng có mômen bậc hai hữu hạn.",
      "Đặt $M=\\mathbb E[X\\mid Y]$, $U=X-M$ và $V=M-g(Y)$. Tích chéo có kỳ vọng bằng 0.",
      "MSE nhỏ nhất khi $g(Y)=M$ hầu chắc chắn. Đây là nghĩa duy nhất của nghiệm dự báo tối ưu."
    ],
    "formula": "$$\n\\mathbb E[UV]=0\n$$",
    "example": "Đổi dự báo khỏi kỳ vọng có điều kiện chỉ có thể tăng MSE, với mức tăng bằng kỳ vọng bình phương độ lệch giữa hai dự báo."
  }
]
