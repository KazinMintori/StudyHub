# Rà soát Guided Practice và bài toán cầu nối Chương 28

## Đối chiếu nguồn

Đã đối chiếu trực tiếp các bài VP28.2.1–28.2.4, VP28.5.1–28.5.4 và VP28.10.1–28.10.4 ở trang in 943–944 (PDF 963–964). Cả ba dòng nhắc ôn ví dụ trước khi giải đều được giữ. Bài toán cầu nối “Magnetic Field of a Charged, Rotating Dielectric Disk” có đủ đề và 8 bước hướng dẫn gốc, kèm Hình 28.30.

## Kết quả kiểm tra độc lập

Suite `raw_materials/physics/verify_chapter28_guided.py` chạy thành công. Mã kiểm tra các tích có hướng và hướng véc-tơ tại VP28.2.1–28.2.4, lực từ tương hỗ tại VP28.2.2, phép chồng chất tại VP28.5.2, các trường theo từng miền trong VP28.10.1–28.10.2, tính liên tục tại biên, các giá trị ống dây/hình xuyến và tích phân vành khăn của bài cầu nối.

Các kết quả số chính từ tính toán độc lập: VP28.2.1 có các trường $3{,}20\times10^{-15}\,\mathrm T$, $8{,}00\times10^{-16}\,\mathrm T$, $0$ và $1{,}13\times10^{-15}\,\mathrm T$ theo các hướng đã nêu; VP28.2.2 cho $1{,}13\times10^{-28}\,\mathrm N$ và hai lực hút hướng vào nhau (lực lên proton $+x$, lên electron $-x$); VP28.2.3 cho $-2{,}88\times10^{-11}\hat k\,\mathrm T$; VP28.2.4 cho $9{,}83\times10^{-23}\hat k\,\mathrm N$. Các bài còn lại cho $2{,}24\,\mathrm A$, ba véc-tơ trường $(-60{,}0,-46{,}7,+86{,}7)\,\mu\mathrm T\hat i$, các dòng $5{,}00\,\mathrm A$ và $1{,}00\,\mathrm A$, $3{,}29\times10^4\,\mathrm A$, bộ trường hình trụ $4{,}94$, $8{,}89$, $6{,}67\,\mu\mathrm T$, $3{,}18\,\mathrm A$, và $833$ vòng với trường biên $2{,}33$/$1{,}75\,\mathrm{mT}$.

Bài cầu nối cho $B=\mu_0nQ/a$. Tích phân số độc lập theo bán kính khớp biểu thức đóng; nếu cùng điện tích dồn ở vành ngoài thì trường tại tâm bằng một nửa kết quả của đĩa tích điện đều.

## Phạm vi tệp

Đề và lời giải được lưu ở `translations/chapter-28/10-luyen-tap-huong-dan.md`. Bộ Guided Practice không có hình riêng; ảnh bài toán cầu nối dùng `img/young-28/hinh-bridge28-30.png`. Không dùng đáp số như bằng chứng thay phép tính.
