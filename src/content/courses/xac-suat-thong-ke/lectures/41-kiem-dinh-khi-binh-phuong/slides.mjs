export const slides = [
  {
    "title": "Pearson so tần số quan sát với kỳ vọng",
    "bullets": [
      "Các nhóm loại trừ nhau, phủ mọi kết cục và có xác suất dương.",
      "Thống kê cộng các bình phương độ lệch, mỗi bình phương chia cho tần số kỳ vọng.",
      "Với xác suất đã cho và các tần số đủ lớn, phân phối xấp xỉ có $k-1$ bậc tự do."
    ],
    "formula": "$$\nQ=\\sum_{i=1}^k\\frac{(O_i-E_i)^2}{E_i}\n$$",
    "example": "Bốn nhóm tỷ lệ $9:3:3:1$ cho $Q=1{,}6444$ và $p=0{,}6493$, chưa bác bỏ mô hình.",
    "note": "41-kiem-dinh-khi-binh-phuong"
  },
  {
    "title": "Trừ tham số phải phù hợp cách khớp mô hình",
    "bullets": [
      "Với các điều kiện chính quy, MLE hoặc cực tiểu Chi bình phương từ tần số nhóm làm mất thêm bậc tự do.",
      "$r$ là số tham số định danh được khớp từ cùng bảng nhóm.",
      "Khớp từ dữ liệu thô rồi phân nhóm có thể cần hiệu chuẩn khác hoặc mô phỏng toàn quy trình."
    ],
    "formula": "$$\n\\nu=k-1-r\n$$",
    "example": "Mô hình chuẩn khớp hai tham số từ tần số trong mười khoảng cố định dùng xấp xỉ bảy bậc tự do.",
    "note": "41-kiem-dinh-khi-binh-phuong"
  },
  {
    "title": "Độc lập và đồng nhất khác thiết kế lấy mẫu",
    "bullets": [
      "Độc lập dùng một mẫu chung, phân loại mỗi đối tượng theo hai tiêu chí.",
      "Đồng nhất cố định trước cỡ mẫu trong các quần thể độc lập.",
      "Có cùng công thức Pearson và xấp xỉ $(r-1)(c-1)$ bậc tự do."
    ],
    "formula": "$$\nE_{ij}=\\frac{R_iC_j}{N}\n$$",
    "example": "Bảng hai dòng, ba cột cho $Q=16{,}6667$ và $p\\approx0{,}00024$.",
    "note": "41-kiem-dinh-khi-binh-phuong"
  },
  {
    "title": "Bảng thưa cần hiệu chuẩn phù hợp",
    "bullets": [
      "Các ngưỡng tần số kỳ vọng là hướng dẫn đánh giá xấp xỉ, không phải bảo đảm cho mọi bảng.",
      "Fisher chính xác cho bảng $2\\times2$ điều kiện hóa trên tổng biên dưới giả thuyết không.",
      "Trong công thức, $m=\\min(r-1,c-1)$. Cramér V đo cường độ liên kết, cần diễn giải theo bối cảnh."
    ],
    "formula": "$$\nV=\\sqrt{\\frac{Q}{Nm}}\n$$",
    "example": "Bảng phản ứng $[3,1]$ và $[1,5]$ cho giá trị $p$ Fisher một phía $25/210$.",
    "note": "41-kiem-dinh-khi-binh-phuong"
  }
]
