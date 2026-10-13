---
title: "Điện trở"
wikiTerm: dien-tro
prev: false
next: false
---

# Điện trở

Điện trở R của một mẫu là tỉ số hiệu điện thế qua mẫu và dòng qua nó, $R=V/I$ với I khác không. Đơn vị SI là ohm. Mẫu trụ đồng nhất, tiết diện đều có $R=\rho L/A$.

<WikiUsage />

## Giải thích kỹ thuật

Đối với dây đồng nhất, tiết diện đều và mật độ dòng đều:

$$
\begin{aligned}
&V = EL,\\
&I = JA,\\
&\frac VI = \rho\frac LA,\\
&R = \frac{\rho L}{A}.
\end{aligned}
$$

Giữ ρ và A, tăng chiều dài làm R tăng. Giữ ρ và L, tăng diện tích làm R giảm. Tiết diện tròn tăng theo bình phương đường kính, nên không lấy tỉ số đường kính làm tỉ số diện tích.

Định nghĩa R = V/I dùng ở một điểm hoạt động có dòng khác không. Linh kiện Ohm có R không đổi theo điện áp hoặc dòng trong điều kiện phù hợp. Điôt có quan hệ dòng và điện áp phi tuyến, nên không mô tả bằng một điện trở cố định cho mọi điểm.

Khi bỏ giãn nở hình học, điện trở biến thiên nhiệt gần như điện trở suất:

$$
R(T)\approx R_0[1+\alpha(T-T_0)].
$$

Ở nguồn giữ điện áp, R tăng làm dòng và công suất giảm. Ở nguồn giữ dòng, R tăng lại làm công suất I²R tăng. Vì vậy phải nêu điều kiện nguồn khi so hai trạng thái.

## Ví dụ

Đoạn dây đồng dài 50,0 m, tiết diện $8.17\times10^{-7}\,\mathrm{m^2}$ và điện trở suất $1.72\times10^{-8}\,\Omega\,\mathrm m$ có điện trở khoảng 1,05 Ω.

## Khi nào cần dùng?

Tính dòng, sụt áp và công suất, phân biệt ảnh hưởng vật liệu với hình học mẫu.

## Câu hỏi ôn lại

V = IR có nghĩa R luôn không đổi theo nhiệt độ hoặc điện áp không?

<details><summary>Xem đáp án</summary>

Không. Muốn gọi quan hệ là định luật Ohm phải có R không đổi trong các điều kiện khảo sát. Dây nóng lên hoặc linh kiện phi tuyến có thể có R thay đổi.

</details>

## Thuật ngữ liên quan

- [Điện trở suất](./dien-tro-suat.md)
- [Dòng điện](./dong-dien.md)
- [Điện thế](./dien-the.md)
- [Công & năng lượng](./cong-nang-luong.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 25, trang 812–835.
