---
section: wiki
concept: cuc-tri-dia-phuong
title: "Cực trị địa phương trong tìm kiếm rời rạc"
---

## Giải thích kỹ thuật

## Khái niệm và Định nghĩa hình thức
Trong lý thuyết tối ưu hóa rời rạc và tìm kiếm cục bộ, bài toán thường được phát biểu dưới dạng tìm kiếm một trạng thái trong không gian cấu hình đầy đủ $S$ nhằm tối thiểu hóa một hàm chi phí mục tiêu $C: S \to \mathbb{R}$. Cấu trúc hình học của không gian tìm kiếm được xác lập thông qua hàm lân cận $N: S \to \mathcal{P}(S)$, trong đó $N(s)$ là tập hợp các trạng thái có thể đạt tới từ $s$ qua một phép biến đổi cục bộ cơ sở.
Một trạng thái $s \in S$ được định nghĩa là một cực tiểu địa phương (local minimum) nếu giá trị hàm chi phí tại $s$ không lớn hơn chi phí tại bất kỳ trạng thái lân cận nào của nó:
$$
C(s) \le C(t), \quad \forall t \in N(s)
$$

## Phân biệt Cực tiểu địa phương và Tối ưu toàn cục
Một cách hiểu sai là cho rằng cực tiểu địa phương bắt buộc phải là một trạng thái xấu hơn nghiệm tối ưu toàn cục. Theo định nghĩa toán học chính xác ở trên:
Trạng thái tối ưu toàn cục (global minimum), ký hiệu là $s^* = \arg\min_{s \in S} C(s)$, luôn luôn thỏa mãn điều kiện $C(s^*) \le C(t)$ với mọi $t \in N(s^*)$. Do đó mọi trạng thái tối ưu toàn cục đều đồng thời là một cực tiểu địa phương.
Trạng thái $s$ thỏa mãn điều kiện cực tiểu địa phương nhưng tồn tại một trạng thái $s^* \in S$ sao cho $C(s^*) < C(s)$ được gọi chính xác là cực tiểu địa phương không tối ưu toàn cục (non-global local minimum). Đây mới chính là các trạng thái bẫy khiến các thuật toán giảm dốc đơn thuần bị mắc kẹt.

## Các đặc trưng địa hình liên quan
Địa hình của không gian tìm kiếm còn chứa các cấu trúc phức tạp khác:
1. Vùng bằng phẳng (Plateau): Tập hợp các trạng thái kề nhau có cùng giá trị hàm chi phí. Nếu vùng bằng phẳng có lối thoát dẫn tới các trạng thái có chi phí thấp hơn, nó được gọi là vai dốc (shoulder). Nếu mọi hướng đi ra khỏi vùng bằng phẳng đều dẫn tới các trạng thái có chi phí cao hơn, nó được gọi là lòng chảo bằng phẳng (flat local minimum).
2. Sống núi (Ridge): Chuỗi các đỉnh dốc mà tại mỗi điểm riêng lẻ, việc thay đổi độc lập từng thành phần tọa độ rời rạc đều làm tăng chi phí, gây khó khăn cho các giải thuật chỉ tìm kiếm theo từng chiều biến.

## Tính phụ thuộc vào cấu trúc lân cận
Khái niệm cực tiểu địa phương không phải là một thuộc tính bất biến của bản thân bài toán hay hàm chi phí, mà phụ thuộc hoàn toàn vào cấu trúc lân cận $N(s)$ được lựa chọn. Một trạng thái có thể là cực tiểu địa phương dưới một phép biến đổi lân cận hẹp nhưng sẽ không còn là cực tiểu địa phương nếu ta mở rộng bán kính lân cận hoặc thay đổi quy tắc biến đổi.
