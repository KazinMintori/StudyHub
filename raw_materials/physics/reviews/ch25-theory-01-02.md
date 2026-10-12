# Rà soát bản chuẩn bị chương 25.1–25.2

## Phạm vi và disposition

Đã đối chiếu nội dung với `raw_materials/physics/source/young-freedman-15.pdf`, các bản trích `qa/physics/full-source/pdf-0833.txt` đến `pdf-0839.txt`, và ảnh render các trang PDF 833–839. Theo PyMuPDF, trang in 813 bắt đầu ở trang PDF một-based 833, tức chỉ số zero-based 832. Trang in 819 tương ứng PDF 839. Phạm vi này bao phủ trọn mục 25.1, mục 25.2 và câu tự kiểm cuối mục 25.2. Phần bắt đầu mục 25.3 trên trang in 819 được nhận diện nhưng không đưa vào hai bản dịch.

| Đơn vị nguồn | Trạng thái | Nội dung đã kiểm |
| --- | --- | --- |
| 25.1, trang in 813 / PDF 833 | Đạt | Định nghĩa dòng điện, chuyển động nhiệt electron, điện trường và lực điện, va chạm và vận tốc trôi, lý do đèn sáng nhanh, chuyển công thành nhiệt, các loại hạt tải và lỗ trống, chiều dòng điện quy ước, định nghĩa ampe và các tiền tố đơn vị. Hình 25.1 được đối chiếu trực tiếp với ảnh trang. |
| 25.1, trang in 814 / PDF 834 | Đạt | Hai tình huống hạt tải dương và âm tạo cùng chiều dòng điện, dòng điện là vô hướng, định nghĩa $I=dQ/dt$, đơn vị SI và các cỡ dòng điện minh họa. Đã giữ nguyên ý cảnh báo dòng điện không phải véc-tơ. |
| 25.1, trang in 814–815 / PDF 834–835 | Đạt | Dẫn xuất từ thể tích quét $Av_d dt$ đến $I=nqv_dA$, định nghĩa mật độ dòng điện vô hướng và véc-tơ, trị tuyệt đối cho độ lớn, dấu điện tích trong véc-tơ, cảnh báo $\vec J$ khác $I$, nhiều loại hạt tải, dòng ổn định qua mạch kín và dung dịch NaCl. Hình 25.2–25.4 được đối chiếu trực tiếp. |
| Ví dụ 25.1 và câu tự kiểm 25.1, trang in 816 / PDF 836 | Đạt | Dữ kiện dây đồng 18 gauge, đường kính, dòng điện, công suất đèn và mật độ electron được giữ đủ. Các bước tính diện tích, mật độ dòng và tốc độ trôi được mở. Câu hỏi thay đường kính gấp đôi và đáp án giảm tốc độ trôi còn một phần tư được giữ cùng lời giải. |
| 25.2, trang in 816–817 / PDF 836–837 | Đạt | Mô hình Ohm, giả thiết tại nhiệt độ cố định, định nghĩa điện trở suất, diễn giải độ lớn, đơn vị, giới hạn vật dẫn/cách điện lý tưởng, độ dẫn điện, Bảng 25.1, tương quan dẫn điện–dẫn nhiệt, đường mạch đồng trên nền cách điện, bán dẫn, phi Ohm và phép tương tự với dòng chất lỏng qua bộ lọc. Bảng 25.1 được kiểm bằng ảnh PDF vì trích chữ làm sai định dạng nhiều số mũ. |
| Nhiệt độ và ứng dụng sinh học, trang in 817–818 / PDF 837–838 | Đạt | Cơ chế va chạm trong kim loại, miền gần đúng tuyến tính và định nghĩa $\rho_0$, $T_0$, $\alpha$, Hình 25.6, hệ số âm của than chì và bán dẫn, nhiệt điện trở, chuyển pha siêu dẫn, dòng tồn tại trong vòng siêu dẫn, các mốc lịch sử và ứng dụng nam châm siêu dẫn. Đã ghi rõ mốc kỷ lục $203{,}5\,\mathrm K$ là số liệu nguồn ghi nhận năm 2018. Đã giữ ứng dụng myelin và sợi trục. |
| Bảng 25.2 và câu tự kiểm 25.2, trang in 818–819 / PDF 838–839 | Đạt | Đủ 12 hệ số nhiệt điện trở suất với đơn vị và dấu. Câu hỏi giữ điều kiện điện trường không đổi, bán dẫn hạ nhiệt độ; lời giải nêu rõ $\rho$ tăng nên $J=E/\rho$ giảm. Phần 25.3 bắt đầu sau câu này và được loại khỏi phạm vi. |

## Kiểm tra số độc lập

Chạy `python -X utf8 -I scripts/verify_chapter25_01_02.py`. Script dùng thư viện chuẩn để tính từ dữ kiện gốc của Ví dụ 25.1, kiểm tra đơn vị và tỉ lệ khi đường kính tăng gấp đôi. Kết quả: $A=8{,}17\times10^{-7}\,\mathrm{m^2}$, $J=2{,}04\times10^6\,\mathrm{A/m^2}$, $v_d=1{,}50\times10^{-4}\,\mathrm{m/s}=0{,}150\,\mathrm{mm/s}$, thời gian đi một mét khoảng $6{,}65\times10^3\,\mathrm s$ (làm tròn gần $6700\,\mathrm s$ như nguồn). Khi đường kính tăng gấp đôi, $v_d=0{,}0376\,\mathrm{mm/s}$, phù hợp đáp số $0{,}038\,\mathrm{mm/s}$. Kiểm tra dấu xác nhận $q\vec v_d$ cùng hướng dòng quy ước cho cả hạt dương lẫn electron. Từ điện trở suất đồng trong Bảng 25.1, độ dẫn điện tính được là $5{,}81\times10^7\,\mathrm{S/m}$.

## Hình và nhãn tiếng Anh trong bitmap

Các tệp Markdown hiện tham chiếu hình 25.1–25.6 tại `img/young-25/hinh-25-NN.png`. Cần crop tương ứng trước khi tích hợp Notes. Phần ứng dụng myelin là ảnh sinh học không đánh số trong nguồn, nên nội dung được diễn đạt bằng văn bản, không gán số hình mới. Hình 25.7 bắt đầu ở mục 25.3 nên không thuộc phạm vi.

| Hình | Nhãn/câu tiếng Anh trong ảnh | Cách giải nghĩa tiếng Việt đề xuất |
| --- | --- | --- |
| 25.1 | Conductor without internal E field | Vật dẫn không có điện trường bên trong |
| 25.1 | Path of electron without E field. Electron moves randomly. | Quỹ đạo electron khi không có điện trường. Electron chuyển động ngẫu nhiên. |
| 25.1 | Conductor with internal E field | Vật dẫn có điện trường bên trong |
| 25.1 | Path of electron with E field. The motion is mostly random, but ... | Quỹ đạo electron khi có điện trường. Chuyển động phần lớn vẫn ngẫu nhiên, nhưng ... |
| 25.1 | ... the E field results in a net displacement along the wire. | ... điện trường tạo ra độ dời thuần dọc theo dây dẫn. |
| 25.1 | An electron has a negative charge q, so the force on it due to the E field is in the direction opposite to E. | Electron mang điện tích âm $q$, nên lực điện do điện trường tác dụng lên nó hướng ngược chiều điện trường. |
| 25.2 | A conventional current is treated as a flow of positive charges, regardless of whether the free charges in the conductor are positive, negative, or both. | Dòng điện quy ước được xem là dòng điện tích dương, bất kể hạt tải tự do là điện tích dương, âm hay gồm cả hai loại. |
| 25.2 | In a metallic conductor, the moving charges are electrons, but the current still points in the direction positive charges would flow. | Trong vật dẫn kim loại, hạt chuyển động là electron, nhưng dòng điện vẫn hướng theo chiều điện tích dương sẽ chuyển động. |
| 25.3 | Current $I=dQ/dt$ | Dòng điện $I=dQ/dt$ |
| 25.3 | Current flows from higher to lower electric potential | Dòng điện đi từ điện thế cao đến điện thế thấp |
| 25.3 | Higher potential / Lower potential | Điện thế cao / Điện thế thấp |
| 25.3 | $V=$ potential difference between ends | $V=$ hiệu điện thế giữa hai đầu |
| 25.5 | Conducting paths (traces) | Đường dẫn điện (đường mạch) |
| 25.6 | Metal: Resistivity increases with increasing temperature. | Kim loại: Điện trở suất tăng khi nhiệt độ tăng. |
| 25.6 | Semiconductor: Resistivity decreases with increasing temperature. | Bán dẫn: Điện trở suất giảm khi nhiệt độ tăng. |
| 25.6 | Superconductor: At temperatures below $T_c$, the resistivity is zero. | Siêu dẫn: Điện trở suất bằng không khi nhiệt độ thấp hơn $T_c$. |

Hình 25.3–25.4 chủ yếu có ký hiệu vật lý, nhãn hình học và chữ viết tắt ion. Các ký hiệu $A$, $v_d dt$, $dQ/dt$, $\mathrm{Na^+}$, $\mathrm{Cl^-}$ không cần dịch. Hình 25.5–25.6 có caption tiếng Anh nằm ngoài bitmap và sẽ dùng caption tiếng Việt trong Notes.

## Giới hạn rà soát

Đây mới là hai bản dịch nguyên liệu cho mục 25.1–25.2. Chưa có crop chương 25 và chưa rà soát tích hợp Notes, Slides, Cheatsheet, Wiki, giao diện 320 px hay build cuối. Không nên xem kết quả này là chứng nhận hoàn tất chương 25.
