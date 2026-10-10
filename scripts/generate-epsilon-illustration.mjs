import { writeFileSync } from 'node:fs'

// Mô hình: f0(x) = x², miền khả thi [1, 3], p* = 1, epsilon = 3.
const X = x => 54 + 88 * x
const Y = y => 342 - 28 * y
const curve = (a, b) => Array.from({ length: 81 }, (_, i) => {
  const x = a + (b - a) * i / 80
  return `${i ? 'L' : 'M'}${X(x).toFixed(3)} ${Y(x * x).toFixed(3)}`
}).join(' ')
const dot = (name, x, tx, ty, color) => `<circle cx="${X(x)}" cy="${Y(x*x)}" r="5.5" fill="${color}" stroke="#fff" stroke-width="2"/><text x="${tx}" y="${ty}" font-size="20" font-weight="700" fill="${color}">${name}</text>`
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 502" width="100%" role="img" aria-labelledby="title desc">
<title id="title">Phân biệt tính khả thi và mức sai số gần tối ưu</title>
<desc id="desc">Đồ thị x bình phương trên miền khả thi từ 1 đến 3. Giá trị tối ưu là 1, ngưỡng gần tối ưu là 4. A tại x bằng 0.5 không khả thi. S tại x bằng 1 tối ưu. B tại x bằng 1.5 gần tối ưu. D tại x bằng 2 nằm đúng ngưỡng. C tại x bằng 2.5 khả thi nhưng vượt sai số cho phép. Khoảng gần tối ưu trên trục x là đoạn đóng từ 1 đến 2.</desc>
<defs><pattern id="infeasible" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#f1eff5"/><path d="M0 10L10 0" stroke="#dcd8e8" stroke-width="1"/></pattern></defs>
<rect x="1" y="1" width="438" height="500" rx="10" fill="#fff" stroke="#dcd8e8"/>
<g font-family="system-ui, -apple-system, 'Segoe UI', sans-serif" font-size="18" fill="#1f1c2b">
<text x="24" y="30" font-size="20" font-weight="600">Điểm nào gần tối ưu?</text>
<text x="24" y="56">Hàm mục tiêu: f₀(x) = x²</text>
<!-- Vạch xiên biểu diễn phần x nhỏ hơn 1, nằm ngoài miền khả thi. -->
<rect x="54" y="90" width="88" height="252" fill="url(#infeasible)"/>
<rect x="142" y="230" width="176" height="84" fill="#e6f4ec"/>
<path d="M142 90V342M230 230V342M318 90V342" stroke="#8a849f" stroke-width="1" stroke-dasharray="3 5"/>
<path d="M54 314H355M54 230H355" stroke="#1d6b45" stroke-width="1.5" stroke-dasharray="6 4"/>
<path d="M54 167H274" stroke="#8a5100" stroke-width="1" stroke-dasharray="3 5"/>
<path d="M54 279H186" stroke="#1d6b45" stroke-width="1" stroke-dasharray="3 5"/>
<path d="M54 90V349M48 342H330" stroke="#4f4a62" stroke-width="1.8" fill="none"/>
<g text-anchor="end" fill="#4f4a62" font-size="16">
<text x="46" y="348">0</text><text x="46" y="320">1</text><text x="46" y="285">2.25</text><text x="46" y="236">4</text><text x="46" y="173">6.25</text><text x="46" y="96">9</text>
</g>
<text x="57" y="82" font-style="italic">f₀(x)</text>
<path d="${curve(0,1)}" fill="none" stroke="#6b6580" stroke-width="3" stroke-dasharray="5 4"/>
<path d="${curve(1,2)}" fill="none" stroke="#1d6b45" stroke-width="4"/>
<path d="${curve(2,3)}" fill="none" stroke="#8a5100" stroke-width="4"/>
<!-- A có giá trị nhỏ nhưng bị loại vì vi phạm ràng buộc. -->
<path d="M93 330L103 340M103 330L93 340" stroke="#6b6580" stroke-width="3"/>
<text x="76" y="327" font-size="20" font-weight="700" fill="#6b6580">A</text>
${dot('S',1,153,335,'#1d6b45')}
${dot('B',1.5,164,271,'#1d6b45')}
${dot('D',2,211,217,'#1d6b45')}
${dot('C',2.5,292,182,'#8a5100')}
<text x="265" y="210" font-weight="600" fill="#1d6b45">p* + ε = 4</text>
<text x="293" y="335" font-weight="600" fill="#1d6b45">p* = 1</text>
<!-- Epsilon là khoảng cách theo trục giá trị mục tiêu giữa hai đường mức. -->
<path d="M363 230H373M368 230V314M363 314H373" stroke="#5a37a8" stroke-width="2" fill="none"/>
<text x="380" y="278" font-weight="600" fill="#5a37a8">ε = 3</text>
<g text-anchor="middle" font-size="16" fill="#4f4a62">
${[0,0.5,1,1.5,2,2.5,3].map(x=>`<path d="M${X(x)} 342v5" stroke="#4f4a62"/><text x="${X(x)}" y="366">${x}</text>`).join('\n')}
</g>
<text x="333" y="366" font-style="italic">x</text>
<!-- Các khoảng của biến x được tách riêng khỏi các mức của hàm mục tiêu. -->
<path d="M54 396H142" stroke="#6b6580" stroke-width="5" stroke-dasharray="4 3"/>
<path d="M142 396H230" stroke="#1d6b45" stroke-width="6"/>
<path d="M230 396H318" stroke="#8a5100" stroke-width="5"/>
<circle cx="142" cy="396" r="5" fill="#1d6b45"/><circle cx="230" cy="396" r="5" fill="#1d6b45"/><circle cx="318" cy="396" r="5" fill="#8a5100"/>
<g text-anchor="middle" font-size="16">
<text x="98" y="426" fill="#6b6580">Không</text><text x="98" y="450" fill="#6b6580">khả thi</text><text x="98" y="476" fill="#6b6580">0 ≤ x &lt; 1</text>
<text x="186" y="426" fill="#1d6b45">Gần tối ưu</text><text x="186" y="450" fill="#1d6b45">Kể cả biên</text><text x="186" y="476" fill="#1d6b45">1 ≤ x ≤ 2</text>
<text x="286" y="426" fill="#8a5100">Khả thi,</text><text x="286" y="450" fill="#8a5100">vượt ngưỡng</text><text x="286" y="476" fill="#8a5100">2 &lt; x ≤ 3</text>
</g>
</g></svg>
`
writeFileSync(new URL('../docs/toan-cho-ai/bai-giang/img/lec-01/epsilon-gan-toi-uu.svg', import.meta.url), svg)
