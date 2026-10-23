# Báo cáo thẩm định kỹ thuật: Physics 1 Chương 20 Lý thuyết A (physics1-20-theory-a-20261022)

- **Ngày thực hiện**: 2026-10-22
- **Tác vụ**: Biên soạn, dịch giải, trích xuất tài nguyên hình ảnh và thẩm định độc lập Chương 20 Lý thuyết A (Young & Freedman, ấn bản 15, các trang PDF 662–671, tương ứng trang in 642–651).
- **Môi trường làm việc**: `C:\Users\Ai\.codex\worktrees\physics1-20-theory-a-20261022\StudyHub`

---

## 1. Danh mục các tệp thuộc quyền sở hữu độc quyền (Owned Paths)

Tất cả các tệp sau đã được tạo lập, hoàn thiện và kiểm thử hoàn chỉnh theo đúng kế hoạch:

1. `raw_materials/physics/translations/chapter-20/00-mo-dau.md`: Mở đầu chương 20, câu hỏi khởi động, mục tiêu học tập (20.1–20.8) và kiến thức nền tảng cần ôn tập.
2. `raw_materials/physics/translations/chapter-20/01-chieu-cua-qua-trinh-nhiet-dong.md`: Mục 20.1 về quá trình thuận nghịch, không thuận nghịch, sự mất trật tự và Câu hỏi kiểm tra hiểu biết 20.1.
3. `raw_materials/physics/translations/chapter-20/02-dong-co-nhiet.md`: Mục 20.2 về động cơ nhiệt, chu trình, nguồn nóng/lạnh, hiệu suất nhiệt, ứng dụng sinh học, Chiến lược giải bài tập 20.1, Ví dụ 20.1 (5 phần a–e) và Câu hỏi kiểm tra hiểu biết 20.2.
4. `raw_materials/physics/translations/chapter-20/03-dong-co-dot-trong.md`: Mục 20.3 về động cơ xăng 4 kỳ, chu trình Otto lý tưởng, chứng minh hiệu suất nhiệt $e = 1 - 1/r^{\gamma-1}$, hiện tượng kích nổ, chu trình Diesel lý tưởng và Câu hỏi kiểm tra hiểu biết 20.3.
5. `raw_materials/physics/translations/chapter-20/04-may-lanh.md`: Mục 20.4 về máy làm lạnh, hệ số hiệu năng $K$, chu trình làm lạnh cơ học thực tế 5 giai đoạn, máy điều hòa không khí, bơm nhiệt, nghịch lý máy lạnh không tốn công và Câu hỏi kiểm tra hiểu biết 20.4. Dừng chính xác trước Mục 20.5 trên trang PDF 671.
6. `scripts/prepare-physics1-20-theory-a-assets.py`: Mã nguồn trích xuất 12 hình ảnh gốc từ PDF bằng PyMuPDF với tỉ lệ scale 3.0, không có kênh alpha, giữ nguyên pixel và nhãn gốc.
7. `docs/.vitepress/physics1-20-theory-a-image-annotations.mjs`: Xuất `physics1Chapter20TheoryAImageAnnotations` gồm 12 mục khớp chính xác nhãn tiếng Anh sang tiếng Việt.
8. `raw_materials/physics/verify_chapter20_theory_a.py`: Bộ kiểm thử Python kiểm tra toàn bộ số học, đại số dẫn xuất, so khớp mảng pixel RGB và schema nhãn chú thích.
9. `raw_materials/physics/reviews/ch20-agy-theory-a-review.md`: Bản báo cáo thẩm định kỹ thuật này.
10. Danh mục 12 ảnh PNG phẳng tại `docs/vat-ly-1/bai-giang/img/young-20/a-*.png`.

---

## 2. Phạm vi nguồn và đối chiếu đơn vị bài giảng

| Đơn vị nguồn | Trang PDF | Trang in | Nội dung chi tiết | Tệp đầu ra |
| :--- | :--- | :--- | :--- | :--- |
| Mở đầu chương | 662 | 642 | Bối cảnh chiều một chiều của nhiệt, cơ năng $\to$ nhiệt, entropy, ảnh mở đầu dung nham, câu hỏi mở đầu, mục tiêu 20.1–20.8, điều kiện tiên quyết | `00-mo-dau.md` |
| Mục 20.1 | 662–664 | 642–644 | Quá trình thuận nghịch và không thuận nghịch, sự mất trật tự, Hình 20.1, Câu hỏi kiểm tra hiểu biết 20.1 | `01-chieu-cua-qua-trinh-nhiet-dong.md` |
| Mục 20.2 | 664–667 | 644–647 | Động cơ nhiệt, nguồn nóng/lạnh, hệ thức $W=Q$, hiệu suất nhiệt (20.1)–(20.4), Hình 20.2, 20.3, Ứng dụng sinh học, Chiến lược 20.1, Ví dụ 20.1 (a–e), Hình 20.4, Câu hỏi kiểm tra 20.2 | `02-dong-co-nhiet.md` |
| Mục 20.3 | 667–669 | 647–649 | Động cơ đốt trong 4 kỳ (Hình 20.5), chu trình Otto (Hình 20.6), chứng minh $e$ (20.5)–(20.6), kích nổ & octan, chu trình Diesel (Hình 20.7), Câu hỏi kiểm tra 20.3 | `03-dong-co-dot-trong.md` |
| Mục 20.4 | 669–671 | 649–651 | Máy làm lạnh (Hình 20.8), hệ thức (20.7)–(20.8), hệ số hiệu năng $K$ (20.9), chu trình 5 bước (Hình 20.9), điều hòa & bơm nhiệt (Hình 20.10), máy lạnh không tốn công, Câu hỏi kiểm tra 20.4 | `04-may-lanh.md` |

> [!NOTE]
> Phạm vi bài giảng dừng lại chính xác tại dòng phân cách trước tiêu đề Mục 20.5 (*20.5 THE SECOND LAW OF THERMODYNAMICS*) trên trang PDF 671, hoàn toàn tuân thủ ranh giới phân công của phần Theory A.

---

## 3. Sổ cái kiểm chứng số học và đại số (Numerical Ledger)

Toàn bộ các phép tính trong các ví dụ và câu hỏi kiểm tra đã được tính toán độc lập và kiểm chứng bằng mã nguồn Python trong `verify_chapter20_theory_a.py`:

| Trường hợp | Đầu vào (Dữ liệu gốc) | Biểu thức tính toán | Kết quả tính toán | Giá trị trong bài | Đơn vị | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ví dụ 20.1 (a)** | $W = 2000\,\mathrm{J}$, $Q_H = 10{,}000\,\mathrm{J}$ | $e = W/Q_H$ | $0{,}20$ | $0{,}20$ ($20\%$) | Không thứ nguyên | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (b)** | $W = 2000\,\mathrm{J}$, $Q_H = 10{,}000\,\mathrm{J}$ | $Q_C = W - Q_H$ | $-8000$ | $-8000$ (thải $8000$) | $\mathrm{J}$ | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (c)** | $W = 2000\,\mathrm{J}$, $f = 25\,\mathrm{s^{-1}}$ | $P = W \cdot f$ | $50{,}000$ | $50{,}000$ ($50\,\mathrm{kW}$) | $\mathrm{W}$ | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (c)** | $P = 50{,}000\,\mathrm{W}$, $1\,\mathrm{hp} = 746\,\mathrm{W}$ | $P_{\mathrm{hp}} = P / 746$ | $67{,}024$ | $67$ | $\mathrm{hp}$ | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (d)** | $Q_H = 10{,}000\,\mathrm{J}$, $L_c = 5{,}0 \times 10^4\,\mathrm{J/g}$ | $m = Q_H / L_c$ | $0{,}20$ | $0{,}20$ | $\mathrm{g}$ | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (e)** | $m = 0{,}20\,\mathrm{g}$, $f = 25\,\mathrm{s^{-1}}$ | $m_s = m \cdot f$ | $5{,}0$ | $5{,}0$ | $\mathrm{g/s}$ | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (e)** | $m_s = 5{,}0\,\mathrm{g/s}$, $t = 3600\,\mathrm{s}$ | $m_h = m_s \cdot 3600$ | $18{,}000$ | $18{,}000$ ($18$) | $\mathrm{g/h}$ ($\mathrm{kg/h}$) | ĐẠT (khớp 100%) |
| **Ví dụ 20.1 (đánh giá)** | $m_h = 18{,}000\,\mathrm{g/h}$, $\rho = 0{,}70\,\mathrm{g/cm^3}$ | $V_h = m_h / \rho$ | $25{,}714$ | $25{,}7$ | $\mathrm{L/h}$ | ĐẠT (khớp 100%) |
| **Kiểm tra 20.2 (i)** | $Q_H = 5000\,\mathrm{J}$, $Q_C = -4500\,\mathrm{J}$ | $e = (5000-4500)/5000$ | $0{,}100$ | $0{,}100$ ($10{,}0\%$) | Không thứ nguyên | ĐẠT (khớp 100%) |
| **Kiểm tra 20.2 (ii)** | $Q_H = 25{,}000\,\mathrm{J}$, $W = 2000\,\mathrm{J}$ | $e = 2000/25000$ | $0{,}080$ | $0{,}080$ ($8{,}0\%$) | Không thứ nguyên | ĐẠT (khớp 100%) |
| **Kiểm tra 20.2 (iii)** | $W = 400\,\mathrm{J}$, $|Q_C| = 2800\,\mathrm{J}$ | $e = 400/(400+2800)$ | $0{,}125$ | $0{,}125$ ($12{,}5\%$) | Không thứ nguyên | ĐẠT (khớp 100%) |
| **Kiểm tra 20.2 (thứ tự)** | $e_{\text{(iii)}} = 12{,}5\%$, $e_{\text{(i)}} = 10{,}0\%$, $e_{\text{(ii)}} = 8{,}0\%$ | Thứ tự giảm dần | (iii) > (i) > (ii) | (iii), (i), (ii) | Thứ bậc | ĐẠT (khớp 100%) |
| **Chu trình Otto** | $r = 8$, $\gamma = 1{,}4$ | $e = 1 - 1/8^{0{,}4}$ | $0{,}5647$ | $\approx 0{,}56$ ($56\%$) | Không thứ nguyên | ĐẠT (khớp 100%) |

---

## 4. Bảng kiểm kê trích xuất hình ảnh (Image Crop Ledger)

Tất cả 12 hình ảnh được cắt trực tiếp từ tệp PDF gốc `raw_materials/physics/source/young-freedman-15.pdf` với hệ số phóng đại `SCALE = 3.0` và cờ `alpha = False`. Đã kiểm chứng so khớp từng pixel (độ sai khác tối đa `max_diff = 0` so với dữ liệu nguồn tươi):

| Tên tệp ảnh | Trang PDF | Bounding Box $(x_0, y_0, x_1, y_1)$ | Kích thước (px) | Số pixel đồ họa (non-white) | Kiểm tra biên |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a-mo-dau-20.png` | 662 | $(210, 0, 648, 245)$ | $1314 \times 735$ | $2{,}887{,}387$ | Biên ảnh chụp tự nhiên |
| `a-hinh-20-01.png` | 663 | $(85, 58, 435, 215)$ | $1050 \times 471$ | $221{,}234$ | Biên trắng 100%, đủ 2 panel (a) và (b) |
| `a-hinh-20-02.png` | 664 | $(36, 402, 192, 642)$ | $468 \times 720$ | $996{,}578$ | Biên ảnh chụp giao thông, không cắt chữ |
| `a-hinh-20-03.png` | 665 | $(465, 205, 605, 380)$ | $420 \times 525$ | $224{,}282$ | Bao trọn nguồn nóng $T_H$, nguồn lạnh $T_C$, $W$ |
| `a-ung-dung-01.png` | 665 | $(455, 596, 648, 742)$ | $579 \times 438$ | $740{,}216$ | Ảnh vận động viên đạp xe, đủ khung |
| `a-hinh-20-04.png` | 666 | $(36, 600, 192, 745)$ | $468 \times 435$ | $15{,}903$ | Đủ sơ đồ dòng năng lượng Ví dụ 20.1 |
| `a-hinh-20-05.png` | 667 | $(76, 525, 612, 745)$ | $1608 \times 660$ | $603{,}251$ | Biên trắng 100%, đủ 5 kỳ nạp/nén/cháy/công/xả |
| `a-hinh-20-06.png` | 668 | $(36, 94, 195, 290)$ | $477 \times 588$ | $82{,}639$ | Đồ thị $p-V$ chu trình Otto, đủ trục và nhãn |
| `a-hinh-20-07.png` | 668 | $(36, 550, 195, 745)$ | $477 \times 585$ | $102{,}023$ | Đồ thị $p-V$ chu trình Diesel, đủ trục và nhãn |
| `a-hinh-20-08.png` | 669 | $(470, 415, 595, 565)$ | $375 \times 450$ | $175{,}185$ | Sơ đồ dòng năng lượng máy làm lạnh |
| `a-hinh-20-09.png` | 670 | $(78, 84, 612, 335)$ | $1602 \times 753$ | $542{,}541$ | Đủ 2 phần (a) nguyên lý và (b) cấu tạo tủ lạnh |
| `a-hinh-20-10.png` | 670 | $(235, 550, 545, 735)$ | $930 \times 555$ | $454{,}192$ | Sơ đồ máy điều hòa không khí qua tường |

---

## 5. Kết quả kiểm tra công thức toán học (`measure-math.mjs`)

Đã chạy công cụ kiểm thử nghiêm ngặt `measure-math.mjs` của dự án trên toàn bộ 5 tệp bài giảng:

```bash
node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . \
  raw_materials/physics/translations/chapter-20/00-mo-dau.md \
  raw_materials/physics/translations/chapter-20/01-chieu-cua-qua-trinh-nhiet-dong.md \
  raw_materials/physics/translations/chapter-20/02-dong-co-nhiet.md \
  raw_materials/physics/translations/chapter-20/03-dong-co-dot-trong.md \
  raw_materials/physics/translations/chapter-20/04-may-lanh.md
```

**Kết quả trả về**:
```json
{
  "status": "passed",
  "scope": "Strict draft math and syntax probe, not semantic or browser acceptance",
  "display": 32,
  "inline": 214,
  "findings": []
}
```

- Tổng số công thức hiển thị (display math `$$...$$`): **32** (tất cả đều có độ rộng $\le 25\,\mathrm{ex}$, dấu `$$` nằm độc lập ở cột 0).
- Tổng số công thức nội dòng (inline math `$...$`): **214** (tất cả đều có độ rộng $\le 27\,\mathrm{ex}$, nằm trên cùng một dòng vật lý).
- Số lỗi phát hiện (findings): **0**.

---

## 6. Lịch sử các lệnh thực thi và mã thoát (Command Log)

1. `C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics1-20-theory-a-assets.py`: Mã thoát `0`. Trích xuất thành công 12 hình ảnh.
2. `node --input-type=module -e "import('./docs/.vitepress/physics1-20-theory-a-image-annotations.mjs').then(m=>console.log(Object.keys(m)))"`: Mã thoát `0`. Xuất khẩu chính xác `['physics1Chapter20TheoryAImageAnnotations']`.
3. `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter20_theory_a.py`: Mã thoát `0`. Kiểm chứng toàn bộ 4 nội dung (số học, dẫn xuất, so khớp RGB ảnh, schema nhãn).
4. `node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs ...`: Mã thoát `0`. 0 lỗi định dạng trên toàn bộ 5 tệp Markdown.

---

## 7. Đánh giá trung thực và bàn giao (Truthful Handoff)

- **Không tự chứng nhận hoàn hảo (No 100% or Browser QA Certification)**: Bản báo cáo này xác nhận mã nguồn và dữ liệu đã vượt qua toàn bộ các bài kiểm tra cú pháp, đơn vị, so khớp pixel và số học nội bộ theo đúng yêu cầu phân công của phần Theory A. Khâu kiểm thử hiển thị giao diện trình duyệt thực tế và tích hợp toàn cục vào hệ thống mục lục/Wiki do tác nhân cha (Parent Agent) thực hiện độc lập.
- **Tình trạng hạn ngạch (Quota Status)**: Hạn ngạch ngoại vi đã được khôi phục bởi người dùng, DNS endpoint công cộng phân giải bình thường, toàn bộ quy trình hoàn thành hoàn toàn cục bộ trong worktree mà không gặp bất kỳ lỗi phân quyền hay gián đoạn nào.
- **Ranh giới sở hữu**: Đảm bảo 100% chỉ thao tác trên các tệp được chỉ định độc quyền, không chạm vào các tệp dùng chung, không tự ý chạy build tĩnh toàn dự án (`npm run ci:build`), không commit, push hay deploy.
