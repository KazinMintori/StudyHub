export const slides = [
  {
    "note": "12-bien-ngau-nhien",
    "title": "Khái niệm biến ngẫu nhiên",
    "bullets": [
      "Biến ngẫu nhiên là một hàm số gán mỗi kết quả của không gian mẫu với một số thực.",
      "Biến ngẫu nhiên rời rạc nhận tập giá trị đếm được hữu hạn hoặc vô hạn đếm được.",
      "Biến ngẫu nhiên liên tục nhận các giá trị lấp đầy một khoảng trên trục số."
    ],
    "formula": "$$\nX: \\Omega \\to \\mathbb{R}\n$$",
    "example": "Tung 3 lần đồng xu: Biến X đếm số mặt ngửa nhận các giá trị trong tập {0, 1, 2, 3}."
  },
  {
    "note": "12-bien-ngau-nhien",
    "title": "Hàm phân phối tích lũy CDF",
    "bullets": [
      "Hàm CDF xác định xác suất biến ngẫu nhiên nhận giá trị không vượt quá x.",
      "Luôn là hàm không giảm, liên tục phải, tiến tới 0 khi x về âm vô cùng và 1 khi x về dương vô cùng.",
      "Với biến rời rạc, đồ thị CDF có dạng hình bậc thang nhảy tại các điểm xác suất."
    ],
    "formula": "$$\n\\begin{aligned}F(x)&=P(X\\le x),\\\\\\lim_{x\\to-\\infty}F(x)&=0,\\\\\\lim_{x\\to+\\infty}F(x)&=1.\\end{aligned}\n$$",
    "example": "Biến ngẫu nhiên X có phân phối: F(1,5) = P(X <= 1,5) = P(X = 0) + P(X = 1) = 0,40."
  },
  {
    "note": "12-bien-ngau-nhien",
    "title": "Phân phối đồng thời và phân phối biên duyên",
    "bullets": [
      "Hàm khối lượng xác suất đồng thời mô tả phân phối xác suất chung của cặp biến (X, Y).",
      "Phân phối biên duyên thu được bằng cách tính tổng theo biến còn lại.",
      "Hai biến ngẫu nhiên độc lập khi hàm đồng thời bằng tích hai hàm biên duyên.",
      "f(x,y) = P(X = x, Y = y) là hàm khối xác suất chung. Tổng lấy theo mọi y trong miền giá trị rời rạc."
    ],
    "formula": "$$\nf_X(x)=\\sum_y f(x,y).\n$$",
    "example": "Tính phân phối biên duyên của số mặt ngửa khi tung hai đồng xu độc lập."
  }
]
