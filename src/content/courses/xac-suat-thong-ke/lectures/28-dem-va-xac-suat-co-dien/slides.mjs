export const slides = [
  {
    "note": "28-dem-va-xac-suat-co-dien",
    "title": "Quy tắc vách ngăn và tổ hợp lặp",
    "bullets": [
      "Chia $k$ vật phẩm giống nhau vào $n$ nhóm phân biệt tương ứng với số nghiệm nguyên của $x_1+\\dots+x_n=k$.",
      "Cho phép nhóm rỗng thì chọn vị trí cho $n-1$ vách ngăn trong $k+n-1$ vị trí.",
      "Nếu mọi nhóm đều có phần tử, cần $k\\ge n\\ge1$ và số cách là $\\binom{k-1}{n-1}$."
    ],
    "formula": "$$\nN=\\binom{k+n-1}{n-1}\n$$",
    "example": "Phân chia $10$ tác vụ cho $4$ máy chủ có $286$ cách khi cho phép máy chủ rảnh, và $84$ cách khi mỗi máy nhận ít nhất một tác vụ."
  },
  {
    "note": "28-dem-va-xac-suat-co-dien",
    "title": "Nguyên lý bù trừ cho ba biến cố",
    "bullets": [
      "Đặt $U=A\\cup B\\cup C$ là biến cố có ít nhất một trong ba sự kiện xảy ra.",
      "Gọi $S_1$ là tổng ba xác suất riêng, $S_2$ là tổng ba xác suất giao đôi và $S_3$ là xác suất giao ba.",
      "Cộng các xác suất riêng, trừ các phần giao đôi rồi cộng lại phần giao ba để mỗi kết quả được tính đúng một lần."
    ],
    "formula": "$$\nP(U)=S_1-S_2+S_3\n$$",
    "example": "Trong ví dụ $120$ sinh viên, số người biết ít nhất một ngôn ngữ là $155-60+10=105$."
  },
  {
    "note": "28-dem-va-xac-suat-co-dien",
    "title": "Xác suất hình học trên miền liên tục",
    "bullets": [
      "Giả sử điểm ngẫu nhiên có phân phối đều trên miền đo được $\\Omega$.",
      "Độ đo của miền phải dương và hữu hạn: $0<\\mu(\\Omega)<\\infty$.",
      "Xác suất bằng tỷ số độ dài, diện tích hoặc thể tích của miền biến cố với miền mẫu."
    ],
    "formula": "$$\nP(A)=\\frac{\\mu(A)}{\\mu(\\Omega)}\n$$",
    "example": "Hai người đến độc lập, đều trong $60$ phút và đợi tối đa $15$ phút có xác suất gặp $7/16=43{,}75\\%$."
  },
  {
    "note": "28-dem-va-xac-suat-co-dien",
    "title": "Tính liên tục của xác suất",
    "bullets": [
      "Tiên đề cộng tính đếm được áp dụng cho một dãy biến cố đôi một xung khắc.",
      "Nếu $A_n$ tăng dần, biến cố giới hạn là hợp của cả dãy.",
      "Nếu $A_n$ giảm dần, biến cố giới hạn là giao của cả dãy."
    ],
    "formula": "$$\n\\lim_{n\\to\\infty}P(A_n)=P(A)\n$$",
    "example": "Với phân phối đều trên $[0,1]$, các khoảng $[0,1/n]$ giảm về $\\{0\\}$ và xác suất tiến về $0$."
  }
]
