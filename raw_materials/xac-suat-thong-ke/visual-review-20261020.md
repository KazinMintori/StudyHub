# Rà soát bộ hình xác suất và thống kê ngày 20/10/2026

Bộ hình thay thế gồm 51 SVG cho bài 28–44, giữ nguyên tên tệp và đặt trong `docs/xac-suat-thong-ke/bai-giang/img/co-dien-refined/`. Ba hình Bayes ở `co-dien-bayes/` được kiểm tra cùng bộ hình này. Các hình được dựng bằng SVG hoặc Matplotlib từ NumPy/SciPy, có thể tái tạo bằng mã nguồn.

## Kết quả kiểm tra cuối

| Phạm vi | Số hình | Chữ bị cắt | Cặp chữ chồng nhau | Nhãn bị đường vẽ xuyên qua |
| --- | ---: | ---: | ---: | ---: |
| Bộ hình thay thế | 51 | 0 | 0 | 0 |
| Bộ thay thế và ba hình Bayes | 54 | 0 | 0 | 0 |

Kiểm tra dùng Chromium/Puppeteer với chiều rộng render 640 px. Tất cả SVG giữ tỉ lệ khi thay đổi chiều rộng. Bộ phát hiện xét hộp bao chữ và lấy mẫu các đường vẽ có stroke đang hiển thị, loại các phần tử trong `defs`. Phần nền tô màu không được coi là va chạm. Kết quả máy nằm tại `C:/Users/Ai/.codex/tmp/xstk-final-54-qa/manifest.json`.

Đã xem sáu contact sheet của toàn bộ 54 bản render cuối. Đã xem riêng bảng phân phối đồng thời 31.1 sau khi đồng bộ với ví dụ trong Notes. Nhãn chú giải nằm trong khoảng trống dành riêng phía trên dữ liệu. Các sơ đồ dùng vùng nối trống, nhãn không đặt trên mũi tên hoặc cạnh hình. Các đường cong liên tục được tính từ hàm chính xác, thường với 601–1201 điểm. Chữ nguồn tối thiểu 14 đơn vị. Font tiếng Việt Be Vietnam Pro được nhúng trong SVG qua bộ hỗ trợ chung.

## Các mô hình và sửa đổi học thuật đã kiểm lại

- Bài 28–29: Kiểm lại tổ hợp `C(9, 3) = 84`, `C(13, 3) = 286`, các miền của biểu đồ Venn, xác suất gặp `7/16`, kỳ vọng hình học và nhị thức âm, tọa độ barycentric của simplex.
- Bài 30: Phân phối mũ dùng cường độ 0.5/phút. Các xác suất đuôi và tính không nhớ được tính bằng hàm survival. Chú giải Beta tách khỏi vùng đỉnh. Nhãn ghi rõ mật độ Beta(0.5, 0.5) không bị chặn tại hai biên.
- Bài 31: Hình 31.1 dùng đúng bảng sáu ô của ví dụ sự cố trong Notes, với lề của X là `(0.7, 0.3)` và lề của Y là `(0.5, 0.3, 0.2)`. Mô hình liên tục là `f(x, y) = (6/5)(x + 2y)` trên `0 < x < y < 1`. Tích phân kép bằng 1. Mật độ lề và mật độ điều kiện tại Y = 0.8 lần lượt là `(6/5)(1 + x − 2x²)` và `1 + 0.625x` trên các miền tương ứng.
- Bài 32: Các số r trong hình phân tán được tính từ chính các điểm vẽ. Mô hình phi tuyến dùng X đều đối xứng trên `[−1, 1]` và Y = X², có tương quan 0 nhưng phụ thuộc. Sơ đồ kỳ vọng toàn phần định nghĩa pᵢ, mᵢ và khai triển ba số hạng. Hình phép chiếu nêu giả thiết momen bậc hai hữu hạn.
- Bài 33–34: Mật độ tổng hai biến đều và ba thống kê thứ tự được kiểm tra chuẩn hóa. MGF là `exp(t²/2)` của N(0, 1), có momen tại 0 đúng. Ví dụ Jensen cho hai giá trị 1.5 và 4.5. Ví dụ Markov/Chebyshev dùng X không âm, kỳ vọng 70, độ lệch chuẩn 10, ngưỡng 90, với hai chặn `7/9` và `1/4`.
- Bài 35: Họ trung bình mẫu trong ví dụ chuẩn dùng phương sai `4/n` trên cùng thang trục. Hình CLT dùng PMF B(100, 0.5) thật và chuẩn N(50, 25), với xác suất chính xác tại 50 bằng 0.0795892374 và xấp xỉ hiệu chỉnh liên tục bằng 0.0796556746. Hình Cauchy ghi rõ kỳ vọng và phương sai không tồn tại. Luật của trung bình các biến Cauchy chuẩn độc lập không đổi theo n.
- Bài 36–38: Phân phối mẫu chuẩn, chi bình phương và Student t được tính trực tiếp. Ví dụ MLE Bernoulli dùng n = 10, k = 7. Ví dụ đều dùng n = 3 và cực đại mẫu 8.5. Cận Cramér–Rao minh họa bằng mẫu chuẩn biết phương sai 4. Ví dụ Rao–Blackwell dùng bốn biến Bernoulli(0.4), biến đổi X₁ thành T/4, làm phương sai giảm từ 0.24 xuống 0.06. Tính đủ được phát biểu qua luật có điều kiện không phụ thuộc tham số cố định θ.
- Bài 39: Mô phỏng dùng `np.random.default_rng(20261020).normal(50, 1.2, 20)`. Mỗi khoảng có nửa độ dài `1.959963984540054 × 1.2`, không sửa kết quả ngẫu nhiên. Có 18/20 khoảng chứa 50 trong lần chạy này. Khoảng Wald với n = 30, k = 2 là `[-0.02259402, 0.15592735]`, Wilson là `[0.01847702, 0.21323458]`. Hai phân vị chi bình phương df = 9 là 2.7003895 và 19.0227678, theo CDF trái.
- Bài 40: p hai phía tại z = 2.30 bằng 0.02144822, và cả hai đuôi đều được tô. Ví dụ sai lầm loại I/II dùng Z chuẩn dưới H₀, dịch trung bình 2.5 dưới H₁, ngưỡng 1.644854, cho β = 0.19623506. Hàm lực dùng mô hình một phía biết σ = 1, μ₀ = 0, n = 9 hoặc 25.
- Bài 41: Tần số quan sát `(85, 30, 15, 70)` và kỳ vọng `(80, 35, 15, 70)` cho thống kê 1.0267857. Bảng liên hợp minh họa 2 × 3 có tổng 120 và các tần số kỳ vọng `(25, 20, 15)` ở mỗi hàng. Quy tắc tần số kỳ vọng được gọi là hướng dẫn xấp xỉ chi bình phương. Fisher chính xác chỉ được giới thiệu trong nhánh bảng 2 × 2, không thay thế mọi kiểm định độ phù hợp thưa.
- Bài 42: Ba nhóm `(2, 3, 4)`, `(4, 5, 6)`, `(6, 7, 8)` cho SSB = 24, SSW = 6, SST = 30, F = 12. Hình miền bác bỏ dùng F(3, 20), ngưỡng 3.0983912 và F quan sát minh họa 4.5. Không khẳng định khác biệt trung bình luôn làm F rất lớn.
- Bài 43: Hình chuẩn có điều kiện dùng `Y | X = x ~ N(2 + 0.8x, 0.8²)`. Hình khoảng dùng n = 15, x̄ = 5, Sxx = 40, s = 0.8 và phân vị t df = 13 đúng bằng 2.1603687. Khoảng cho trung bình được ghi là khoảng tại từng điểm. Các đồ thị phần dư có trục và nhãn ngắn, dữ liệu chẩn đoán chỉ là minh họa.
- Bài 44: Sơ đồ chọn kiểm định bắt đầu từ đại lượng cần so sánh và thiết kế. Có điều kiện đối xứng cho Wilcoxon hạng dấu và giới hạn diễn giải Mann–Whitney. Các hiệu số 1.2, −2.5, 4.8 sau khi loại 0 cho T⁺ = 4, T⁻ = 2, W = 2. KS dùng mẫu `[-1.2, −0.4, 0.2, 0.8, 1.5]`, xét cả giới hạn trái và giá trị phải tại mỗi bước nhảy. D đúng bằng 0.1881446014, đạt ở x = 0.8 tại giới hạn trái của ECDF. Kết quả khớp `scipy.stats.kstest`.

## Tái tạo và xác minh

```powershell
python scripts/generate-xstk-refined-figures.py
python scripts/generate-xstk-refined-figures.py --check
$env:QA_OUTPUT='C:/Users/Ai/.codex/tmp/xstk-final-54-qa'
node scripts/qa/xstk-figure-gallery.mjs docs/xac-suat-thong-ke/bai-giang/img/co-dien-refined docs/xac-suat-thong-ke/bai-giang/img/co-dien-bayes
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

Kiểm tra Python cho các mô hình và nhãn số đã đạt. Bộ kiểm thử skill đạt 39/39. Kiểm tra toàn bộ bài giảng tại thời điểm trước khi chuyển đường dẫn hình đạt 0 lỗi, với hai cảnh báo chữ nhỏ từ tài sản cũ của hình 34.3 và 35.2. Chuyển sang bộ hình mới loại hai tài sản chữ nhỏ đó khỏi các bài liên quan. Không chạy build toàn cục trên máy cục bộ.

Sau tích hợp, cả 51 hình của bài 28–44 đều được tham chiếu đúng một lần từ Notes và đều dùng thư mục co-dien-refined/. Hình 28.3 được đặt cạnh bài toán cuộc hẹn. Không thiếu tệp, không lệch tên và không có hình mới bị bỏ sót.
