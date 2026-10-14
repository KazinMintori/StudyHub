---
title: "Hỗ cảm"
wikiTerm: ho-cam
prev: false
next: false
---

# Hỗ cảm

Hỗ cảm M liên hệ dòng ở một mạch với từ thông móc vòng ở mạch khác: $N_2\Phi_{B2}=Mi_1$. Trong mô hình hình học cố định, môi trường từ tuyến tính thuận nghịch, cùng M dùng khi đổi vai hai mạch.

<WikiUsage />

## Giải thích kỹ thuật

Chọn chiều dòng và chiều từ thông của hai cuộn trước khi dùng một hệ số hỗ cảm có dấu. Trong mô hình cố định, tuyến tính, từ thông móc vòng do cuộn 1 gây ra ở cuộn 2 là $\Lambda_2=Mi_1$. Lấy đạo hàm rồi áp dụng Faraday cho

$$
\mathcal E_2=-M\frac{di_1}{dt}.
$$

Tính đối xứng $M_{12}=M_{21}$ cần mô hình môi trường thuận nghịch phù hợp. Nó không yêu cầu số vòng hoặc kích thước hai cuộn bằng nhau. Hai từ thông trung bình mỗi vòng vẫn có thể khác nhau.

Với hai cuộn nối tiếp có trường hỗ trợ, tự cảm bộ bằng $L_1+L_2+2M$. Trường đối nhau cho $L_1+L_2-2M$, khi M là độ lớn hỗ cảm theo quy ước đó. Không được bỏ hỗ cảm khi hai cuộn có liên kết từ đáng kể. Với môi trường phi tuyến, từ thông không còn là một hàm tuyến tính của dòng và hệ số hằng phải được thay bằng mô hình thích hợp.

## Ví dụ

Hai cuộn có $M=4\,\mathrm{mH}$. Dòng nguồn tăng $2\,\mathrm{A/s}$ gây suất điện động độ lớn $8\,\mathrm{mV}$ ở cuộn kia.

## Khi nào cần dùng?

Phân tích hai cuộn ghép từ, máy biến áp và cảm ứng không tiếp xúc.

## Câu hỏi ôn lại

Hỗ cảm và tự cảm có mô tả cùng một từ thông nguồn không?

<details><summary>Xem đáp án</summary>

Không. Hỗ cảm liên hệ hai mạch, tự cảm liên hệ dòng và từ thông của chính một mạch.

</details>

## Thuật ngữ liên quan

- [Từ thông móc vòng](./tu-thong-moc-vong.md)
- [Định luật Faraday](./dinh-luat-faraday.md)
- [Tự cảm](./tu-cam.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
