import fs from 'node:fs'
import path from 'node:path'
import { themePrintedSvg } from './svg-theme.mjs'

const publicDir = path.resolve('docs/public/img/lec-03')
const docDir = path.resolve('docs/giai-thuat-du-lieu/bai-giang/img/lec-03')

for (const dir of [publicDir, docDir]) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true })
}

const svgs = {}

// 1. graph-pages.svg: 4 nodes A, B, C, D
svgs['graph-pages.svg'] = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 440" width="100%" height="100%" style="background:#f8fafc; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#3b82f6"/>
    </marker>
    <marker id="arr-dark" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <linearGradient id="nodeGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
    <linearGradient id="nodeGradA" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#eff6ff"/>
      <stop offset="100%" stop-color="#dbeafe"/>
    </linearGradient>
  </defs>

  <!-- Title / Legend -->
  <text x="340" y="36" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">Đồ thị 4 trang web (Hình 5.1 MMDS - n = 4, m = 8)</text>
  <text x="340" y="58" text-anchor="middle" font-size="12" fill="#64748b">Cạnh j → i biểu diễn trang j trỏ tới trang i (A: dA=3 | B: dB=2 | C: dC=1 | D: dD=2)</text>

  <!-- Directed Edges -->
  <!-- A: (200, 140) | B: (480, 140) | C: (200, 320) | D: (480, 320) -->

  <!-- A -> B: straight top curve -->
  <path d="M 235 130 C 310 105, 370 105, 445 130" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <!-- B -> A: straight bottom curve -->
  <path d="M 445 150 C 370 175, 310 175, 235 150" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- A -> C: straight left curve -->
  <path d="M 190 175 C 170 220, 170 240, 190 285" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <!-- C -> A: straight right curve -->
  <path d="M 210 285 C 230 240, 230 220, 210 175" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- A -> D: diagonal center curve down-right -->
  <path d="M 225 160 C 280 200, 390 260, 450 300" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- B -> D: straight curve right -->
  <path d="M 490 175 C 505 220, 505 240, 490 285" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- D -> B: straight curve left -->
  <path d="M 470 285 C 455 240, 455 220, 470 175" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- D -> C: straight bottom curve -->
  <path d="M 445 330 C 370 355, 310 355, 235 330" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- Nodes -->
  <!-- Node A -->
  <g transform="translate(200, 140)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGradA)" stroke="#2563eb" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="20" font-weight="800" fill="#1e3a8a">A</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#1d4ed8">Bậc ra: 3</text>
  </g>

  <!-- Node B -->
  <g transform="translate(480, 140)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">B</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>

  <!-- Node C -->
  <g transform="translate(200, 320)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">C</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 1</text>
  </g>

  <!-- Node D -->
  <g transform="translate(480, 320)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">D</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>

  <!-- Out degree and matrix insight note -->
  <g transform="translate(340, 230)">
    <rect x="-65" y="-14" width="130" height="28" rx="14" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text y="4" text-anchor="middle" font-size="11" font-weight="600" fill="#334155">Mọi nút đều có 2 cạnh vào</text>
  </g>
</svg>
`

// 2. model-dead-redistribute.svg: Dead end C redistributing mass equally
svgs['model-dead-redistribute.svg'] = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 460" width="100%" height="100%" style="background:#f8fafc; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d97706"/>
    </marker>
  </defs>

  <!-- Title / Legend -->
  <text x="360" y="32" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">Xử lý Nút cụt (Dead End) bằng cơ chế bù điểm toàn cục</text>
  <text x="360" y="52" text-anchor="middle" font-size="12" fill="#64748b">Khi xóa cạnh C → A, C có bậc ra 0. Điểm δ = r_C được phân phối lại đều δ/n = r_C/4 cho cả 4 trang</text>

  <!-- Regular links (dimmed) -->
  <!-- A -> B -->
  <path d="M 235 120 C 310 95, 410 95, 485 120" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- B -> A -->
  <path d="M 485 140 C 410 165, 310 165, 235 140" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- A -> C -->
  <path d="M 190 165 L 190 295" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- A -> D -->
  <path d="M 225 150 L 490 310" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- B -> D -->
  <path d="M 525 165 L 525 295" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- D -> B -->
  <path d="M 505 295 L 505 165" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>
  <!-- D -> C -->
  <path d="M 485 340 L 235 340" fill="none" stroke="#93c5fd" stroke-width="1.8" marker-end="url(#arr-blue)"/>

  <!-- Redistribution from Dead End C (Amber dashed lines) -->
  <!-- C -> A -->
  <path d="M 215 295 C 235 240, 235 220, 215 165" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arr-amber)"/>
  <!-- C -> B -->
  <path d="M 225 315 C 330 250, 410 200, 485 150" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arr-amber)"/>
  <!-- C -> D -->
  <path d="M 235 325 C 320 310, 400 310, 480 325" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arr-amber)"/>
  <!-- C -> C (self loop redistribute) -->
  <path d="M 175 345 C 130 380, 130 300, 170 320" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arr-amber)"/>

  <!-- Nodes -->
  <!-- Node A -->
  <g transform="translate(200, 130)" filter="url(#shadow)">
    <circle r="32" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#1e3a8a">A</text>
    <text y="48" text-anchor="middle" font-size="11" fill="#2563eb">+ β·δ/4</text>
  </g>

  <!-- Node B -->
  <g transform="translate(520, 130)" filter="url(#shadow)">
    <circle r="32" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">B</text>
    <text y="48" text-anchor="middle" font-size="11" fill="#d97706">+ β·δ/4</text>
  </g>

  <!-- Node C (DEAD END) -->
  <g transform="translate(200, 330)" filter="url(#shadow)">
    <circle r="34" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#b45309">C</text>
    <rect x="-42" y="44" width="84" height="22" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text y="59" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c">NÚT CỤT (dC=0)</text>
  </g>

  <!-- Node D -->
  <g transform="translate(520, 330)" filter="url(#shadow)">
    <circle r="32" fill="#ffffff" stroke="#64748b" stroke-width="2"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">D</text>
    <text y="48" text-anchor="middle" font-size="11" fill="#d97706">+ β·δ/4</text>
  </g>

  <!-- Bottom Explanatory Box -->
  <g transform="translate(360, 415)">
    <rect x="-240" y="-18" width="480" height="36" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1.2"/>
    <text y="4" text-anchor="middle" font-size="12" font-weight="600" fill="#92400e">
      Phần bù chung: [(1 − β) + β·δ] / n bảo toàn tổng phân phối xác suất ∑ r_i = 1
    </text>
  </g>
</svg>
`

// 3. rlarge-blocks-grid.svg: Block partition k=2
svgs['rlarge-blocks-grid.svg'] = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480" width="100%" height="100%" style="background:#f8fafc; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Header -->
  <text x="380" y="32" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">Chia khối ma trận liên kết theo MapReduce (MMDS 5.2.3–5.2.4)</text>
  <text x="380" y="52" text-anchor="middle" font-size="12" fill="#64748b">Chia vector thành k = 2 dải và ma trận M₀ thành k² = 4 khối để mỗi tác vụ Map vừa RAM</text>

  <!-- Matrix Grid Outer Frame -->
  <!-- Center matrix at (260, 120) to (580, 420): size 320x280 -->

  <!-- Column Headers: Source Strips V_b -->
  <rect x="260" y="75" width="150" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="335" y="94" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8">Dải nguồn 1: V₁ = {A, B}</text>
  <text x="335" y="106" text-anchor="middle" font-size="10" fill="#3b82f6">Vector đầu vào: r₁ = [rA, rB]ᵀ</text>

  <rect x="430" y="75" width="150" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="505" y="94" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8">Dải nguồn 2: V₂ = {C, D}</text>
  <text x="505" y="106" text-anchor="middle" font-size="10" fill="#3b82f6">Vector đầu vào: r₂ = [rC, rD]ᵀ</text>

  <!-- Row Headers: Destination Strips U_a -->
  <rect x="45" y="130" width="195" height="125" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="142" y="180" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Dải đích 1: U₁ = {A, B}</text>
  <text x="142" y="200" text-anchor="middle" font-size="11" fill="#16a34a">Tích lũy ra: z₁ = [zA, zB]ᵀ</text>

  <rect x="45" y="275" width="195" height="125" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="142" y="325" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Dải đích 2: U₂ = {C, D}</text>
  <text x="142" y="345" text-anchor="middle" font-size="11" fill="#16a34a">Tích lũy ra: z₂ = [zC, zD]ᵀ</text>

  <!-- 4 Blocks -->
  <!-- Block M11 -->
  <g transform="translate(260, 130)" filter="url(#shadow)">
    <rect width="150" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
    <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">Khối M₁₁</text>
    <text x="75" y="42" text-anchor="middle" font-size="10.5" fill="#64748b">Nguồn {A, B} → Đích {A, B}</text>
    <line x1="15" y1="52" x2="135" y2="52" stroke="#f1f5f9" stroke-width="1"/>
    <text x="25" y="74" font-size="11" font-weight="600" fill="#2563eb">• B → A (đóng góp 1/2)</text>
    <text x="25" y="96" font-size="11" font-weight="600" fill="#2563eb">• A → B (đóng góp 1/3)</text>
    <text x="25" y="115" font-size="10" fill="#94a3b8">Số cạnh: 2 | Bậc toàn cục: 3, 2</text>
  </g>

  <!-- Block M12 -->
  <g transform="translate(430, 130)" filter="url(#shadow)">
    <rect width="150" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
    <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">Khối M₁₂</text>
    <text x="75" y="42" text-anchor="middle" font-size="10.5" fill="#64748b">Nguồn {C, D} → Đích {A, B}</text>
    <line x1="15" y1="52" x2="135" y2="52" stroke="#f1f5f9" stroke-width="1"/>
    <text x="25" y="74" font-size="11" font-weight="600" fill="#2563eb">• C → A (đóng góp 1/1)</text>
    <text x="25" y="96" font-size="11" font-weight="600" fill="#2563eb">• D → B (đóng góp 1/2)</text>
    <text x="25" y="115" font-size="10" fill="#94a3b8">Số cạnh: 2 | Bậc toàn cục: 1, 2</text>
  </g>

  <!-- Block M21 -->
  <g transform="translate(260, 275)" filter="url(#shadow)">
    <rect width="150" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
    <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">Khối M₂₁</text>
    <text x="75" y="42" text-anchor="middle" font-size="10.5" fill="#64748b">Nguồn {A, B} → Đích {C, D}</text>
    <line x1="15" y1="52" x2="135" y2="52" stroke="#f1f5f9" stroke-width="1"/>
    <text x="25" y="68" font-size="11" font-weight="600" fill="#2563eb">• A → C (1/3), A → D (1/3)</text>
    <text x="25" y="86" font-size="11" font-weight="600" fill="#2563eb">• B → D (1/2)</text>
    <rect x="20" y="94" width="110" height="20" rx="3" fill="#fef3c7" stroke="#f59e0b" stroke-width="0.8"/>
    <text x="75" y="108" text-anchor="middle" font-size="9.5" font-weight="700" fill="#b45309">Combine gộp 2 đóng góp vào D</text>
  </g>

  <!-- Block M22 -->
  <g transform="translate(430, 275)" filter="url(#shadow)">
    <rect width="150" height="125" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
    <text x="75" y="24" text-anchor="middle" font-size="13" font-weight="800" fill="#0f172a">Khối M₂₂</text>
    <text x="75" y="42" text-anchor="middle" font-size="10.5" fill="#64748b">Nguồn {C, D} → Đích {C, D}</text>
    <line x1="15" y1="52" x2="135" y2="52" stroke="#f1f5f9" stroke-width="1"/>
    <text x="25" y="74" font-size="11" font-weight="600" fill="#2563eb">• D → C (đóng góp 1/2)</text>
    <text x="25" y="96" font-size="10.5" fill="#94a3b8">(C không trỏ C hoặc D)</text>
    <text x="25" y="115" font-size="10" fill="#94a3b8">Số cạnh: 1 | Bậc toàn cục: 2</text>
  </g>

  <!-- Memory Footprint Sidebar / Summary -->
  <g transform="translate(605, 130)">
    <rect width="135" height="270" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="67" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Bộ nhớ 1 tác vụ Map</text>
    <line x1="15" y1="40" x2="120" y2="40" stroke="#cbd5e1" stroke-width="1"/>
    <text x="15" y="65" font-size="11" font-weight="600" fill="#334155">B_task ≈ 16n/k + B_buf</text>
    <text x="15" y="90" font-size="10.5" fill="#64748b">• Giữ dải vào r_b</text>
    <text x="15" y="110" font-size="10.5" fill="#64748b">• Giữ dải tích lũy z_a</text>
    <text x="15" y="130" font-size="10.5" fill="#64748b">• Đọc khối qua đệm</text>
    <line x1="15" y1="145" x2="120" y2="145" stroke="#cbd5e1" stroke-width="1"/>
    <text x="67" y="170" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Với n = 4, k = 2:</text>
    <text x="67" y="195" text-anchor="middle" font-size="14" font-weight="800" fill="#15803d">32 bytes + đệm</text>
    <text x="15" y="225" font-size="10" fill="#64748b">Tiết kiệm đáng kể khi n quy mô hàng tỷ trang web.</text>
  </g>

  <!-- Bottom workflow indicator -->
  <g transform="translate(380, 445)">
    <text text-anchor="middle" font-size="12" font-weight="600" fill="#475569">
      Map(B_ab, r_b)  →  Combine(i, sum)  →  Truyền mạng (Shuffle)  →  Reduce(i, L_i) hoàn tất véc tơ z_a
    </text>
  </g>
</svg>
`

// 4. ex-fig-57.svg: 3 nodes a, b, c with loops
svgs['ex-fig-57.svg'] = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%" style="background:#f8fafc; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
    </marker>
    <linearGradient id="nodeGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
  </defs>

  <!-- Title -->
  <text x="300" y="36" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">Đồ thị Hình 5.7 MMDS (Bài tập 1 &amp; 2)</text>
  <text x="300" y="58" text-anchor="middle" font-size="12" fill="#64748b">a → a, b, c (da=3) | b → a, c (db=2) | c → b, c (dc=2) — 7 cạnh, 2 khuyên</text>

  <!-- Edges -->
  <!-- Triangle layout: a: (180, 150) | b: (420, 150) | c: (300, 310) -->

  <!-- Loop at a: a -> a -->
  <path d="M 155 140 C 95 120, 95 60, 165 120" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- Loop at c: c -> c -->
  <path d="M 285 335 C 240 395, 360 405, 325 335" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- a -> b -->
  <path d="M 215 140 C 270 120, 330 120, 385 140" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <!-- b -> a -->
  <path d="M 385 160 C 330 180, 270 180, 215 160" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- a -> c -->
  <path d="M 200 175 L 280 285" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- b -> c -->
  <path d="M 390 175 C 375 220, 350 250, 325 285" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <!-- c -> b -->
  <path d="M 315 285 C 335 245, 365 210, 405 175" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- Nodes -->
  <!-- Node a -->
  <g transform="translate(180, 150)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#2563eb" stroke-width="2.5"/>
    <text y="6" text-anchor="middle" font-size="20" font-weight="800" fill="#1e3a8a">a</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#1d4ed8">Bậc ra: 3</text>
  </g>

  <!-- Node b -->
  <g transform="translate(420, 150)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="6" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">b</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>

  <!-- Node c -->
  <g transform="translate(300, 310)" filter="url(#shadow)">
    <circle r="34" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="6" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">c</text>
    <rect x="-35" y="40" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="54" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>
</svg>
`

// 5. ex-fig-54.svg: 5 nodes A, B, C, D, E with dead end E
svgs['ex-fig-54.svg'] = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 440" width="100%" height="100%" style="background:#f8fafc; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
    </marker>
    <linearGradient id="nodeGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
  </defs>

  <!-- Title -->
  <text x="340" y="34" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">Đồ thị Hình 5.4 MMDS (Bài tập 4)</text>
  <text x="340" y="54" text-anchor="middle" font-size="12" fill="#64748b">A → B, C, D | B → A, D | C → E | D → B, C | E không có liên kết ra (nút cụt)</text>

  <!-- Positions:
       A: (160, 140) | B: (380, 140)
       C: (160, 300) | D: (380, 300)
       E: (560, 300)
  -->

  <!-- A -> B & B -> A -->
  <path d="M 195 130 C 255 110, 300 110, 345 130" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <path d="M 345 150 C 300 170, 255 170, 195 150" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- A -> C -->
  <path d="M 160 175 L 160 265" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- A -> D -->
  <path d="M 185 160 L 355 280" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- B -> D & D -> B -->
  <path d="M 390 175 C 405 210, 405 235, 390 265" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>
  <path d="M 370 265 C 355 235, 355 210, 370 175" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- D -> C -->
  <path d="M 345 300 L 195 300" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- C -> E -->
  <path d="M 195 315 C 300 375, 430 375, 525 315" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr)"/>

  <!-- Nodes -->
  <!-- Node A -->
  <g transform="translate(160, 140)" filter="url(#shadow)">
    <circle r="32" fill="url(#nodeGrad)" stroke="#2563eb" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#1e3a8a">A</text>
    <rect x="-35" y="38" width="70" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
    <text y="52" text-anchor="middle" font-size="11" font-weight="600" fill="#1d4ed8">Bậc ra: 3</text>
  </g>

  <!-- Node B -->
  <g transform="translate(380, 140)" filter="url(#shadow)">
    <circle r="32" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">B</text>
    <rect x="-35" y="38" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="52" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>

  <!-- Node C -->
  <g transform="translate(160, 300)" filter="url(#shadow)">
    <circle r="32" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">C</text>
    <rect x="-35" y="38" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="52" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 1</text>
  </g>

  <!-- Node D -->
  <g transform="translate(380, 300)" filter="url(#shadow)">
    <circle r="32" fill="url(#nodeGrad)" stroke="#64748b" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">D</text>
    <rect x="-35" y="38" width="70" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text y="52" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Bậc ra: 2</text>
  </g>

  <!-- Node E (Dead End) -->
  <g transform="translate(560, 300)" filter="url(#shadow)">
    <circle r="32" fill="#fef2f2" stroke="#ef4444" stroke-width="2.5"/>
    <text y="5" text-anchor="middle" font-size="18" font-weight="800" fill="#b91c1c">E</text>
    <rect x="-42" y="38" width="84" height="20" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1"/>
    <text y="52" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b91c1c">Bậc ra: 0 (CỤT)</text>
  </g>
</svg>
`

for (const [name, content] of Object.entries(svgs)) {
  fs.writeFileSync(path.join(publicDir, name), themePrintedSvg(content.trim()), 'utf8')
  fs.writeFileSync(path.join(docDir, name), themePrintedSvg(content.trim()), 'utf8')
  console.log(`Generated ${name}`)
}

console.log('All 5 Lecture 03 SVGs generated successfully.')
