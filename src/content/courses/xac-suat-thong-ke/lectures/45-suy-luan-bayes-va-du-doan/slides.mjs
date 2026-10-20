export const slides = [
  {
    "note": "45-suy-luan-bayes-va-du-doan",
    "title": "Hậu nghiệm kết hợp tiên nghiệm với hàm hợp lý",
    "bullets": [
      "Tiên nghiệm mô tả thông tin về tham số trước dữ kiện đang xét.",
      "Hàm hợp lý giữ dữ liệu cố định và thay đổi tham số.",
      "Nhân hai thành phần rồi chuẩn hóa, với hằng số chuẩn hóa dương và hữu hạn."
    ],
    "formula": "$$\n\\pi(\\theta\\mid D)\\propto L(\\theta)\\pi_0(\\theta)\n$$",
    "example": "Trong mô hình hai trạng thái của ví dụ, một lần thấy lỗi cập nhật xác suất trạng thái B từ 0,1 thành 4/13."
  },
  {
    "note": "45-suy-luan-bayes-va-du-doan",
    "title": "Beta liên hợp với mẫu Bernoulli",
    "bullets": [
      "Các kết quả độc lập và cùng xác suất thành công khi biết tham số.",
      "Với tiên nghiệm beta, đặt $a^{\\prime}=a+s$ và $b^{\\prime}=b+n-s$ sau $s$ thành công trong $n$ lần thử.",
      "Trung bình hậu nghiệm và điểm cực đại mật độ trả lời hai câu hỏi khác nhau."
    ],
    "formula": "$$\n\\theta\\mid D\\sim\\mathrm{Beta}(a^{\\prime},b^{\\prime})\n$$",
    "example": "Tiên nghiệm Beta(1,1), ba thành công trong bốn lần thử cho hậu nghiệm Beta(4,2), có trung bình 2/3."
  },
  {
    "note": "45-suy-luan-bayes-va-du-doan",
    "title": "Dự đoán dùng toàn bộ phân phối hậu nghiệm",
    "bullets": [
      "Tích phân xác suất có điều kiện qua hậu nghiệm tính cả sự chưa biết về tham số.",
      "Một lần thử Bernoulli tiếp theo có xác suất thành công bằng trung bình hậu nghiệm.",
      "Hai lần cùng thành công cần kỳ vọng bình phương, với giả thiết độc lập khi biết tham số."
    ],
    "formula": "$$\nP(Y=1\\mid D)=E(\\theta\\mid D)\n$$",
    "example": "Với hậu nghiệm Beta(4,2), xác suất hai lần tiếp theo cùng thành công là 10/21, khác 4/9 khi chỉ bình phương trung bình."
  },
  {
    "note": "45-suy-luan-bayes-va-du-doan",
    "title": "Khoảng hậu nghiệm cần diễn giải theo mô hình Bayes",
    "bullets": [
      "Khoảng xác suất hậu nghiệm được xác định sau khi điều kiện hóa theo dữ liệu.",
      "Xác suất tham số thuộc khoảng dùng tiên nghiệm và hàm hợp lý đã nêu.",
      "Mức tin cậy tần suất mô tả độ bao phủ qua lấy mẫu lặp lại và cần cách diễn giải riêng."
    ],
    "formula": "",
    "example": "Với hậu nghiệm beta có tham số 4 và 2, khoảng hai đuôi bằng nhau 95% có cận xấp xỉ 0,2836 và 0,9473."
  }
]
