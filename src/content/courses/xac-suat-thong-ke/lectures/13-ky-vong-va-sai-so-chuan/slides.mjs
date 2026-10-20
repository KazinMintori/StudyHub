export const slides = [
  {
    "note": "13-ky-vong-va-sai-so-chuan",
    "title": "Kỳ vọng toán học và tính tuyến tính",
    "bullets": [
      "Kỳ vọng là trọng tâm cân bằng xác suất của biến ngẫu nhiên.",
      "Có tính tuyến tính tổng quát với mọi biến ngẫu nhiên có kỳ vọng hữu hạn.",
      "Tính cộng tính không đòi hỏi tính độc lập giữa các biến ngẫu nhiên."
    ],
    "formula": "$$\nE(X+Y)=E(X)+E(Y).\n$$",
    "example": "Gieo con xúc xắc 6 mặt cân bằng: Kỳ vọng số chấm xuất hiện là đúng 3,5."
  },
  {
    "note": "13-ky-vong-va-sai-so-chuan",
    "title": "Phương sai và điều kiện mômen bậc hai",
    "bullets": [
      "Phương sai đo lường mức độ phân tán quanh giá trị kỳ vọng.",
      "Đòi hỏi điều kiện mômen bậc hai hữu hạn E(X^2) < vô cùng.",
      "Công thức tính nhanh: Kỳ vọng của bình phương trừ đi bình phương kỳ vọng."
    ],
    "formula": "$$\n\\operatorname{Var}(X)=E(X^2)-[E(X)]^2\n$$",
    "example": "Biến Bernoulli có tham số p: Kỳ vọng E(X) = p và phương sai Var(X) = p(1 - p)."
  },
  {
    "note": "13-ky-vong-va-sai-so-chuan",
    "title": "Độ lệch chuẩn và tính cộng tính khi độc lập",
    "bullets": [
      "Độ lệch chuẩn là căn bậc hai của phương sai, cùng đơn vị đo với biến gốc.",
      "Khoảng 1 độ lệch chuẩn không có bảo đảm xác suất bao phủ cố định cho mọi phân phối.",
      "Phương sai có tính cộng tính khi các biến độc lập thống kê.",
      "Điều kiện đủ: Hai biến độc lập và có phương sai hữu hạn. Điều kiện cần và đủ cho tính cộng này là hiệp phương sai bằng 0, không phải tính độc lập."
    ],
    "formula": "$$\n\\begin{aligned}V_X&=\\operatorname{Var}(X),\\\\V_Y&=\\operatorname{Var}(Y),\\\\\\operatorname{Var}(X\\pm Y)&=V_X+V_Y.\\end{aligned}\n$$",
    "example": "Phương sai của hiệu hai biến độc lập bằng tổng hai phương sai do sự bất định tích lũy."
  }
]
