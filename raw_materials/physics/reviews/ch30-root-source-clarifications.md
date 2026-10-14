# Các điểm đối chiếu nguồn và mô hình chương 30

Đã đọc trang in 988–1017, PDF 1008–1037, và đáp số A-18 tại PDF 1563. Tệp văn bản trích xuất dùng font Pearson thường biến ký tự µ thành m, nên các tiền tố đã được đọc trên ảnh trang khi cần.

## Dữ kiện, điều kiện và số hiệu

- Ví dụ 30.1 dùng hỗ cảm khoảng 25 µH. Ví dụ 30.2 dùng thời điểm 3,0 µs. Ví dụ 30.3 cho 40 µH, Ví dụ 30.4 tăng dòng từ 0 đến 6,0 A trong 3,0 µs, không phải ngắt dòng.
- Câu hỏi mở đầu có đúng bốn lựa chọn về vật liệu dẫn, vật liệu cách điện mang điện tích tổng khác không, vật liệu sắt từ và vật liệu sắt từ đã từ hóa. Tự kiểm 30.1 có năm lựa chọn, gồm lựa chọn thứ năm là hỗ cảm còn một phần tư. Bản thảo AGY từng đổi câu hỏi mở đầu và bỏ lựa chọn thứ năm, đã được phục hồi khi rà tại Codex.
- Phương trình 30.20 là phương trình dao động điện tích q''+q/(LC)=0, không phải phương trình vòng chưa thay dòng bằng đạo hàm điện tích. Nhãn đã được chuyển đúng chỗ.
- Ví dụ 30.6 cho L chưa làm tròn 0,06937271788076092 H. Bản thảo từng ghi 0,0687 H dù phép chia hiển thị là 0,01015/0,14631. Đã sửa phép tính. Khi dùng L làm tròn 69 mH, hằng số thời gian được ghi xấp xỉ 390 µs như mức làm tròn của phép đánh giá tiếp theo.
- Ví dụ 30.7 hỏi phần năng lượng bị tiêu tán sau 2,3 hằng số thời gian. Bản thảo từng đảo thành câu hỏi thời gian để mất 99%, đã khôi phục đúng đề và tính trực tiếp 1-exp(-4,6).
- Tự kiểm 30.6 có điện tích 2,0 µC, tự cảm 3,0/6,0/3,0 µH và điện dung 6,0/3,0/3,0 µF. Cả đề lẫn verifier từng thay bằng milli, làm các tỉ số tình cờ vẫn đúng, đã sửa toàn bộ.
- Hình 30.17 có tiếp điểm d để nạp tụ và a để nối vòng RLC phóng điện. Hai vị trí từng bị mô tả ngược trong bản thảo.
- VP30.4.2, VP30.4.3, VP30.10.1, VP30.10.2 và bài cầu nối có các tiền tố micro đã đọc trực tiếp. Điện dung ở VP30.10.3 và VP30.10.4 lần lượt 35,1 µF và 61,1 µF.
- Bài 30.37 thật sự hỏi tại 2,50 ms. Span văn bản dùng TimesLTPro-Roman cho toàn bộ cụm này, không phải ký tự µ bị ánh xạ thành m.
- Bài 30.57 hỏi tại 0,115 ms. Ba cuộn có L tương đương 10,8 mH và hằng số thời gian 0,144 ms.

## Bài 30.53: Giả thiết xung và điều kiện đầu

Từ hình học và điện trở dây: L=0,3553057584 mH, R=0,6276902122 Ω, C=10 µF. Xung Faraday có tích phân độ lớn K=N A ΔB=0,00942477796 V·s.

Phụ lục cho Q=K/R=15,0 mC, U=11,3 J, thời gian phóng hết 93,8 µs và thời gian năng lượng còn 10% là 1,30 ms. Phép Q=K/R bỏ điện áp tự cảm và điện áp tụ trong tích phân xung. Nó không phải giới hạn bật trường bậc thang của mạch RLC đã nêu. Trong giới hạn bậc thang, điện tích vẫn bằng không ngay sau xung, còn dòng nhảy với độ lớn K/L=26,5258 A. Điện tích cực đại đầu tiên là 1,4595 mC ở 90,617 µs, với năng lượng tụ 0,106509 J.

Khi bắt đầu giai đoạn mới với tụ tích đầy và i(0)=0, nghiệm phải có cả cosin và sin: q=q0 exp(-αt)[cos(ωd t)+(α/ωd)sin(ωd t)]. Lần đầu q=0 là 96,9056 µs. Giá trị 93,8 µs là ước lượng một phần tư chu kỳ bỏ hiệu chỉnh pha. Giữ năng lượng chính xác cho thời gian còn 10% là 1,27550 ms, còn bao năng lượng yếu tắt dần cho 1,30338 ms.

Lời giải giữ các câu hỏi và trình bày rõ mô hình cho từng giá trị, không đưa điện lượng và năng lượng của xung điện trở thành đáp án duy nhất của mô hình RLC đầy đủ.

## Bài 30.69: Dấu hỗ cảm

Ảnh phụ lục A-18 ghi công thức đối nhau µ0π(N1²b²-N2²a²)/ℓ và số 10,3 mH. Các từ thông ở chính phụ lục lại phù hợp trường trong lõi chung tỉ lệ với N1-N2.

Với dòng nối tiếp tạo trường đối nhau, từ thông móc vòng tổng phải là N1Φ1-N2Φ2. Tự cảm đúng là L1+L2-2M, với M=µ0πN1N2a²/ℓ. Kết quả 8,927057 mH được tính độc lập bằng năng lượng hai vùng và bằng ma trận tự cảm. Cấu hình hỗ trợ cho 16,033172 mH, phù hợp đáp số làm tròn 16,0 mH.

Lời giải dùng 8,93 mH và chỉ rõ quy ước móc vòng, không lặp lại dấu sai trong đáp số.

## Các điện áp và dữ liệu đồ thị

- 30.9–30.10 có dòng từ b đến a. Điện áp v_ab phải được đổi dấu trước khi dùng quy ước thụ động.
- 30.61 có v_cd=-156 V sau mở, với d cao thế hơn c. Phụ lục ghi 156 V theo độ lớn cùng đầu cao thế, nên lời giải ghi rõ dấu của điện áp đã định nghĩa.
- 30.63 đo v_cb trên cả nhánh R,L, không chỉ trên cuộn. 30.64 nối tắt cả đoạn c-b. Dòng cuộn ban đầu vẫn 0,180 A, rồi giảm với L/R, trong khi nguồn tiếp tục cấp qua R0.
- 30.59 khớp đủ tám cặp dữ liệu. Các đồ thị nguồn ở 30.67, 30.68 có lần lượt 18 và 13 điểm, được đọc từ tọa độ vector PDF để đối chiếu các ước lượng hằng số thời gian.

Các hồ sơ tính toán nằm trong qa/physics/chapter30. Không chèn nhật ký kiểm chứng vào bài học.
