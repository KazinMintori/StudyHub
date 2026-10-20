export const slides = [
  {
    "note": "35-luat-so-lon-va-dinh-ly-gioi-han",
    "title": "Ba dạng hội tụ có độ mạnh khác nhau",
    "bullets": [
      "Hội tụ theo phân phối yêu cầu CDF hội tụ tại mọi điểm liên tục của CDF giới hạn.",
      "Hội tụ theo xác suất yêu cầu xác suất vượt một ngưỡng sai số dương tiến về 0.",
      "Hội tụ hầu chắc chắn yêu cầu từng quỹ đạo hội tụ, ngoại trừ tập có xác suất 0."
    ],
    "formula": "$$\nX_n\\xrightarrow{a.s.}X\\implies X_n\\xrightarrow{P}X\n$$",
    "example": "Dãy khoảng trượt hội tụ theo xác suất về 0, nhưng không hội tụ hầu chắc chắn. Hội tụ theo xác suất luôn kéo theo hội tụ theo phân phối."
  },
  {
    "note": "35-luat-so-lon-va-dinh-ly-gioi-han",
    "title": "Luật số lớn cần tính khả tích",
    "bullets": [
      "Giả sử dãy quan sát độc lập, cùng phân phối và có $\\mathbb E[|X_i|]<\\infty$.",
      "Luật yếu cho trung bình mẫu hội tụ theo xác suất về kỳ vọng.",
      "Luật mạnh cho hội tụ hầu chắc chắn. Chứng minh bằng Chebyshev trong Notes dùng thêm phương sai hữu hạn."
    ],
    "formula": "$$\n\\bar X_n\\xrightarrow{a.s.}\\mu\n$$",
    "example": "Tỷ lệ mặt ngửa của các lần tung đồng xu cân đối độc lập hội tụ hầu chắc chắn về $0{,}5$."
  },
  {
    "note": "35-luat-so-lon-va-dinh-ly-gioi-han",
    "title": "CLT mô tả độ lệch đã chuẩn hóa",
    "bullets": [
      "Giả sử quan sát độc lập, cùng phân phối, có trung bình $\\mu$ và $0<\\sigma^2<\\infty$.",
      "Đặt $Z_n=(\\bar X_n-\\mu)/(\\sigma/\\sqrt n)$. Biến này hội tụ theo phân phối về Chuẩn chuẩn tắc.",
      "Thang độ lệch chuẩn $1/\\sqrt n$ không phải một cận tốc độ sai số xấp xỉ phân phối."
    ],
    "formula": "$$\nZ_n\\xrightarrow{d}\\mathcal N(0,1)\n$$",
    "example": "Tổng $12$ biến $U(0,1)$ độc lập trừ $6$ có trung bình $0$ và phương sai $1$, nhưng chỉ xấp xỉ Chuẩn ở vùng trung tâm."
  },
  {
    "note": "35-luat-so-lon-va-dinh-ly-gioi-han",
    "title": "Hiệu chỉnh liên tục và giới hạn của CLT",
    "bullets": [
      "Khi xấp xỉ biến Nhị thức bằng biến Chuẩn, khoảng nguyên từ $a$ đến $b$ được nới sang $a-0{,}5$ và $b+0{,}5$.",
      "Độ chính xác phải được kiểm tra cho biến cố đang xét, nhất là ở đuôi xa.",
      "Biến Cauchy không có kỳ vọng xác định. Trung bình của các biến Cauchy chuẩn độc lập vẫn có cùng phân phối Cauchy chuẩn."
    ],
    "formula": "$$\n\\bar X_n\\sim\\mathrm{Cauchy}(0,1)\n$$",
    "example": "Với $100$ lần tung đồng xu, xác suất có từ $45$ đến $55$ mặt ngửa là $0{,}728747$. Xấp xỉ có hiệu chỉnh cho $0{,}728668$."
  }
]
