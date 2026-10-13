export const physicsMotionSlides = []
const d=tex=>'$$\n'+tex+'\n$$'
export const physicsMotionCheatsheet={
 summary:'Định nghĩa, tính chất và công thức của chuyển động thẳng, cùng quy ước trục và điều kiện áp dụng.',
 sections:[
  {id:'definitions',title:'Định nghĩa và đơn vị',badge:'Mục 2.1–2.3',items:[
   {name:'Độ dời và vận tốc trung bình',formulaRows:[
    {label:'Độ dời giữa hai thời điểm',formula:d(String.raw`\Delta x=x_2-x_1`)},
    {label:'Vận tốc trung bình, Δt > 0',formula:d(String.raw`v_{\mathrm{av}-x}=\Delta x/\Delta t`)}
   ],variables:[
    String.raw`$\Delta x$: Độ dời của chất điểm dọc theo trục $x$ ($\mathrm{m}$)`,
    String.raw`$x_1, x_2$: Tọa độ vị trí tại các thời điểm $t_1, t_2$ ($\mathrm{m}$)`,
    String.raw`$v_{\mathrm{av}-x}$: Vận tốc trung bình theo trục $x$ ($\mathrm{m/s}$)`,
    String.raw`$\Delta t$: Khoảng thời gian chuyển động ($\mathrm{s}$)`
   ],description:'Tọa độ và độ dời tính bằng mét, vận tốc tính bằng m/s. Độ dời và vận tốc theo trục có thể dương, âm hoặc bằng không.'},
   {name:'Vận tốc tức thời và tốc độ',formulaRows:[
    {label:'Vận tốc theo trục x',formula:d(String.raw`v_x=dx/dt`)},
    {label:'Tốc độ tức thời',formula:d(String.raw`v=|v_x|`)}
   ],variables:[
    String.raw`$v_x$: Vận tốc tức thời theo trục $x$ ($\mathrm{m/s}$)`,
    String.raw`$x$: Tọa độ vị trí theo hàm thời gian $t$ ($\mathrm{m}$)`,
    String.raw`$t$: Thời điểm khảo sát chuyển động ($\mathrm{s}$)`,
    String.raw`$v$: Tốc độ tức thời ($\mathrm{m/s}$)`
   ],description:'Tốc độ tức thời không âm. Tốc độ trung bình bằng toàn bộ quãng đường chia toàn bộ thời gian, khác độ lớn vận tốc trung bình khi hành trình đổi chiều.'},
   {name:'Gia tốc trung bình và tức thời',formulaRows:[
    {label:'Gia tốc trung bình, Δt > 0',formula:d(String.raw`a_{\mathrm{av}-x}=\Delta v_x/\Delta t`)},
    {label:'Đạo hàm của vận tốc',formula:d(String.raw`a_x=dv_x/dt`)},
    {label:'Đạo hàm bậc hai của vị trí',formula:d(String.raw`a_x=d^2x/dt^2`)}
   ],variables:[
    String.raw`$a_{\mathrm{av}-x}$: Gia tốc trung bình theo trục $x$ ($\mathrm{m/s^2}$)`,
    String.raw`$a_x$: Gia tốc tức thời theo trục $x$ ($\mathrm{m/s^2}$)`,
    String.raw`$\Delta v_x$: Độ biến thiên vận tốc theo trục $x$ ($\mathrm{m/s}$)`,
    String.raw`$\Delta t$: Khoảng thời gian xảy ra biến thiên vận tốc ($\mathrm{s}$)`
   ],description:'Gia tốc có đơn vị m/s². Trong chuyển động thẳng, gia tốc và vận tốc cùng dấu thì tốc độ tăng, trái dấu thì tốc độ giảm.'}
  ]},
  {id:'constant-acceleration',title:'Gia tốc không đổi',badge:'Mục 2.4',items:[
   {name:'Bốn phương trình động học',formulaRows:[
    {label:'Vận tốc sau thời gian t',formula:d(String.raw`v_x=v_{0x}+a_xt`)},
    {label:'Độ dời sau thời gian t',formula:d(String.raw`x-x_0=v_{0x}t+\tfrac12a_xt^2`)},
    {label:'Quan hệ không chứa thời gian',formula:d(String.raw`v_x^2-v_{0x}^2=2a_x(x-x_0)`)},
    {label:'Độ dời theo hai vận tốc đầu, cuối',formula:d(String.raw`x-x_0=\tfrac12(v_{0x}+v_x)t`)}
   ],variables:[
    String.raw`$v_x$: Vận tốc tức thời tại thời điểm $t$ ($\mathrm{m/s}$)`,
    String.raw`$v_{0x}$: Vận tốc ban đầu tại thời điểm $t = 0$ ($\mathrm{m/s}$)`,
    String.raw`$a_x$: Gia tốc không đổi theo trục $x$ ($\mathrm{m/s^2}$)`,
    String.raw`$x - x_0$: Độ dời của vật từ vị trí ban đầu $x_0$ đến vị trí $x$ ($\mathrm{m}$)`,
    String.raw`$t$: Thời gian chuyển động ($\mathrm{s}$)`
   ],description:'Các phương trình dùng khi gia tốc không đổi trên toàn khoảng xét. Vị trí đầu và vận tốc đầu là điều kiện tại t = 0.'},
   {name:'Vận tốc trung bình trong trường hợp này',formula:d(String.raw`v_{\mathrm{av}-x}=\frac{v_{0x}+v_x}{2}`),variables:[
    String.raw`$v_{\mathrm{av}-x}$: Vận tốc trung bình khi gia tốc biến thiên tuyến tính ($\mathrm{m/s}$)`,
    String.raw`$v_{0x}$: Vận tốc ban đầu ($\mathrm{m/s}$)`,
    String.raw`$v_x$: Vận tốc tức thời cuối khoảng xét ($\mathrm{m/s}$)`
   ],description:'Quan hệ này theo vận tốc biến thiên tuyến tính theo thời gian, không dùng như định nghĩa tổng quát khi gia tốc thay đổi.'}
  ]},
  {id:'free-fall',title:'Rơi tự do',badge:'Mục 2.5',items:[
   {name:'Chọn +y hướng lên',formulaRows:[
    {label:'Gia tốc hướng xuống',formula:d(String.raw`a_y=-g`)},
    {label:'Độ lớn gia tốc trọng trường, g > 0',formula:d(String.raw`g\approx9.80\,\mathrm{m/s^2}`)},
    {label:'Vận tốc sau thời gian t',formula:d(String.raw`v_y=v_{0y}-gt`)},
    {label:'Độ dời theo thời gian',formula:d(String.raw`y-y_0=v_{0y}t-\tfrac12gt^2`)},
    {label:'Quan hệ không chứa thời gian',formula:d(String.raw`v_y^2=v_{0y}^2-2g(y-y_0)`)}
   ],variables:[
    String.raw`$a_y$: Gia tốc theo trục thẳng đứng hướng lên ($\mathrm{m/s^2}$)`,
    String.raw`$g$: Gia tốc rơi tự do gần mặt đất ($\approx 9{,}80\,\mathrm{m/s^2}$)`,
    String.raw`$v_y$: Vận tốc theo trục thẳng đứng tại thời điểm $t$ ($\mathrm{m/s}$)`,
    String.raw`$v_{0y}$: Vận tốc ban đầu theo trục thẳng đứng ($\mathrm{m/s}$)`,
    String.raw`$y - y_0$: Độ dời thẳng đứng từ vị trí ban đầu $y_0$ ($\mathrm{m}$)`,
    String.raw`$t$: Thời gian rơi tự do ($\mathrm{s}$)`
   ],description:'Bỏ lực cản không khí, xét quãng rơi nhỏ so với bán kính Trái Đất và bỏ ảnh hưởng quay. Gia tốc hướng xuống trong cả nhánh đi lên và đi xuống. Tại đỉnh vᵧ = 0 nhưng aᵧ = −g.'}
  ]},
  {id:'graphs',title:'Đọc đồ thị',badge:'Mục 2.2–2.3, 2.6',table:{
   headers:['Đồ thị','Độ dốc tiếp tuyến','Diện tích có dấu'],
   rows:[['Vị trí x theo thời gian t','Vận tốc vₓ','Không dùng để tính vận tốc hoặc độ dời'],['Vận tốc vₓ theo t','Gia tốc aₓ','Độ dời Δx'],['Gia tốc aₓ theo t','Không dùng trong công thức chương này','Độ biến thiên vận tốc Δvₓ']]
  }},
  {id:'integration',title:'Gia tốc biến thiên và điều kiện đầu',badge:'Mục 2.6',items:[
   {name:'Tích phân giữa hai thời điểm',formulaRows:[
    {label:'Độ biến thiên vận tốc',formula:d(String.raw`v_{2x}-v_{1x}=\int_{t_1}^{t_2}a_x\,dt`)},
    {label:'Độ dời',formula:d(String.raw`x_2-x_1=\int_{t_1}^{t_2}v_x\,dt`)}
   ],variables:[
    String.raw`$v_{1x}, v_{2x}$: Vận tốc tức thời tại các thời điểm $t_1, t_2$ ($\mathrm{m/s}$)`,
    String.raw`$x_1, x_2$: Tọa độ vị trí tại các thời điểm $t_1, t_2$ ($\mathrm{m}$)`,
    String.raw`$a_x(t)$: Gia tốc tức thời biến thiên theo thời gian ($\mathrm{m/s^2}$)`,
    String.raw`$v_x(t)$: Vận tốc tức thời biến thiên theo thời gian ($\mathrm{m/s}$)`,
    String.raw`$t_1, t_2$: Các thời điểm giới hạn khoảng tích phân ($\mathrm{s}$)`
   ],description:'Các tích phân cho độ biến thiên có dấu. Muốn tìm vận tốc hoặc vị trí tuyệt đối theo mốc tọa độ phải dùng thêm vận tốc đầu hoặc vị trí đầu.'},
   {name:'Hai vật gặp nhau',formula:d(String.raw`x_A(t)=x_B(t)`),variables:[
    String.raw`$x_A(t), x_B(t)$: Tọa độ vị trí của hai vật $A$ và $B$ theo thời gian ($\mathrm{m}$)`,
    String.raw`$t$: Thời điểm hai vật gặp nhau tại cùng tọa độ ($\mathrm{s}$)`
   ],description:'Hai vật gặp nhau khi có cùng tọa độ tại cùng thời điểm. Vận tốc của chúng khi gặp có thể khác nhau.'}
  ]}
 ]
}
