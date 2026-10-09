// Các thẻ ôn và bảng tra cứu chỉ rút từ chương 2, không bổ sung ví dụ ngoài sách.
const note = '02-chuyen-dong-thang'
export const physicsMotionSlides = [
  { note, title: 'Độ dời và vận tốc trung bình',
    bullets: ['Chọn trục và chiều dương trước khi lấy tọa độ cuối trừ tọa độ đầu.', 'Vận tốc trung bình phụ thuộc hai đầu khoảng thời gian, không mô tả mọi biến đổi ở bên trong.', 'Trên đồ thị vị trí theo thời gian, vận tốc trung bình là độ dốc dây cung.'],
    formula: '$$\\Delta x=x_2-x_1,\\qquad v_{\\mathrm{av}-x}=\\frac{x_2-x_1}{t_2-t_1},\\quad t_2>t_1$$',
    example: 'Hình 2.1: từ 19 m lúc 1,0 s đến 277 m lúc 4,0 s cho độ dời 258 m và vận tốc trung bình 86 m/s.' },
  { note, title: 'Vận tốc tức thời và tốc độ là hai đại lượng khác nhau',
    bullets: ['Vận tốc tức thời là giới hạn của vận tốc trung bình và bằng độ dốc tiếp tuyến đồ thị vị trí.', 'Tốc độ tức thời là độ lớn vận tốc; tốc độ trung bình dùng quãng đường thay cho độ dời.', 'Đi rồi trở về điểm đầu có thể có vận tốc trung bình bằng không dù tốc độ trung bình dương.'],
    formula: '$$v_x=\\frac{dx}{dt},\\qquad v=|v_x|$$',
    example: 'Ví dụ 2.1: báo có vận tốc trung bình 15 m/s từ 1,0 s đến 2,0 s; vận tốc tức thời tại 1,0 s là 10 m/s.' },
  { note, title: 'Dấu của gia tốc cần được xét cùng dấu vận tốc',
    bullets: ['Gia tốc trung bình bằng độ biến thiên vận tốc chia khoảng thời gian.', 'Gia tốc tức thời là độ dốc tiếp tuyến của đồ thị vận tốc theo thời gian.', 'Trong chuyển động thẳng, cùng dấu vận tốc và gia tốc thì nhanh dần; trái dấu thì chậm dần.'],
    formula: '$$a_{\\mathrm{av}-x}=\\frac{v_{2x}-v_{1x}}{t_2-t_1},\\qquad a_x=\\frac{dv_x}{dt}=\\frac{d^2x}{dt^2}$$',
    example: 'Ví dụ 2.2(c): vận tốc giảm từ −0,4 đến −1,0 m/s trong 2,0 s; gia tốc trung bình âm nhưng tốc độ tăng.' },
  { note, title: 'Bốn phương trình dùng khi gia tốc không đổi',
    bullets: ['Vị trí đầu và vận tốc đầu phải được xác định ở cùng mốc t = 0.', 'Chọn phương trình theo đại lượng đã biết và đại lượng cần tìm; giải bằng ký hiệu trước khi thay số.', 'Vận tốc trung bình bằng nửa tổng vận tốc đầu và cuối trong trường hợp gia tốc không đổi.'],
    formula: '$$\\begin{aligned}v_x&=v_{0x}+a_xt\\\\x&=x_0+v_{0x}t+\\tfrac12a_xt^2\\\\v_x^2&=v_{0x}^2+2a_x(x-x_0)\\\\x-x_0&=\\tfrac12(v_{0x}+v_x)t\\end{aligned}$$',
    example: 'Ví dụ 2.4: x₀ = 5,0 m, v₀ₓ = 15 m/s, aₓ = 4,0 m/s² cho x = 43 m và vₓ = 23 m/s tại t = 2,0 s.' },
  { note, title: 'Rơi tự do gồm cả lúc đi lên và lúc đi xuống',
    bullets: ['Bỏ lực cản không khí và xét gần mặt đất để coi gia tốc trọng trường không đổi.', 'Độ lớn g dương; chọn trục thẳng đứng hướng lên thì thành phần gia tốc âm.', 'Ở điểm cao nhất, vận tốc bằng không nhưng gia tốc vẫn hướng xuống.'],
    formula: '$$a_y=-g,\\qquad y=y_0+v_{0y}t-\\tfrac12gt^2,\\qquad v_y=v_{0y}-gt$$',
    example: 'Ví dụ 2.7: bóng rời tay với 15,0 m/s hướng lên đạt độ cao cực đại khoảng 11,5 m so với tay.' },
  { note, title: 'Tích phân nối gia tốc, vận tốc và vị trí',
    bullets: ['Nếu biết gia tốc theo thời gian, tích phân một lần và dùng vận tốc đầu để tìm vận tốc.', 'Tích phân vận tốc và dùng vị trí đầu để tìm vị trí.', 'Diện tích có dấu dưới đồ thị gia tốc cho biến thiên vận tốc; dưới đồ thị vận tốc cho độ dời.'],
    formula: '$$v_x=v_{0x}+\\int_0^t a_x\\,dt,\\qquad x=x_0+\\int_0^t v_x\\,dt$$',
    example: 'Ví dụ 2.9: aₓ = 2,0 m/s² − (0,10 m/s³)t cho vận tốc lớn nhất 30 m/s tại t = 20 s, khi x ≈ 517 m.' }
]

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
