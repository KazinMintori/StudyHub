---
title: "Thomas Bayes: Đổi chiều câu hỏi xác suất"
prev: false
next: false
---

# Thomas Bayes: Đổi chiều câu hỏi xác suất

Nếu một bộ lọc thường đánh dấu thư rác, có thể kết luận mọi thư bị đánh dấu đều là thư rác không? Câu hỏi đảo chiều đòi hỏi biết cả tỷ lệ ban đầu và khả năng đánh dấu nhầm.

## Dấu mốc năm 1763

Bài luận *An Essay towards Solving a Problem in the Doctrine of Chances* của Thomas Bayes được công bố sau khi ông qua đời, do Richard Price chuyển tới Royal Society năm 1763. Công trình gắn với lịch sử suy luận xác suất từ những quan sát đã có.

Ngày nay, công thức mang tên Bayes diễn đạt mối quan hệ giữa hai xác suất có điều kiện. Với $P(B)>0$:

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
$$

Tử số đo phần đồng thời có A và B. Mẫu số xác định tập trường hợp mà ta đang xét sau khi quan sát B. Điều kiện đổi chiều vì tập dùng làm mẫu số đã thay đổi.

## Nhìn bằng số đếm

Trong một tập dữ liệu minh họa có 100 thư, 20 thư là thư rác. Bộ lọc đánh dấu 18 thư rác và 16 thư thường. Trong 34 thư bị đánh dấu, 18 thư thật sự là thư rác:

$$
P(A\mid B)=\frac{18}{34}=\frac9{17}.
$$

Kết quả xấp xỉ $52{,}94\%$. Trong khi đó, tỷ lệ đánh dấu đúng trong nhóm thư rác là $18/20=90\%$. Hai con số trả lời hai câu hỏi khác nhau.

![Hình 1: Nhóm được đánh dấu chứa cả thư rác và thư thường.](../img/atlas/bayes.svg)

Các số đếm trên tạo thành một ví dụ tính toán, không phải đánh giá một bộ lọc thực tế. Để dùng trong hệ thống thật, cần ước lượng tỷ lệ và sai số trên dữ liệu phù hợp.

## Câu hỏi tự kiểm

Nếu giữ nguyên tỷ lệ đánh dấu của bộ lọc nhưng thư rác hiếm hơn, tỷ lệ thư rác trong nhóm bị đánh dấu có nhất thiết giữ nguyên không?

::: details Xem gợi ý
Không. Khi tỷ lệ ban đầu thay đổi, thành phần của nhóm bị đánh dấu cũng thay đổi. Đây là lý do phải kiểm tra xác suất ban đầu cùng các xác suất có điều kiện.
:::

## Đọc tiếp

- [Xác suất có điều kiện](../xac-suat-co-dieu-kien.md)
- [Likelihood](../likelihood.md)
- [Độc lập](../doc-lap.md)
- [Khám phá Wiki](../index.md)

## Tài liệu tham khảo

- T. Bayes. [An Essay towards Solving a Problem in the Doctrine of Chances](https://www.gtfp.cs.rhul.ac.uk/pulskamp/Bayes/bayesessay-rjp.pdf), *Philosophical Transactions*, 53, tr. 370–418, 1763.
