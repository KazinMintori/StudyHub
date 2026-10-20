export const slides = [
  {
    "note": "09-co-so-xac-suat",
    "title": "Không gian mẫu và biến cố",
    "bullets": [
      "Không gian mẫu Omega là tập hợp tất cả các kết quả sơ cấp khả dĩ.",
      "Biến cố A là một tập con bất kỳ của không gian mẫu.",
      "Biến cố rỗng không bao giờ xảy ra, biến cố chắc chắn luôn xảy ra."
    ],
    "formula": "$$\n\\begin{aligned}&A\\subseteq\\Omega,\\\\&P(\\varnothing)=0,\\\\&P(\\Omega)=1.\\end{aligned}\n$$",
    "example": "Gieo con xúc xắc 6 mặt có không gian mẫu gồm các số từ 1 đến 6, biến cố ra mặt chẵn là {2, 4, 6}."
  },
  {
    "note": "09-co-so-xac-suat",
    "title": "Hệ tiên đề xác suất Kolmogorov",
    "bullets": [
      "Tiên đề 1: Xác suất của mọi biến cố luôn không âm.",
      "Tiên đề 2: Xác suất của toàn bộ không gian mẫu bằng 1.",
      "Tiên đề 3: Xác suất của hợp các biến cố xung khắc bằng tổng xác suất thành phần.",
      "Công thức cộng trên áp dụng cho hai biến cố rời nhau. Tính cộng đếm được áp dụng cho cả dãy biến cố đôi một rời nhau."
    ],
    "formula": "$$\n\\begin{aligned}&P(A)\\ge0,\\\\&P(A\\cup B)=P(A)+P(B).\\end{aligned}\n$$",
    "example": "Tung đồng xu cân bằng: Xác suất ra ngửa bằng 0,5 và sấp bằng 0,5, tổng xác suất bằng 1."
  },
  {
    "note": "09-co-so-xac-suat",
    "title": "Quy tắc phần bù và quy tắc cộng tổng quát",
    "bullets": [
      "Xác suất của biến cố đối lập bằng 1 trừ đi xác suất của biến cố gốc.",
      "Quy tắc cộng tổng quát trừ đi phần giao để tránh đếm trùng lặp hai lần.",
      "Dùng khi hai biến cố không xung khắc lẫn nhau."
    ],
    "formula": "$$\n\\begin{aligned}&u=P(A),\\quad v=P(B),\\\\&w=P(A\\cap B),\\\\&P(A\\cup B)=u+v-w.\\end{aligned}\n$$",
    "example": "Rút một lá bài từ bộ bài 52 lá: Biến cố rút lá Át hoặc lá chất Cơ có phần giao là lá Át Cơ."
  }
]
