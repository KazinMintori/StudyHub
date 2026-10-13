# Rà soát bài 28.31–28.60

## Phạm vi nguồn

Đã đối chiếu trực tiếp PDF trang in 947–949 (PDF 966–968) cho các bài 28.31–28.60, gồm hình E28.32, E28.33, E28.38, E28.39, P28.49, P28.58, P28.59 và P28.60. Đề, đơn vị, số liệu và mọi tiểu câu được giữ trong `raw_materials/physics/translations/chapter-28/13-bai-tap-31-60.md`.

## Kiểm tra tính toán

Suite `raw_materials/physics/verify_chapter28_31_60.py` chạy qua bốn nhóm kiểm tra:

- 28.31–28.36: đổi gauss sang tesla, từ trường cung tròn, triệt tiêu trường tâm hai vòng, dòng và vị trí nửa trường, số vòng cuộn dây.
- 28.37–28.48: dấu dòng theo chiều đường Ampere, tổng dòng trong các đường E28.38, các cấu hình cáp đồng trục, ống dây và xuyến, cùng trường/từ hóa của lõi từ.
- 28.49–28.56: tích có hướng của trường điện tích chuyển động và lực lên điện tích, vị trí triệt tiêu trường của dây, lực từ và điện trường cân bằng.
- 28.57–28.60: ước lượng điện thoại, trường của hai dây ngược chiều, triệt tiêu tại P/Q và lực tổng hợp lên vòng chữ nhật.

Các kết quả chính đã tính lại gồm dòng tương đương $I_{31}=3{,}82\times10^{-7}\,\mathrm A$ cho vòng não, $I_{40}=16{,}4\,\mathrm A$, $B_{44}=2{,}656\,\mathrm{mT}$, ba dòng ở bài 28.45 lần lượt $3{,}72\times10^6$, $2{,}49\times10^5$ và $237\,\mathrm A$, cùng lực hướng lên ở bài 28.60 là $8{,}55\times10^{-5}\,\mathrm N$.

Kiểm tra cấu trúc xác nhận 30 hộp bài tập, 30 lời giải gập kế tiếp và không có H1. MathJax theo cấu hình repo đo 564 công thức inline (rộng nhất 36,5 ex, không công thức nào vượt 38 ex) và 67 công thức hiển thị (rộng nhất 26,9 ex). Bộ rà câu tiếng Việt trả về không có gợi ý.

## Giả định và xử lý độ chính xác

- Bài 28.43 cho mật độ vòng tối thiểu liên tục $1{,}7905\times10^3\,\mathrm{m^{-1}}$. Với ống dài $0{,}400\,\mathrm m$, phải làm tròn số vòng lên thành 717 để không thấp hơn trường yêu cầu. Chiều dài dây ước tính là $63{,}1\,\mathrm m$, bỏ qua độ dài tăng thêm do bước xoắn.
- Bài 28.47 dùng độ từ thẩm tương đối không đổi $K_m=5200$ như mô hình của đề. Kết quả $B=5{,}88\,\mathrm T$ là giá trị theo mô hình tuyến tính đã cho, không phải dự đoán có xét bão hòa thép.
- Bài 28.53 là ước lượng theo mô hình các vòng giống nhau cách nhau $d\ll R$. Để minh họa phép thế, dùng các giả định nêu trong lời giải: lực tách 5 N và diện tích 25 cm². Chúng được ghi là giả định bài toán, không gán cho một sản phẩm cụ thể.
- Bài 28.57 không chỉ định hãng hoặc mẫu điện thoại, nên không gán công suất phát số học như một đặc tính chung. Giữ công suất $P$ làm tham số và biểu diễn kết quả theo $P$. Giá trị $0{,}10\,\mathrm W$ chỉ là kịch bản minh họa có ghi rõ, không được gọi là công suất “điển hình”. Hình học cũng nêu giả định riêng: bề rộng đầu 16 cm, đường kính loa 2 cm và điểm giữa tai nằm trên trục vòng tương đương. Theo mô hình đề bài, pin được giả sử cấp công suất $P$ tại 1,5 V.
- Với bài 28.58, mũi tên hình xác nhận dây tại $y=+a$ mang dòng ra khỏi trang và dây tại $y=-a$ mang dòng vào trang. Vì thế trường tổng trên trục $x$ hướng $+x$, đạt cực đại tại $x=0$ và giảm như $1/x^2$ khi $|x|\gg a$.
- Với bài 28.59, hình xác nhận $I_1$ đi vào trang. Dòng triệt tiêu tại P phải là $I_2=2{,}00\,\mathrm A$ đi ra trang. Thành phần tại S được tính từ tọa độ $(0{,}36,0{,}48)\,\mathrm m$, suy ra từ ba khoảng cách trong hình.
- Với bài 28.60, dòng ở cạnh gần cùng chiều dòng dây thẳng nên bị hút lên. Dòng cạnh xa ngược chiều nên bị đẩy xuống. Lực hai cạnh ngắn cân bằng theo phương ngang.

Không thấy sai lệch giữa các dữ kiện chữ, ký hiệu chiều trên hình và các kết quả đã kiểm tra cho nhóm này. Không tra cứu công suất của mẫu điện thoại ngoài vì bài và giao việc không nêu mẫu cụ thể.
