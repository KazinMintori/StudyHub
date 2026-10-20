export const slides = [
  {
    "note": "19-kiem-dinh-gia-thuyet-2",
    "title": "Mô hình Benford và giới hạn áp dụng",
    "bullets": [
      "Chữ số đầu có phân phối logarit trong mô hình Benford.",
      "Dữ liệu không tự động tuân theo mô hình này. Cần kiểm tra cơ chế sinh và phạm vi độ lớn.",
      "Bác bỏ Benford không chứng minh hành vi gian lận."
    ],
    "formula": "$$\n\\begin{aligned}p_d&=\\log_{10}(1+1/d),\\\\d&=1,2,\\dots,9.\\end{aligned}\n$$",
    "example": "Chữ số 1 có xác suất khoảng 0,301 trong mô hình Benford."
  },
  {
    "note": "19-kiem-dinh-gia-thuyet-2",
    "title": "Thống kê Chi bình phương về độ phù hợp",
    "bullets": [
      "Oᵢ là tần số quan sát và Eᵢ là tần số kỳ vọng dương.",
      "Mỗi ô đóng góp bình phương sai lệch chia cho kỳ vọng.",
      "Dùng mô phỏng khi xấp xỉ tiệm cận không đủ tin cậy."
    ],
    "formula": "$$\n\\begin{aligned}r_i&=(O_i-E_i)^2/E_i,\\\\\\chi^2&=r_1+\\dots+r_k.\\end{aligned}\n$$",
    "example": "Ba đóng góp 0, 81 và 8,1 cho tổng χ² = 89,1."
  },
  {
    "note": "19-kiem-dinh-gia-thuyet-2",
    "title": "Đuôi phải và diễn giải p-value",
    "bullets": [
      "Giá trị χ² lớn cho thấy sai lệch lớn so với mô hình.",
      "Bậc tự do k−1 áp dụng khi mọi xác suất nhóm đã biết và không ước lượng thêm tham số.",
      "Mô phỏng hữu hạn không có lần vượt ngưỡng vẫn không chứng minh xác suất bằng 0."
    ],
    "formula": "$$\np=P(\\chi^2_{k-1}\\ge\\chi^2_{\\mathrm{obs}}).\n$$",
    "example": "Với χ² = 28,08 và 8 bậc tự do, p xấp xỉ 0,000459."
  }
]
