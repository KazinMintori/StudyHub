export const slides = [
  {
    "note": "phu-luc-a-numpy-nang-cao",
    "title": "Metadata mô tả cách truy cập vùng dữ liệu",
    "bullets": [
      "dtype, shape và strides cùng quyết định cách đọc một mảng.",
      "Phân biệt kiểu vô hướng NumPy với đối tượng mô tả dtype."
    ],
    "formula": "",
    "example": "Một mảng cấu trúc vẫn có một dtype chung gồm nhiều trường."
  },
  {
    "note": "phu-luc-a-numpy-nang-cao",
    "title": "Đổi bố trí không luôn sao chép",
    "bullets": [
      "reshape và ravel cần bố trí tương thích để dùng lại dữ liệu theo thứ tự yêu cầu.",
      "flatten tạo vùng chứa mới, nhưng với dtype object vẫn cần phân biệt bản sao nông của tham chiếu."
    ],
    "formula": "",
    "example": "Kiểm np.shares_memory trên đúng hai mảng cần so."
  },
  {
    "note": "phu-luc-a-numpy-nang-cao",
    "title": "Tổ chức phép toán theo trục và thứ tự",
    "bullets": [
      "Ufunc có các thao tác reduce, accumulate, outer và reduceat.",
      "argsort, lexsort, partition và searchsorted phục vụ những dạng sắp xếp hoặc tìm vị trí khác nhau."
    ],
    "formula": "",
    "example": "searchsorted giả sử đầu vào đã được sắp theo quy tắc đang dùng."
  },
  {
    "note": "phu-luc-a-numpy-nang-cao",
    "title": "Hiệu năng phải được đo trên nhiệm vụ thực tế",
    "bullets": [
      "vectorize và frompyfunc không tự biến hàm Python thành vòng lặp số học đã biên dịch.",
      "Numba, mảng liên tục và memmap có ích trong điều kiện phù hợp, nhưng không bảo đảm mọi bước đều nhanh hay ít RAM."
    ],
    "formula": "",
    "example": "Một biểu thức trên memmap vẫn có thể tạo mảng trung gian lớn."
  }
]
