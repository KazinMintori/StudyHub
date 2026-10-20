export const slides = [
  {
    "title": "Suy luận hồi quy có điều kiện trên thiết kế",
    "bullets": [
      "Mô hình đường thẳng cần các giá trị thiết kế không đồng nhất và $n>2$.",
      "Sai số chuẩn độc lập, trung bình bằng không và cùng phương sai cho phân phối mẫu chính xác.",
      "Hồi quy trên dữ liệu quan sát không tự xác lập quan hệ nhân quả."
    ],
    "formula": "$$\n\\hat\\beta_1\\sim\\mathcal N\\left(\\beta_1,\\frac{\\sigma^2}{S_{XX}}\\right)\n$$",
    "example": "Năm cặp dữ liệu cho hệ số chặn $1{,}30$, hệ số dốc $0{,}90$ và độ lệch chuẩn dư $0{,}7958$.",
    "note": "43-suy-luan-hoi-quy-tuyen-tinh"
  },
  {
    "title": "Student kiểm tra hệ số dốc dưới giả thuyết không",
    "bullets": [
      "Sai số chuẩn của hệ số dốc là độ lệch chuẩn dư chia căn của $S_{XX}$.",
      "Dưới giả thuyết hệ số dốc bằng không, thống kê có $n-2$ bậc tự do.",
      "Khoảng tin cậy hệ số dốc và kiểm định hai phía cùng mức cho kết luận tương ứng."
    ],
    "formula": "$$\nT=\\frac{\\hat\\beta_1}{s_e/\\sqrt{S_{XX}}}\\sim t(n-2)\n$$",
    "example": "Ví dụ cho $t=3{,}576$ và $p\\approx0{,}0374$, khoảng hệ số dốc $[0{,}0991,1{,}7009]$.",
    "note": "43-suy-luan-hoi-quy-tuyen-tinh"
  },
  {
    "title": "Quan sát mới còn chứa sai số cá thể",
    "bullets": [
      "Khoảng tin cậy kỳ vọng đo bất định của đường hồi quy tại một điểm thiết kế cố định.",
      "Khoảng dự báo cho quan sát mới độc lập chứa thêm phương sai $\\sigma^2$.",
      "Các khoảng tại từng điểm không phải dải bao phủ đồng thời toàn đường hồi quy."
    ],
    "formula": "$$\n\\mathrm{Var}(Y_0-\\hat y_0)=\\sigma^2(1+V_0)\n$$",
    "example": "Tại tâm $x_0=3$, khoảng cho kỳ vọng là $[2{,}87,5{,}13]$, khoảng dự báo là $[1{,}23,6{,}77]$.",
    "note": "43-suy-luan-hoi-quy-tuyen-tinh"
  },
  {
    "title": "Hồi quy bội cần hạng đầy đủ và bậc tự do dương",
    "bullets": [
      "$k$ là số biến dự báo và $p=k+1$ tính cả hệ số chặn.",
      "Ma trận thiết kế cần hạng cột đầy đủ và $n>p$.",
      "Biểu đồ phần dư giúp phát hiện vi phạm. Chúng không chứng minh các giả thiết đúng."
    ],
    "formula": "$$\ns_e^2=\\frac{\\mathrm{RSS}}{n-p}\n$$",
    "example": "Với hồi quy đơn, $p=2$ và kiểm định Fisher toàn cục thỏa $F=T^2$.",
    "note": "43-suy-luan-hoi-quy-tuyen-tinh"
  }
]
