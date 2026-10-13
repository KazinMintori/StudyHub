# Rà soát đối chiếu: Luyện tập có hướng dẫn Chương 27

## Phạm vi nguồn

Đã đối chiếu phần Guided Practice ở trang in 907 (PDF 927), bài toán cầu nối và đầu phần Discussion Questions ở trang in 908 (PDF 928). Bài luyện có đúng 12 biến thể hướng dẫn: VP27.1.1–27.1.4, VP27.6.1–27.6.4 và VP27.7.1–27.7.4. Bài toán cầu nối “Magnetic Torque on a Current-Carrying Ring” nằm ngay sau đó và đã được giữ đủ các tiểu mục (a)–(c) cùng bảy bước Solution Guide.

## Đối chiếu và tính lại

- VP27.1.1–27.1.4 giữ đủ điều kiện, đơn vị và các phần độ lớn/hướng. Lực electron VP27.1.1 hướng $-z$, VP27.1.3 yêu cầu $\vec B$ hướng $+z$, và ion sắt VP27.1.4 chịu lực hướng $-y$.
- VP27.6.1–27.6.4 giữ các bài quỹ đạo proton, chuyển động xoắn ốc, bộ chọn vận tốc và tách đồng vị. Các kết quả số khớp khóa đáp số trang A-17: bán kính $0{,}435\,\mathrm{mm}$ và $0{,}348\,\mathrm{mm}$, bước xoắn $1{,}64\,\mathrm{mm}$, tốc độ chọn $8{,}00\times10^5\,\mathrm{m/s}$, và bán kính $6{,}64\,\mathrm{cm}$, $7{,}47\,\mathrm{cm}$ cho hai đồng vị.
- VP27.7.1–27.7.4 giữ toàn bộ thành phần véc-tơ và câu hỏi hai góc. Lực VP27.7.1 hướng $+z$, dòng VP27.7.2 hướng lên, véc-tơ lực VP27.7.3 có hai thành phần âm và độ lớn $4{,}90\times10^{-3}\,\mathrm{N}$, còn VP27.7.4 cho hai góc $41{,}0^\circ$ và $139{,}0^\circ$.
- Bài cầu nối dùng đúng $B_z<0$ như Hình PDF 928: $\vec B=(1{,}15\times10^{-2}\,\mathrm{T})(12\hat\imath+3\hat\jmath-4\hat{k})$. Tính độc lập cho các thành phần mômen lực $(-1{,}54,-2{,}05,-6{,}14)\times10^{-4}\,\mathrm{N\,m}$, năng lượng thế giảm $7{,}55\times10^{-4}\,\mathrm{J}$ và tốc độ góc $42{,}1\,\mathrm{rad/s}$, khớp đáp số A-17.

Script Python `raw_materials/physics/verify_chapter27_guided.py` chạy đạt sau khi chuẩn hóa phép so sánh sai số theo độ lớn của đại lượng. Script kiểm tra 12 bài tập, cầu nối và các kết quả véc-tơ dùng chung. MathJax render độc lập 23 công thức hiển thị và 270 công thức nội dòng trong hai tệp liên quan: Không có lỗi TeX, công thức hiển thị rộng hơn 30ex hay công thức nội dòng rộng hơn 38ex. Công cụ rà soát văn bản trả về 0 gợi ý. Bản PDF render trang 927–929 để đối chiếu nằm trong `raw_materials/physics/reviews/ch27-guided-discussion-pages/`.

## Ranh giới

Trang 907 cũng chứa phần kết của hiệu ứng Hall ngay trước nhan đề Guided Practice. Phần đó thuộc mục 27.9, nên không được nhập vào bộ 12 bài tập. Bài cầu nối thuộc Guided Practice; Q27.1–Q27.18 bắt đầu riêng dưới nhan đề Discussion Questions ở trang 908.
