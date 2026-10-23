# Báo Cáo Rà Soát Độc Lập Bản Thảo Lý Thuyết Chương 10 Vật Lý 1

- **Người thực hiện**: Antigravity (Call 1 of 3 — Rà soát độc lập bản thảo lý thuyết mới)
- **Kế hoạch thực hiện**: `docs/agy-plans/2026-10-23-physics1-ch10-parent-review.md`
- **Thời gian thực hiện**: 23/10/2026
- **Môi trường cách ly**: `C:/Users/Ai/.codex/worktrees/physics1-ch10-parent-review-20261023/StudyHub`
- **Phạm vi quyền hạn**: Chỉ ghi duy nhất tệp báo cáo này (`raw_materials/physics/reviews/ch10-agy-parent-draft-review-20261023.md`). Toàn bộ các tệp bài giảng, mã nguồn, catalog và ảnh là chỉ đọc (read-only). Không thực hiện thay đổi bài giảng, không commit, không push, không build dev/full, không cài đặt dependency và không gọi agent phụ.
- **Tuyên bố giới hạn**: Báo cáo dựa trên việc đối chiếu văn bản, kiểm tra mã Python và tệp tĩnh; không kiểm tra hiển thị trình duyệt trực tiếp (browser review) và không khẳng định độ bao phủ 100% tuyệt đối.

---

## 1. Danh Mục Tệp & Nguồn Tư Liệu Được Rà Soát

### 1.1. Danh mục 9 tệp bản thảo lý thuyết (đóng băng, chỉ đọc)
1. `raw_materials/physics/translations/chapter-10/00-mo-dau.md` (Mở đầu chương 10, câu hỏi mở đầu)
2. `raw_materials/physics/translations/chapter-10/01-momen-luc.md` (Mục 10.1 Mômen lực, Ví dụ 10.1, Câu tự kiểm 10.1)
3. `raw_materials/physics/translations/chapter-10/02-momen-luc-va-gia-toc-goc.md` (Mục 10.2 Mômen lực và gia tốc góc của vật rắn, Ví dụ 10.2, Ví dụ 10.3, Câu tự kiểm 10.2)
4. `raw_materials/physics/translations/chapter-10/03-quay-quanh-truc-chuyen-dong.md` (Mục 10.3 Vật rắn quay quanh trục chuyển động, Ví dụ 10.4, Ví dụ 10.5, Ví dụ 10.6, Ví dụ 10.7, Câu tự kiểm 10.3)
5. `raw_materials/physics/translations/chapter-10/04-cong-va-cong-suat-quay.md` (Mục 10.4 Công và công suất trong chuyển động quay, Ví dụ 10.8, Câu tự kiểm 10.4)
6. `raw_materials/physics/translations/chapter-10/05-momen-dong-luong.md` (Mục 10.5 Mômen động lượng, Ví dụ 10.9, Câu tự kiểm 10.5)
7. `raw_materials/physics/translations/chapter-10/06-bao-toan-momen-dong-luong.md` (Mục 10.6 Bảo toàn mômen động lượng, Ví dụ 10.10, Ví dụ 10.11, Ví dụ 10.12, Câu tự kiểm 10.6)
8. `raw_materials/physics/translations/chapter-10/07-con-quay-va-tien-dong.md` (Mục 10.7 Con quay và tiến động, Ví dụ 10.13, Câu tự kiểm 10.7)
9. `raw_materials/physics/translations/chapter-10/17-tom-tat.md` (Tổng kết chương 10, phương trình và hình tổng kết)

### 1.2. Nguồn tư liệu gốc đối chiếu (Source Data)
- **Giáo trình gốc**: Hugh D. Young & Roger A. Freedman, *University Physics with Modern Physics*, 15th Edition, Pearson. Chương 10: *Dynamics of Rotational Motion*, trang 302–325.
- **Trích xuất nguồn đối chiếu**: `raw_materials/physics/review-source/ch10/pdf-0322.txt` đến `pdf-0345.txt` (tương ứng trang PDF 322 đến 345).
- **Bộ tài nguyên hình ảnh**: 47 tệp PNG tại `docs/vat-ly-1/bai-giang/img/young-10/` (gồm các tệp tiền tố `a-` và `b-`).
- **Mô-đun chú thích hình ảnh song ngữ**:
  - `docs/.vitepress/physics1-10-theory-a-image-annotations.mjs`
  - `docs/.vitepress/physics1-10-theory-b-image-annotations.mjs`

---

## 2. Lệnh Xác Minh & Kết Quả Tính Toán (Python Read-Only)

Tất cả lệnh xác minh số học và cú pháp được thực thi trực tiếp bằng lệnh một dòng `C:/Users/Ai/miniconda3/python.exe -X utf8 -c "..."` mà không ghi bất kỳ tệp tạm nào vào đĩa.

### 2.1. Kiểm tra số học 13 ví dụ giảng dạy (Tolerance & Verification)

| Ví dụ | Dữ kiện đầu vào | Đại lượng tính toán | Giá trị sách gốc | Giá trị bản dịch | Giá trị Python độc lập | Sai số | Đánh giá |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **10.1** | $F=900\,\mathrm N, r=0{,}80\,\mathrm m, \theta=19^\circ$ | Cánh tay đòn $l$, mômen $\tau$ | $0{,}76\,\mathrm m; 680\,\mathrm{N\cdot m}$ | $0{,}756\,\mathrm m; 681 \to 680\,\mathrm{N\cdot m}$ | $l=0{,}7564\,\mathrm m; \tau=680{,}77\,\mathrm{N\cdot m}$ | $0{,}0\%$ | Chính xác (dung sai $< 0{,}2\%$) |
| **10.2** | $M=50\,\mathrm{kg}, R=0{,}060\,\mathrm m, F=9{,}0\,\mathrm N$ | Gia tốc góc $\alpha_z$, gia tốc dài $a$, tốc độ $v$ ($s=2\,\mathrm m$) | $6{,}0\,\mathrm{rad/s^2}; 0{,}36\,\mathrm{m/s^2}; 1{,}2\,\mathrm{m/s}$ | $6{,}0\,\mathrm{rad/s^2}; 0{,}36\,\mathrm{m/s^2}; 1{,}2\,\mathrm{m/s}$ | $\alpha=6{,}0; a=0{,}36; v=1{,}2$ | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.3** | Trụ $M$, vật treo $m$ | Gia tốc rơi $a$, lực căng $T$, tốc độ $v$ | $\frac{g}{1+M/(2m)}; \frac{mg}{1+2m/M}; \sqrt{\frac{2gh}{1+M/(2m)}}$ | Đặt $c=\frac{M}{2m}: \frac{g}{1+c}; \frac{mg}{1+2m/M}; \sqrt{\frac{2gh}{1+c}}$ | Đại số trùng khớp | $0{,}0\%$ | Đúng đại số, đổi biến $c$ |
| **10.4** | Yo-yo trụ đặc $M, R$ rơi hạ độ cao $h$ | Động năng $K_2$, tốc độ $v_{\mathrm{cm}}$ | $K_2=\frac{3}{4}Mv^2; v_{\mathrm{cm}}=\sqrt{\frac{4}{3}gh}$ | $K=\frac{3}{4}Mv^2; v=\sqrt{\frac{4}{3}gh}$ | Trùng khớp đại số | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.5** | Lăn không trượt dốc nghiêng cao $h$ | $v_{\mathrm{cm}}=\sqrt{\frac{2gh}{1+c}}$, thứ tự vật lăn | Cầu đặc ($0{,}4$) $>$ Trụ đặc ($0{,}5$) $>$ Vỏ cầu ($0{,}67$) $>$ Trụ rỗng ($1{,}0$) | Trùng khớp hoàn toàn | Trùng khớp | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.6** | Động lực học yo-yo trụ đặc | Gia tốc $a$, lực căng dây $T$ | $a=\frac{2}{3}g; T=\frac{1}{3}Mg$ | $a=\frac{2}{3}g; T=\frac{1}{3}Mg$ | $a=\frac{2}{3}g; T=\frac{1}{3}Mg$ | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.7** | Cầu đặc bowling lăn dốc nghiêng $\beta$ | Gia tốc $a$, ma sát $f$ | $a=\frac{5}{7}g\sin\beta; f=\frac{2}{7}Mg\sin\beta$ | $a=\frac{5}{7}g\sin\beta; f=\frac{2}{7}Mg\sin\beta$ | Trùng khớp | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.8** | $\tau=10\,\mathrm{N\cdot m}, I=2{,}0\,\mathrm{kg\cdot m^2}, t=8{,}0\,\mathrm s$ | $\Delta\theta, W, \omega, K, P_{\mathrm{av}}, P_{\mathrm{max}}$ | $160\,\mathrm{rad}; 1600\,\mathrm J; 40\,\mathrm{rad/s}; 1600\,\mathrm J; 200\,\mathrm W; 400\,\mathrm W$ | $160\,\mathrm{rad}; 1600\,\mathrm J; 40\,\mathrm{rad/s}; 1600\,\mathrm J; 200\,\mathrm W; 400\,\mathrm W$ | $\Delta\theta=160; W=1600; \omega=40; K=1600; P_{\mathrm{av}}=200; P_{\mathrm{max}}=400$ | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.9** | Quạt turbine $I=2{,}5\,\mathrm{kg\cdot m^2}, \omega_z=40t^2$ | $L_z(3\,\mathrm s), \tau_z(3\,\mathrm s)$ | $900\,\mathrm{kg\cdot m^2/s}; 600\,\mathrm{N\cdot m}$ | $900\,\mathrm{kg\cdot m^2/s}; 600\,\mathrm{N\cdot m}$ | $L=900{,}0; \tau=600{,}0$ | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.10** | Giáo sư xoay tạ $5\,\mathrm{kg}$, $I_1 \to I_2$ | $I_1, I_2, \omega_2, K_1, K_2$ | $13; 2{,}6\,\mathrm{kg\cdot m^2}; 15{,}7\,\mathrm{rad/s}; 64\,\mathrm J; 320\,\mathrm J$ | $13; 2{,}6\,\mathrm{kg\cdot m^2}; 15{,}7\,\mathrm{rad/s}; 64\,\mathrm J; 321\,\mathrm J$ | $K_1=64{,}15\,\mathrm J; K_2=320{,}76\,\mathrm J$ | $0{,}3\%$ | Chấp nhận được ($321\,\mathrm J$ do tính từ $5\pi$) |
| **10.11** | Đĩa A ($2\,\mathrm{kg}, 0{,}2\,\mathrm m, 50\,\mathrm{rad/s}$) + Đĩa B ($4\,\mathrm{kg}, 0{,}1\,\mathrm m, 200\,\mathrm{rad/s}$) | $\omega, K_1, K_2, \Delta K$ | $\omega=100\,\mathrm{rad/s}; K_1=450\,\mathrm J; K_2=300\,\mathrm J; \Delta K=150\,\mathrm J$ | $\omega=100\,\mathrm{rad/s}; K_1=450\,\mathrm J; K_2=300\,\mathrm J; \Delta K=150\,\mathrm J$ | $\omega=100{,}0; K_1=450{,}0; K_2=300{,}0; \Delta K=150{,}0$ | $0{,}0\%$ | Trùng khớp tuyệt đối |
| **10.12** | Đạn $10\,\mathrm g, 400\,\mathrm{m/s}$ găm tâm cửa $15\,\mathrm{kg}, 1\,\mathrm m$ | $L, I, \omega, K_1, K_2, t_{90^\circ}$ | $2{,}0\,\mathrm{kg\cdot m^2/s}; 5{,}0025; 0{,}40\,\mathrm{rad/s}; 800\,\mathrm J; 0{,}40\,\mathrm J; 3{,}9\,\mathrm s$ | $2{,}0\,\mathrm{kg\cdot m^2/s}; 0{,}40\,\mathrm{rad/s}; 800\,\mathrm J; 0{,}40\,\mathrm J; 3{,}9\,\mathrm s$ | $\omega=0{,}3998; K_2=0{,}3996; t=3{,}928\,\mathrm s$ | $< 0{,}1\%$ | Trùng khớp |
| **10.13** | Con quay đĩa $R=3\,\mathrm{cm}, r=2\,\mathrm{cm}, T_p=4\,\mathrm s$ | $\Omega, \omega, \text{vòng/phút}, \Omega/\omega$ | $1{,}57\,\mathrm{rad/s}; 280\,\mathrm{rad/s}; 2600\,\mathrm{rpm}; 0{,}6\%$ | $1{,}57\,\mathrm{rad/s}; 280\,\mathrm{rad/s}; 2600\,\mathrm{rpm}; 0{,}6\%$ | $\Omega=1{,}5708; \omega=277{,}28 \to 280; \mathrm{rpm}=2648 \to 2600; \text{tỷ lệ}=0{,}00566$ | $< 0{,}1\%$ | Trùng khớp |

### 2.2. Kiểm tra 7 câu hỏi tự kiểm (Self-Checks)
- **Tự kiểm 10.1**: Lực thẳng đứng $P$ tại đầu thanh nghiêng $\theta$. Đáp án (ii) $PL\cos\theta$. -> Bản dịch phân tích chuẩn xác, đúng đáp án.
- **Tự kiểm 10.2**: Vật trượt trên đệm khí nối vật treo qua ròng rọc có khối lượng. Đáp án $m_2g > T_2 > T_1$. -> Bản dịch giải thích rõ điều kiện mômen và định luật II Newton.
- **Tự kiểm 10.3**: Thay trụ đặc bằng trụ rỗng có cùng khối lượng và bán kính. Đáp án: gia tốc giảm từ $2g/3$ xuống $g/2$; lực căng tăng từ $Mg/3$ lên $Mg/2$. -> Bản dịch giải chi tiết và đầy đủ.
- **Tự kiểm 10.4**: Cùng mômen không đổi tác dụng lên hai trụ quay được 1 vòng. Đáp án (iii) Hai trụ nhận cùng động năng vì cùng công $W = \tau_z \Delta\theta$. -> Bản dịch giải thích chuẩn xác.
- **Tự kiểm 10.5**: Quay bóng buộc dây theo đường tròn nằm ngang với tốc độ không đổi. Đáp án: Động lượng $\vec p$ thay đổi hướng; mômen động lượng $\vec L$ không đổi cả về độ lớn và hướng. -> Bản dịch phân tích rõ ràng.
- **Tự kiểm 10.6**: Băng ở các cực tan làm nước phân bố về xích đạo. Đáp án: Mômen quán tính tăng làm tốc độ góc giảm $\implies$ Độ dài ngày tăng. -> Bản dịch phân tích đúng nguyên lý bảo toàn mômen động lượng.
- **Tự kiểm 10.7**: Khối lượng bánh đà con quay tăng gấp đôi, giữ nguyên bán kính và tốc độ tự quay. Đáp án (iii) Tốc độ tiến động $\Omega$ không đổi vì trọng lượng $w$ và mômen quán tính $I$ cùng tăng gấp đôi. -> Bản dịch giải thích chuẩn xác.

---

## 3. Tổng Hợp Các Phát Hiện Rà Soát Theo Mức Độ Ưu Tiên

### 3.1. Nhóm Ưu Tiên 1 (P1 — Sai sót cấu trúc kỹ thuật & Liên kết tài nguyên)

#### P1.1: Đường dẫn hình ảnh không nhất quán và sai tương đối trên toàn bộ 9 tệp bản dịch
- **Vị trí**:
  - `00-mo-dau.md:3`: `./img/young-10/a-mo-dau.png`
  - `01-momen-luc.md:5, 19, 41, 55, 63, 89`: `../img/young-10/...`
  - `02-momen-luc-va-gia-toc-goc.md:5, 11, 44, 68, 97, 140`: `../img/young-10/...`
  - `03-quay-quanh-truc-chuyen-dong.md:5, 17, 67, 81, 93, 99, 127, 166, 174, 206, 242, 246`: `../img/young-10/...`
  - `04-cong-va-cong-suat-quay.md:5, 52`: `../img/young-10/...`
  - `05-momen-dong-luong.md:21, 49, 66, 68, 72`: `../img/young-10/...`
  - `06-bao-toan-momen-dong-luong.md:33, 43, 75, 114`: `../img/young-10/...`
  - `07-con-quay-va-tien-dong.md:5, 23, 31, 43, 79`: `../img/young-10/...`
  - `17-tom-tat.md:17, 29, 41, 56, 70, 72`: `./img/young-10/...`
- **Bằng chứng**:
  - Thư mục hình ảnh thực tế được lưu tại `docs/vat-ly-1/bai-giang/img/young-10/`.
  - Bên trong thư mục nguồn `raw_materials/physics/translations/` không có thư mục con `img/young-10/`. Do đó, cả hai dạng đường dẫn `./img/young-10/...` và `../img/young-10/...` đều không trỏ tới ảnh khi xem độc lập trong thư mục `raw_materials`.
  - Hơn nữa, có sự xung đột nội bộ giữa các tệp bản dịch: Tệp `00` và `17` dùng `./img/young-10/...`, trong khi các tệp `01` đến `07` lại dùng `../img/young-10/...`. Nếu ghép các tệp này vào bài giảng chính thức `docs/vat-ly-1/bai-giang/10-dong-luc-hoc-quay.md`, toàn bộ các đường dẫn `../img/young-10/...` sẽ bị hỏng hiển thị (404 Not Found) vì từ `docs/vat-ly-1/bai-giang/` đường dẫn hợp lệ phải là `./img/young-10/...` hoặc `img/young-10/...`.
- **Đề xuất khắc phục**: Khi tổng hợp thành bài giảng chính thức, quy chuẩn toàn bộ 47 liên kết ảnh về định dạng `./img/young-10/<tên-ảnh>.png`.

#### P1.2: Bỏ sót bản chất vật lý của ví dụ sinh học cây cỏ lăn (Rolling Friction)
- **Vị trí**: `03-quay-quanh-truc-chuyen-dong.md:244–246`
- **Trang sách gốc**: Trang 314 (`pdf-0334.txt`), khung *BIO APPLICATION: Rolling for Reproduction*.
- **Bằng chứng**:
  - Trong sách gốc, ví dụ cây cỏ lăn (*Russian thistle / Kali tragus / tumbleweed*) được đặt ngay trong mục nhỏ **Cản lăn (Rolling Friction)** để minh họa: Vì cây cỏ lăn có cấu trúc mềm xốp, dễ bị biến dạng khi tiếp xúc với mặt đất, nó chịu **lực cản lăn rất lớn** (*substantial rolling friction*) và sẽ nhanh chóng dừng lại nếu không có gió liên tục đẩy đi.
  - Bản dịch hiện tại chỉ viết: *"Một cây cỏ lăn sau khi khô và tách khỏi gốc có thể được gió đẩy đi bằng chuyển động lăn. Hình dạng phân nhánh giúp nó lăn và phát tán hạt trên mặt đất."*
  - Đoạn văn này làm mất hoàn toàn mối liên hệ vật lý với lực cản lăn và sự tiêu tán cơ năng do biến dạng, khiến ví dụ trở thành một mẩu thông tin sinh học thuần túy không phục vụ bài học.
- **Đề xuất khắc phục**: Bổ sung phân tích vật lý: Nêu rõ vì cây cỏ lăn dễ biến dạng nên chịu lực cản lăn đáng kể từ mặt đất, dẫn đến cơ năng suy giảm nhanh và cây sẽ dừng lại ngay khi gió ngừng thổi.

#### P1.3: Đổi ký hiệu đột ngột trong phép chứng minh động năng ($\vec u \to \vec v_{\mathrm{cm}}$)
- **Vị trí**: `03-quay-quanh-truc-chuyen-dong.md:11–56`
- **Trang sách gốc**: Trang 309 (`pdf-0329.txt`), Eq (10.8)–(10.10).
- **Bằng chứng**:
  - Tại dòng 11, tác giả bản dịch định nghĩa vận tốc khối tâm bằng ký hiệu $\vec u$ và vận tốc tương đối là $\vec w_i$: *"Gọi $\vec u$ là vận tốc khối tâm và $\vec w_i$ là vận tốc phần tử $i$ tương đối với khối tâm... Vận tốc trong hệ quán tính là $\vec v_i = \vec u + \vec w_i$."*
  - Biến đổi tiếp tục dùng $u$: $K = \frac{1}{2} M u^2 + \vec u \cdot \vec P' + K'$.
  - Nhưng ngay tại kết luận (dòng 54), công thức (10.8) lại viết:
    $$K = \tfrac{1}{2} M v_{\mathrm{cm}}^2 + \tfrac{1}{2} I_{\mathrm{cm}} \omega^2$$
    mà không có dòng chuyển tiếp quy ước $u \equiv v_{\mathrm{cm}}$.
  - Trong sách gốc Young & Freedman, ký hiệu $\vec v_{\mathrm{cm}}$ và $\vec v'_i$ được giữ đồng nhất từ đầu đến cuối. Việc tự ý đổi sang $\vec u$ rồi nhảy ngược lại $\vec v_{\mathrm{cm}}$ tạo ra sự thiếu liền mạch cho sinh viên.
- **Đề xuất khắc phục**: Dùng đồng nhất ký hiệu chuẩn mực $\vec v_{\mathrm{cm}}$ và $\vec v'_i$ (hoặc bổ sung ghi chú $u = v_{\mathrm{cm}}$).

---

### 3.2. Nhóm Ưu Tiên 2 (P2 — Chuẩn mực toán học & Ngắt dòng công thức)

#### P2.1: Lạm dụng môi trường `aligned` để bẻ gãy các công thức ngắn (Vi phạm Quy tắc 8)
- **Vị trí & Bằng chứng**:
  1. `01-momen-luc.md:71–78`:
     $$\begin{aligned} l&=r\sin109^\circ\\ &\approx0{,}756\,\mathrm m,\\ \tau&=Fl\\ &\approx681\,\mathrm{N\cdot m}. \end{aligned}$$
     Hai phép tính ngắn $l = r\sin 109^\circ \approx 0{,}76\,\mathrm m$ và $\tau = Fl \approx 680\,\mathrm{N\cdot m}$ bị bẻ đôi thành 4 dòng ngắn cụt cỡn, đồng thời căn lề ép hai đại lượng vật lý khác hẳn nhau ($l$ và $\tau$) vào chung một cột dấu bằng.
  2. `03-quay-quanh-truc-chuyen-dong.md:108–111`:
     $$\begin{aligned} K&=\tfrac12Mv^2+\tfrac14Mv^2\\ &=\tfrac34Mv^2. \end{aligned}$$
     Biểu thức số học chỉ có một dấu bằng và vừa vặn trên 1 dòng đơn, bọc vào `aligned` làm gãy khúc công thức.
  3. `03-quay-quanh-truc-chuyen-dong.md:193–196` & `225–228`:
     Các hệ kết quả nghiệm đơn lẻ như $a = \frac{2}{3}g$, $T = \frac{1}{3}Mg$ hay $a = \frac{5}{7}g\sin\beta$, $f = \frac{2}{7}Mg\sin\beta$ bị đóng khung trong `aligned` không cần thiết.
  4. `04-cong-va-cong-suat-quay.md:81–86` & `92–95`:
     $\Delta\theta = \frac{1}{2}\alpha_z t^2 = 160\,\mathrm{rad}$ và $\omega_z = \alpha_z t = 40\,\mathrm{rad/s}$ bị bẻ thành 4 dòng ngắn vụn.
  5. `05-momen-dong-luong.md:54–57`:
     $L_z = \sum_{i=1}^N L_{iz} = I\omega_z$ bị bẻ thành 2 dòng ngắn.
  6. `06-bao-toan-momen-dong-luong.md:52–57` & `129–134`:
     Biểu thức tính mômen quán tính $I_1, I_2$ và $I_{\mathrm{cửa}}, I_{\mathrm{đạn}}$ bị ngắt dòng giữa chừng sau dấu bằng.
  7. `17-tom-tat.md:48–51`:
     Hai định nghĩa độc lập $W = \int \tau_z d\theta$ và $P = \tau_z \omega_z$ bị bọc vào chung `aligned`.
- **Quy tắc vi phạm**: Quy tắc 8 (*Chuẩn mực toán học & Quy tắc ngắt dòng*): *"Nếu một công thức hoặc phương trình vừa vặn trên một dòng... Bắt buộc giữ nguyên trên 1 dòng đơn giản trong `$$...$$`. Tuyệt đối không bọc vào `\begin{aligned}` rồi ngắt vụn thành các dòng ngắn cụt cỡn ở giữa trang."*
- **Đề xuất khắc phục**: Chuyển các công thức vừa vặn trên 1 dòng thành biểu thức hiển thị đơn giản `$$A = B = C$$`. Với các cặp kết quả, đặt trên một dòng cách nhau bởi dấu phẩy hoặc tách thành các khối công thức độc lập.

#### P2.2: Gộp nhãn phương trình dồn cục (`\tag{10.14–10.16}` và `\tag{10.17–10.18}`)
- **Vị trí**:
  - `03-quay-quanh-truc-chuyen-dong.md:187`: `\end{aligned} \tag{10.14–10.16}`
  - `03-quay-quanh-truc-chuyen-dong.md:219`: `\end{aligned} \tag{10.17–10.18}`
- **Bằng chứng**:
  - Trong sách gốc, mỗi phương trình mang một số hiệu riêng: (10.14) cho phương trình tịnh tiến, (10.15) cho phương trình quay quanh khối tâm, và (10.16) cho điều kiện liên kết không trượt.
  - Việc gán nhãn dồn `\tag{10.14–10.16}` vào một khối `aligned` khiến MathJax / KaTeX chỉ hiển thị duy nhất một nhãn gộp ở bên phải dòng cuối, làm mất tính định danh riêng của từng định luật khi người đọc muốn trích dẫn lại.
- **Đề xuất khắc phục**: Tách các phương trình hoặc tham chiếu trực tiếp theo tên gọi vật lý (phương trình tịnh tiến, phương trình quay, điều kiện lăn không trượt).

#### P2.3: Bỏ qua bước giải thích trung gian trong định lý công - động năng quay
- **Vị trí**: `04-cong-va-cong-suat-quay.md:35–42`
- **Trang sách gốc**: Trang 315 (`pdf-0335.txt`), biến đổi $\tau_z d\theta = (I\alpha_z) d\theta = I \frac{d\omega_z}{dt} d\theta = I \frac{d\theta}{dt} d\omega_z = I\omega_z d\omega_z$.
- **Bằng chứng**:
  - Sách gốc Young & Freedman trình bày tường minh việc tráo vi phân $\frac{d\theta}{dt} = \omega_z$ để người học hiểu tại sao $\alpha_z d\theta$ lại biến thành $\omega_z d\omega_z$.
  - Bản dịch viết nhảy bước: *"Dùng đạo hàm theo chuỗi khi vận tốc góc khác không: $\alpha_z\,d\theta=\omega_z\,d\omega_z$. Quan hệ tích phân cũng dùng được qua thời điểm vận tốc góc bằng không bằng cách xét liên tục theo thời gian."*
  - Việc thêm điều kiện *"khi vận tốc góc khác không"* là không cần thiết về mặt vi phân (đẳng thức $d\theta \frac{d\omega}{dt} = \omega d\omega$ luôn đúng), đồng thời làm sinh viên hoang mang tưởng rằng công thức vi phân bị gián đoạn tại $\omega = 0$.
- **Đề xuất khắc phục**: Khai triển đầy đủ chuỗi vi phân $\alpha_z d\theta = \frac{d\omega_z}{dt} d\theta = \frac{d\theta}{dt} d\omega_z = \omega_z d\omega_z$ theo đúng nguyên tắc "Mở bước khó" (Quy tắc 4).

#### P2.4: Dùng ký hiệu đạo hàm chấm Newton ($\dot{\vec r}, \dot{\vec p}$) trong chứng minh vectơ tổng quát
- **Vị trí**: `05-momen-dong-luong.md:30–33`
- **Trang sách gốc**: Trang 317 (`pdf-0336.txt`).
- **Bằng chứng**:
  - Tác giả viết: $\frac{d\vec L}{dt} = \dot{\vec r}\times\vec p + \vec r\times\dot{\vec p}$.
  - Ký hiệu chấm trên đầu ($\dot{\vec r}$) là ký hiệu của cơ học giải tích nâng cao. Giáo trình Vật lý đại cương 1 (Young & Freedman và chương trình chuẩn UET) sử dụng đồng nhất ký hiệu Leibniz $\frac{d\vec r}{dt}$ và $\frac{d\vec p}{dt}$.
- **Đề xuất khắc phục**: Chuyển thành $\frac{d\vec L}{dt} = \left(\frac{d\vec r}{dt}\times\vec p\right) + \left(\vec r\times\frac{d\vec p}{dt}\right)$.

---

### 3.3. Nhóm Ưu Tiên 3 (P3 — Văn phong sư phạm, Thuật ngữ song ngữ & Trải nghiệm sinh viên)

#### P3.1: Hoàn toàn thiếu vắng thuật ngữ tiếng Anh đối chiếu (English Academic Glosses)
- **Vị trí**: Toàn bộ 9 tệp bản thảo.
- **Bằng chứng**:
  - Qua rà soát tự động toàn bộ văn bản, không có bất kỳ thuật ngữ chuyên môn nào được mở ngoặc tiếng Anh đối chiếu.
  - Các thuật ngữ trọng tâm của môn học như:
    - *Mômen lực (torque)*
    - *Cánh tay đòn (lever arm / moment arm)*
    - *Đường tác dụng (line of action)*
    - *Gia tốc góc (angular acceleration)*
    - *Mômen quán tính (moment of inertia)*
    - *Mômen động lượng (angular momentum)*
    - *Lăn không trượt (rolling without slipping)*
    - *Cản lăn (rolling friction)*
    - *Tiến động (precession)*
    - *Chương động (nutation)*
    - *Bánh đà (flywheel)*
    - *Đĩa ly hợp (clutch plate)*
  - Việc thiếu thuật ngữ đối chiếu khiến sinh viên khó khăn trong việc tra cứu tài liệu quốc tế hoặc làm các bài tập kiểm tra chuẩn tiếng Anh của UET.
- **Đề xuất khắc phục**: Bổ sung thuật ngữ tiếng Anh học thuật trong ngoặc đơn ở lần đầu tiên thuật ngữ xuất hiện trong mỗi phần.

#### P3.2: Đặt thêm ẩn phụ không cần thiết $c = M/(2m)$ trong Ví dụ 10.3
- **Vị trí**: `02-momen-luc-va-gia-toc-goc.md:113–133`
- **Bằng chứng**:
  - Tác giả đặt $c = M/(2m)$ rồi viết $a = \frac{g}{1+c}$, $v = \sqrt{\frac{2gh}{1+c}}$, nhưng biểu thức lực căng dây lại viết $T = \frac{mg}{1+2m/M}$ (không dùng $c$).
  - Trong sách gốc, công thức được giữ trực diện theo $M$ và $m$: $a = \frac{g}{1 + M/(2m)}$. Việc đặt thêm biến $c$ cục bộ làm công thức mất đi tính tường minh của các tham số vật lý ban đầu.
- **Đề xuất khắc phục**: Trình bày trực tiếp $a = \frac{g}{1 + M/(2m)}$ và $v = \sqrt{\frac{2gh}{1 + M/(2m)}}$.

#### P3.3: Chưa khai triển tường minh ký hiệu dồn $\sum$ trước khi viết tắt (Vi phạm Quy tắc 9)
- **Vị trí**:
  - `02-momen-luc-va-gia-toc-goc.md:37–38`: $\tau_z = \sum_{i=1}^N \tau_{iz}$; $I = \sum_{i=1}^N m_i r_i^2$.
  - `03-quay-quanh-truc-chuyen-dong.md:39–41`: $M = \sum_{i=1}^N m_i$; $\vec P' = \sum_{i=1}^N m_i \vec w_i$; $K' = \sum_{i=1}^N R_i$.
  - `05-momen-dong-luong.md:55`: $L_z = \sum_{i=1}^N L_{iz}$.
- **Bằng chứng**:
  - Dù tác giả có nêu trực giác hai hạt ($k=2$) trong văn xuôi, nhưng trong khối công thức hiển thị, tổng $N$ hạt lại được viết ngay dưới dạng viết tắt dồn $\sum_{i=1}^N$ mà không khai triển dạng tường minh $\dots + \dots$.
  - Quy tắc 9 yêu cầu: *"Mọi công thức chứa ký hiệu viết tắt dồn ($\sum$, $\prod$, ...) bắt buộc phải được khai triển tường minh ít nhất một lần khi giới thiệu: $\sum_{i=1}^k \theta_i = \theta_1 + \theta_2 + \dots + \theta_k$."*
- **Đề xuất khắc phục**: Khai triển tường minh một lần:
  $$I = \sum_{i=1}^N m_i r_i^2 = m_1 r_1^2 + m_2 r_2^2 + \dots + m_N r_N^2,$$
  $$L_z = \sum_{i=1}^N L_{iz} = L_{1z} + L_{2z} + \dots + L_{Nz} = I\omega_z.$$

#### P3.4: Tệp mở đầu chương (`00-mo-dau.md`) thiếu mục tiêu học tập và danh mục ôn tập kiến thức nền
- **Vị trí**: `00-mo-dau.md:20`
- **Trang sách gốc**: Trang 302 (`pdf-0322.txt`).
- **Bằng chứng**:
  - Trang 302 trong sách gốc có hai khung sư phạm quan trọng:
    1. *Learning Outcomes* (Mục tiêu học tập 10.1 đến 10.7).
    2. *You'll need to review* (Kiến thức cần ôn tập: Tích có hướng 1.10, Định luật II Newton 5.2, Công và định lý động năng 6.1–6.4, Nội lực và khối tâm 8.2–8.5, Động học quay và định lý Steiner 9.1–9.5).
  - Tệp `00-mo-dau.md` chỉ có đoạn văn tóm tắt ngắn gọn cuối bài, chưa có danh sách mục tiêu cụ thể và liên kết kiến thức nền cho sinh viên chuẩn bị trước khi vào bài.
- **Đề xuất khắc phục**: Bổ sung bảng *Mục tiêu học tập* và hộp *Kiến thức nền cần chuẩn bị*.

---

## 4. Rà Soát Tính Tuân Thủ Các Quy Chuẩn Sư Phạm Dự Án

| Quy chuẩn kiểm tra | Trạng thái | Ghi chú & Chi tiết kiểm tra |
| :--- | :---: | :--- |
| **Chủ quyền bài giảng (Quy tắc 6)** | **ĐẠT** | Không có các cụm từ bị cấm (*“theo sách”*, *“giáo trình dùng”*, *“nguyên tác”*, *“bản dịch”*). Văn phong độc lập, đĩnh đạc. |
| **Văn phong giáo sư & Trực giác sư phạm (Quy tắc 7)** | **ĐẠT** | Giảng giải xuất phát từ thực tế, giải thích cơ chế vật lý tự nhiên, không dùng khẩu hiệu sáo rỗng AI. |
| **Không nghĩ thành tiếng trong lời giải (Quy tắc 19)** | **ĐẠT** | Lời giải cả 13 ví dụ dứt khoát, mạch lạc, không có câu tự độc thoại kiểu *“Khoan đã”*, *“À không”*. |
| **Không bịa đặt tần suất lỗi sinh viên (Quy tắc 20)** | **ĐẠT** | Không có các câu thống kê cảm tính như *“Sinh viên rất hay nhầm”*, *“Bẫy thi cử phổ biến”*. |
| **Quy tắc viết hoa sau dấu hai chấm (Quy tắc 12)** | **ĐẠT (100%)** | Toàn bộ các câu sau dấu `:` trong văn xuôi, tiêu đề, đề mục và chú thích đều viết hoa chữ cái đầu. Không có trường hợp vi phạm. |
| **Hạn chế dấu gạch ngang dài em-dash (Quy tắc 16)** | **ĐẠT (100%)** | Không lạm dụng dấu `—` trong văn xuôi. |
| **Hạn chế dấu chấm phẩy trong văn xuôi (Quy tắc 10)** | **ĐẠT (100%)** | Không có dấu `;` trong văn xuôi; các vế câu được nối bằng từ nối tiếng Việt chuẩn mực hoặc tách câu đơn. |
| **Cú pháp trị tuyệt đối và chuẩn (Quy tắc 18)** | **ĐẠT** | Sử dụng trực tiếp `|d\vec L|` và `L`, không có `\vert` hay `\Vert`. |
| **Quy tắc ngắt dòng toán học (Quy tắc 8)** | **CẦN SỬA** | Còn nhiều vị trí lạm dụng `aligned` cho công thức ngắn hoặc bẻ đôi công thức một dòng (xem phát hiện P2.1). |
| **Khai triển tường minh tổng dồn (Quy tắc 9)** | **CẦN SỬA** | Thiếu dạng khai triển tường minh $\dots + \dots$ cho ký hiệu $\sum$ (xem phát hiện P3.3). |

---

## 5. Các Hạng Mục Chưa Thực Hiện Rà Soát (Missing Review Items)

1. **Hiển thị giao diện trình duyệt thực tế (Browser Rendering / Visual CSS)**: Không chạy dev server hoặc trình duyệt đồ họa để kiểm tra responsive, hộp popover chú thích hoặc hiển thị MathJax thực tế trên màn hình mobile.
2. **Quy trình build VitePress toàn cục**: Tuân thủ tuyệt đối quy định không chạy `npm run ci:build` trên máy cục bộ để tránh nghẽn RAM/CPU; khâu build được ủy thác tự động cho GitHub Actions khi mã được đẩy lên nhánh chính.
3. **Bộ bài tập cuối chương 10 (End-of-Chapter Exercises 10.1 – 10.90)**: Phạm vi rà soát này chỉ giới hạn nghiêm ngặt ở phần lý thuyết (Theory: 7 mục, 13 ví dụ bài giảng, 7 câu tự kiểm và tổng kết chương). Phần lời giải bài tập cuối chương sẽ thuộc một quy trình rà soát riêng biệt khi hoàn thành.

---

## 6. Kết Luận & Đánh Giá Tổng Thể

- **Đánh giá chung**: Bản thảo lý thuyết Chương 10 do Codex biên soạn đạt chất lượng học thuật và sư phạm rất cao. Về mặt số học và vật lý học, toàn bộ 13 ví dụ và 7 câu hỏi tự kiểm đều chính xác tuyệt đối, lập luận chặt chẽ và không có sai số tính toán. Văn phong tiếng Việt tự nhiên, đĩnh đạc, tuân thủ xuất sắc các quy định nghiêm ngặt về chủ quyền bài giảng, dấu câu và viết hoa sau dấu hai chấm.
- **Các điểm cần hoàn thiện trước khi xuất bản**:
  1. Chuẩn hóa đường dẫn tương đối của 47 hình ảnh về `./img/young-10/` để tránh lỗi ảnh vỡ khi tích hợp vào trang bài giảng chính.
  2. Bổ sung giải thích vật lý về lực cản lăn ở ví dụ cây cỏ lăn trong Mục 10.3.
  3. Làm sạch các khối công thức toán: Tháo bỏ môi trường `aligned` ở các công thức ngắn một dòng để tránh gãy vụn hiển thị trên màn hình nhỏ.
  4. Bổ sung thuật ngữ tiếng Anh đối chiếu trong ngoặc đơn cho các khái niệm vật lý cốt lõi.
