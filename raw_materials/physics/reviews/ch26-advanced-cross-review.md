# Rà soát đối chiếu độc lập: Bài nâng cao Chương 26

## Phạm vi

Đối chiếu tệp `12-bai-nang-cao-mcat.md` với Young–Freedman 15e, trang in 876–877 (PDF 896–897), và khóa đáp số trang A-16–A-17 (PDF 1561–1562). Đã xem trực tiếp các trang nguồn, sơ đồ mạch liên quan và hai trang khóa đáp số. Các tệp nguồn được giữ nguyên, ngoại trừ bản sửa P26.85 theo kết quả đối chiếu.

## Phát hiện cần sửa

- **P26.85, mức nghiêm trọng cao:** Bản cũ ghi sai độ dài đoạn là $1{,}0\,\mathrm{mm}$ thay vì $1{,}0\,\mathrm{\mu m}$. Vì vậy phép tính coi quãng đường $2{,}0\,\mathrm{mm}$ là hai đoạn đã sai hệ số mũ. Nguồn quy định $\Delta x=1{,}0\,\mathrm{\mu m}$, tức $2000$ đoạn trên quãng đường đó. Khóa đáp số cho $3{,}4\times10^{-4}$ ở phần (d) và $0{,}88$ ở phần (e), đều là tỉ số điện áp còn lại.
- Đã khôi phục ngữ cảnh sinh học bị lược ở phần (e): Sợi trục thụ động cần phục hồi điện áp định kỳ, tốc độ truyền xung khoảng $30\,\mathrm{m/s}$, myelin tạo các đoạn cách nhau bởi nút Ranvier, và tăng điện trở màng trên đoạn dài $1{,}0\,\mathrm{\mu m}$.
- Đã sửa lời giải để phân biệt tỉ số điện áp còn lại với phần điện áp bị suy giảm. Sau $2000$ đoạn, trường hợp không myelin còn $3{,}3546\times10^{-4}$, nghĩa là giảm $99{,}96645\%$. Trường hợp myelin còn $0{,}88289$, nghĩa là giảm $11{,}71146\%$.

## Kiểm tra độc lập các bài ưu tiên

- **P26.82:** Hai hằng số thời gian là $4RC$ khi nạp và $(4R\parallel R)C=0{,}8RC$ khi phóng. Với $R=10{,}0\,\mathrm{k\Omega}$ và $C=10{,}0\,\mathrm{\mu F}$, chu kỳ khoảng $0{,}377\,\mathrm{s}$ và tần số $2{,}65\,\mathrm{Hz}$.
- **P26.83–26.84:** Chọn nghiệm dương của phương trình tự đồng dạng cho $R_T=R_1+\sqrt{R_1^2+2R_1R_2}$. Đối xứng khối lập phương cho $R_{eq}=5R/6$.
- **P26.85:** Script Python độc lập xác nhận $R_T=3{,}2064\,\mathrm{M\Omega}$ và $\beta=0{,}004008$ ở phần (c). Với myelin, $R_T=205{,}53\,\mathrm{M\Omega}$ và $\beta=6{,}2282\times10^{-5}$. Kết quả khớp khóa đáp số khi diễn giải $0{,}00034$ và $0{,}88$ là điện áp còn lại.
- **P26.63:** Phân tích theo cực tính đang vẽ cho $\mathcal E=-108{,}75\,\mathrm{V}$, nên nguồn phải đảo cực và có độ lớn $108{,}75\,\mathrm{V}$ (làm tròn $109\,\mathrm{V}$). Dòng qua điện trở $10\,\Omega$ là $2/3\,\mathrm{A}$, nên thời gian tỏa $60{,}0\,\mathrm{J}$ là $13{,}5\,\mathrm{s}$.
- **P26.62, .67, .68, .70, .71 và .75:** Phân tích nút, giới hạn tụ tại $t=0^+$ và trạng thái ổn định, bảo toàn điện tích, cùng cân bằng năng lượng cho kết quả lần lượt khớp lời giải đang có: $R_{eq,62}=1{,}40\,\Omega$, $V_{ab,67}=-12{,}0\,\mathrm{V}$ và $I_S=1{,}71\,\mathrm{A}$, $P_{song\ song,68}=405\,\mathrm{W}$, $I_{R1,R2,R3,70}=(4{,}20;1{,}40;2{,}80)\,\mathrm{A}$, $Q_{f,70}=72{,}0\,\mathrm{\mu C}$, và $V_b=6{,}00\,\mathrm{V}$ ở P26.75.

## Độ đầy đủ câu hỏi

Các bài P26.81–26.88 giữ các tiểu mục và lựa chọn MCAT. Đoạn đọc MCAT về tế bào thần kinh còn đủ ý chính. P26.81 giữ nguyên mốc $15{,}0\,\mathrm{V}$ được in trong nguồn dù mốc này không tương thích với $V_{out}=7{,}5\,\mathrm{V}$ theo quan hệ truyền lý tưởng. Lời giải hiện đã chỉ rõ mâu thuẫn thay vì lặng lẽ sửa đề.

## Xác minh

Chạy thành công hai phép tính Python bằng runtime đi kèm môi trường:

- `raw_materials/physics/verify_chapter26_advanced_cross.py`
- `raw_materials/physics/verify_chapter26_61_88.py`

Phạm vi này là đối chiếu độc lập các bài nêu trên. Nó không phải xác nhận toàn bộ chương hoặc toàn bộ khóa học.
