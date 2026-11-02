import { mkdir, writeFile } from 'node:fs/promises'
import { resolve } from 'node:path'
const root = resolve(process.argv[2] || '../math-ai-visual-content')
const dir = resolve(root, 'docs/toan-cho-ai/bai-giang/img/lec-00')
await mkdir(dir, { recursive: true })
const start = (height, title, desc) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 ${height}" width="100%" role="img" aria-labelledby="title desc"><title id="title">${title}</title><desc id="desc">${desc}</desc><style>text{font-family:system-ui,'Segoe UI',sans-serif;fill:#302b38;font-size:17px}.title{font-size:20px;font-weight:650}.muted{fill:#625a6a}.card{fill:#fff;stroke:#d7cfde;stroke-width:1.4}.ink{fill:#77519d}.good{fill:#39715a}.arrow{fill:none;stroke:#77519d;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}</style><rect width="360" height="${height}" fill="#fbf8fd"/>`
const arrow = y => `<path d="M180 ${y}v27m-7-7 7 7 7-7" class="arrow"/>`
const grid = (x, y, values) => values.flatMap((row, i) => row.map((v, j) => `<rect x="${x + j*44}" y="${y + i*32}" width="44" height="32" fill="${v === '0' ? '#f1edf5' : '#e5d9ef'}" stroke="#fff"/><text x="${x+j*44+22}" y="${y+i*32+22}" text-anchor="middle">${v}</text>`)).join('')
const card = (y, number, title, content) => `<rect x="14" y="${y}" width="332" height="136" rx="12" class="card"/><text x="30" y="${y+30}" class="title">${number}. ${title}</text>${content}`
let cholesky = start(600, 'Giải hệ qua phân tích Cholesky', 'Phân tích H thành LL chuyển vị, giải thế tiến tìm y, rồi thế lùi tìm x. Với H bằng 4,2;2,3 và b bằng 6,5, nghiệm là 1,1.')
cholesky += '<text x="20" y="29" class="title">Một phép phân tích, hai bước thế</text>'
cholesky += card(48, '1', 'Phân tích H = LLᵀ', grid(34, 95, [['2', '0'], ['1', '√2']]) + '<text x="144" y="118">L: Tam giác dưới</text><text x="144" y="149" class="muted">Hệ số được giữ lại</text>')
cholesky += arrow(191)
cholesky += card(230, '2', 'Thế tiến: Ly = b', '<text x="34" y="288">Hàng đầu tìm y₁ = 3</text><text x="34" y="321">Hàng sau dùng y₁ tìm y₂ = √2</text><path d="M319 278v45m-5-7 5 7 5-7" class="arrow"/>')
cholesky += arrow(373)
cholesky += card(412, '3', 'Thế lùi: Lᵀx = y', '<text x="34" y="470">Hàng cuối tìm x₂ = 1</text><text x="34" y="503">Hàng đầu dùng x₂ tìm x₁ = 1</text><path d="M319 512v-45m-5 7 5-7 5 7" class="arrow"/>')
cholesky += '<text x="20" y="580" class="good">Kiểm tra: H(1, 1)ᵀ = (6, 5)ᵀ</text></svg>'
await writeFile(resolve(dir, 'cholesky-process.svg'), cholesky)
let band = start(506, 'Ma trận đặc và ma trận băng', 'Hai ma trận cỡ bảy. Ma trận đặc có 49 vị trí cần lưu; ma trận băng với nửa độ rộng băng bằng một có 19 vị trí có thể khác không.')
band += '<text x="20" y="29" class="title">Cùng số hàng, khác cấu trúc</text>'
for (const [top, isBand, label] of [[58, false, 'Ma trận đặc'], [287, true, 'Ma trận băng k = 1']]) {
  band += `<text x="20" y="${top}" font-weight="600">${label}</text>`
  for (let i=0;i<7;i++) for(let j=0;j<7;j++) band += `<rect x="${20+j*24}" y="${top+17+i*24}" width="22" height="22" rx="2" fill="${isBand && Math.abs(i-j)>1 ? '#eae5ee' : '#b398cb'}"/>`
  band += `<text x="212" y="${top+71}">${isBand ? '19' : '49'} vị trí</text><text x="212" y="${top+101}">có thể</text><text x="212" y="${top+131}">khác 0</text>`
}
band += '<text x="20" y="494" class="muted">Ô xám: Bằng 0 theo cấu trúc đã cho.</text></svg>'
await writeFile(resolve(dir, 'dense-and-banded.svg'), band)
console.log('Generated two deterministic Lecture 00 SVG diagrams')
