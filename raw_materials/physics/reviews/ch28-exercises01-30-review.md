# Rà soát nội bộ: Bài tập 28.1–28.30

## Phạm vi đối chiếu

Đã đối chiếu trực tiếp bài tập 28.1–28.30 với các trang in 945–947 của *University Physics with Modern Physics*, ấn bản 15, và xem các hình E28.3, E28.4, E28.6, E28.8, E28.9, E28.12, E28.13, E28.19, E28.21, E28.23–E28.25, E28.27–E28.29. Fragment giữ đủ 30 câu, mọi tiểu phần và các hình được dẫn. Mỗi bài có khối lời giải gập, tóm tắt, hướng giải có nêu lý do, và trình tự tính toán.

## Kết quả kiểm tra độc lập

Suite `raw_materials/physics/verify_chapter28_01_30.py` chạy bằng Python cùng NumPy, kiểm tra tích có hướng, hướng trường, lực từ, lực giữa dây, cấu hình đối xứng, các giá trị số và đơn vị. Kết quả chạy gần nhất: `Chapter 28 exercises 28.1–28.30: independent numerical and vector checks passed.`

Các giá trị trọng yếu để đối chiếu lời giải:

| Bài | Kết quả kiểm tra |
| ---: | --- |
| 28.1 | (a) $-19{,}2\,\mu\mathrm T\hat{k}$; (b) $0$; (c) $+19{,}2\,\mu\mathrm T\hat\imath$; (d) $+6{,}79\,\mu\mathrm T\hat\imath$ |
| 28.3 | A, B: mỗi điểm $60{,}0\,\mathrm{nT}$, cả hai ra khỏi trang; C: $120\,\mathrm{nT}$ ra khỏi trang; D: $0$ |
| 28.6 | $B_P=0{,}4375\,\mathrm{mT}$; $F_E=3{,}745\,\mathrm N$; $F_B=1{,}6875\,\mathrm{mN}$; tỉ số gần $2{,}22\times10^3$ |
| 28.8 | Trường tổng tại O: $1{,}21\,\mathrm{mT}$ vào trang; trường electron tại proton: $0{,}224\,\mathrm{mT}$ vào trang |
| 28.9 | A: $0{,}440\,\mu\mathrm T$; B: $16{,}7\,\mathrm{nT}$; C: $0$ |
| 28.12–13 | 28.12: $0{,}527\,\mu\mathrm T$ vào trang; 28.13: $4{,}40\,\mu\mathrm T$ vào trang |
| 28.14–20 | 28.14: $v_x=-22{,}5\,\mathrm{km/s}$, $v_y=-12{,}5\,\mathrm{km/s}$; 28.16: $B=6{,}57\,\mu\mathrm T$ hướng bắc; 28.17: $250\,\mu\mathrm A$; 28.20: $3{,}75\,\mu\mathrm T$, bằng $7{,}5\%$ trường Trái Đất |
| 28.21–25 | 28.21: $0$, $6{,}67\,\mu\mathrm T$ lên, $7{,}53\,\mu\mathrm T$ sang trái; 28.22: $2{,}64\,\mathrm A$; 28.23: lần lượt $0$, $0$, $400\,\mu\mathrm T$ sang trái; 28.24: $2{,}00\,\mathrm A$ xuống; 28.25: (a) $41\,\mu\mathrm T$ tại P/Q; (b) $9\,\mu\mathrm T$ tại P/Q |
| 28.26–30 | 28.26: hữu hạn $28{,}6\,\mu\mathrm T$, vô hạn $32{,}0\,\mu\mathrm T$, chênh $11{,}8\%$ nếu lấy kết quả hữu hạn làm mốc; 28.29: $6{,}00$ và $24{,}0\,\mu\mathrm N$; 28.30: $8{,}33\,\mathrm A$, dòng ngược chiều |

## Sai lệch đáp số và hình cần lưu ý

- E28.17 ghi từ trường $10\,\mu\mathrm G$ và khoảng cách $5{,}0\,\mathrm{cm}$. Định luật dây thẳng cho $250\,\mu\mathrm A$. Đáp số lẻ trong phụ lục ghi $25\,\mu\mathrm A$, lệch hệ số 10. Bản lời giải giữ kết quả từ dữ kiện và ghi nhận sai lệch ở đây.
- Hình E28.28 có mũi tên dòng điện dây giữa ở phía phải dây, hướng sang trái. Crop cũ kết thúc trước mũi tên này. `scripts/prepare-physics28-exercise-assets.py` đã nới cạnh phải từ 590 lên 630 điểm và dựng lại hình, hiện thấy đủ nhãn $I$ cùng mũi tên.
- Crop P28.72 giữ đủ nhãn trục ngang $I\,(\mathrm{mA})$. Crop P28.76 có cả mũi tên trục x và nhãn $x$. Crop P28.77 giữ trọn đường bao hình cầu.
- Hình E28.25 ghi dòng dây đứng $12\,\mathrm A$; prompt trong fragment đã giữ đúng con số từ hình.

## Kiểm tra trình bày

Đã chạy `node scripts/audit-physics-math.mjs 28`. Với file 12, không có công thức TeX lỗi và không còn công thức hiển thị hay nội dòng vượt ngưỡng của audit. Các cảnh báo còn lại thuộc file 10 và 14 do tác nhân khác sở hữu.
