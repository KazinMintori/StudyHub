export const slides = [
  {
    "note": "18-kiem-dinh-gia-thuyet-1",
    "title": "Cấu trúc kiểm định giả thuyết thống kê",
    "bullets": [
      "Giả thuyết không H0 đại diện cho trạng thái mặc định, không có hiệu ứng hay khác biệt.",
      "Giả thuyết đối H1 là điều nhà nghiên cứu tìm kiếm bằng chứng để ủng hộ.",
      "Thống kê kiểm định tóm tắt dữ liệu mẫu để đối chiếu với phân phối dưới H0."
    ],
    "formula": "$$\n\\begin{aligned}&H_0:\\ \\theta=\\theta_0,\\\\&H_1:\\ \\theta\\ne\\theta_0.\\end{aligned}\n$$",
    "example": "Kiểm định xem một đồng xu có cân bằng hay không: H0: p = 0,5 đối với H1: p khác 0,5."
  },
  {
    "note": "18-kiem-dinh-gia-thuyet-1",
    "title": "Khái niệm giá trị p-value",
    "bullets": [
      "Xác suất quan sát được kết quả cực đoan như mẫu khi giả thiết H0 đúng tuyệt đối.",
      "Giá trị p càng nhỏ cho thấy dữ liệu càng mâu thuẫn mạnh mẽ với giả thuyết H0.",
      "Giá trị p không phải là xác suất giả thuyết H0 đúng.",
      "Công thức dùng thống kê |T| cho kiểm định hai phía đối xứng. Cách định nghĩa “cực đoan” phải phù hợp với đối thuyết."
    ],
    "formula": "$$\np=P_{H_0}(|T|\\ge|t_{\\mathrm{obs}}|).\n$$",
    "example": "Thu được p-value = 0,012 nghĩa là nếu H0 đúng, chỉ có 1,2% cơ hội quan sát thấy khác biệt lớn như vậy."
  },
  {
    "note": "18-kiem-dinh-gia-thuyet-1",
    "title": "Quy tắc quyết định và Mức ý nghĩa alpha",
    "bullets": [
      "Mức ý nghĩa alpha là ngưỡng rủi ro được ấn định trước khi phân tích dữ liệu.",
      "Bác bỏ giả thuyết không H0 nếu giá trị p-value nhỏ hơn hoặc bằng alpha.",
      "Không bác bỏ H0 không đồng nghĩa với việc đã chứng minh H0 là chân lý."
    ],
    "formula": "$$\np\\le\\alpha\n$$",
    "example": "Bác bỏ H₀ khi p ≤ α. Không bác bỏ H₀ có nghĩa chưa đủ bằng chứng chống lại H₀ ở mức đã chọn."
  }
]
