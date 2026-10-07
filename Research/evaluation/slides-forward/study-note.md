# Một bước gradient descent và quy ước dấu của nhân tử Lagrange

Bài giảng tiếng Việt 12 phút · 8 slide · phiên bản nội dung 1.0.

Người học: sinh viên biết đạo hàm, mới học tối ưu. Phần tính toán chỉ dùng một biến thực. Đây là bản nội dung và đặc tả; chưa phải PDF hoặc bộ slide đã render.

Mục tiêu: tính được bước cập nhật, nhận ra giới hạn của điều kiện α > 0, lập L với một h cụ thể và phân biệt quy ước dấu của αₖ và ν.

Tự học: đọc phần “Note tự học” theo thứ tự. Với Slide 4 và Slide 7, tự trả lời trước khi mở lời giải ở mục kế tiếp. Phần “Lời giảng” dùng để tổ chức buổi học trực tiếp.

<a id="slide-1"></a>
## Slide 1: Từ đạo hàm đến một bước tìm giá trị nhỏ hơn

Thời gian dự kiến: 0.75 phút.

### Chữ trên slide

$$
f(x)=(x-3)^2,\qquad x_0=0
$$

Ta muốn chọn x để hàm mục tiêu f(x) nhỏ nhất.

$$
f(x)\geq 0,\qquad f(3)=0
$$

Ta sẽ dùng đạo hàm để tính từng bước từ x₀ = 0.

### Lời giảng

Hàm này nhỏ nhất ở đâu? Vì bình phương không âm và bằng 0 tại x = 3, ta đã biết đích của ví dụ. Nhưng hôm nay ta học cách dùng đạo hàm để tính từng bước từ x₀ = 0. Sau bài, ta cần tính được một bước mới, giải thích dấu trừ và phân biệt hai quy ước dấu xuất hiện trong nguồn.

### Note tự học

Hàm mục tiêu là hàm dùng để đánh giá lựa chọn x. Trong ví dụ, ta muốn làm f(x) = (x − 3)² nhỏ nhất. Với mọi x thực, f(x) không âm; tại x = 3, f(3) = 0. Vì thế x = 3 cho giá trị nhỏ nhất. Biết đích trong ví dụ giúp kiểm tra các bước tính sau, nhưng quy tắc cập nhật vẫn cần được học riêng.

Câu nối: Để chọn bước từ x₀, ta đọc quy tắc gradient descent.

<a id="slide-2"></a>
## Slide 2: Dấu trừ chọn hướng; αₖ điều chỉnh độ dời

Thời gian dự kiến: 1.75 phút.

### Chữ trên slide

$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),\qquad \alpha_k>0
$$

xₖ là giá trị ở bước k; xₖ₊₁ là giá trị sau cập nhật. αₖ là bước học.

Gradient gom các đạo hàm riêng trong bài nhiều biến. Với một biến, ∇f(x) là f′(x).

Nếu f′(xₖ) < 0, cập nhật làm x tăng; nếu f′(xₖ) > 0, cập nhật làm x giảm.

Đi theo hướng này chưa bảo đảm f giảm với mọi bước học dương.

### Lời giảng

Chỉ số k đếm số lần cập nhật, không phải số mũ. Ta lấy gradient tại xₖ rồi nhân với αₖ. Với một biến, hãy đọc gradient như đạo hàm đã biết. Khi đạo hàm âm, hàm giảm nếu x tăng một lượng đủ nhỏ; dấu trừ làm độ dời dương. Khi đạo hàm dương thì hướng ngược lại. Hướng là điều ta chọn trước, còn độ dời bằng −αₖf′(xₖ). Một αₖ quá lớn vẫn có thể đưa ta đến giá trị hàm lớn hơn.

### Note tự học

Gradient descent là quy tắc tạo dãy các giá trị x₀, x₁, x₂, … cho bài toán không ràng buộc. Trong công thức, k là chỉ số bước; αₖ > 0 điều chỉnh mức thay đổi. Gradient ∇f gom các đạo hàm riêng khi có nhiều biến. Bài này chỉ tính một biến, nên ∇f(x) = f′(x). Nếu f′(xₖ) âm thì −αₖf′(xₖ) dương, do đó xₖ₊₁ > xₖ. Nếu f′(xₖ) dương thì độ dời âm. Dấu đạo hàm mô tả thay đổi ở gần xₖ; nó không bảo đảm mọi αₖ dương đều làm f giảm. Bài không đưa ra định lý hội tụ cho hàm tổng quát.

Câu nối: Ta dùng quy tắc ấy để tính bước đầu của ví dụ.

<a id="slide-3"></a>
## Slide 3: Bước đầu đưa x từ 0 đến 1,5

Thời gian dự kiến: 2 phút.

### Chữ trên slide

$$
f(x)=(x-3)^2,\quad x_0=0,\quad\alpha=\tfrac14
$$

$$
f\prime(x)=2(x-3),\qquad f\prime(0)=-6
$$

$$
\Delta x_0=-\tfrac14(-6)=\tfrac32,\qquad x_1=0+\tfrac32=1{,}5
$$

$$
f(x_0)=9,\qquad f(x_1)=2{,}25
$$

### Lời giảng

Ta tính đạo hàm trước: f′(x) = 2(x − 3). Thay x₀ = 0 được −6. Vì α = 1/4, độ dời là −(1/4)(−6) = 1,5. Hai dấu âm triệt tiêu, nên x tăng từ 0 lên 1,5. Δx₀ chỉ là ký hiệu cho độ dời ở bước đầu; x₁ mới là điểm sau cập nhật. Kiểm tra lại: bình phương khoảng cách đến 3 giảm từ 9 xuống 2,25.

### Note tự học

Với f(x) = (x − 3)², đạo hàm là f′(x) = 2(x − 3). Tại x₀ = 0, đạo hàm bằng −6. Ký hiệu Δx₀ là độ dời x₁ − x₀. Theo quy tắc cập nhật, Δx₀ = −(1/4)(−6) = 3/2, nên x₁ = 1,5. Giá trị hàm tại x₀ là 9, còn tại x₁ là (1,5 − 3)² = 2,25. Bước này thực sự làm hàm giảm. Kết quả đó được kiểm tra bằng giá trị hàm, không chỉ bằng dấu của đạo hàm.

Câu nối: Ở bước tiếp theo, ta phải lấy đạo hàm tại đâu?

<a id="slide-4"></a>
## Slide 4: Tự tính bước từ x₁ đến x₂

Thời gian dự kiến: 1.25 phút.

### Chữ trên slide

$$
x_1=1{,}5,\qquad\alpha=\tfrac14,\qquad f\prime(x)=2(x-3)
$$

Tính f′(x₁), x₂ và f(x₂). Giá trị hàm tăng hay giảm?

### Lời giảng

Dành 35 giây để tự tính ba giá trị. Điểm cần kiểm tra là đạo hàm phải được lấy tại x₁ = 1,5. Chưa chiếu lời giải. Nếu người học dùng −6 lần nữa, hỏi họ ký hiệu xₖ trong công thức đang ứng với giá trị nào. Sau khi có câu trả lời, chuyển sang trang kế tiếp để đối chiếu.

### Note tự học

Hãy tự tính trước khi đọc lời giải ở mục Slide 5. Dùng f′(x₁) với x₁ = 1,5 và α = 1/4 để tìm x₂, rồi thay x₂ vào f(x) = (x − 3)². Bài đạt khi chọn đúng điểm lấy đạo hàm, xử lý đúng dấu và dùng giá trị hàm để kết luận tăng hay giảm.

Câu nối: Ta đối chiếu từng bước, rồi xét xem α dương đã đủ chưa.

<a id="slide-5"></a>
## Slide 5: Cập nhật đúng; bước học lớn vẫn có thể làm hàm tăng

Thời gian dự kiến: 1.75 phút.

### Chữ trên slide

$$
f\prime(1{,}5)=-3,\quad x_2=1{,}5-\tfrac14(-3)=2{,}25
$$

$$
f(x_2)=(2{,}25-3)^2=0{,}5625<2{,}25
$$

Thử thay riêng bước học ở x₀ = 0 bằng α = 2.

$$
x_1=0-2(-6)=12,\qquad f(12)=81>9=f(0)
$$

### Lời giảng

Đạo hàm tại 1,5 bằng −3. Độ dời là 0,75, nên x₂ = 2,25. Giá trị hàm tiếp tục giảm còn 0,5625. Bây giờ chỉ thay bước học của bước đầu bằng 2, vẫn là số dương. Ta đến x₁ = 12 và giá trị hàm bằng 81, lớn hơn 9. Ví dụ này cho thấy α > 0 chưa đủ để bảo đảm giảm. Nó không phủ nhận kết quả vừa tính với α = 1/4 và cũng không chứng minh một điều kiện chọn bước cho mọi hàm.

### Note tự học

Lời giải Slide 4: f′(1,5) = 2(1,5 − 3) = −3. Do đó x₂ = 1,5 − (1/4)(−3) = 2,25 và f(x₂) = (2,25 − 3)² = 0,5625. Giá trị này nhỏ hơn f(x₁) = 2,25. Để kiểm tra giới hạn của quy tắc, giữ f và x₀ = 0 nhưng thay riêng α bằng 2. Khi đó x₁ = 12, f(x₁) = 81 > 9. Đây là ví dụ bổ sung để bác bỏ phát biểu “mọi bước học dương đều làm hàm giảm”. Không suy từ ví dụ rằng mọi α lớn đều thất bại hoặc mọi α nhỏ đều hội tụ.

Câu nối: α là tham số cập nhật. Nguồn còn có một tham số khác trong bài có ràng buộc.

<a id="slide-6"></a>
## Slide 6: Với h(x) = 0, lập hàm Lagrange

Thời gian dự kiến: 1.75 phút.

### Chữ trên slide

$$
h(x)=0,\qquad L(x,\nu)=f(x)+\nu h(x)
$$

Ràng buộc đẳng thức yêu cầu chỉ xét x thỏa h(x) = 0. ν là nhân tử Lagrange.

Trong quy ước này, ν không bị giới hạn dấu.

$$
\text{Ví dụ: } h(x)=x-1,\qquad L(x,\nu)=(x-3)^2+\nu(x-1)
$$

Điều kiện x − 1 = 0 chỉ cho phép x = 1. Bài này chỉ học cách lập L.

### Lời giảng

Nguồn chuyển sang một bài toán khác: x còn phải thỏa h(x) = 0. Ví dụ x − 1 = 0 chỉ cho phép x = 1. Hàm Lagrange kết hợp hàm mục tiêu với ν lần h(x); ν được gọi là nhân tử Lagrange. Nguồn quy định ν không bị giới hạn dấu cho ràng buộc đẳng thức. Ta giữ đúng quy ước dấu cộng trước νh(x). Ta chưa học điều kiện tìm ν hay cách giải tối ưu có ràng buộc trong buổi này.

### Note tự học

Ràng buộc đẳng thức h(x) = 0 giới hạn các giá trị x được phép xét. Hàm Lagrange trong nguồn được định nghĩa bởi L(x,ν) = f(x) + νh(x). ν là nhân tử Lagrange và không bị giới hạn dấu trong quy ước này. Với ví dụ bổ sung h(x) = x − 1 và hàm mục tiêu cũ, L(x,ν) = (x − 3)² + ν(x − 1). Ràng buộc chỉ cho phép x = 1. Khi x thỏa h(x) = 0, số hạng νh(x) bằng 0, nên L(x,ν) = f(x) với mọi ν. Quan sát này là phép thay vào công thức; nó không chọn ν hay chứng minh các điều kiện tối ưu. Bài chỉ giới thiệu cách lập L và quy ước dấu của ν.

Câu nối: Dấu của ν có giống điều kiện αₖ > 0 không?

<a id="slide-7"></a>
## Slide 7: ν = −2 có bị loại vì âm không?

Thời gian dự kiến: 1.25 phút.

### Chữ trên slide

$$
L(x,\nu)=f(x)+\nu h(x),\qquad h(x)=x-1
$$

Một bạn viết: “αₖ > 0, nên ν cũng phải > 0.” Suy luận này đúng không?

Nếu ν = −2, hãy viết L(x, −2). Có bị loại chỉ vì ν âm không?

### Lời giảng

Chờ 25 giây để người học viết một câu giải thích và biểu thức L(x, −2). Cần phân biệt điều kiện đối với bước học αₖ và quy ước đối với nhân tử ν. Không yêu cầu tìm ν tối ưu. Nếu người học nói ν = −2 chắc chắn là nghiệm, nhắc rằng câu hỏi chỉ kiểm tra dấu có được phép hay không.

### Note tự học

Tự trả lời trước khi xem Slide 8: αₖ > 0 có kéo theo ν > 0 không? Với h(x) = x − 1 và ν = −2, hãy viết L(x, −2). Đánh giá riêng hai việc: giá trị ν âm có được phép theo quy ước đẳng thức hay không, và bài đã đủ thông tin để khẳng định ν ấy là một nhân tử của nghiệm hay chưa.

Câu nối: Ta sửa suy luận về dấu và nhắc lại việc từng tham số làm.

<a id="slide-8"></a>
## Slide 8: Hai tham số có hai vai trò khác nhau

Thời gian dự kiến: 1.5 phút.

### Chữ trên slide

$$
L(x,-2)=f(x)-2(x-1)
$$

| Tham số | Vai trò | Điều kiện dấu trong nguồn |
| --- | --- | --- |
| αₖ | Điều chỉnh bước cập nhật | αₖ > 0 |
| ν | Nhân h(x) trong L | Không bị giới hạn dấu |

ν = −2 được phép về dấu; ta chưa kết luận đó là nhân tử tại nghiệm.

Một bước gradient descent: lấy đạo hàm tại xₖ, tính độ dời, tìm xₖ₊₁, rồi kiểm tra giá trị hàm.

### Lời giảng

Suy luận ở trang trước không đúng. αₖ và ν có hai vai trò khác nhau, nên điều kiện dấu của αₖ không chuyển sang ν. Với ν = −2, L(x, −2) = f(x) − 2(x − 1). Giá trị âm được phép về dấu, nhưng chưa có kết luận rằng đây là nhân tử tại nghiệm. Dành 15 giây để người học nói lại quy trình bước cập nhật: đạo hàm tại xₖ, độ dời, điểm mới, kiểm tra f. Nhắc rằng bước học dương vẫn có thể làm f tăng như ví dụ α = 2.

### Note tự học

Lời giải Slide 7: từ L(x,ν) = f(x) + νh(x), thay h(x) = x − 1 và ν = −2 được L(x,−2) = f(x) − 2(x − 1). ν không bị giới hạn dấu đối với ràng buộc đẳng thức trong nguồn, nên không loại giá trị −2 chỉ vì nó âm. Điều kiện αₖ > 0 thuộc quy tắc gradient descent, nơi αₖ điều chỉnh bước cập nhật; ν thuộc hàm Lagrange, nơi nó nhân h(x). Bài chưa cung cấp các điều kiện để tìm nhân tử tại nghiệm. Để thực hiện gradient descent một biến, tính f′(xₖ), tính −αₖf′(xₖ), cộng độ dời vào xₖ, rồi kiểm tra f(xₖ₊₁). Kiểm tra bằng ví dụ không thay thế định lý hội tụ.

Câu nối: Kết thúc bài; xem note để tự làm lại hai checkpoint.

## Nguồn và phạm vi bổ sung

Nguồn duy nhất là ba câu tự viết do người dùng cung cấp; không có sách, số trang hoặc hình nguồn. SRC-01 là quy tắc cập nhật; SRC-02 là ví dụ; SRC-03 là ràng buộc đẳng thức, L và dấu ν. Tất cả đều có mặt trong tuyến chính.

Phần bổ sung sư phạm gồm cách đọc gradient một biến, các phép tính x₁ và x₂, thử α = 2, ví dụ h(x) = x − 1 và hai checkpoint. Các phần này có lý do và liên kết nguồn trong course-spec.json; không gán chúng cho tác giả nguồn.

Không mở rộng sang điều kiện tối ưu có ràng buộc, KKT hay định lý hội tụ. Thời gian 12 phút là ước lượng, gồm 35 giây tự tính ở Slide 4, 25 giây ở Slide 7 và 15 giây nhắc lại ở Slide 8.

## Giới hạn kiểm tra

Không render theo yêu cầu của môi trường đánh giá. Chưa kiểm chứng kích thước chữ, glyph tiếng Việt, font toán, ngắt dòng, tương phản trên output cuối hoặc chất lượng bố cục. Audit cấu trúc không chứng minh hiệu quả học tập hay chất lượng hình thức. Kết quả audit và phép tính được lưu riêng cùng thư mục.
