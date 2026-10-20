export const slides = [
  {
    "note": "11-phan-phoi-xac-suat",
    "title": "Khái niệm phân phối xác suất rời rạc",
    "bullets": [
      "Phân phối xác suất mô tả cách phân bổ 100% xác suất cho các giá trị rời rạc.",
      "Hàm khối lượng xác suất PMF luôn không âm và có tổng bằng đúng 1.",
      "Biểu đồ xác suất lý thuyết phản ánh mô hình toán học tiên nghiệm."
    ],
    "formula": "$$\n\\begin{aligned}&p_i=P(X=x_i)\\ge0,\\\\&p_1+p_2+\\dots=1.\\end{aligned}\n$$",
    "example": "Gieo đồng thời 2 xúc xắc: Tổng điểm nhận các giá trị từ 2 đến 12 với đỉnh xác suất tại 7."
  },
  {
    "note": "11-phan-phoi-xac-suat",
    "title": "Phân phối Nhị thức Binomial",
    "bullets": [
      "Định nghĩa chuẩn tắc qua n phép thử Bernoulli độc lập với cùng xác suất p.",
      "Hệ số nhị thức đếm số chuỗi kết quả có đúng k lần thành công.",
      "Lấy mẫu có hoàn lại từ tổng thể hữu hạn là một hiện thực hóa cụ thể của phân phối.",
      "Ký hiệu pₖ = P(X = k), với k = 0,…,n."
    ],
    "formula": "$$\np_k=\\binom nkp^k(1-p)^{n-k}.\n$$",
    "example": "Tung đồng xu lệch có xác suất ngửa 0,7 năm lần: Xác suất có đúng 4 mặt ngửa xấp xỉ 36,02%."
  },
  {
    "note": "11-phan-phoi-xac-suat",
    "title": "Phân phối Siêu bội và ranh giới xấp xỉ",
    "bullets": [
      "Mô tả số lần thành công khi rút mẫu không hoàn lại từ tổng thể hữu hạn N.",
      "Khi tỷ lệ lấy mẫu n/N <= 0,05, có thể dùng phân phối Nhị thức để xấp xỉ phần trung tâm.",
      "Cần thận trọng với các biến cố hiếm ở vùng đuôi vì sai số tương đối có thể lớn."
    ],
    "formula": "$$\nP(X = k) = \\frac{\\binom{G}{k}\\binom{N-G}{n-k}}{\\binom{N}{n}}\n$$",
    "example": "Rút không hoàn lại 3 thẻ từ hộp 10 thẻ có 6 thẻ tốt: Xác suất có đúng 2 thẻ tốt là đúng 0,50."
  }
]
