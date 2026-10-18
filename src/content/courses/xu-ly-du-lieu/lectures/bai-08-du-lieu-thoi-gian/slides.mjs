export const slides = [
  {
    "note": "bai-08-du-lieu-thoi-gian",
    "title": "Thời điểm, khoảng thời gian và kỳ khác nhau",
    "bullets": [
      "Timestamp chỉ một mốc, Timedelta chỉ độ dài, Period chỉ một kỳ theo lịch.",
      "Đọc chuỗi ngày theo định dạng nguồn và giữ cờ lỗi chuyển đổi."
    ],
    "formula": "",
    "example": "Ngày không tồn tại và ngày bị thiếu có thể cùng thành NaT sau coerce."
  },
  {
    "note": "bai-08-du-lieu-thoi-gian",
    "title": "Gắn múi giờ khác đổi múi giờ",
    "bullets": [
      "tz_localize gán ngữ cảnh múi giờ cho dữ liệu chưa có múi giờ.",
      "tz_convert đổi cách biểu diễn một thời điểm đã gắn múi giờ."
    ],
    "formula": "",
    "example": "08:00 tại Hà Nội là 01:00 UTC trong ví dụ đang xét."
  },
  {
    "note": "bai-08-du-lieu-thoi-gian",
    "title": "Lịch quan sát quyết định kỳ so sánh",
    "bullets": [
      "shift theo hàng không tự hiểu tháng vắng trong bảng.",
      "Resample cần quy tắc biên, phép tổng hợp và kiểm kỳ đã kết thúc hay chưa."
    ],
    "formula": "",
    "example": "Mốc 29/06 chưa hoàn tất quý có nhãn 30/06."
  },
  {
    "note": "bai-08-du-lieu-thoi-gian",
    "title": "Cửa sổ và cùng kỳ cần giữ phạm vi",
    "bullets": [
      "Chọn rõ độ dài, min_periods và vị trí gắn kết quả cửa sổ.",
      "So cùng kỳ cần cùng tần số và mẫu số, không tự loại hết mùa vụ."
    ],
    "formula": "",
    "example": "Cửa sổ 7 ngày kết thúc hôm nay chỉ dùng hôm nay và sáu ngày trước."
  }
]
