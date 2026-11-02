import {mkdir,readFile,writeFile} from 'node:fs/promises'
import path from 'node:path'
const target=path.resolve('../math-ai-visual-content/docs/toan-cho-ai/bai-giang/img/lec-02/sparse-count-envelope.svg')
const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300" role="img" aria-labelledby="title desc">
<title id="title">Hàm đếm một chiều và bao lồi dưới</title>
<desc id="desc">Trên đoạn từ âm một tới một, hàm đếm bằng một trừ tại gốc bằng không. Đồ thị trị tuyệt đối nối gốc tới hai đầu mút và là hàm lồi lớn nhất không vượt hàm đếm.</desc>
<rect width="400" height="300" rx="10" fill="#fffdf8"/>
<g font-family="Segoe UI,Arial,sans-serif" font-size="20" fill="#242038">
<path d="M35 30H65" stroke="#7658b1" stroke-width="2.3"/><text x="78" y="37">ℓ₀(t)</text>
<path d="M230 30H260" stroke="#24734a" stroke-width="2.3"/><text x="273" y="37">|t|</text>
<path d="M30 245H370 M200 55V265" stroke="#888394" stroke-width="1" fill="none"/>
<path d="M50 75H192 M208 75H350" stroke="#7658b1" stroke-width="2.3" fill="none"/>
<path d="M50 75L200 245L350 75" stroke="#24734a" stroke-width="2.3" fill="none"/>
<circle cx="200" cy="75" r="7" fill="#fffdf8" stroke="#7658b1" stroke-width="2.1"/>
<g fill="#242038"><circle cx="50" cy="75" r="4"/><circle cx="350" cy="75" r="4"/><circle cx="200" cy="245" r="5"/></g>
<text x="12" y="82">1</text><text x="38" y="275">−1</text><text x="208" y="275">0</text><text x="344" y="275">1</text><text x="375" y="250">t</text>
</g></svg>
`
await mkdir(path.dirname(target),{recursive:true})
let previous
try{previous=await readFile(target,'utf8')}catch(error){if(error.code!=='ENOENT')throw error}
if(previous&&previous!==svg)throw Error('Preserve unexpected existing figure edits; inspect before replacing')
if(!previous)await writeFile(target,svg)
console.log('Sparse-count envelope SVG is reproducible and present in the course checkout')
