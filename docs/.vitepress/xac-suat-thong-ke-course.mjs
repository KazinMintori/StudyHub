// UC Berkeley STAT 20: Understanding the World with Data
// Cấu trúc 5 phần, 27 bài giảng chuẩn hóa theo chương trình Stat 20 của UC Berkeley

export const xacSuatThongKeCourse = {
  id: 'xac-suat-thong-ke',
  code: '03',
  name: 'Xác suất thống kê',
  short: 'Xác suất thống kê',
  current: true,
  description: 'Học theo UC Berkeley STAT 20: Từ câu hỏi nghiên cứu, dữ liệu quan sát, tóm tắt trực quan đến suy rộng thống kê, quan hệ nhân quả và mô hình dự đoán.',
  foundations: [
    'thong-ke-mo-ta',
    'suy-rong-thong-ke',
    'mau-tong-the',
    'ket-luan-nhan-qua',
    'du-doan-thong-ke',
    'tap-hop',
    'khong-gian-mau',
    'to-hop',
    'xac-suat-co-dieu-kien',
    'doc-lap',
    'bien-ngau-nhien',
    'ky-vong',
    'phuong-sai',
    'tich-phan',
    'dataframe'
  ],
  parts: [
    {
      title: 'Phần 1. Câu hỏi và dữ liệu',
      description: 'Phân loại các phát biểu thống kê, cấu trúc bảng dữ liệu và thu thập quan sát.',
      lessons: [
        '01-hieu-the-gioi-bang-du-lieu',
        '02-phan-loai-du-lieu'
      ]
    },
    {
      title: 'Phần 2. Tóm tắt dữ liệu',
      description: 'Tóm tắt dữ liệu định tính, định lượng, ngữ pháp đồ họa và mô hình hồi quy.',
      lessons: [
        '03-tom-tat-du-lieu-dinh-tinh',
        '04-tom-tat-du-lieu-dinh-luong',
        '05-ngu-phap-do-hoa',
        '06-phan-tich-co-dieu-kien',
        '07-tom-tat-lien-he-bien-so',
        '08-hoi-quy-tuyen-tinh-boi'
      ]
    },
    {
      title: 'Phần 3. Suy rộng thống kê',
      description: 'Cơ sở xác suất, biến ngẫu nhiên, phân phối mẫu, khoảng tin cậy và kiểm định giả thuyết.',
      lessons: [
        '09-co-so-xac-suat',
        '10-tinh-toan-xac-suat',
        '11-phan-phoi-xac-suat',
        '12-bien-ngau-nhien',
        '13-ky-vong-va-sai-so-chuan',
        '14-phan-phoi-lien-tuc-va-xap-xi-chuan',
        '15-tu-mau-den-tong-the',
        '16-khoang-tin-cay',
        '17-phuong-phap-bootstrapping',
        '18-kiem-dinh-gia-thuyet-1',
        '19-kiem-dinh-gia-thuyet-2',
        '20-sai-lech-do-thiet-ke'
      ]
    },
    {
      title: 'Phần 4. Quan hệ nhân quả',
      description: 'Định nghĩa nhân quả, thí nghiệm ngẫu nhiên có đối chứng và suy luận trong nghiên cứu quan sát.',
      lessons: [
        '21-dinh-nghia-nhan-qua',
        '22-thi-nghiem-ngau-nhien',
        '23-tac-dong-nhan-qua-nghien-cuu-quan-sat'
      ]
    },
    {
      title: 'Phần 5. Mô hình dự đoán',
      description: 'Phương pháp bình phương bé nhất, đánh giá sai số, hiện tượng quá khớp và hồi quy Logistic.',
      lessons: [
        '24-phuong-phap-binh-phuong-be-nhat',
        '25-danh-gia-va-cai-thien-du-doan',
        '26-hien-tuong-qua-khop',
        '27-hoi-quy-logistic'
      ]
    }
  ],
  lessons: [
    {
      slug: '01-hieu-the-gioi-bang-du-lieu',
      title: 'Hiểu thế giới bằng dữ liệu',
      prerequisites: [],
      supportingConcepts: ['thong-ke-mo-ta', 'suy-rong-thong-ke', 'mau-tong-the', 'ket-luan-nhan-qua', 'du-doan-thong-ke'],
      status: 'ready',
      number: 1,
      hasChapterExercises: true,
      description: 'Bốn loại phát biểu từ dữ liệu: Mô tả, suy rộng thống kê, kết luận nhân quả và dự đoán.'
    },
    {
      slug: '02-phan-loai-du-lieu',
      title: 'Hệ thống phân loại dữ liệu & Cấu trúc Data Frame',
      prerequisites: [],
      supportingConcepts: ['dataframe', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 2,
      hasChapterExercises: true,
      description: 'Phân loại biến số: Định tính, định lượng, rời rạc, liên tục, thứ bậc, danh nghĩa và cấu trúc Data Frame.'
    },
    {
      slug: '03-tom-tat-du-lieu-dinh-tinh',
      title: 'Tóm tắt dữ liệu định tính & Biểu đồ thanh',
      prerequisites: [],
      supportingConcepts: ['thong-ke-mo-ta'],
      status: 'ready',
      number: 3,
      hasChapterExercises: true,
      description: 'Bảng tần số chéo, tỷ lệ đồng thời, tỷ lệ biên, tỷ lệ điều kiện, biểu đồ thanh và nhận diện mối liên hệ giữa các biến định tính.'
    },
    {
      slug: '04-tom-tat-du-lieu-dinh-luong',
      title: 'Tóm tắt dữ liệu định lượng & Đo lường phân tán',
      prerequisites: [],
      supportingConcepts: ['khoang-tu-phan-vi', 'ngoai-lai', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 4,
      hasChapterExercises: true,
      description: 'Biểu đồ phân phối, các số đo xu hướng trung tâm và độ phân tán: Mean, Median, Mode, Variance, SD, IQR, MAD.'
    },
    {
      slug: '05-ngu-phap-do-hoa',
      title: 'Ngữ pháp đồ họa & Khung phân tích trực quan hóa',
      prerequisites: [],
      supportingConcepts: ['histogram', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 5,
      hasChapterExercises: true,
      description: 'Nguyên lý The Grammar of Graphics: Dữ liệu (Data), Ánh xạ thẩm mỹ (Aesthetics) và Hình học biểu diễn (Geometries) trong ggplot2.'
    },
    {
      slug: '06-phan-tich-co-dieu-kien',
      title: 'Phân tích có điều kiện: Lọc dữ liệu, Thao tác nhóm & Đường ống phân tích',
      prerequisites: [],
      supportingConcepts: ['dataframe', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 6,
      hasChapterExercises: true,
      description: 'Kỹ thuật phân tích có điều kiện: Lọc hàng (filter), các phép toán logic và so sánh, bản chất kiểu dữ liệu Logical, thao tác theo nhóm (group_by) và xây dựng đường ống phân tích (Data Pipelines).'
    },
    {
      slug: '07-tom-tat-lien-he-bien-so',
      title: 'Tóm tắt mối liên hệ định lượng: Hệ số tương quan & Mô hình tuyến tính đơn',
      prerequisites: [],
      supportingConcepts: ['phuong-sai', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 7,
      hasChapterExercises: true,
      description: 'Khảo sát mối liên hệ giữa hai biến định lượng: Biểu đồ phân tán, hệ số tương quan Pearson r, đường hồi quy bình phương tối thiểu và phần dư (residuals).'
    },
    {
      slug: '08-hoi-quy-tuyen-tinh-boi',
      title: 'Hồi quy tuyến tính bội: Mô hình hóa mối quan hệ đa chiều',
      prerequisites: [],
      supportingConcepts: ['phuong-sai', 'thong-ke-mo-ta'],
      status: 'ready',
      number: 8,
      hasChapterExercises: true,
      description: 'Mở rộng mô hình tuyến tính lên nhiều chiều: Hồi quy với biến định lượng và biến định tính (biến giả dummy), giải thích hệ số hồi quy riêng phần và kiểm soát biến số.'
    },
    {
      slug: '09-co-so-xac-suat',
      title: 'Cơ sở lý thuyết xác suất & Hệ tiên đề Kolmogorov',
      prerequisites: ['tap-hop', 'khong-gian-mau'],
      supportingConcepts: ['thong-ke-mo-ta'],
      status: 'ready',
      number: 9,
      hasChapterExercises: true,
      description: 'Nền tảng lý thuyết xác suất: Phép thử ngẫu nhiên, không gian mẫu, biến cố, hệ tiên đề Kolmogorov, quy tắc biến cố đối và nghịch lý Chevalier de Méré.'
    },
    {
      slug: '10-tinh-toan-xac-suat',
      title: 'Tính toán xác suất & Quy tắc nhân, cộng',
      prerequisites: ['khong-gian-mau', 'xac-suat-co-dieu-kien', 'doc-lap'],
      supportingConcepts: [],
      status: 'ready',
      number: 10,
      hasChapterExercises: true,
      description: 'Quy tắc cộng, xác suất có điều kiện, quy tắc nhân, định lý xác suất đầy đủ và định lý Bayes.'
    },
    {
      slug: '11-phan-phoi-xac-suat',
      title: 'Phân phối xác suất rời rạc',
      prerequisites: ['to-hop', 'khong-gian-mau'],
      supportingConcepts: [],
      status: 'ready',
      number: 11,
      hasChapterExercises: true,
      description: 'Mô hình hộp rút thăm, phân phối Bernoulli, phân phối Đều rời rạc, phân phối Nhị thức và phân phối Siêu bội.'
    },
    {
      slug: '12-bien-ngau-nhien',
      title: 'Biến ngẫu nhiên & Hàm phân phối',
      prerequisites: ['bien-ngau-nhien'],
      supportingConcepts: [],
      status: 'ready',
      number: 12,
      hasChapterExercises: true,
      description: 'Định nghĩa biến ngẫu nhiên, phân loại rời rạc và liên tục, hàm khối lượng xác suất PMF, phân phối Poisson và hàm phân phối tích lũy CDF.'
    },
    {
      slug: '13-ky-vong-va-sai-so-chuan',
      title: 'Kỳ vọng, phương sai & Sai số chuẩn',
      prerequisites: ['ky-vong', 'phuong-sai'],
      supportingConcepts: [],
      status: 'ready',
      number: 13,
      hasChapterExercises: true,
      description: 'Kỳ vọng toán học E(X) làm trọng tâm cân bằng, tính tuyến tính của kỳ vọng, phương sai Var(X) và độ lệch chuẩn SD(X).'
    },
    {
      slug: '14-phan-phoi-lien-tuc-va-xap-xi-chuan',
      title: 'Phân phối liên tục & Xấp xỉ chuẩn',
      prerequisites: ['tich-phan', 'bien-ngau-nhien'],
      supportingConcepts: [],
      status: 'ready',
      number: 14,
      hasChapterExercises: true,
      description: 'Hàm mật độ xác suất PDF, phân phối chuẩn Gauss, quy tắc thực nghiệm 68-95-99.7 và định lý giới hạn trung tâm.'
    },
    {
      slug: '15-tu-mau-den-tong-the',
      title: 'Từ mẫu đến tổng thể',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 15,
      hasChapterExercises: true,
      description: 'Khung chọn mẫu, lấy mẫu ngẫu nhiên đơn giản, sai số chọn mẫu và độ lệch chọn mẫu.'
    },
    {
      slug: '16-khoang-tin-cay',
      title: 'Khoảng tin cậy',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 16,
      hasChapterExercises: true,
      description: 'Ước lượng điểm, khoảng tin cậy 95%, mức độ tin cậy và giải thích khoảng tin cậy đúng chuẩn.'
    },
    {
      slug: '17-phuong-phap-bootstrapping',
      title: 'Phương pháp tái lấy mẫu Bootstrapping',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 17,
      hasChapterExercises: true,
      description: 'Nguyên lý tái lấy mẫu có hoàn lại (resampling with replacement) và khoảng tin cậy Bootstrap.'
    },
    {
      slug: '18-kiem-dinh-gia-thuyet-1',
      title: 'Kiểm định giả thuyết thống kê I',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 18,
      hasChapterExercises: true,
      description: 'Giả thuyết không H0, giả thuyết đối H1, đại lượng thống kê kiểm định và giá trị p-value.'
    },
    {
      slug: '19-kiem-dinh-gia-thuyet-2',
      title: 'Kiểm định giả thuyết thống kê II: Kiểm định Chi bình phương',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 19,
      hasChapterExercises: true,
      description: 'Kiểm định nhiều tỉ lệ, kiểm định Chi bình phương (Chi-squared test), Luật Benford và hiệu ứng Bouba/Kiki.'
    },
    {
      slug: '20-sai-lech-do-thiet-ke',
      title: 'Sai lệch do thiết kế: Sai lầm loại I, loại II và Lực kiểm định',
      prerequisites: ['mau-tong-the', 'suy-rong-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 20,
      hasChapterExercises: true,
      description: 'Bản chất sai lầm thống kê loại I và loại II, mức ý nghĩa alpha, kiểm định một phía và hai phía, lực kiểm định (Statistical Power) và cỡ mẫu.'
    },
    {
      slug: '21-dinh-nghia-nhan-qua',
      title: 'Định nghĩa tính nhân quả & Mô hình kết quả tiềm năng',
      prerequisites: ['ket-luan-nhan-qua'],
      supportingConcepts: [],
      status: 'ready',
      number: 21,
      hasChapterExercises: true,
      description: 'Mô hình kết quả tiềm năng (Potential Outcomes Framework), bài toán cơ bản của suy luận nhân quả, hiệu ứng can thiệp trung bình ATE và thiên lệch lựa chọn.'
    },
    {
      slug: '22-thi-nghiem-ngau-nhien',
      title: 'Thử nghiệm ngẫu nhiên có đối chứng (RCT) & Cân bằng hiệp biến',
      prerequisites: ['ket-luan-nhan-qua'],
      supportingConcepts: [],
      status: 'ready',
      number: 22,
      hasChapterExercises: true,
      description: 'Nguyên lý thiết kế thử nghiệm ngẫu nhiên có đối chứng (RCT), phân nhóm ngẫu nhiên, làm mù đôi, kiểm soát hiệp biến và biểu đồ Love Plot.'
    },
    {
      slug: '23-tac-dong-nhan-qua-nghien-cuu-quan-sat',
      title: 'Tác động nhân quả trong nghiên cứu quan sát & Phương pháp ghép cặp (Matching)',
      prerequisites: ['ket-luan-nhan-qua'],
      supportingConcepts: [],
      status: 'ready',
      number: 23,
      hasChapterExercises: true,
      description: 'Thí nghiệm tự nhiên (Natural Experiments), phương pháp ghép cặp tối ưu (Matching), Nghịch lý Simpson và biến gây nhiễu tiềm ẩn.'
    },
    {
      slug: '24-phuong-phap-binh-phuong-be-nhat',
      title: 'Phương pháp bình phương bé nhất (OLS)',
      prerequisites: ['du-doan-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 24,
      hasChapterExercises: true,
      description: 'Bản chất bài toán dự báo, hàm tổn thất tổng bình phương phần dư (RSS), nghiệm giải tích OLS và thuật toán tối ưu hóa Gradient Descent.'
    },
    {
      slug: '25-danh-gia-va-cai-thien-du-doan',
      title: 'Đánh giá & Cải thiện dự báo: Hệ số R bình phương, Biến đổi phi tuyến và Đa thức',
      prerequisites: ['du-doan-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 25,
      hasChapterExercises: true,
      description: 'Hệ số xác định R bình phương, phân rã phương sai TSS = SSR + RSS, kỹ thuật bổ sung biến dự báo, biến đổi logarit và hồi quy đa thức.'
    },
    {
      slug: '26-hien-tuong-qua-khop',
      title: 'Hiện tượng quá khớp (Overfitting) & Quy trình Huấn luyện - Kiểm thử',
      prerequisites: ['du-doan-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 26,
      hasChapterExercises: true,
      description: 'Tập huấn luyện (Training Set), tập kiểm thử (Testing Set), sai số MSE/RMSE, hiện tượng quá khớp và đánh đổi Độ chệch - Phương sai.'
    },
    {
      slug: '27-hoi-quy-logistic',
      title: 'Hồi quy Logistic & Phân loại nhị phân',
      prerequisites: ['du-doan-thong-ke'],
      supportingConcepts: [],
      status: 'ready',
      number: 27,
      hasChapterExercises: true,
      description: 'Biến mục tiêu nhị phân, hàm Sigmoid, tỷ số cơ hội (Odds Ratio), hàm Logit, ma trận nhầm lẫn và tối ưu hóa ngưỡng quyết định.'
    }
  ],
  slides: [],
  illustration: 'bayes',
  contentPolicy: 'full-source-translation'
}
