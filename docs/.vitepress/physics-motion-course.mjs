export const physicsMotionSlides = []

export const physicsMotionCheatsheet = {
  summary: 'Tra cứu từ tóm tắt chương 2 và mục 2.1–2.6 của Young & Freedman, trang in 34–56. Công thức luôn đi cùng quy ước trục và điều kiện áp dụng.',
  sections: [
    { id: 'definitions', title: 'Định nghĩa và đơn vị', badge: 'Mục 2.1–2.3', items: [
      { name: 'Độ dời và vận tốc trung bình', formula: '$$\\Delta x=x_2-x_1,\\qquad v_{\\mathrm{av}-x}=\\frac{\\Delta x}{\\Delta t},\\quad\\Delta t>0$$', description: 'Tọa độ và độ dời tính bằng mét; vận tốc tính bằng m/s. Độ dời và vận tốc theo trục có thể dương, âm hoặc bằng không.' },
      { name: 'Vận tốc tức thời và tốc độ', formula: '$$v_x=\\frac{dx}{dt},\\qquad v=|v_x|$$', description: 'Tốc độ tức thời không âm. Tốc độ trung bình bằng toàn bộ quãng đường chia toàn bộ thời gian, khác độ lớn vận tốc trung bình khi hành trình đổi chiều.' },
      { name: 'Gia tốc trung bình và tức thời', formula: '$$a_{\\mathrm{av}-x}=\\frac{\\Delta v_x}{\\Delta t},\\qquad a_x=\\frac{dv_x}{dt}=\\frac{d^2x}{dt^2}$$', description: 'Gia tốc có đơn vị m/s². Trong chuyển động thẳng, gia tốc và vận tốc cùng dấu thì tốc độ tăng, trái dấu thì tốc độ giảm.' }
    ] },
    { id: 'constant-acceleration', title: 'Gia tốc không đổi', badge: 'Mục 2.4', items: [
      { name: 'Bốn phương trình động học', formula: '$$\\begin{aligned}v_x&=v_{0x}+a_xt\\\\x-x_0&=v_{0x}t+\\tfrac12a_xt^2\\\\v_x^2-v_{0x}^2&=2a_x(x-x_0)\\\\x-x_0&=\\tfrac12(v_{0x}+v_x)t\\end{aligned}$$', description: 'Chỉ dùng khi aₓ không đổi trên toàn khoảng xét. x₀ và v₀ₓ là điều kiện đầu tại t = 0. Chọn phương trình không chứa đại lượng chưa biết mà đề không yêu cầu.' },
      { name: 'Vận tốc trung bình trong trường hợp này', formula: '$$v_{\\mathrm{av}-x}=\\frac{v_{0x}+v_x}{2}$$', description: 'Quan hệ này theo vận tốc biến thiên tuyến tính theo thời gian; không dùng như định nghĩa tổng quát khi gia tốc thay đổi.' }
    ] },
    { id: 'free-fall', title: 'Rơi tự do', badge: 'Mục 2.5', items: [
      { name: 'Chọn +y hướng lên', formula: '$$\\begin{aligned}a_y&=-g,\\quad g\\approx9.80\\,\\mathrm{m/s^2}>0\\\\v_y&=v_{0y}-gt\\\\y-y_0&=v_{0y}t-\\tfrac12gt^2\\\\v_y^2&=v_{0y}^2-2g(y-y_0)\\end{aligned}$$', description: 'Bỏ lực cản không khí, xét quãng rơi nhỏ so với bán kính Trái Đất và bỏ ảnh hưởng quay. Gia tốc hướng xuống trong cả nhánh đi lên và đi xuống; tại đỉnh vᵧ = 0 nhưng aᵧ = −g.' }
    ] },
    { id: 'graphs', title: 'Đọc đồ thị', badge: 'Mục 2.2–2.3, 2.6', table: {
      headers: ['Đồ thị', 'Độ dốc tiếp tuyến', 'Diện tích có dấu'],
      rows: [['Vị trí x theo thời gian t', 'Vận tốc vₓ', 'Không dùng để tính vận tốc hoặc độ dời'], ['Vận tốc vₓ theo t', 'Gia tốc aₓ', 'Độ dời Δx'], ['Gia tốc aₓ theo t', 'Không dùng trong công thức chương này', 'Độ biến thiên vận tốc Δvₓ']]
    } },
    { id: 'integration', title: 'Gia tốc biến thiên và điều kiện đầu', badge: 'Mục 2.6', items: [
      { name: 'Tích phân giữa hai thời điểm', formula: '$$v_{2x}-v_{1x}=\\int_{t_1}^{t_2}a_x\\,dt,\\qquad x_2-x_1=\\int_{t_1}^{t_2}v_x\\,dt$$', description: 'Các tích phân cho độ biến thiên có dấu. Muốn tìm vận tốc hoặc vị trí tuyệt đối theo mốc tọa độ phải dùng thêm vận tốc đầu hoặc vị trí đầu.' },
      { name: 'Hai vật gặp nhau', formula: '$$x_A(t)=x_B(t)$$', description: 'Theo Ví dụ 2.5, hai vật gặp nhau khi có cùng tọa độ tại cùng thời điểm; vận tốc khi gặp vẫn có thể khác nhau. Phân biệt nghiệm t = 0 với lần đuổi kịp sau đó.' }
    ] }
  ]
}
