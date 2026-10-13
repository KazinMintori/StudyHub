# Rà soát riêng: Bộ bài tập 27.31–27.60

## Phạm vi và nguồn

Đã đối chiếu nguyên văn bài tập trên trang in 910–914 (trang PDF 930–934) của *Young and Freedman, University Physics, 15th edition*. Bản dịch gồm đủ 30 bài, giữ toàn bộ câu hỏi, tiểu mục và ngữ cảnh được nêu trong nguồn. Các hình được tham chiếu theo quy ước tương lai img/young-27/hinh-e27/p27-NN.png; không tạo hay sửa tài sản hình ảnh trong lượt này.

## Kết quả rà soát

- Mỗi bài 27.31–27.60 có một khối exercise và ngay sau đó là một khối solution với Tóm tắt đề bài, Hướng đi và lời giải.
- Các sơ đồ được dùng để xác định đúng cực dương, chiều lực, hướng trục và kích thước cần lấy. Bài 27.37 chỉ có các câu (a)–(c) trong nguồn. Phần (d)–(e) vốn có trong bản nháp đã bị loại bỏ.
- Mô hình Hall của bài 27.45 nêu rõ hướng điện trường Hall theo trục $+z$. Bài 27.55 nêu chiều dòng điện theo quy tắc bàn tay phải thay vì đoán một chiều không xác định khi chưa biết cách đặt hai đầu nguồn.
- Công thức inline được đo bằng MathJax: 464 biểu thức, rộng nhất 33,776ex, không có biểu thức vượt 38ex. Các dòng công thức hiển thị được đo riêng bằng MathJax: tối đa 29,974ex, không có dòng nào vượt 30ex. Cả 66 khối công thức hiển thị đều đóng dấu phân cách đúng.

## Các số liệu được hiệu chỉnh sau khi tính lại

| Bài | Kết quả kiểm lại | Ghi chú |
| --- | --- | --- |
| 27.31 | $V_{\max}=817\,\mathrm{V}$, $a_0=112{,}7\,\mathrm{m/s^2}$ | Mạch hình chỉ có điện trở $25\,\Omega$; sau đó điện trở giảm còn $2\,\Omega$. |
| 27.37 | $F_{ab}=1{,}20\,\mathrm{N}$ vào trang, $F_{cd}=1{,}20\,\mathrm{N}$ ra trang, $|\tau|=0{,}420\,\mathrm{N\,m}$ | Hình cho bản lề dài $0{,}200\,\mathrm{m}$ và tay đòn $0{,}350\,\mathrm{m}$. |
| 27.39 | $I_{A2}=1{,}03\times10^{-2}\,\mathrm{kg\,m^2}$, $\alpha=2{,}91\times10^2\,\mathrm{rad/s^2}$ | Mômen quán tính là của khung dây mảnh quanh trục A2 nằm ngang. |
| 27.49 | $v=8{,}30\times10^6\,\mathrm{m/s}$, $B=0{,}139\,\mathrm{T}$ | Bảo toàn năng lượng cho hai hạt đơteri có cùng tốc độ. |
| 27.50 | $\mu=9{,}33\times10^{-24}\,\mathrm{A\,m^2}$ | Tính lại từ chu kì quỹ đạo và diện tích vòng. |
| 27.52 | Proton: $8{,}86\times10^{-13}\,\mathrm{J}=5{,}54\,\mathrm{MeV}$. Hạt alpha: $5{,}57\,\mathrm{MeV}$. | Dùng đúng dữ kiện khối lượng và điện tích của từng hạt. |
| 27.53 | Hai khoảng tách liền kề đều $1{,}68\times10^{-3}\,\mathrm{m}$. | Khoảng tách là millimet, không phải centimét. |
| 27.54 | $V=2{,}26\times10^4\,\mathrm{V}$, độ tách $0{,}1667\,\mathrm{m}$. | Tính điện áp từ $qV=mv^2/2$ và $R=mv/(qB)$. |
| 27.56 | $I=3{,}43\,\mathrm{A}$, $a_0=17{,}6\,\mathrm{m/s^2}$ | Hai điện trở $25\,\Omega$ và $10\,\Omega$ mắc nối tiếp như trong hình. |

## Kiểm tra tính toán và vectơ

Chương trình verify_chapter27_31_60.py dùng NumPy để kiểm tra các giá trị số, các thành phần lực và tích có hướng trong các sơ đồ. Chương trình chạy thành công bằng Python Miniconda, và in “Chapter 27 Exercises 27.31–27.60: numerical/vector checks passed.” Không dùng SymPy.

Các mục chính được kiểm tra gồm lực từ trên thanh và khung, mômen quanh bản lề, mômen quán tính, cân bằng động cơ, chiều lực Hall, chuyển động trong điện trường và từ trường, chuyển động hạt tích điện, các bán kính cyclotron và lực trên dây 3D.

## Sai khác riêng tư so với bản nháp/phiên bản tính cũ

Bản nháp trước lượt hoàn thiện dừng ở bài 27.42. Tập kiểm tra ban đầu có các phương trình và kết quả không khớp hình hoặc phép tính ở bài 27.31, 27.37, 27.39, 27.49–27.50, 27.52–27.54 và 27.56. Các kết quả đã được sửa trong bản dịch và bộ kiểm tra. Riêng bài 27.37, phần (d)–(e) trong bản nháp không thuộc đề trên trang nguồn 911 nên đã bỏ.
