---
title: "Cuộn cảm"
wikiTerm: cuon-cam
prev: false
next: false
---

# Cuộn cảm

Cuộn cảm là phần tử được chế tạo để có tự cảm xác định. Với cuộn lý tưởng, điện áp theo quy ước thụ động là $v_L=L\,di/dt$, điện trở dây quấn được bỏ qua.

<WikiUsage />

## Giải thích kỹ thuật

Với cuộn lý tưởng, bỏ qua điện trở dây quấn, nhưng giữ tự cảm. Nguồn ngoài phải cấp công để tăng năng lượng từ trường. Với dòng dương,

$$
\begin{aligned}
p_L&=v_Li\\
&=Li\frac{di}{dt}\\
&=\frac{d}{dt}\left(\frac12Li^2\right).
\end{aligned}
$$

Công suất dương nghĩa cuộn nhận năng lượng, âm nghĩa cuộn trả năng lượng. Dấu này không được suy chỉ từ dấu dòng, mà cần cả điện áp.

Tích phân điện áp qua thời gian chuyển mạch cho $\Delta i=(1/L)\int v_Ldt$. Điện áp hữu hạn trong một khoảng tiến về không không tạo bước nhảy dòng. Một xung điện áp lý tưởng có diện tích hữu hạn có thể tạo bước nhảy trong mô hình, nhưng khác trường hợp chuyển mạch với điện áp hữu hạn.

Chấn lưu từ và các mạch hạn chế biến thiên dòng dùng tính chất này. Cần tính thêm điện trở, tổn hao vật liệu và giới hạn tuyến tính khi mô tả một cuộn thực.

## Ví dụ

Dòng dương đang giảm làm điện áp cuộn theo chiều dòng âm. Cuộn đang nhả năng lượng cho phần còn lại của mạch.

## Khi nào cần dùng?

Đọc sơ đồ mạch và chọn dấu điện áp khi áp dụng Kirchhoff.

## Câu hỏi ôn lại

Dòng cuộn có thể nhảy tức thời khi điện áp đặt vào chỉ hữu hạn không?

<details><summary>Xem đáp án</summary>

Không nếu L khác không. Đạo hàm dòng có thể nhảy, còn dòng liên tục.

</details>

## Thuật ngữ liên quan

- [Tự cảm](./tu-cam.md)
- [Quy tắc Kirchhoff](./quy-tac-kirchhoff.md)
- [Mạch RL](./mach-rl.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
