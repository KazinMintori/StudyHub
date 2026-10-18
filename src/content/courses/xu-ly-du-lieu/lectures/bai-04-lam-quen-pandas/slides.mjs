export const slides = [
  {
    "note": "bai-04-lam-quen-pandas",
    "title": "Series và DataFrame mang nhãn",
    "bullets": [
      "Series có một trục nhãn, DataFrame có nhãn hàng và cột.",
      "Kiểm tra kiểu cột và giá thiếu trước khi tính hoặc so sánh."
    ],
    "formula": "",
    "example": "Chọn một tên cột trả Series, còn danh sách tên cột giữ kết quả DataFrame."
  },
  {
    "note": "bai-04-lam-quen-pandas",
    "title": "Chọn theo nhãn hoặc theo vị trí",
    "bullets": [
      "loc chọn theo nhãn, iloc chọn theo vị trí.",
      "Trong pandas 3, gán qua đối tượng trung gian không cập nhật DataFrame gốc."
    ],
    "formula": "",
    "example": "Dùng df.loc[mask, \"gia\"] = ... để chỉ rõ hàng và cột đích."
  },
  {
    "note": "bai-04-lam-quen-pandas",
    "title": "Phép toán khớp nhãn trước khi tính",
    "bullets": [
      "Hai Series khác thứ tự vẫn được ghép theo nhãn.",
      "Nhãn chỉ có một bên có thể tạo kết quả thiếu, cần nêu cách xử lý."
    ],
    "formula": "",
    "example": "Nhãn b có giá 20 và 30 cho tổng 50 dù nằm ở hai vị trí khác nhau."
  },
  {
    "note": "bai-04-lam-quen-pandas",
    "title": "Mẫu số và tập hàng là một phần của kết luận",
    "bullets": [
      "count và số hàng có thể khác nhau khi có giá thiếu.",
      "So hai trung bình qua thời gian cần kiểm tra tập đối tượng được quan sát."
    ],
    "formula": "",
    "example": "Trong bài tập, trung bình toàn cột giảm nhưng trung bình trên cùng a, b lại tăng."
  }
]
