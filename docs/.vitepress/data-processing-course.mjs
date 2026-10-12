const lesson = (slug, title, prerequisites, supportingConcepts = []) => ({ slug, title, prerequisites, supportingConcepts, status: 'ready' })
const slide = (title, bullets, note, example = '') => ({ title, bullets, note, formula: '', example })
const ids = {
  intro: 'bai-01-tong-quan-cong-cu-chinh-sach-ai', python: 'bai-02-python-co-ban',
  numpy: 'bai-03-numpy', pandas: 'bai-04-lam-quen-pandas', tables: 'bai-05-series-dataframe-chuyen-sau',
  io: 'bai-06-ket-noi-truy-xuat-du-lieu', text: 'bai-07-xu-ly-chuoi', time: 'bai-08-du-lieu-thoi-gian',
  clean: 'bai-10-lam-sach-du-lieu', llm: 'bai-11-llm-du-lieu-phi-cau-truc',
  plot: 'bai-12-truc-quan-hoa-co-ban', advanced: 'bai-13-truc-quan-hoa-nang-cao', report: 'bai-14-ke-chuyen-bang-du-lieu'
}

export const dataProcessingCourse = {
  id: 'xu-ly-du-lieu', code: '04', name: 'Lập trình xử lý dữ liệu', short: 'Xử lý dữ liệu', current: true,
  description: 'Học theo Python for Data Analysis: Từ Python, NumPy và pandas đến làm sạch, trực quan hóa và kiểm tra kết luận.',
  foundations: ['bien-kieu', 'list', 'dictionary', 'ham-lap-trinh', 'vong-lap', 'mang', 'chi-muc', 'con-tro', 'vector-hoa', 'broadcasting', 'gia-tri-thieu', 'dataframe', 'groupby', 'thong-ke-mo-ta'],
  parts: [
    { title: 'Phần 1. Công cụ và Python', description: 'Đặt câu hỏi, dựng môi trường và viết các bước xử lý bằng Python.', lessons: [ids.intro, ids.python] },
    { title: 'Phần 2. NumPy và pandas', description: 'Tính trên mảng, chọn dữ liệu bảng, tổng hợp nhóm, nối và chuyển dạng.', lessons: [ids.numpy, ids.pandas, ids.tables] },
    { title: 'Phần 3. Nạp, chuẩn hóa và làm sạch dữ liệu', description: 'Đọc tệp và SQL, xử lý chuỗi, thời gian, giá trị thiếu và dữ liệu không hợp lệ.', lessons: [ids.io, ids.text, ids.time, ids.clean] },
    { title: 'Phần 4. Trích xuất văn bản bằng LLM', description: 'Phần bổ sung: Schema, kiểm tra phản hồi và đánh giá trên mẫu đã gán nhãn.', lessons: [ids.llm] },
    { title: 'Phần 5. Biểu đồ và kết luận', description: 'Chọn biểu đồ, đọc thang đo và kiểm tra mẫu số, cơ cấu nhóm và phạm vi kết luận.', lessons: [ids.plot, ids.advanced, ids.report] }
  ],
  lessons: [
    lesson(ids.intro, 'Tổng quan xử lý dữ liệu & công cụ', ['bien-kieu', 'list', 'dictionary']),
    lesson(ids.python, 'Python cơ bản cho xử lý dữ liệu', ['bien-kieu', 'list', 'dictionary', 'vong-lap', 'ham-lap-trinh'], ['json-du-lieu']),
    lesson(ids.numpy, 'NumPy & tư duy vector hóa', ['mang', 'chi-muc', 'con-tro', 'vector-hoa', 'broadcasting']),
    lesson(ids.pandas, 'Làm quen với pandas', ['chi-muc', 'dictionary', 'gia-tri-thieu'], ['dataframe']),
    lesson(ids.tables, 'Series & DataFrame chuyên sâu', ['chi-muc', 'gia-tri-thieu', 'vector-hoa'], ['dataframe', 'groupby', 'noi-bang', 'du-lieu-dang-dai']),
    lesson(ids.io, 'Đọc, lưu trữ & truy xuất dữ liệu', ['dictionary', 'ham-lap-trinh', 'gia-tri-thieu'], ['json-du-lieu', 'api-du-lieu', 'schema-du-lieu']),
    lesson(ids.text, 'Xử lý dữ liệu chuỗi', ['bien-kieu', 'gia-tri-thieu', 'vector-hoa'], ['bieu-thuc-chinh-quy']),
    lesson(ids.time, 'Xử lý dữ liệu thời gian', ['chi-muc', 'gia-tri-thieu'], ['mui-gio', 'cua-so-truot']),
    lesson(ids.clean, 'Làm sạch dữ liệu có cấu trúc', ['gia-tri-thieu', 'dictionary'], ['schema-du-lieu', 'ngoai-lai', 'khoang-tu-phan-vi']),
    lesson(ids.llm, 'Trích xuất dữ liệu văn bản bằng LLM', ['dictionary', 'ham-lap-trinh', 'gia-tri-thieu'], ['schema-du-lieu', 'json-du-lieu', 'llm-trich-xuat']),
    lesson(ids.plot, 'Trực quan hóa cơ bản', ['gia-tri-thieu', 'thong-ke-mo-ta'], ['histogram']),
    lesson(ids.advanced, 'Trực quan hóa nâng cao & đọc biểu đồ', ['thong-ke-mo-ta', 'gia-tri-thieu'], ['histogram', 'ngoai-lai', 'khoang-tu-phan-vi']),
    lesson(ids.report, 'Kể chuyện bằng dữ liệu & thẩm định phân tích AI', ['gia-tri-thieu', 'thong-ke-mo-ta', 'ket-luan-nhan-qua', 'suy-rong-thong-ke'], ['groupby'])
  ],
  slides: [],
  illustration: 'broadcast'
}
