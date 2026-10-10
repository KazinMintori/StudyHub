// Sơ đồ trình bày của môn Xử lý dữ liệu. Dữ liệu số giữ cùng ví dụ trong Notes.
export const dataDiagrams = {
  effort: {
    layout: 'effort', title: 'Thời gian nằm ở đâu trong một dự án dữ liệu?',
    steps: ['Thu thập', 'Khám phá', 'Làm sạch', 'Biến đổi', 'Thẩm định'],
    caption: 'Tỷ lệ 80/20 minh họa trọng tâm công việc, không phải định mức cố định cho mọi dự án.'
  },
  'python-stack': {
    layout: 'stack', title: 'Ngăn xếp tính toán khoa học Python',
    items: [
      { label: '05', title: 'Ứng dụng chuyên sâu', text: 'Học máy: Scikit-learn · Học sâu: PyTorch' },
      { label: '04', title: 'Trực quan hóa dữ liệu', text: 'Matplotlib · Seaborn' },
      { label: '03', title: 'Xử lý dữ liệu bảng', text: 'Pandas · DataFrame · Series' },
      { label: '02', title: 'Mảng đa chiều và đại số tuyến tính', text: 'NumPy · ndarray' },
      { label: '01', title: 'Ngôn ngữ nền tảng', text: 'Python Core · CPython Runtime' }
    ], caption: 'Đọc từ dưới lên: từ nền tảng ngôn ngữ đến các công cụ ứng dụng.'
  },
  jupyter: {
    title: 'Từ ô mã đến kết quả trong Jupyter',
    items: [
      { title: 'Giao diện trình duyệt · Client', text: 'Nhập mã trong cell và xem kết quả trả về.' },
      { title: 'Máy chủ Notebook · Server', text: 'Chuyển tiếp yêu cầu thực thi và kết quả giữa trình duyệt với kernel.' },
      { title: 'IPython Kernel', text: 'Tiến trình Python thực thi mã và lưu trạng thái trong RAM.', code: 'Yêu cầu thực thi → Python → Kết quả trả về' }
    ], caption: 'Luồng trao đổi đi cả hai chiều. Kênh trình duyệt–máy chủ dùng WebSocket, còn máy chủ–kernel dùng thông điệp ZeroMQ.'
  },
  'python-collections': {
    layout: 'compare', title: 'Bốn cấu trúc dữ liệu, bốn cách tổ chức bộ nhớ',
    items: [
      { title: 'list', text: 'Mảng động chứa con trỏ', lines: ['Truy cập theo chỉ số nguyên: O(1).', 'Kiểm tra tồn tại: O(n), quét tuần tự.'] },
      { title: 'tuple', text: 'Mảng con trỏ cố định, bất biến', lines: ['Truy cập theo chỉ số nguyên: O(1).', 'Kiểm tra tồn tại: O(n), quét tuần tự.'] },
      { title: 'dict', text: 'Bảng băm ánh xạ khóa tới giá trị', lines: ['Tra cứu theo khóa: O(1) trung bình.', 'Kiểm tra tồn tại của khóa: O(1) trung bình.'] },
      { title: 'set', text: 'Bảng băm chỉ chứa khóa', lines: ['Không hỗ trợ truy cập theo chỉ số.', 'Kiểm tra tồn tại: O(1) trung bình.'] }
    ]
  },
  'ndarray-memory': {
    layout: 'stack', title: 'ndarray = siêu dữ liệu + vùng đệm',
    items: [{ title: 'Siêu dữ liệu của mảng', lines: ['dtype: np.int64 · 8 byte/phần tử', 'shape: (4, 3) · 4 hàng, 3 cột', 'strides: (24, 8) · 24 byte/hàng, 8 byte/cột', 'data pointer: Trỏ tới đầu vùng nhớ đệm liên tục'] }],
    memory: [[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]],
    caption: 'Các phần tử được lưu nối tiếp theo thứ tự hàng 0 → 1 → 2 → 3. Màu đánh dấu ranh giới hàng trong cùng một vùng đệm.'
  },
  'view-copy': {
    layout: 'compare', title: 'Truy cập ndarray: Dùng chung hay tách bộ nhớ?',
    items: [
      { title: 'Lát cắt cơ bản → View', code: 'arr[1:3, :]', lines: ['Dùng chung vùng đệm bộ nhớ.', 'Thay đổi view làm thay đổi mảng gốc.'] },
      { title: 'Chỉ mục mảng → Copy', code: 'arr[[0, 2], :]\narr[arr > 0]', lines: ['Cấp phát vùng nhớ mới độc lập.', 'Thay đổi copy không ảnh hưởng mảng gốc.'] }
    ]
  },
  'dataframe-series': {
    title: 'Từ bảng hai chiều đến một cột có nhãn',
    items: [
      { title: 'DataFrame · 2D', text: 'Các cột Series dùng chung Index. Index bên trái là nhãn hàng.', columns: ['Index', 'name', 'price', 'room_type'], rows: [['0 (id 101)', 'Depto Plaza Ñuñoa', '45000.0', 'Entire'], ['1 (id 102)', 'Pieza cerca metro', '18000.0', 'Private'], ['2 (id 103)', 'Loft Irarrázaval', '72000.0', 'Entire']] },
      { title: 'Trích xuất một cột', code: 'df["price"]' },
      { title: 'Series · 1D', text: 'Mảng dữ liệu một chiều gắn liền với mảng nhãn.', columns: ['Index', 'price'], rows: [['0', '45000.0'], ['1', '18000.0'], ['2', '72000.0']] }
    ]
  },
  'index-alignment': {
    title: 'Phép trừ căn chỉnh theo nhãn, không theo vị trí',
    items: [
      { title: 'Hai Series ban đầu', columns: ['Vị trí', 'Series A · Giá cũ', 'Series B · Giá mới'], rows: [['0', 'A → 100', 'B → 220'], ['1', 'B → 200', 'A → 90'], ['2', 'C → 50', 'D → 70']] },
      { title: 'Kết quả B − A', code: 'B - A', columns: ['Index', 'Phép toán tương ứng', 'Kết quả'], rows: [['A', '90 − 100', '−10'], ['B', '220 − 200', '20'], ['C', 'NaN − 50', 'NaN'], ['D', '70 − NaN', 'NaN']] }
    ], caption: 'Pandas ghép các giá trị cùng nhãn trước khi trừ. Thiếu một phía thì kết quả tại nhãn đó là NaN.'
  },
  groupby: {
    layout: 'compare', title: 'Cùng một cách chia nhóm, hai dạng kết quả',
    intro: 'Bảng gốc: 12 dòng → groupby("phan_khuc")', groups: ['Nhóm “re”', 'Nhóm “trung”', 'Nhóm “cao”'],
    items: [
      { title: 'agg → Thu gọn còn 3 dòng', code: '.agg(...)', columns: ['phan_khuc', 'gia_trung_vi'], rows: [['re', '21,500.0'], ['trung', '55,000.0'], ['cao', '120,000.0']] },
      { title: 'transform → Giữ nguyên 12 dòng', code: '.transform(...)', text: 'Mỗi dòng nhận đúng giá trị thống kê của nhóm chứa nó.', lines: ['Gắn cờ theo nhóm.', 'Chuẩn hóa trong từng nhóm.'] }
    ]
  },
  'csv-loading': {
    layout: 'compare', title: 'Đọc toàn bộ hay chỉ đọc phần cần phân tích?',
    intro: 'Tệp CSV lớn trên đĩa · 90 cột: id, name, summary, space, description, …, price, …, first_review, …',
    items: [
      { title: 'Nạp toàn bộ', code: 'pd.read_csv(file)', lines: ['Nạp 90 cột vào RAM.', 'RAM: 1.2 GB.', 'Thời gian I/O: 15.4 giây.', 'Cột ngày vẫn là chuỗi thô.'], tone: 2 },
      { title: 'Đọc chọn lọc', code: 'pd.read_csv(file,\n    usecols=[...],\n    parse_dates=[...])', lines: ['Chỉ nạp 5 cột cần thiết.', 'RAM: khoảng 180 MB, giảm 85%.', 'Thời gian I/O: 2.1 giây.', 'Cột ngày chuyển thành datetime64.'], tone: 1 }
    ], caption: 'Các con số minh họa sự khác biệt giữa hai cách đọc, không phải cam kết hiệu năng trên mọi tệp và máy tính.'
  },
  'csv-parquet': {
    layout: 'compare', title: 'CSV và Parquet: lựa chọn theo nhu cầu lưu trữ',
    items: [
      { title: 'CSV · Văn bản', columns: ['Tiêu chí', 'Đặc điểm'], rows: [['Tổ chức', 'Theo dòng tuần tự'], ['Dung lượng', 'Lớn khi lưu văn bản thô không nén'], ['Kiểu dữ liệu', 'Không lưu schema kiểu, cần suy luận khi đọc'], ['Truy vấn cột', 'Phải đọc và phân tích nội dung tệp'], ['Phân vùng', 'Cần tự tổ chức tệp và thư mục']] },
      { title: 'Apache Parquet · Nhị phân', columns: ['Tiêu chí', 'Đặc điểm'], rows: [['Tổ chức', 'Định hướng cột'], ['Dung lượng', 'Hỗ trợ nén Snappy/ZSTD'], ['Kiểu dữ liệu', 'Lưu schema kiểu dữ liệu'], ['Truy vấn cột', 'Có thể chỉ đọc các cột cần thiết'], ['Phân vùng', 'Thường kết hợp thư mục kiểu Hive']] }
    ]
  },
  'api-provenance': {
    title: 'Lấy dữ liệu API và bảo toàn dấu vết',
    items: [
      { title: 'Open-Meteo API', text: 'Gọi HTTP GET một lần.' },
      { title: 'Response JSON thô', text: 'Lưu một bản trước khi chuyển đổi.', code: 'raw/weather_2025-01.json', lines: ['Bản lưu giữ dấu vết đầu vào để đối chiếu và tái lập.'] },
      { title: 'Bảng phân tích nội bộ', code: 'pd.DataFrame(payload["daily"])' }
    ]
  },
  'string-cleaning': {
    title: 'Làm sạch chuỗi qua từng phép biến đổi',
    items: [
      { title: 'Văn bản thô', code: '"   Excelente ubicación.<br/>Metro!   "' },
      { title: 'Thay thẻ HTML bằng khoảng trắng', code: '.str.replace("<br/>", " ", regex=False)', text: '"   Excelente ubicación. Metro!   "' },
      { title: 'Bỏ khoảng trắng ở hai đầu', code: '.str.strip()', text: '"Excelente ubicación. Metro!"' },
      { title: 'Chuyển thành chữ thường', code: '.str.lower()', text: '"excelente ubicación. metro!"' }
    ]
  },
  'llm-validation': {
    title: 'Hai tầng kiểm tra trước khi nhận dữ liệu từ LLM',
    items: [
      { title: 'Văn bản gốc → LLM sinh JSON', text: 'Giữ văn bản đầu vào để đối chiếu kết quả trích xuất.' },
      { title: 'Tầng 1 · Pydantic Schema', text: 'Kiểm tra kiểu dữ liệu và tập nhãn hợp lệ.', lines: ['Lỗi kiểu hoặc nhãn lạ → hàng đợi xem xét lại (DLQ).'] },
      { title: 'Tầng 2 · Mỏ neo bằng chứng', text: 'Đối chiếu trường trích xuất với bằng chứng trong văn bản gốc.', lines: ['Ảo giác hoặc trích sai → hàng đợi xem xét lại (DLQ).'] },
      { title: 'Bảng dữ liệu sạch', text: 'Chỉ nhận bản ghi đã vượt qua cả hai tầng kiểm tra.', tone: 1 }
    ], caption: 'DLQ lưu các bản ghi cần xem xét lại. Bản ghi không đạt không đi tiếp vào bảng dữ liệu sạch.'
  },
  'truncated-axis': {
    layout: 'compare', title: 'Cùng dữ liệu, khác gốc trục: cảm nhận khác nhau',
    items: [
      { title: 'Trục cắt cụt · 92–98%', tone: 2, min: 92, max: 98, bars: [93.5, 94.8, 97.2], chartLabel: 'Trục 92 đến 98 phần trăm. A: 93.5%, B: 94.8%, C: 97.2%. Chiều cao cột C khoảng 3.47 lần cột A.' },
      { title: 'Trục đầy đủ · 0–100%', tone: 1, min: 0, max: 100, bars: [93.5, 94.8, 97.2], chartLabel: 'Trục 0 đến 100 phần trăm. A: 93.5%, B: 94.8%, C: 97.2%. Ba cột có chiều cao gần nhau.' }
    ], caption: 'A, B, C là ba dịch vụ. Khi gốc trục là 92%, cột C trông cao khoảng 3.47 lần cột A, dù tỷ lệ chỉ chênh 3.7 điểm phần trăm.'
  },
  'report-pyramid': {
    title: 'Báo cáo theo thứ tự người đọc cần biết',
    items: [
      { title: 'Kết luận điều hành', text: 'Câu trả lời cốt lõi cho bên đặt hàng.' },
      { title: 'Bằng chứng định lượng', text: 'Số liệu kiểm chứng, so sánh và đồ thị.' },
      { title: 'Phạm vi và giới hạn', text: 'Ranh giới áp dụng và cảnh báo sai số.' },
      { title: 'Chi tiết phương pháp', text: 'Cỡ mẫu, mã nguồn thực thi và phụ lục kỹ thuật.' }
    ]
  },
  'claim-audit': {
    title: 'Bốn bước thẩm định một phát biểu dữ liệu',
    items: [
      { title: 'Truy số', text: 'Tính lại con số trực tiếp từ dữ liệu gốc để xác nhận con số có tồn tại.' },
      { title: 'Kiểm phương pháp', text: 'Đánh giá việc chọn trung bình hay trung vị, cách xử lý ngoại lai và tính trọn vẹn của kỳ báo cáo.' },
      { title: 'Kiểm diễn giải', text: 'Soát xét mức độ kết luận của lời văn và phân biệt tương quan với nhân quả.' },
      { title: 'Phán quyết', text: 'Đúng · Cần sửa đổi · Bác bỏ · Chưa thể kiểm chứng' }
    ]
  }
}
