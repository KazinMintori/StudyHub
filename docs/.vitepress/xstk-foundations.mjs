const term = (name, aliases, definition, example, use, question, answer) => ({
  name, aliases: [name, ...aliases], definition, example, use, question, answer,
})

export const xstkConcepts = {
  'phan-phoi-dong-thoi': term('Phân phối đồng thời', ['phân phối đồng thời', 'phân phối chung'],
    'Phân phối đồng thời mô tả xác suất của nhiều biến ngẫu nhiên cùng lúc. Từ đó có thể tìm phân phối riêng của từng biến, phân phối có điều kiện và kiểm tra độc lập.',
    'Tung hai đồng xu cân bằng độc lập, gọi X và Y là các chỉ báo ngửa. Mỗi cặp (0, 0), (0, 1), (1, 0), (1, 1) có xác suất 1/4.',
    'Tính xác suất có nhiều điều kiện và mô hình hóa sự phụ thuộc.',
    'Biết riêng phân phối của X và Y đã xác định phân phối đồng thời chưa?',
    'Chưa. Hai phân phối biên không xác định cách X và Y phụ thuộc nhau.'),
  'ky-vong-co-dieu-kien': term('Kỳ vọng có điều kiện', ['kỳ vọng có điều kiện', 'conditional expectation'],
    'Kỳ vọng có điều kiện là trung bình theo phân phối sau khi biết thông tin bổ sung. Với X có moment bậc hai hữu hạn, kỳ vọng của X khi biết Y là dự đoán tốt nhất bằng hàm của Y theo sai số bình phương trung bình.',
    'Trong một nhóm giả định gồm ba sản phẩm có chi phí 2, 4 và 6, chọn đều một sản phẩm cho chi phí kỳ vọng bằng 4. Khi biết nhóm được chọn, phải tính trung bình trong đúng nhóm đó.',
    'Phân rã kỳ vọng, phương sai và xây dựng dự đoán từ thông tin quan sát.',
    'Kỳ vọng của X khi biết Y có nhất thiết là hằng số không?',
    'Không. Trước khi quan sát Y, đó là một biến ngẫu nhiên phụ thuộc Y. Khi Y có giá trị cụ thể, ta có một giá trị dự đoán.'),
  'hiep-phuong-sai': term('Hiệp phương sai', ['hiệp phương sai', 'covariance'],
    'Hiệp phương sai đo trung bình tích hai độ lệch khỏi kỳ vọng. Với hai biến có moment bậc hai hữu hạn, độc lập kéo theo hiệp phương sai bằng 0. Chiều ngược lại không đúng nói chung.',
    'Nếu X nhận đều các giá trị -1, 0, 1 và Y là bình phương của X, hiệp phương sai bằng 0 nhưng Y vẫn do X xác định.',
    'Tính phương sai của tổng các biến phụ thuộc và phân biệt phụ thuộc với liên hệ tuyến tính.',
    'Không tương quan có bảo đảm độc lập không?',
    'Không. Ví dụ X đối xứng quanh 0 và Y là bình phương của X cho một phản ví dụ.'),
  'ham-sinh-momen': term('Hàm sinh mômen', ['hàm sinh mômen', 'hàm sinh moment', 'moment generating function'],
    'Hàm sinh mômen của X là kỳ vọng của hàm mũ exp(tX), khi kỳ vọng này hữu hạn. Nếu hữu hạn trên một khoảng mở chứa 0, các đạo hàm tại 0 cho các mômen và hàm này xác định duy nhất phân phối.',
    'Với X là chỉ báo Bernoulli có xác suất thành công 1/2, hàm sinh mômen bằng (1 + exp(t))/2.',
    'Tìm mômen và nhận diện phân phối của tổng các biến độc lập.',
    'Mọi biến ngẫu nhiên có hàm sinh mômen hữu hạn gần 0 không?',
    'Không. Phân phối Cauchy không có hàm sinh mômen hữu hạn trên một khoảng mở chứa 0.'),
  'luat-so-lon': term('Luật số lớn', ['luật số lớn', 'law of large numbers'],
    'Luật số lớn mô tả sự hội tụ của trung bình mẫu về kỳ vọng khi cỡ mẫu tăng. Với các biến độc lập, cùng phân phối và có kỳ vọng tuyệt đối hữu hạn, trung bình mẫu hội tụ hầu chắc chắn về kỳ vọng.',
    'Tung đồng xu độc lập cùng xác suất ngửa 1/2, tỷ lệ ngửa hội tụ về 1/2 khi số lần tung tăng.',
    'Giải thích trung bình dài hạn và kiểm tra điều kiện nhất quán của ước lượng.',
    'Luật số lớn có nói số lần ngửa trừ số lần sấp tiến về 0 không?',
    'Không. Luật mô tả tỷ lệ hoặc trung bình, không khẳng định chênh lệch số đếm tiến về 0.'),
  'dinh-ly-gioi-han-trung-tam': term('Định lý giới hạn trung tâm', ['định lý giới hạn trung tâm', 'central limit theorem'],
    'Với các biến độc lập, cùng phân phối, có phương sai hữu hạn và dương, tổng sau khi trừ kỳ vọng và chia độ lệch chuẩn hội tụ theo phân phối về chuẩn tắc. Đây là kết quả về dao động của tổng hoặc trung bình, không phải phân phối của từng quan sát.',
    'Tổng của n phép thử Bernoulli độc lập có trung bình n/2 và độ lệch chuẩn bằng căn n chia 2 khi xác suất thành công là 1/2.',
    'Xấp xỉ phân phối của tổng, trung bình mẫu và nhiều thống kê khi có đủ điều kiện.',
    'Có phải cứ có 30 quan sát là mọi xấp xỉ chuẩn đều chính xác không?',
    'Không. Độ chính xác phụ thuộc phân phối gốc, mức lệch, đuôi phân phối và xác suất cần tính.'),
  'phan-phoi-mau': term('Phân phối mẫu', ['phân phối mẫu', 'phân phối lấy mẫu', 'sampling distribution'],
    'Phân phối mẫu của một thống kê là phân phối xác suất của thống kê đó khi lặp lại quy trình lấy mẫu. Nó khác phân phối của từng quan sát và khác biểu đồ của một mẫu đã thu được.',
    'Với hai quan sát độc lập chuẩn có phương sai 4, trung bình mẫu có phương sai 2. Phân phối của trung bình hẹp hơn phân phối của từng quan sát.',
    'Tính sai số chuẩn và xây dựng khoảng tin cậy, kiểm định.',
    'Sai số chuẩn của trung bình có phải độ lệch chuẩn của dữ liệu không?',
    'Không. Sai số chuẩn là độ lệch chuẩn của phân phối trung bình mẫu.'),
  'uoc-luong-khong-chech': term('Ước lượng không chệch', ['ước lượng không chệch', 'unbiased estimator'],
    'Một ước lượng không chệch có kỳ vọng bằng tham số cần ước lượng tại mọi giá trị tham số trong mô hình. Tính chất này nói về trung bình qua các mẫu lặp lại, không bảo đảm một kết quả ước lượng riêng lẻ gần tham số.',
    'Với mẫu độc lập cùng phân phối có phương sai hữu hạn, trung bình mẫu là ước lượng không chệch của kỳ vọng tổng thể.',
    'So sánh độ chệch, phương sai và sai số bình phương trung bình của các ước lượng.',
    'Ước lượng không chệch có luôn tốt hơn ước lượng chệch theo sai số bình phương trung bình không?',
    'Không. Một ước lượng có độ chệch nhỏ nhưng phương sai thấp hơn có thể có sai số bình phương trung bình nhỏ hơn.'),
  'uoc-luong-hop-ly-cuc-dai': term('Ước lượng hợp lý cực đại', ['ước lượng hợp lý cực đại', 'maximum likelihood estimation', 'MLE'],
    'Ước lượng hợp lý cực đại chọn giá trị tham số làm hàm hợp lý của dữ liệu quan sát đạt lớn nhất trong miền tham số. Phải kiểm tra biên miền, điểm cực trị và sự tồn tại của cực đại.',
    'Với 3 lần thành công trong 4 phép thử Bernoulli độc lập, ước lượng hợp lý cực đại của xác suất thành công bằng 3/4.',
    'Ước lượng tham số từ một mô hình xác suất được phát biểu rõ.',
    'Nghiệm đạo hàm log hợp lý bằng 0 có luôn là MLE không?',
    'Không. Có thể đó là cực tiểu, điểm yên ngựa, hoặc cực đại thực sự nằm ở biên miền tham số.'),
  'thong-ke-du': term('Thống kê đủ', ['thống kê đủ', 'sufficient statistic'],
    'Thống kê đủ giữ toàn bộ thông tin của mẫu về tham số trong mô hình đã chọn. Khi biết thống kê đủ, phân phối có điều kiện của mẫu không còn phụ thuộc tham số đó.',
    'Trong n phép thử Bernoulli độc lập cùng xác suất thành công p, tổng số thành công là thống kê đủ cho p. Thứ tự thành công không cung cấp thêm thông tin về p trong mô hình này.',
    'Rút gọn dữ liệu và xây dựng ước lượng có phương sai nhỏ hơn bằng điều kiện hóa.',
    'Thống kê đủ có giữ mọi thông tin cho mọi mô hình không?',
    'Không. Tính đủ luôn gắn với mô hình và tham số đang xét.'),
  'thong-tin-fisher': term('Thông tin Fisher', ['thông tin Fisher', 'Fisher information'],
    'Trong mô hình chính quy, thông tin Fisher là kỳ vọng bình phương đạo hàm log hợp lý theo tham số. Nó đo mức nhạy của phân phối đối với thay đổi tham số và xuất hiện trong cận phương sai Cramér–Rao.',
    'Một phép thử Bernoulli với p bằng 1/2 có thông tin Fisher bằng 4 về p. Với n phép thử độc lập, thông tin bằng 4n.',
    'Đánh giá hiệu quả ước lượng và sai số tiệm cận khi thỏa điều kiện chính quy.',
    'Có được áp dụng cận Cramér–Rao chỉ vì tính được đạo hàm không?',
    'Không. Cần kiểm tra các điều kiện chính quy, đặc biệt khi miền giá trị của dữ liệu phụ thuộc tham số.'),
  'khoang-tin-cay': term('Khoảng tin cậy', ['khoảng tin cậy', 'confidence interval'],
    'Khoảng tin cậy là một quy tắc tạo khoảng từ mẫu với xác suất bao phủ tham số được kiểm soát trước khi quan sát dữ liệu. Mức 95% nói về tỷ lệ bao phủ dài hạn của quy trình dưới mô hình và giả thiết lấy mẫu.',
    'Nếu các giả thiết đúng, một quy trình có độ bao phủ 95% sẽ tạo khoảng chứa tham số trong khoảng 95% số lần lặp lấy mẫu. Một khoảng đã tính không chứa 95% các quan sát.',
    'Diễn đạt độ bất định của ước lượng tham số và phân biệt với khoảng dự đoán.',
    'Sau khi đã quan sát mẫu, độ tin cậy 95% có phải xác suất hậu nghiệm 95% của tham số không?',
    'Không trong diễn giải tần suất. Xác suất hậu nghiệm cần một mô hình Bayes với phân phối tiên nghiệm.'),
  'kiem-dinh-gia-thuyet': term('Kiểm định giả thuyết', ['kiểm định giả thuyết', 'hypothesis test'],
    'Kiểm định giả thuyết dùng dữ liệu và một quy tắc quyết định để đánh giá giả thuyết không so với giả thuyết đối. Mức ý nghĩa kiểm soát xác suất bác bỏ giả thuyết không khi nó đúng, theo mô hình đã nêu.',
    'Kiểm định mức 5% có xác suất sai lầm loại I không vượt 5% theo các điều kiện của phép kiểm định. Điều đó không có nghĩa giả thuyết không có xác suất đúng 5%.',
    'Đánh giá bằng chứng thống kê và phân biệt ý nghĩa thống kê với độ lớn tác động.',
    'Không bác bỏ giả thuyết không có chứng minh nó đúng không?',
    'Không. Dữ liệu có thể chưa đủ mạnh để phân biệt giả thuyết không với những phương án gần nó.'),
  'cong-suat-kiem-dinh': term('Công suất kiểm định', ['công suất kiểm định', 'lực kiểm định', 'statistical power'],
    'Công suất là xác suất bác bỏ giả thuyết không tại một giá trị tham số cụ thể thuộc giả thuyết đối. Công suất bằng một trừ xác suất sai lầm loại II tại chính giá trị đó.',
    'Nếu một phép kiểm định có xác suất bỏ sót tác động đang xét bằng 0,2 thì công suất phát hiện tác động đó bằng 0,8.',
    'Lập kế hoạch cỡ mẫu và đánh giá khả năng phát hiện tác động có ý nghĩa thực tế.',
    'Một phép kiểm định có công suất 80% với mọi tác động không?',
    'Không. Công suất thay đổi theo độ lớn tác động, độ biến thiên, cỡ mẫu và mức ý nghĩa.'),
  'phan-phoi-tien-nghiem': term('Phân phối tiên nghiệm', ['phân phối tiên nghiệm', 'prior distribution'],
    'Trong mô hình Bayes, phân phối tiên nghiệm mô tả thông tin về tham số trước dữ kiện đang xét. Nó phải đi cùng mô hình và cách lựa chọn được giải thích rõ.',
    'Một tiên nghiệm đều cho xác suất thành công trên khoảng từ 0 đến 1 gán cùng xác suất cho các đoạn con cùng độ dài.',
    'Phát biểu thông tin ban đầu trước khi cập nhật Bayes và kiểm tra độ nhạy của kết luận.',
    'Tiên nghiệm có nhất thiết là dữ liệu giả lập thêm vào mẫu không?',
    'Không. Tiên nghiệm là một thành phần của mô hình xác suất, không phải những quan sát mới.'),
  'phan-phoi-hau-nghiem': term('Phân phối hậu nghiệm', ['phân phối hậu nghiệm', 'posterior distribution'],
    'Phân phối hậu nghiệm là phân phối của tham số sau khi điều kiện hóa theo dữ liệu trong mô hình Bayes. Nó kết hợp tiên nghiệm và hàm hợp lý, sau đó chuẩn hóa để tổng xác suất hoặc tích phân mật độ bằng 1.',
    'Tiên nghiệm beta với hai tham số bằng 1, cùng ba thành công trong bốn phép thử Bernoulli độc lập khi biết tham số, cho hậu nghiệm beta với hai tham số 4 và 2.',
    'Tính xác suất của tham số sau dữ liệu, khoảng xác suất hậu nghiệm và phân phối dự đoán.',
    'Với tham số liên tục, mật độ hậu nghiệm tại một điểm có phải xác suất tham số bằng đúng điểm đó không?',
    'Không. Xác suất trên một miền được tính bằng tích phân mật độ trên miền đó.'),
  'phan-tich-phuong-sai': term('Phân tích phương sai', ['phân tích phương sai', 'ANOVA'],
    'Phân tích phương sai so sánh các trung bình nhóm thông qua biến thiên giữa nhóm và trong nhóm. Kiểm định F một nhân tố cổ điển giả thiết các sai số độc lập, chuẩn và có cùng phương sai.',
    'So sánh thời gian xử lý của ba phương pháp bằng ANOVA kiểm tra giả thuyết ba trung bình bằng nhau. Bác bỏ chỉ cho biết có ít nhất một trung bình khác.',
    'So sánh nhiều trung bình và phân tích tác động của các nhân tố trong thí nghiệm.',
    'Bác bỏ ANOVA có cho biết mọi cặp trung bình đều khác nhau không?',
    'Không. Cần các phép so sánh tiếp theo có kiểm soát vấn đề kiểm định nhiều lần.'),
}

export const xstkWikiDetails = {
  'phan-phoi-tien-nghiem': 'Tiên nghiệm được phát biểu trước dữ kiện đang đưa vào hàm hợp lý. Nó có thể biểu diễn thông tin từ nghiên cứu trước hoặc lựa chọn mô hình khi thông tin còn ít. Cần kiểm tra độ nhạy của kết luận theo những tiên nghiệm hợp lý khác nhau.\n\nNếu phân phối tiên nghiệm và hậu nghiệm cùng thuộc một họ, ta có tính liên hợp đối với mô hình lấy mẫu đang xét. Beta liên hợp với mẫu Bernoulli, còn gamma liên hợp với số đếm Poisson theo quy ước hình dạng và tốc độ.\n\nXem [Suy luận Bayes và phân phối dự đoán](/xac-suat-thong-ke/bai-giang/45-suy-luan-bayes-va-du-doan).',
  'phan-phoi-hau-nghiem': 'Nhân hàm hợp lý với mật độ tiên nghiệm cho một hàm chưa chuẩn hóa. Tích phân hàm đó trên miền tham số là hằng số chuẩn hóa, cần dương và hữu hạn. Với tham số rời rạc, thay tích phân bằng tổng trên các giá trị tham số.\n\nPhân phối dự đoán lấy trung bình xác suất có điều kiện của dữ liệu tương lai theo hậu nghiệm. Thay tham số bằng trung bình hậu nghiệm không cho cùng kết quả trong mọi câu hỏi. Đặc biệt, kỳ vọng bình phương còn chứa phương sai của tham số.\n\nXem [Suy luận Bayes và phân phối dự đoán](/xac-suat-thong-ke/bai-giang/45-suy-luan-bayes-va-du-doan).',
  'phan-phoi-dong-thoi': String.raw`Với biến rời rạc, đặt $p(x,y)=P(X=x,Y=y)$. Mọi xác suất không âm và tổng trên toàn bộ các cặp bằng 1. Cộng xác suất theo từng hàng hoặc cột cho các phân phối biên. Với mật độ liên tục, phải tích phân trên đúng miền hỗ trợ.

Hai biến độc lập khi phân phối đồng thời bằng tích hai phân phối biên, ở mọi điểm rời rạc hoặc hầu khắp nơi đối với mật độ. Chỉ kiểm tra một cặp giá trị chưa đủ.

Xem [Vector ngẫu nhiên và phân phối đồng thời](/xac-suat-thong-ke/bai-giang/31-vector-ngau-nhien-va-phan-phoi-dong-thoi).`,
  'ky-vong-co-dieu-kien': String.raw`Với $P(Y=y)>0$, hãy lập phân phối của X khi biết Y bằng y rồi lấy trung bình theo phân phối ấy. Nếu X khả tích, luật kỳ vọng toàn phần cho biết kỳ vọng của kỳ vọng có điều kiện bằng kỳ vọng ban đầu.

Khi có moment bậc hai hữu hạn, phương sai toàn phần gồm trung bình phương sai trong nhóm và phương sai giữa các trung bình nhóm. Điều kiện hóa có thể làm phương sai của một nhóm cụ thể tăng, nên không nói rằng biết thêm thông tin luôn giảm phương sai tại từng giá trị quan sát.

Xem [Hiệp phương sai và kỳ vọng có điều kiện](/xac-suat-thong-ke/bai-giang/32-hiep-phuong-sai-va-ky-vong-co-dieu-kien).`,
  'hiep-phuong-sai': String.raw`Với các moment bậc hai hữu hạn, đặt $\mu_X=E(X)$ và $\mu_Y=E(Y)$.

$$
\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)].
$$

Giá trị bằng 0 chỉ loại bỏ liên hệ tuyến tính đo bằng đại lượng này. Nếu cả hai phương sai dương, chia hiệp phương sai cho tích hai độ lệch chuẩn cho hệ số tương quan. Cộng hằng số không đổi hiệp phương sai, còn đổi dấu một biến làm đổi dấu hiệp phương sai.

Xem [Hiệp phương sai và kỳ vọng có điều kiện](/xac-suat-thong-ke/bai-giang/32-hiep-phuong-sai-va-ky-vong-co-dieu-kien).`,
  'ham-sinh-momen': String.raw`Đặt $M_X(t)=E(e^{tX})$ tại những t mà kỳ vọng hữu hạn. Nếu hàm hữu hạn trên một khoảng mở chứa 0, đạo hàm bậc k tại 0 bằng mômen bậc k. Chẳng hạn, đạo hàm thứ nhất cho kỳ vọng, đạo hàm thứ hai cho kỳ vọng bình phương.

Với hai biến độc lập, hàm sinh mômen của tổng là tích hai hàm sinh mômen tại những điểm chúng hữu hạn. Tồn tại mọi mômen không tự bảo đảm hàm sinh mômen hữu hạn gần 0.

Xem [Mômen, hàm sinh và bất đẳng thức](/xac-suat-thong-ke/bai-giang/34-momen-ham-sinh-va-bat-dang-thuc).`,
  'luat-so-lon': String.raw`Với các biến độc lập cùng phân phối và $E(|X_1|)<\infty$, trung bình mẫu hội tụ hầu chắc chắn về kỳ vọng. Luật yếu chỉ yêu cầu kết luận hội tụ theo xác suất, còn luật mạnh cho kết luận hầu chắc chắn.

Luật không quy định một cỡ mẫu hữu hạn đủ lớn cho mọi mô hình. Nó cũng không sửa sai lệch chọn mẫu hoặc bảo đảm trung bình mẫu có ý nghĩa khi kỳ vọng không tồn tại.

Xem [Luật số lớn và định lý giới hạn](/xac-suat-thong-ke/bai-giang/35-luat-so-lon-va-dinh-ly-gioi-han).`,
  'dinh-ly-gioi-han-trung-tam': String.raw`Trong phiên bản độc lập cùng phân phối, giả sử kỳ vọng hữu hạn và phương sai hữu hạn, dương. Lấy tổng trừ n lần kỳ vọng, sau đó chia cho độ lệch chuẩn của tổng. Phân phối của đại lượng chuẩn hóa tiến tới phân phối chuẩn tắc.

Đây là hội tụ theo phân phối. Nó không biến phân phối gốc thành chuẩn và không cung cấp sai số xấp xỉ hữu hạn nếu chưa có điều kiện hoặc định lý bổ sung. Khi xấp xỉ biến đếm bằng chuẩn, hiệu chỉnh liên tục có thể cải thiện kết quả.

Xem [Luật số lớn và định lý giới hạn](/xac-suat-thong-ke/bai-giang/35-luat-so-lon-va-dinh-ly-gioi-han).`,
  'phan-phoi-mau': String.raw`Một thống kê là hàm của mẫu không chứa tham số chưa biết trong quy tắc tính. Vì mẫu ngẫu nhiên, thống kê có phân phối. Sai số chuẩn là độ lệch chuẩn của phân phối này, có thể phải ước lượng từ dữ liệu.

Các phân phối Student, khi bình phương và Fisher cho những suy luận chính xác với mẫu chuẩn dưới các điều kiện tương ứng. Thay đổi thiết kế lấy mẫu hoặc vi phạm giả thiết độc lập có thể làm các công thức sai.

Xem [Phân phối mẫu chính xác](/xac-suat-thong-ke/bai-giang/36-phan-phoi-mau-chinh-xac).`,
  'uoc-luong-khong-chech': String.raw`Tính không chệch yêu cầu $E_\theta(T)=\theta$ với mọi giá trị tham số trong mô hình. Sai số bình phương trung bình phân rã thành phương sai cộng bình phương độ chệch.

Không chệch và nhất quán là hai tính chất khác nhau. Tính nhất quán xét một dãy ước lượng khi cỡ mẫu tăng. Một ước lượng không chệch vẫn có thể rất biến động tại cỡ mẫu đang có.

Xem [Ước lượng điểm, mômen và hợp lý cực đại](/xac-suat-thong-ke/bai-giang/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai).`,
  'uoc-luong-hop-ly-cuc-dai': String.raw`Hàm hợp lý xem dữ liệu đã quan sát là cố định và tham số là biến số cần tối ưu. Giá trị hàm hợp lý không phải xác suất của tham số. Với mẫu độc lập, hàm hợp lý là tích các khối lượng xác suất hoặc mật độ tại từng quan sát.

Logarit thường chuyển tích thành tổng và giữ nguyên vị trí cực đại khi hàm hợp lý dương. Nếu miền hỗ trợ phụ thuộc tham số, phải giữ điều kiện hỗ trợ khi tối ưu. MLE không mặc nhiên không chệch hoặc có phân phối chuẩn ở mọi cỡ mẫu.

Xem [Ước lượng điểm, mômen và hợp lý cực đại](/xac-suat-thong-ke/bai-giang/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai).`,
  'thong-ke-du': String.raw`Tiêu chuẩn phân tích nhân tử cho phép nhận diện tính đủ khi mật độ hoặc hàm khối lượng có thể tách thành một thừa số chỉ phụ thuộc mẫu qua thống kê đang xét và tham số, cùng một thừa số không phụ thuộc tham số.

Nếu một ước lượng có phương sai hữu hạn, điều kiện hóa nó theo thống kê đủ giữ nguyên kỳ vọng và không tăng phương sai. Đây là cơ chế của định lý Rao–Blackwell. Để kết luận ước lượng không chệch có phương sai nhỏ nhất duy nhất bằng định lý Lehmann–Scheffé, còn cần tính đầy đủ của thống kê đủ.

Xem [Tính đủ và hiệu quả ước lượng](/xac-suat-thong-ke/bai-giang/38-tinh-du-va-hieu-qua-uoc-luong).`,
  'thong-tin-fisher': String.raw`Đạo hàm của log hợp lý theo tham số được gọi là hàm điểm. Trong mô hình chính quy một tham số, kỳ vọng của hàm điểm bằng 0 và thông tin Fisher là kỳ vọng bình phương của nó. Với các quan sát độc lập, thông tin cộng lại.

Cận Cramér–Rao cho ước lượng không chệch của tham số bằng nghịch đảo thông tin của toàn mẫu, dưới các điều kiện chính quy cần thiết. Không bỏ qua điều kiện cho phép đổi thứ tự đạo hàm và tích phân hoặc điều kiện về miền hỗ trợ.

Xem [Tính đủ và hiệu quả ước lượng](/xac-suat-thong-ke/bai-giang/38-tinh-du-va-hieu-qua-uoc-luong).`,
  'khoang-tin-cay': String.raw`Trước khi lấy mẫu, hai đầu mút là các thống kê ngẫu nhiên và tham số là một hằng số chưa biết. Độ bao phủ là xác suất khoảng ngẫu nhiên chứa hằng số đó. Sau khi quan sát mẫu, hai đầu mút đã có giá trị cụ thể.

Khoảng tin cậy cho trung bình khác khoảng dự đoán cho một quan sát mới. Các khoảng chính xác và xấp xỉ có điều kiện áp dụng khác nhau. Mức danh nghĩa 95% chưa bảo đảm độ bao phủ thực tế bằng 95% khi giả thiết bị vi phạm.

Xem [Khoảng tin cậy tham số](/xac-suat-thong-ke/bai-giang/39-khoang-tin-cay-tham-so).`,
  'kiem-dinh-gia-thuyet': String.raw`Phải xác định giả thuyết không, giả thuyết đối và thống kê kiểm định trước khi đọc kết quả. Giá trị p đo mức cực đoan của dữ liệu theo giả thuyết không với quy tắc so sánh đã chọn. Nó không phải xác suất giả thuyết không đúng.

Không bác bỏ không đồng nghĩa chấp nhận hoặc chứng minh giả thuyết không. Khi kiểm định nhiều giả thuyết, cần xem xét xác suất sai lầm chung. Kết luận phải đi cùng ước lượng độ lớn tác động và độ bất định.

Xem [Kiểm định tham số và công suất](/xac-suat-thong-ke/bai-giang/40-kiem-dinh-tham-so-va-cong-suat).`,
  'cong-suat-kiem-dinh': String.raw`Với một giá trị tham số thuộc giả thuyết đối, gọi xác suất không bác bỏ là beta. Công suất tại giá trị đó bằng một trừ beta. Một phép kiểm định có cả một hàm công suất theo tham số, không chỉ một con số.

Khi lập kế hoạch cỡ mẫu, cần chọn trước mức ý nghĩa, công suất mục tiêu, độ lớn tác động cần phát hiện và giả định về độ biến thiên. Tăng cỡ mẫu thường tăng công suất trong mô hình chuẩn, nhưng không sửa sai lệch thiết kế.

Xem [Kiểm định tham số và công suất](/xac-suat-thong-ke/bai-giang/40-kiem-dinh-tham-so-va-cong-suat).`,
  'phan-tich-phuong-sai': String.raw`Trong ANOVA một nhân tố, tổng bình phương độ lệch quanh trung bình chung tách thành biến thiên giữa nhóm và trong nhóm. Chia mỗi tổng bình phương cho bậc tự do tương ứng cho các trung bình bình phương. Tỷ số giữa nhóm trên trong nhóm là thống kê F.

Bác bỏ giả thuyết tất cả trung bình bằng nhau chưa xác định nhóm nào khác. So sánh tiếp theo phải kiểm soát kiểm định nhiều lần. Nếu phương sai nhóm khác nhau hoặc dữ liệu là đo lặp trên cùng đối tượng, cần phương pháp phù hợp với cấu trúc đó.

Xem [Phân tích phương sai](/xac-suat-thong-ke/bai-giang/42-phan-tich-phuong-sai).`,
}

export const xstkWikiConnections = {
  'phan-phoi-tien-nghiem': ['phan-phoi-hau-nghiem', 'likelihood', 'xac-suat-co-dieu-kien'],
  'phan-phoi-hau-nghiem': ['phan-phoi-tien-nghiem', 'likelihood', 'ky-vong-co-dieu-kien'],
  'phan-phoi-dong-thoi': ['bien-ngau-nhien', 'doc-lap', 'ky-vong-co-dieu-kien'],
  'ky-vong-co-dieu-kien': ['phan-phoi-dong-thoi', 'ky-vong', 'phuong-sai'],
  'hiep-phuong-sai': ['phuong-sai', 'phan-phoi-dong-thoi', 'ma-tran-hiep-phuong-sai'],
  'ham-sinh-momen': ['ky-vong', 'phuong-sai', 'bien-ngau-nhien'],
  'luat-so-lon': ['ky-vong', 'dinh-ly-gioi-han-trung-tam', 'phan-phoi-mau'],
  'dinh-ly-gioi-han-trung-tam': ['luat-so-lon', 'phan-phoi-gauss', 'phan-phoi-mau'],
  'phan-phoi-mau': ['mau-tong-the', 'dinh-ly-gioi-han-trung-tam', 'khoang-tin-cay'],
  'uoc-luong-khong-chech': ['uoc-luong-hop-ly-cuc-dai', 'thong-ke-du', 'phuong-sai'],
  'uoc-luong-hop-ly-cuc-dai': ['likelihood', 'thong-tin-fisher', 'uoc-luong-khong-chech'],
  'thong-ke-du': ['uoc-luong-khong-chech', 'uoc-luong-hop-ly-cuc-dai', 'ky-vong-co-dieu-kien'],
  'thong-tin-fisher': ['uoc-luong-hop-ly-cuc-dai', 'phuong-sai', 'thong-ke-du'],
  'khoang-tin-cay': ['phan-phoi-mau', 'kiem-dinh-gia-thuyet', 'tham-so-toan-hoc'],
  'kiem-dinh-gia-thuyet': ['cong-suat-kiem-dinh', 'khoang-tin-cay', 'phan-phoi-mau'],
  'cong-suat-kiem-dinh': ['kiem-dinh-gia-thuyet', 'phan-phoi-mau', 'mau-tong-the'],
  'phan-tich-phuong-sai': ['kiem-dinh-gia-thuyet', 'phuong-sai', 'binh-phuong-toi-thieu'],
}
