export const slides = [
  {
    "title": "Kiểm định dấu cần hai dấu cân bằng",
    "bullets": [
      "Với mẫu liên tục độc lập, kiểm định dấu khảo sát trung vị mà không cần đối xứng.",
      "Khi bỏ các hiệu bằng không, phải kiểm tra giả thuyết cân bằng dấu trên các hiệu còn lại.",
      "Với dữ liệu rời rạc, điều kiện trung vị đơn thuần chưa đủ cho cách bỏ số không."
    ],
    "formula": "$$\nK\\sim\\mathrm{Binomial}(n^*,1/2)\n$$",
    "example": "Bảy dấu dương trên chín hiệu khác không cho giá trị $p$ hai phía $0{,}17969$.",
    "note": "44-phuong-phap-phi-tham-so"
  },
  {
    "title": "Wilcoxon cần đối xứng và xử lý hạng trùng",
    "bullets": [
      "Xếp hạng trị tuyệt đối của hiệu, rồi cộng hạng dương và hạng âm.",
      "Các hiệu độc lập, đối xứng cho phép xét các cách gán dấu dưới giả thuyết không.",
      "Hạng trùng cần phân phối hoán dấu phù hợp, không dùng nguyên bảng không trùng."
    ],
    "formula": "$$\nW=\\min(W^+,W^-)\n$$",
    "example": "Chín hiệu có hai hạng $2{,}5$ cho $W=3{,}5$ và giá trị $p$ chính xác $12/512=0{,}0234375$.",
    "note": "44-phuong-phap-phi-tham-so"
  },
  {
    "title": "Mann–Whitney không kiểm định mọi trung vị",
    "bullets": [
      "Phép thử cổ điển được hiệu chuẩn khi hai mẫu độc lập có cùng phân phối dưới giả thuyết không.",
      "Chỉ trong mô hình cùng hình dạng, khác vị trí mới diễn giải thành so sánh trung vị.",
      "Spearman là tương quan Pearson của hạng. Công thức hiệu hạng rút gọn chỉ dùng khi không có trùng."
    ],
    "formula": "$$\nU_1=R_1-\\frac{n_1(n_1+1)}2\n$$",
    "example": "Hai nhóm cỡ $4$ và $5$ cho $U_1=17$, $U_2=3$ và giá trị $p$ hai phía $14/126$.",
    "note": "44-phuong-phap-phi-tham-so"
  },
  {
    "title": "K–S thông thường cần giả thuyết liên tục đã cho",
    "bullets": [
      "Thống kê là khoảng cách dọc lớn nhất giữa hàm thực nghiệm và hàm giả thuyết.",
      "Các tham số giả thuyết phải được cho trước khi lấy mẫu.",
      "Nếu khớp tham số từ mẫu, dùng hiệu chỉnh phù hợp hoặc mô phỏng có khớp lại mỗi lần."
    ],
    "formula": "$$\nD_n=\\sup_x|F_n(x)-F_0(x)|\n$$",
    "example": "Năm điểm so với $U(0,1)$ cho $D_n=0{,}20$, chưa bác bỏ ở mức $5\\%$.",
    "note": "44-phuong-phap-phi-tham-so"
  }
]
