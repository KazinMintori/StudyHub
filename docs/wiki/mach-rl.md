---
title: "Mạch RL"
wikiTerm: mach-rl
prev: false
next: false
---

# Mạch RL

Mạch RL chứa điện trở và cuộn cảm. Khi nối nguồn không đổi vào mạch ban đầu không dòng, dòng tiến về $\mathcal E/R$. Khi tách nguồn nhưng giữ vòng kín, dòng suy giảm theo hàm mũ.

<WikiUsage />

## Giải thích kỹ thuật

Trong mạch nối nguồn hằng, R biểu diễn tổng điện trở trong vòng. Định luật vòng cho

$$
L\frac{di}{dt}+Ri=\mathcal E.
$$

Với dòng đầu bằng không, nghiệm là $i=(\mathcal E/R)(1-e^{-tR/L})$. Dòng đầu bằng không nhưng đạo hàm đầu bằng $\mathcal E/L$. Dòng cuối bằng $\mathcal E/R$ và không phụ thuộc L.

Khi tách nguồn nhưng vẫn giữ vòng RL kín, nghiệm trở thành $i=I_0e^{-tR/L}$. Dòng đầu I0 được lấy từ ngay trước chuyển mạch vì dòng cuộn liên tục dưới điện áp hữu hạn.

Với mạch phân nhánh, R trong hằng số thời gian không tự động bằng tổng tất cả điện trở trên hình. Phải lập Kirchhoff hoặc tìm điện trở hiệu dụng mà cuộn nhìn thấy, đồng thời giữ đúng điều kiện đầu.

## Ví dụ

Ngay sau đóng nguồn vào cuộn chưa có dòng, điện trở chưa có điện áp và cuộn nhận toàn bộ điện áp nguồn.

## Khi nào cần dùng?

Phân tích đóng, ngắt nguồn và các mạch có cuộn thực.

## Câu hỏi ôn lại

Dòng cuối của mạch RL nối nguồn một chiều không đổi phụ thuộc L không?

<details><summary>Xem đáp án</summary>

Không trong mô hình đã cho. L quyết định thời gian tiến đến giá trị cuối.

</details>

## Thuật ngữ liên quan

- [Cuộn cảm](./cuon-cam.md)
- [Hằng số thời gian RL](./hang-so-thoi-gian-rl.md)
- [Quy tắc Kirchhoff](./quy-tac-kirchhoff.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
