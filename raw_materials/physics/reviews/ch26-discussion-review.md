# Rà soát câu hỏi thảo luận Chương 26

## Ranh giới nguồn

Phần “Discussion Questions” bắt đầu ở trang in 869, PDF một-based 889 (`qa/physics/full-source/pdf-0889.txt`) và tiếp tục ở trang in 870, PDF 890 (`pdf-0890.txt`). Danh sách câu hỏi kết thúc ở Q26.21 trên trang in 870. Phần “Exercises” mở đầu ngay sau đó, vì vậy bài tập 26.1 trở đi không thuộc bản dịch này.

Đã đọc toàn bộ hai trang trích xuất và render trực tiếp PDF 889–890 để đối chiếu các sơ đồ. Bản dịch giữ đủ Q26.1–Q26.21, bao gồm toàn bộ tiểu mục (a)–(h) của Q26.5 và (a)–(i) của Q26.6, cùng các câu hỏi về bóng đèn ở Q26.4, Q26.7, Q26.9, Q26.10, Q26.12, Q26.14 và Q26.16, hai mạch tụ ở Q26.18, và câu hỏi đơn vị/thời gian ở Q26.19–Q26.21.

## Bản đồ hình và nhãn

Các đường dẫn dưới đây là crop dự kiến trong `docs/vat-ly-2/bai-giang/img/young-26/`. Khi rà soát, thư mục chưa có các file này. Caption đã được viết trong bản dịch, còn nhãn nằm trong ảnh cần root crop và bổ sung vào bản đồ chú giải tiếng Việt.

| Hình nguồn | Trang in / PDF | Crop dự kiến | Nhãn và quan hệ cần giữ |
| --- | --- | --- | --- |
| Q26.4 | 869 / 889 | `hinh-q26-04.png` | Nguồn $\mathcal E$; bóng A ở nhánh giữa; B và C nối tiếp ở nhánh dưới. Hai nhánh mắc song song. |
| Q26.5 | 869 / 889 | `hinh-q26-05.png` | $R_1$, $R_2$, các điểm $a,b,c$ và các mũi tên $I_1,I_2,I_3$ cùng hướng qua nhánh nối tiếp. |
| Q26.6 | 869 / 889 | `hinh-q26-06.png` | Hai nhánh song song $R_1$, $R_2$; các đầu nhánh $c,d,e,f$; nút $a,b$; dòng tổng $I_3,I_4$ và dòng nhánh $I_1,I_2$. |
| Q26.7 | 869 / 889 | `hinh-q26-07.png` | Ba nhánh song song, bóng B1/B2 luôn nối với nguồn; nhánh bóng B có công tắc S. |
| Q26.8 | 869 / 889 | `hinh-q26-08.png` | Ba dải kim loại tạo các đường song song; ampe kế A nối tiếp mạng và pin cấp nguồn. |
| Q26.9 | 869 / 889 | `hinh-q26-09.png` | Cụm điện trở song song có nhánh trên chứa S, mắc nối tiếp với một điện trở riêng, bóng và pin. |
| Q26.10 | 869 / 889 | `hinh-q26-10.png` | Bóng ở một nhánh tải. Nhánh kia có S nối tiếp điện trở. Hai nhánh đặt vào pin thực có điện trở trong dù phần tử đó không vẽ riêng. |
| Q26.12 | 869 / 889 | `hinh-q26-12.png` | Nhánh trên gồm hai bóng nối tiếp; nhánh dưới có một bóng; nhánh giữa có điện trở và S; ba nhánh cùng mắc song song với nguồn. |
| Q26.14 | 869 / 889 | `hinh-q26-14.png` | B1 và B2 nối tiếp; công tắc S tạo đường nối tắt qua B2. |
| Q26.16 | 870 / 890 | `hinh-q26-16.png` | Bóng A, B, C nối tiếp; S mắc song song qua C. |
| Q26.18 | 870 / 890 | `hinh-q26-18.png` | (a) Hai tụ C nối tiếp sau R. (b) Hai tụ C song song sau R. Cả hai sơ đồ có nguồn $\mathcal E$ và công tắc S. |

Điểm cần giữ riêng khi gắn hình là Q26.9 và Q26.10. Q26.9 thêm một nhánh vào cụm song song nằm nối tiếp với bóng. Q26.10 mắc tải mới song song trực tiếp lên pin thực. Cùng thao tác đóng công tắc nhưng ảnh hưởng độ sáng trái ngược nhau. Q26.11 tiếp tục Q26.10 với pin lý tưởng, còn Q26.12 yêu cầu phân biệt nguồn lý tưởng và nguồn có điện trở trong.

## Kiểm tra tính toán

Chạy `python -I raw_materials/physics/verify_chapter26_discussion.py`, các assertion cho Q26.1–Q26.21 đều qua. Script kiểm tra điện trở và điện áp bóng đèn, tải nối tiếp/song song, công suất của các nhánh, độ sáng trong các mạng công tắc đã chọn, pin có điện trở trong khác không, các điện dung tương đương và hằng số thời gian, cùng thứ nguyên $RC$.

Các kết quả kiểm tra tiêu biểu:

- Q26.2: Bóng $25\,\mathrm W$ có $R=576\,\Omega$, nhận khoảng $213{,}3\,\mathrm V$ và tiêu thụ khoảng $79{,}0\,\mathrm W$ trong ước tính điện trở cố định. Bóng $200\,\mathrm W$ nhận khoảng $26{,}7\,\mathrm V$.
- Q26.10: Với một bộ giá trị đại diện và điện trở trong khác không, đóng nhánh tải làm công suất bóng giảm. Script xác nhận tỉ số công suất là $4/9$ trong bộ giá trị thử, chỉ để kiểm tra chiều biến thiên.
- Q26.18: Với $R=2\,\mathrm{M\Omega}$ và mỗi tụ $1\,\mathrm{\mu F}$, mạch nối tiếp có $\tau=1\,\mathrm s$, còn mạch song song có $\tau=4\,\mathrm s$. Dòng ban đầu bằng nhau, nhưng điện tích cuối trên mỗi tụ lần lượt là $6\,\mathrm{\mu C}$ và $12\,\mathrm{\mu C}$.
- Q26.19: Thứ nguyên SI của $\Omega\cdot\mathrm F$ rút gọn thành giây. Q26.20 dùng $R=\tau/C$ để suy điện trở từ điện dung đã biết và thời gian đáp ứng đo được. Q26.21 có điện tích cuối $Q_{\max}=C\mathcal E$, không chứa điện trở nối tiếp.

## Giới hạn

Các crop Q26 chưa có trong thư mục hình khi viết báo cáo, nên chưa xác nhận việc ánh xạ nhãn trên ảnh, hiển thị trang sau tích hợp hoặc bề rộng công thức trên thiết bị di động. Phần này chỉ đối chiếu các câu hỏi và sơ đồ nguồn ở hai trang nêu trên, không bao gồm bài tập cuối chương.
