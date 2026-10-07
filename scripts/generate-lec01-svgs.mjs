import { mkdir, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../', import.meta.url))
const targets = [
  path.join(root, 'docs/public/img/lec-01'),
  path.join(root, 'docs/giai-thuat-du-lieu/bai-giang/img/lec-01')
]

for (const dir of targets) {
  await mkdir(dir, { recursive: true })
}

function svgWrapper(width, height, content) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="100%" height="auto" style="max-width: ${width}px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#244bd6"/>
      <stop offset="100%" stop-color="#1b3cac"/>
    </linearGradient>
    <linearGradient id="softBlue" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#edf2fe"/>
      <stop offset="100%" stop-color="#e2ebfd"/>
    </linearGradient>
    <linearGradient id="softAmber" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
    <linearGradient id="softGreen" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <linearGradient id="softRed" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef2f2"/>
      <stop offset="100%" stop-color="#fee2e2"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#244bd6"/>
    </marker>
    <marker id="grayArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
    <marker id="redArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/>
    </marker>
    <marker id="greenArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
    </marker>
  </defs>
  <rect width="${width}" height="${height}" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  ${content}
</svg>`
}

const diagrams = {
  // 1. kho-nhat-ky-bo-nho.svg
  'kho-nhat-ky-bo-nho.svg': svgWrapper(760, 240, `
    <text x="380" y="30" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Quá tải bộ nhớ: Tệp nhật ký D trên đĩa và Bộ nhớ chính M khả dụng</text>
    
    <!-- Disk File -->
    <rect x="40" y="55" width="230" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="155" y="80" font-size="14" font-weight="700" fill="#b45309" text-anchor="middle">Ổ đĩa (Tệp nhật ký D)</text>
    <rect x="55" y="95" width="200" height="24" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="65" y="111" font-size="12" fill="#334155">a.vn, 40 byte, 2026-03-01</text>
    <rect x="55" y="125" width="200" height="24" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="65" y="141" font-size="12" fill="#334155">b.vn, 25 byte, 2026-03-01</text>
    <rect x="55" y="155" width="200" height="24" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="65" y="171" font-size="12" fill="#334155">a.vn, 15 byte, 2026-03-02</text>
    <text x="155" y="196" font-size="11" fill="#78350f" text-anchor="middle">Dung lượng D vượt quá RAM (D &gt; M)</text>

    <!-- Scanning Arrow -->
    <path d="M 285 130 L 460 130" stroke="#244bd6" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow)"/>
    <text x="372" y="120" font-size="12" font-weight="600" fill="#244bd6" text-anchor="middle">Đọc tuần tự từng dòng</text>

    <!-- RAM Table -->
    <rect x="475" y="55" width="245" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="597" y="80" font-size="14" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bộ nhớ chính RAM (Ngân sách M)</text>
    <rect x="495" y="95" width="205" height="24" rx="4" fill="#ffffff" stroke="#bfdbfe"/>
    <text x="505" y="111" font-size="12" font-weight="600" fill="#1e293b">a.vn → 40 + 15 = 55 byte</text>
    <rect x="495" y="125" width="205" height="24" rx="4" fill="#ffffff" stroke="#bfdbfe"/>
    <text x="505" y="141" font-size="12" font-weight="600" fill="#1e293b">b.vn → 25 byte</text>
    <rect x="495" y="155" width="205" height="24" rx="4" fill="#ffffff" stroke="#bfdbfe"/>
    <text x="505" y="171" font-size="12" font-weight="600" fill="#1e293b">c.vn → 0 byte</text>
    <text x="597" y="196" font-size="11" fill="#1e40af" text-anchor="middle">Chỉ giữ bảng tổng theo máy chủ phân biệt</text>
  `),

  // 2. ung-dung-tong-hop-phan-tan.svg
  'ung-dung-tong-hop-phan-tan.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Đếm từ phân tán: Gom toàn bộ dữ liệu vs Gom số đếm trung gian</text>
    
    <!-- Worker 1 -->
    <rect x="40" y="55" width="180" height="70" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="130" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Máy phân tán 1</text>
    <text x="130" y="102" font-size="12" fill="#334155" text-anchor="middle">Chứa: docA (có từ w)</text>

    <!-- Worker 2 -->
    <rect x="40" y="145" width="180" height="70" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="130" y="170" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Máy phân tán 2</text>
    <text x="130" y="192" font-size="12" fill="#334155" text-anchor="middle">Chứa: docB (có từ w)</text>

    <!-- Transfer labels -->
    <path d="M 230 85 L 490 100" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#redArrow)"/>
    <text x="340" y="82" font-size="11" fill="#dc2626" font-weight="600">Cách thô: Truyền cả văn bản (Nghẽn mạng)</text>

    <path d="M 230 185 L 490 145" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>
    <text x="340" y="178" font-size="11" fill="#059669" font-weight="700">MapReduce: Đếm cục bộ (w, c) rồi gửi</text>

    <!-- Reducer -->
    <rect x="500" y="70" width="220" height="120" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="610" y="98" font-size="14" font-weight="700" fill="#065f46" text-anchor="middle">Máy tổng hợp (Reducer)</text>
    <rect x="520" y="112" width="180" height="30" rx="4" fill="#ffffff" stroke="#a7f3d0"/>
    <text x="610" y="132" font-size="12" font-weight="600" fill="#047857" text-anchor="middle">Tổng w = c₁ + c₂</text>
    <text x="610" y="165" font-size="11" fill="#065f46" text-anchor="middle">Tránh quá tải 1 máy duy nhất</text>
  `),

  // 3. ung-dung-xep-hang-web.svg
  'ung-dung-xep-hang-web.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Đồ thị liên kết PageRank 3 đỉnh: Cập nhật lặp r = M·r</text>
    
    <!-- Node y -->
    <circle cx="150" cy="130" r="34" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="150" y="136" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">y</text>
    <!-- Self loop on y -->
    <path d="M 125 110 C 90 60, 160 40, 155 95" fill="none" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="125" y="55" font-size="11" fill="#244bd6" font-weight="600">tự trỏ y</text>

    <!-- Node a -->
    <circle cx="380" cy="130" r="34" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="380" y="136" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">a</text>

    <!-- Node m -->
    <circle cx="610" cy="130" r="34" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="610" y="136" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">m</text>

    <!-- y to a -->
    <path d="M 185 120 L 340 120" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <!-- a to y -->
    <path d="M 345 140 L 190 140" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- a to m -->
    <path d="M 415 120 L 570 120" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <!-- m to a -->
    <path d="M 575 140 L 420 140" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>

    <text x="265" y="110" font-size="12" fill="#244bd6" text-anchor="middle">y → a (1/2)</text>
    <text x="265" y="160" font-size="12" fill="#244bd6" text-anchor="middle">a → y (1/2)</text>
    <text x="495" y="110" font-size="12" fill="#244bd6" text-anchor="middle">a → m (1/2)</text>
    <text x="495" y="160" font-size="12" fill="#244bd6" text-anchor="middle">m → a (1)</text>

    <text x="380" y="215" font-size="12" fill="#64748b" text-anchor="middle">Điểm của mỗi trang phụ thuộc vào điểm của các trang trỏ tới nó qua từng vòng lặp</text>
  `),

  // 4. ung-dung-truy-van-theo-chu-de.svg
  'ung-dung-truy-van-theo-chu-de.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Truy vấn theo chủ đề (Topic-Sensitive PageRank): Ngữ nghĩa từ &quot;Jaguar&quot;</text>
    
    <!-- Central Query -->
    <rect x="40" y="80" width="180" height="80" rx="8" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="130" y="115" font-size="16" font-weight="700" fill="#ffffff" text-anchor="middle">Truy vấn: &quot;Jaguar&quot;</text>
    <text x="130" y="140" font-size="11" fill="#e2ebfd" text-anchor="middle">(Từ khóa đa nghĩa)</text>

    <!-- 4 Topics -->
    <path d="M 225 95 L 340 60" stroke="#64748b" stroke-width="1.5" marker-end="url(#grayArrow)"/>
    <rect x="350" y="45" width="170" height="32" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="435" y="66" font-size="12" fill="#475569" text-anchor="middle">1. Loài báo (Động vật)</text>

    <path d="M 225 110 L 340 100" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="350" y="85" width="170" height="34" rx="4" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="435" y="106" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">2. Hãng ô tô (Xe cộ) ★</text>

    <path d="M 225 130 L 340 140" stroke="#64748b" stroke-width="1.5" marker-end="url(#grayArrow)"/>
    <rect x="350" y="125" width="170" height="32" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="435" y="146" font-size="12" fill="#475569" text-anchor="middle">3. Apple OS X Jaguar</text>

    <path d="M 225 145 L 340 180" stroke="#64748b" stroke-width="1.5" marker-end="url(#grayArrow)"/>
    <rect x="350" y="165" width="170" height="32" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="435" y="186" font-size="12" fill="#475569" text-anchor="middle">4. Máy game Atari Jaguar</text>

    <!-- Context Result -->
    <rect x="545" y="70" width="180" height="100" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="635" y="98" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Chủ đề xác định: Xe</text>
    <text x="635" y="125" font-size="11" fill="#334155" text-anchor="middle">Ưu tiên các trang bán xe,</text>
    <text x="635" y="145" font-size="11" fill="#334155" text-anchor="middle">thay vì trang sở thú</text>
  `),

  // 5. ung-dung-lien-ket-thao-tung.svg
  'ung-dung-lien-ket-thao-tung.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Mô hình liên kết thao túng (Spam Farm - Hình 5.16 MMDS)</text>
    
    <!-- Inaccessible web -->
    <rect x="40" y="60" width="170" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="125" y="85" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">Web ngoài tầm</text>
    <text x="125" y="110" font-size="11" fill="#64748b" text-anchor="middle">(Không tác động được)</text>
    <circle cx="125" cy="150" r="22" fill="#e2e8f0"/>
    <text x="125" y="155" font-size="12" fill="#475569" text-anchor="middle">Tin cậy</text>

    <!-- Accessible web -->
    <rect x="235" y="60" width="170" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="320" y="85" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Trang đặt link</text>
    <text x="320" y="110" font-size="11" fill="#78350f" text-anchor="middle">(Blog, comment, forum)</text>
    <circle cx="320" cy="150" r="22" fill="#ffffff" stroke="#f59e0b"/>
    <text x="320" y="155" font-size="12" fill="#b45309" text-anchor="middle">Link out</text>

    <!-- Spam Farm Cluster -->
    <rect x="430" y="60" width="290" height="150" rx="8" fill="url(#softRed)" stroke="#ef4444" stroke-width="1.5"/>
    <text x="575" y="85" font-size="13" font-weight="700" fill="#b91c1c" text-anchor="middle">Cụm kiểm soát (Spam Farm)</text>
    
    <circle cx="485" cy="140" r="26" fill="#ef4444" filter="url(#shadow)"/>
    <text x="485" y="146" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">Đích t</text>

    <circle cx="640" cy="110" r="18" fill="#ffffff" stroke="#ef4444"/>
    <text x="640" y="115" font-size="10" fill="#b91c1c" text-anchor="middle">s₁</text>
    <circle cx="640" cy="150" r="18" fill="#ffffff" stroke="#ef4444"/>
    <text x="640" y="155" font-size="10" fill="#b91c1c" text-anchor="middle">s₂</text>
    <circle cx="640" cy="185" r="18" fill="#ffffff" stroke="#ef4444"/>
    <text x="640" y="190" font-size="10" fill="#b91c1c" text-anchor="middle">sm</text>

    <!-- Links -->
    <path d="M 345 150 L 455 142" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <path d="M 515 130 L 618 112" stroke="#ef4444" stroke-width="1.5" marker-end="url(#redArrow)"/>
    <path d="M 618 118 L 515 136" stroke="#ef4444" stroke-width="1.5" marker-end="url(#redArrow)"/>
    <path d="M 515 142 L 618 150" stroke="#ef4444" stroke-width="1.5" marker-end="url(#redArrow)"/>
    <path d="M 618 154 L 515 146" stroke="#ef4444" stroke-width="1.5" marker-end="url(#redArrow)"/>

    <text x="575" y="200" font-size="10" fill="#7f1d1d" text-anchor="middle">Hàng nghìn trang hỗ trợ trỏ 2 chiều với đích t</text>
  `),

  // 6. ung-dung-tai-lieu-gan-trung.svg
  'ung-dung-tai-lieu-gan-trung.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">So sánh trực tiếp mọi cặp tài liệu: Bùng nổ tổ hợp N(N-1)/2</text>
    
    <!-- Doc 1 -->
    <rect x="50" y="60" width="160" height="145" rx="6" fill="#ffffff" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="130" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Tài liệu C₁</text>
    <rect x="65" y="100" width="130" height="12" rx="3" fill="#93c5fd"/>
    <rect x="65" y="120" width="130" height="12" rx="3" fill="#86efac"/>
    <rect x="65" y="140" width="80" height="12" rx="3" fill="#93c5fd"/>
    <rect x="65" y="160" width="130" height="12" rx="3" fill="#fca5a5"/>
    <text x="130" y="195" font-size="10" fill="#64748b" text-anchor="middle">Bản gốc</text>

    <!-- Doc 2 -->
    <rect x="250" y="60" width="160" height="145" rx="6" fill="#ffffff" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="330" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Tài liệu C₂</text>
    <rect x="265" y="100" width="130" height="12" rx="3" fill="#93c5fd"/>
    <rect x="265" y="120" width="130" height="12" rx="3" fill="#86efac"/>
    <rect x="265" y="140" width="80" height="12" rx="3" fill="#93c5fd"/>
    <rect x="265" y="160" width="110" height="12" rx="3" fill="#fdba74"/>
    <text x="330" y="195" font-size="10" fill="#64748b" text-anchor="middle">Sửa vài đoạn (gần trùng)</text>

    <!-- Calculation box -->
    <rect x="450" y="60" width="270" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="585" y="90" font-size="14" font-weight="700" fill="#1e3a8a" text-anchor="middle">Xét mọi cặp trong kho:</text>
    <text x="585" y="120" font-size="15" font-weight="700" fill="#244bd6" text-anchor="middle">C(N, 2) = N(N − 1) / 2</text>
    <text x="585" y="150" font-size="12" fill="#1e293b" text-anchor="middle">Với N = 10⁶ tài liệu:</text>
    <text x="585" y="172" font-size="13" font-weight="700" fill="#b91c1c" text-anchor="middle">≈ 500 TỶ CẶP SO SÁNH!</text>
    <text x="585" y="194" font-size="11" fill="#64748b" text-anchor="middle">Cần Shingling + MinHash + LSH</text>
  `),

  // 7. ung-dung-truy-hoi-vec-to.svg
  'ung-dung-truy-hoi-vec-to.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Truy hồi vector: Tìm k đoạn văn bản gần nhất với truy vấn q</text>
    
    <!-- Query Vector -->
    <rect x="40" y="65" width="170" height="135" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="125" y="92" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Truy vấn q</text>
    <text x="125" y="115" font-size="11" fill="#334155" text-anchor="middle">Mã hóa thành vector:</text>
    <rect x="55" y="130" width="140" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="125" y="150" font-size="12" font-weight="600" fill="#244bd6" text-anchor="middle">[0.14, -0.82, ..., 0.45]</text>
    <text x="125" y="185" font-size="11" fill="#64748b" text-anchor="middle">D = 3072 chiều</text>

    <!-- Search process -->
    <path d="M 215 130 L 330 130" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="272" y="120" font-size="11" fill="#244bd6" font-weight="600" text-anchor="middle">Kho 10 tỷ vector</text>

    <!-- Vector Space -->
    <rect x="340" y="60" width="220" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="450" y="82" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Không gian vector embedding</text>
    <!-- Query dot -->
    <circle cx="450" cy="140" r="7" fill="#ef4444"/>
    <text x="450" y="130" font-size="11" font-weight="700" fill="#ef4444" text-anchor="middle">q</text>
    <circle cx="450" cy="140" r="45" fill="none" stroke="#ef4444" stroke-dasharray="4,4"/>
    <!-- Near neighbors -->
    <circle cx="430" cy="135" r="5" fill="#10b981"/>
    <circle cx="465" cy="125" r="5" fill="#10b981"/>
    <circle cx="445" cy="165" r="5" fill="#10b981"/>
    <!-- Far vectors -->
    <circle cx="370" cy="100" r="4" fill="#94a3b8"/>
    <circle cx="520" cy="170" r="4" fill="#94a3b8"/>
    <circle cx="510" cy="95" r="4" fill="#94a3b8"/>
    <text x="450" y="200" font-size="10" fill="#10b981" font-weight="600" text-anchor="middle">k láng giềng gần nhất</text>

    <!-- Top-k results -->
    <rect x="580" y="65" width="140" height="135" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="650" y="92" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Đầu ra top-k</text>
    <rect x="595" y="105" width="110" height="20" rx="3" fill="#ffffff"/>
    <text x="650" y="120" font-size="11" fill="#047857" text-anchor="middle">1. Đoạn doc 42</text>
    <rect x="595" y="132" width="110" height="20" rx="3" fill="#ffffff"/>
    <text x="650" y="147" font-size="11" fill="#047857" text-anchor="middle">2. Đoạn doc 108</text>
    <rect x="595" y="159" width="110" height="20" rx="3" fill="#ffffff"/>
    <text x="650" y="174" font-size="11" fill="#047857" text-anchor="middle">3. Đoạn doc 99</text>
  `),

  // 8. ung-dung-dong-truy-van.svg
  'ung-dung-dong-truy-van.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Xử lý dòng dữ liệu: Mẫu theo người dùng &amp; Bộ lọc Bloom Filter</text>
    
    <!-- Part 1: Sampling by User Key -->
    <rect x="40" y="55" width="320" height="155" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="200" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">1. Lấy mẫu nhật ký tìm kiếm</text>
    <text x="60" y="105" font-size="11" fill="#334155">• Dòng truy vấn liên tục (User, Query, Time)</text>
    <text x="60" y="125" font-size="11" fill="#334155">• Lấy mẫu từng dòng lẻ: Mất hành vi lặp</text>
    <rect x="60" y="138" width="280" height="32" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="200" y="158" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Băm User_ID: hash(u) % 10 == 0</text>
    <text x="200" y="195" font-size="11" fill="#1e40af" text-anchor="middle">→ Giữ trọn vẹn toàn bộ lịch sử 10% người dùng</text>

    <!-- Part 2: Bloom Filter Mail Filter -->
    <rect x="400" y="55" width="320" height="155" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="560" y="80" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">2. Bộ lọc Bloom (Lọc thư)</text>
    <text x="420" y="105" font-size="11" fill="#334155">• Thư đến kèm địa chỉ gửi</text>
    <text x="420" y="125" font-size="11" fill="#334155">• Danh sách trắng vượt quá RAM</text>
    <rect x="420" y="138" width="280" height="32" rx="4" fill="#ffffff" stroke="#a7f3d0"/>
    <text x="560" y="158" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">Mảng bit: [0, 1, 0, 1, 1, 0, ...]</text>
    <text x="560" y="185" font-size="11" fill="#065f46" text-anchor="middle">Báo &quot;KHÔNG&quot; → chắc chắn 100%</text>
    <text x="560" y="200" font-size="10" fill="#64748b" text-anchor="middle">Báo &quot;CÓ THỂ CÓ&quot; → mới tra cứu đĩa</text>
  `),

  // 9. ung-dung-thong-ke-cua-so.svg
  'ung-dung-thong-ke-cua-so.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Thống kê trên cửa sổ trượt: Phân biệt số lượt vs số người phân biệt</text>
    
    <!-- Timeline Axis -->
    <line x1="60" y1="120" x2="700" y2="120" stroke="#94a3b8" stroke-width="3"/>
    <polygon points="705,120 695,114 695,126" fill="#94a3b8"/>
    <text x="690" y="145" font-size="11" fill="#64748b">Thời gian t →</text>

    <!-- Expired Area -->
    <rect x="60" y="65" width="220" height="110" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-dasharray="4,4"/>
    <text x="170" y="90" font-size="12" font-weight="700" fill="#94a3b8" text-anchor="middle">Dữ liệu quá hạn (&gt; 24h)</text>
    <circle cx="120" cy="120" r="14" fill="#e2e8f0"/>
    <text x="120" y="125" font-size="10" fill="#64748b" text-anchor="middle">User A</text>
    <circle cx="190" cy="120" r="14" fill="#e2e8f0"/>
    <text x="190" y="125" font-size="10" fill="#64748b" text-anchor="middle">User B</text>

    <!-- Active Window Area -->
    <rect x="310" y="55" width="370" height="130" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="2" filter="url(#shadow)"/>
    <text x="495" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Cửa sổ gần đây (24 giờ qua)</text>

    <!-- Events inside window -->
    <circle cx="360" cy="120" r="16" fill="#93c5fd" stroke="#244bd6"/>
    <text x="360" y="125" font-size="10" font-weight="700" fill="#1e3a8a" text-anchor="middle">User A</text>
    
    <circle cx="430" cy="120" r="16" fill="#86efac" stroke="#10b981"/>
    <text x="430" y="125" font-size="10" font-weight="700" fill="#065f46" text-anchor="middle">User C</text>

    <circle cx="500" cy="120" r="16" fill="#93c5fd" stroke="#244bd6"/>
    <text x="500" y="125" font-size="10" font-weight="700" fill="#1e3a8a" text-anchor="middle">User A</text>

    <circle cx="570" cy="120" r="16" fill="#93c5fd" stroke="#244bd6"/>
    <text x="570" y="125" font-size="10" font-weight="700" fill="#1e3a8a" text-anchor="middle">User A</text>

    <circle cx="640" cy="120" r="16" fill="#fcd34d" stroke="#f59e0b"/>
    <text x="640" y="125" font-size="10" font-weight="700" fill="#78350f" text-anchor="middle">User D</text>

    <!-- Stats below -->
    <text x="495" y="165" font-size="12" font-weight="700" fill="#1e293b" text-anchor="middle">Tổng lượt truy cập = 5 lượt  |  Số người phân biệt = 3 (A, C, D)</text>
    <text x="380" y="215" font-size="11" fill="#64748b" text-anchor="middle">Không thể chỉ dùng 1 bộ đếm tăng dần; cần cấu trúc cửa sổ (như thuật toán DGIM)</text>
  `),

  // 10. ung-dung-nen-van-ban.svg
  'ung-dung-nen-van-ban.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Nén văn bản không mất thông tin: Khôi phục chính xác chuỗi gốc</text>
    
    <!-- Original string -->
    <rect x="40" y="60" width="200" height="145" rx="8" fill="#ffffff" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="140" y="88" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Chuỗi văn bản gốc</text>
    <rect x="55" y="105" width="170" height="35" rx="4" fill="url(#softAmber)"/>
    <text x="140" y="128" font-size="13" font-weight="700" fill="#92400e" text-anchor="middle">aabaacabcabcb</text>
    <text x="140" y="165" font-size="11" fill="#64748b" text-anchor="middle">Các cụm lặp: ab, abc</text>
    <text x="140" y="185" font-size="11" fill="#64748b" text-anchor="middle">Kích thước: 13 ký tự</text>

    <!-- Compression arrow -->
    <path d="M 255 132 L 345 132" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="300" y="122" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Mã hóa LZ</text>

    <!-- Compressed Representation -->
    <rect x="360" y="60" width="210" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="465" y="88" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bản lưu trữ nén</text>
    <rect x="375" y="105" width="180" height="25" rx="4" fill="#ffffff" stroke="#bfdbfe"/>
    <text x="465" y="122" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Bit stream mã hóa</text>
    <rect x="375" y="138" width="180" height="25" rx="4" fill="#ffffff" stroke="#bfdbfe"/>
    <text x="465" y="155" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">+ Từ điển / Cây mã</text>
    <text x="465" y="188" font-size="10" fill="#64748b" text-anchor="middle">Phải tính cả dung lượng phụ trợ!</text>

    <!-- Decompress arrow -->
    <path d="M 585 132 L 670 132" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>
    <text x="627" y="122" font-size="11" font-weight="600" fill="#10b981" text-anchor="middle">Giải mã</text>

    <!-- Decoded match -->
    <rect x="680" y="85" width="40" height="95" rx="4" fill="url(#softGreen)" stroke="#10b981"/>
    <text x="700" y="130" font-size="16" font-weight="700" fill="#047857" text-anchor="middle" transform="rotate(-90 700 130)">100% Khớp</text>
  `),

  // 11. ung-dung-nen-anh.svg
  'ung-dung-nen-anh.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Nén ảnh có mất thông tin (JPEG): Lượng tử hóa làm tròn các mức sáng</text>
    
    <!-- Continuous levels -->
    <rect x="50" y="60" width="220" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="160" y="85" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Mức sáng gốc (256 mức)</text>
    <rect x="70" y="100" width="180" height="18" fill="#1e293b"/>
    <rect x="70" y="120" width="180" height="18" fill="#475569"/>
    <rect x="70" y="140" width="180" height="18" fill="#94a3b8"/>
    <rect x="70" y="160" width="180" height="18" fill="#cbd5e1"/>
    <text x="160" y="195" font-size="10" fill="#64748b" text-anchor="middle">Mức xám 118, 120, 123, 127...</text>

    <!-- Quantization Arrow -->
    <path d="M 285 132 L 400 132" stroke="#ef4444" stroke-width="2.5" marker-end="url(#redArrow)"/>
    <text x="342" y="115" font-size="11" font-weight="700" fill="#b91c1c" text-anchor="middle">Lượng tử hóa</text>
    <text x="342" y="152" font-size="10" fill="#64748b" text-anchor="middle">(Làm tròn số)</text>

    <!-- Quantized levels -->
    <rect x="420" y="60" width="290" height="145" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="565" y="85" font-size="13" font-weight="700" fill="#92400e" text-anchor="middle">Gộp thành 1 mức đại diện</text>
    <rect x="445" y="105" width="240" height="40" rx="4" fill="#64748b"/>
    <text x="565" y="130" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">Đại diện chung = 120</text>
    <text x="565" y="170" font-size="11" fill="#78350f" text-anchor="middle">Mất sự phân biệt tinh tế giữa các mức ban đầu</text>
    <text x="565" y="190" font-size="10" font-weight="600" fill="#b91c1c" text-anchor="middle">Giảm đáng kể dung lượng nhưng có sai số tái tạo</text>
  `),

  // 12. ung-dung-sap-xep-ngoai.svg
  'ung-dung-sap-xep-ngoai.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Sắp xếp ngoài (External Merge Sort): Đọc từng phần vừa RAM rồi trộn</text>
    
    <!-- Disk File Unsorted -->
    <rect x="40" y="60" width="180" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="130" y="85" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Tệp chưa sắp xếp (Đĩa)</text>
    <rect x="55" y="100" width="150" height="20" rx="3" fill="#fca5a5"/><text x="130" y="114" font-size="10" fill="#7f1d1d" text-anchor="middle">Khối 1: [84, 12, 60]</text>
    <rect x="55" y="125" width="150" height="20" rx="3" fill="#fca5a5"/><text x="130" y="139" font-size="10" fill="#7f1d1d" text-anchor="middle">Khối 2: [25, 91, 03]</text>
    <rect x="55" y="150" width="150" height="20" rx="3" fill="#fca5a5"/><text x="130" y="164" font-size="10" fill="#7f1d1d" text-anchor="middle">Khối 3: [55, 38, 17]</text>
    <text x="130" y="195" font-size="10" fill="#64748b" text-anchor="middle">Vượt quá bộ nhớ RAM</text>

    <!-- Phase 1: Sort in RAM -->
    <path d="M 230 110 L 295 110" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="305" y="60" width="160" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="385" y="85" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">Pha 1: Tạo các Run</text>
    <rect x="320" y="100" width="130" height="20" rx="3" fill="#bfdbfe"/><text x="385" y="114" font-size="10" fill="#1e3a8a" text-anchor="middle">Run 1: [12, 60, 84]</text>
    <rect x="320" y="125" width="130" height="20" rx="3" fill="#bfdbfe"/><text x="385" y="139" font-size="10" fill="#1e3a8a" text-anchor="middle">Run 2: [03, 25, 91]</text>
    <rect x="320" y="150" width="130" height="20" rx="3" fill="#bfdbfe"/><text x="385" y="164" font-size="10" fill="#1e3a8a" text-anchor="middle">Run 3: [17, 38, 55]</text>
    <text x="385" y="195" font-size="10" fill="#244bd6" text-anchor="middle">Sắp từng mẩu trong RAM</text>

    <!-- Phase 2: Merge -->
    <path d="M 475 130 L 535 130" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>
    <rect x="545" y="60" width="175" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="632" y="85" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">Pha 2: Trộn (Merge)</text>
    <rect x="560" y="105" width="145" height="40" rx="4" fill="#ffffff" stroke="#86efac"/>
    <text x="632" y="125" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">[03, 12, 17, 25,</text>
    <text x="632" y="139" font-size="11" font-weight="700" fill="#047857" text-anchor="middle"> 38, 55, 60, 84, 91]</text>
    <text x="632" y="175" font-size="10" fill="#065f46" text-anchor="middle">Tệp đã sắp tăng dần</text>
    <text x="632" y="195" font-size="9" fill="#065f46" text-anchor="middle">Chi phí: đọc/ghi khối đĩa</text>
  `),

  // 13. ung-dung-tra-cuu-khoa.svg
  'ung-dung-tra-cuu-khoa.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chỉ mục bảng: Truy vấn theo khóa điểm (ID) vs Truy vấn khoảng (Salary)</text>
    
    <!-- Exact ID search -->
    <rect x="40" y="60" width="320" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="200" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">1. Tra cứu theo mã: ID = 22222</text>
    <rect x="60" y="105" width="280" height="35" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="200" y="127" font-size="12" font-weight="600" fill="#244bd6" text-anchor="middle">Băm hoặc Cây B-Tree → 1 hồ sơ duy nhất</text>
    <rect x="60" y="150" width="280" height="40" rx="4" fill="#ffffff"/>
    <text x="200" y="174" font-size="11" fill="#334155" text-anchor="middle">Kết quả: (22222, Einstein, Physics, 95000)</text>

    <!-- Range Salary search -->
    <rect x="400" y="60" width="320" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="560" y="85" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">2. Tra cứu khoảng: salary ∈ [60k, 80k]</text>
    <rect x="420" y="105" width="280" height="35" rx="4" fill="#ffffff" stroke="#a7f3d0"/>
    <text x="560" y="127" font-size="12" font-weight="600" fill="#047857" text-anchor="middle">Cây B+-Tree: Duyệt chuỗi lá liên kết</text>
    <rect x="420" y="150" width="280" height="40" rx="4" fill="#ffffff"/>
    <text x="560" y="167" font-size="11" fill="#334155" text-anchor="middle">Trả tất cả hồ sơ có lương trong đoạn:</text>
    <text x="560" y="183" font-size="11" font-weight="600" fill="#065f46" text-anchor="middle">Katz (65k), Califieri (62k), Singh (80k)...</text>
  `),

  // 14. ung-dung-tim-tu-khoa.svg
  'ung-dung-tim-tu-khoa.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chỉ mục đảo (Inverted Index): Giao hai danh sách để tìm tài liệu chứa đồng thời 2 từ</text>
    
    <!-- Word 1 -->
    <rect x="40" y="60" width="280" height="65" rx="6" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="100" y="85" font-size="13" font-weight="700" fill="#1e3a8a">Từ: &quot;dữ liệu&quot;</text>
    <text x="100" y="108" font-size="11" fill="#334155">Danh sách Doc: [ 1,  4,  7,  9,  15 ]</text>

    <!-- Word 2 -->
    <rect x="40" y="140" width="280" height="65" rx="6" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="100" y="165" font-size="13" font-weight="700" fill="#92400e">Từ: &quot;giải thuật&quot;</text>
    <text x="100" y="188" font-size="11" fill="#334155">Danh sách Doc: [ 2,  4,  5,  9,  20 ]</text>

    <!-- Intersection process -->
    <path d="M 335 92 L 440 120" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <path d="M 335 172 L 440 145" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="385" y="145" font-size="14" font-weight="700" fill="#1e293b" text-anchor="middle">∩</text>

    <!-- Result -->
    <rect x="455" y="75" width="265" height="115" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="587" y="105" font-size="14" font-weight="700" fill="#065f46" text-anchor="middle">Tài liệu chứa cả 2 từ:</text>
    <rect x="480" y="120" width="215" height="35" rx="4" fill="#ffffff" stroke="#86efac"/>
    <text x="587" y="142" font-size="14" font-weight="700" fill="#047857" text-anchor="middle">Doc 4, Doc 9</text>
    <text x="587" y="175" font-size="11" fill="#065f46" text-anchor="middle">Thuật toán 2 con trỏ duyệt song song O(L₁+L₂)</text>
  `),

  // 15. ung-dung-truy-van-khong-gian.svg
  'ung-dung-truy-van-khong-gian.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Truy vấn không gian: Vùng Q giao hộp bao A và B (Chỉ mục R-tree)</text>
    
    <!-- 2D Canvas -->
    <rect x="50" y="55" width="400" height="160" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    
    <!-- Bounding Box A -->
    <rect x="80" y="70" width="160" height="80" fill="#bfdbfe" fill-opacity="0.5" stroke="#244bd6" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="95" y="90" font-size="12" font-weight="700" fill="#1e3a8a">Hộp bao A</text>
    <circle cx="120" cy="110" r="8" fill="#244bd6"/>
    <circle cx="180" cy="125" r="8" fill="#244bd6"/>
    <polygon points="140,80 155,95 130,95" fill="#244bd6"/>

    <!-- Bounding Box B -->
    <rect x="220" y="110" width="190" height="90" fill="#fde68a" fill-opacity="0.5" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="365" y="130" font-size="12" font-weight="700" fill="#b45309">Hộp bao B</text>
    <circle cx="260" cy="160" r="8" fill="#f59e0b"/>
    <circle cx="340" cy="170" r="8" fill="#f59e0b"/>

    <!-- Query Region Q -->
    <rect x="170" y="85" width="150" height="90" fill="#fca5a5" fill-opacity="0.4" stroke="#ef4444" stroke-width="2.5"/>
    <text x="245" y="105" font-size="13" font-weight="700" fill="#b91c1c" text-anchor="middle">Vùng truy vấn Q</text>

    <!-- Explanation Box -->
    <rect x="470" y="55" width="250" height="160" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="595" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Cắt nhánh R-tree:</text>
    <text x="485" y="105" font-size="11" fill="#334155">• Q giao cả hộp A và hộp B</text>
    <text x="485" y="125" font-size="11" fill="#334155">• Không thể bỏ qua nhánh nào</text>
    <text x="485" y="145" font-size="11" fill="#334155">• Phải kiểm tra chi tiết các đối</text>
    <text x="485" y="160" font-size="11" fill="#334155">  tượng bên trong mỗi hộp bao</text>
    <text x="485" y="190" font-size="10" font-weight="600" fill="#244bd6">→ Lọc thô rồi tinh lọc chính xác</text>
  `),

  // 16. ung-dung-noi-bang.svg
  'ung-dung-noi-bang.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Nối bảng (Join): Ghép sinh viên với các môn đã đăng ký</text>
    
    <!-- Table student -->
    <rect x="40" y="55" width="190" height="155" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="135" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bảng student</text>
    <text x="135" y="100" font-size="11" fill="#64748b" text-anchor="middle">5.000 dòng · 100 khối</text>
    <rect x="55" y="112" width="160" height="24" rx="3" fill="#ffffff"/>
    <text x="65" y="128" font-size="11" fill="#1e293b">ID: 00128, Zhang, Comp.</text>
    <rect x="55" y="142" width="160" height="24" rx="3" fill="#ffffff"/>
    <text x="65" y="158" font-size="11" fill="#1e293b">ID: 12345, Shankar, CS</text>

    <!-- Table takes -->
    <rect x="250" y="55" width="190" height="155" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="345" y="80" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Bảng takes</text>
    <text x="345" y="100" font-size="11" fill="#64748b" text-anchor="middle">10.000 dòng · 400 khối</text>
    <rect x="265" y="112" width="160" height="24" rx="3" fill="#ffffff"/>
    <text x="275" y="128" font-size="11" fill="#1e293b">ID: 00128, CS-101, A</text>
    <rect x="265" y="142" width="160" height="24" rx="3" fill="#ffffff"/>
    <text x="275" y="158" font-size="11" fill="#1e293b">ID: 00128, CS-315, A-</text>

    <!-- Join Arrow -->
    <path d="M 450 132 L 500 132" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>

    <!-- Joined Result -->
    <rect x="510" y="55" width="210" height="155" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="615" y="80" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Kết quả JOIN</text>
    <rect x="525" y="95" width="180" height="32" rx="3" fill="#ffffff" stroke="#86efac"/>
    <text x="535" y="115" font-size="10" font-weight="600" fill="#047857">00128 | Zhang | CS-101</text>
    <rect x="525" y="132" width="180" height="32" rx="3" fill="#ffffff" stroke="#86efac"/>
    <text x="535" y="152" font-size="10" font-weight="600" fill="#047857">00128 | Zhang | CS-315</text>
    <text x="615" y="195" font-size="10" fill="#065f46" text-anchor="middle">Bộ nhớ RAM chỉ có 20 khối!</text>
  `),

  // 17. danh-gia-jaccard.svg
  'danh-gia-jaccard.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Độ tương đồng Jaccard (MMDS Ví dụ 3.1): J(S, T) = |S ∩ T| / |S ∪ T|</text>
    
    <!-- Circle S -->
    <circle cx="270" cy="130" r="75" fill="#93c5fd" fill-opacity="0.6" stroke="#244bd6" stroke-width="2"/>
    <!-- Circle T -->
    <circle cx="370" cy="130" r="75" fill="#86efac" fill-opacity="0.6" stroke="#10b981" stroke-width="2"/>

    <!-- Labels -->
    <text x="220" y="90" font-size="14" font-weight="700" fill="#1e3a8a">Tập S</text>
    <text x="420" y="90" font-size="14" font-weight="700" fill="#065f46">Tập T</text>

    <!-- Elements in S only -->
    <text x="235" y="125" font-size="12" font-weight="600" fill="#1e293b">2 phần tử</text>
    <text x="235" y="145" font-size="11" fill="#475569">chỉ thuộc S</text>

    <!-- Intersection elements -->
    <text x="320" y="125" font-size="14" font-weight="700" fill="#1e293b" text-anchor="middle">3</text>
    <text x="320" y="145" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">chung</text>

    <!-- Elements in T only -->
    <text x="405" y="125" font-size="12" font-weight="600" fill="#1e293b">3 phần tử</text>
    <text x="405" y="145" font-size="11" fill="#475569">chỉ thuộc T</text>

    <!-- Formula Box -->
    <rect x="500" y="65" width="220" height="135" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="610" y="95" font-size="14" font-weight="700" fill="#1e3a8a" text-anchor="middle">Tính Jaccard:</text>
    <text x="610" y="125" font-size="16" font-weight="700" fill="#244bd6" text-anchor="middle">J(S, T) = 3 / (2+3+3)</text>
    <text x="610" y="155" font-size="18" font-weight="700" fill="#b91c1c" text-anchor="middle">= 3 / 8 = 0.375</text>
    <text x="610" y="185" font-size="11" fill="#475569" text-anchor="middle">Đạt yêu cầu khi ngưỡng τ ≤ 3/8</text>
  `),

  // 18. danh-gia-tinh-dung.svg
  'danh-gia-tinh-dung.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bất biến tính đúng của thuật toán duyệt mọi cặp 1 ≤ i &lt; j ≤ N</text>
    
    <!-- Pair Grid Matrix representation -->
    <g transform="translate(60, 55)">
      <rect x="0" y="0" width="260" height="150" fill="#f8fafc" stroke="#cbd5e1" rx="6"/>
      <!-- Grid items (i, j) -->
      <rect x="20" y="20" width="45" height="30" rx="3" fill="#86efac" stroke="#10b981"/>
      <text x="42" y="40" font-size="11" font-weight="700" fill="#065f46" text-anchor="middle">(1, 2) ✓</text>

      <rect x="75" y="20" width="45" height="30" rx="3" fill="#86efac" stroke="#10b981"/>
      <text x="97" y="40" font-size="11" font-weight="700" fill="#065f46" text-anchor="middle">(1, 3) ✓</text>

      <rect x="130" y="20" width="45" height="30" rx="3" fill="#86efac" stroke="#10b981"/>
      <text x="152" y="40" font-size="11" font-weight="700" fill="#065f46" text-anchor="middle">(1, 4) ✓</text>

      <rect x="75" y="60" width="45" height="30" rx="3" fill="#bfdbfe" stroke="#244bd6" stroke-width="2"/>
      <text x="97" y="80" font-size="11" font-weight="700" fill="#1e3a8a" text-anchor="middle">(2, 3) ⚙</text>

      <rect x="130" y="60" width="45" height="30" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="152" y="80" font-size="11" fill="#94a3b8" text-anchor="middle">(2, 4)</text>

      <rect x="130" y="100" width="45" height="30" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="152" y="120" font-size="11" fill="#94a3b8" text-anchor="middle">(3, 4)</text>

      <text x="210" y="40" font-size="10" fill="#10b981">Đã xét</text>
      <text x="210" y="80" font-size="10" fill="#244bd6">Đang xét</text>
      <text x="210" y="120" font-size="10" fill="#94a3b8">Chưa xét</text>
    </g>

    <!-- Invariant Box -->
    <rect x="360" y="55" width="360" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="540" y="80" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bất biến vòng lặp (Loop Invariant):</text>
    <text x="380" y="105" font-size="11" fill="#1e293b">• Sau mỗi bước, tập kết quả R_curr chứa đúng các</text>
    <text x="380" y="123" font-size="11" fill="#1e293b">  cặp có J(Cᵢ, Cⱼ) ≥ τ trong phần ĐÃ XÉT.</text>
    <text x="380" y="145" font-size="11" fill="#1e293b">• Không bỏ sót, không trùng lặp vì i &lt; j tăng nghiêm ngặt.</text>
    <text x="380" y="165" font-size="11" font-weight="700" fill="#047857">• Khi dừng: phần đã xét = toàn bộ N(N-1)/2 cặp.</text>
    <text x="540" y="190" font-size="11" font-weight="700" fill="#244bd6" text-anchor="middle">→ Kết quả cuối cùng R chính xác 100%</text>
  `),

  // 19. danh-gia-bo-nho.svg
  'danh-gia-bo-nho.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Đánh giá bộ nhớ làm việc: Giới hạn RAM so với kích thước tệp đĩa</text>
    
    <!-- Disk Sizes -->
    <rect x="50" y="60" width="300" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="200" y="85" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Dữ liệu trên Đĩa (Ví dụ Bài 15)</text>
    <rect x="70" y="100" width="260" height="30" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="200" y="120" font-size="12" fill="#78350f" text-anchor="middle">Bảng student: 100 khối đĩa</text>
    <rect x="70" y="140" width="260" height="30" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="200" y="160" font-size="12" fill="#78350f" text-anchor="middle">Bảng takes: 400 khối đĩa</text>
    <text x="200" y="195" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">Tổng cộng: 500 khối đĩa</text>

    <!-- RAM Budget -->
    <rect x="410" y="60" width="300" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="2" filter="url(#shadow)"/>
    <text x="560" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Ngân sách RAM làm việc</text>
    <rect x="430" y="100" width="260" height="50" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="560" y="125" font-size="16" font-weight="700" fill="#244bd6" text-anchor="middle">M_khối = 20 khối RAM</text>
    <text x="560" y="142" font-size="10" fill="#64748b" text-anchor="middle">(Chỉ chứa được 4% tổng dữ liệu!)</text>
    <text x="560" y="175" font-size="11" fill="#1e293b" text-anchor="middle">Phải phân bổ: Buffer bảng ngoài,</text>
    <text x="560" y="192" font-size="11" fill="#1e293b" text-anchor="middle">Buffer bảng trong và Buffer đầu ra</text>
  `),

  // 20. danh-gia-doc-ghi.svg
  'danh-gia-doc-ghi.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chi phí Đọc/Ghi đĩa (I/O) và Số lượt quét (Passes)</text>
    
    <!-- Flow: Disk to Buffer to Temp to Output -->
    <rect x="50" y="65" width="130" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="115" y="90" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">Tệp F khối</text>
    <text x="115" y="115" font-size="11" fill="#64748b" text-anchor="middle">Chưa có trong</text>
    <text x="115" y="132" font-size="11" fill="#64748b" text-anchor="middle">bộ đệm đĩa</text>
    <rect x="65" y="150" width="100" height="30" rx="4" fill="#e2e8f0"/>
    <text x="115" y="170" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">F lần đọc</text>

    <!-- Arrow 1 -->
    <path d="M 190 132 L 255 132" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- RAM Buffers -->
    <rect x="265" y="65" width="190" height="135" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="360" y="90" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bộ đệm trong RAM</text>
    <rect x="280" y="110" width="160" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="360" y="130" font-size="11" fill="#244bd6" text-anchor="middle">Xử lý / Sắp / Trộn</text>
    <text x="360" y="165" font-size="10" fill="#1e40af" text-anchor="middle">1 lượt quét đọc hết dữ liệu</text>
    <text x="360" y="182" font-size="10" fill="#1e40af" text-anchor="middle">→ Chi phí chuyển = 2F (nếu ghi)</text>

    <!-- Arrow 2 -->
    <path d="M 465 132 L 530 132" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>

    <!-- Disk Output -->
    <rect x="540" y="65" width="170" height="135" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="625" y="90" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">Ghi dãy / Kết quả</text>
    <text x="625" y="120" font-size="11" fill="#047857" text-anchor="middle">Các lượt trộn sau</text>
    <text x="625" y="140" font-size="11" fill="#047857" text-anchor="middle">tiếp tục đọc &amp; ghi</text>
    <text x="625" y="175" font-size="10" font-weight="700" fill="#b91c1c" text-anchor="middle">I/O đĩa thường là nút thắt</text>
    <text x="625" y="190" font-size="9" fill="#64748b" text-anchor="middle">lớn hơn số phép so sánh CPU</text>
  `),

  // 21. danh-gia-truyen-mang.svg
  'danh-gia-truyen-mang.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chi phí truyền thông mạng: Tổng hợp cục bộ trước khi truyền</text>
    
    <!-- Worker A -->
    <rect x="40" y="65" width="190" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="135" y="90" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Máy trạm A (1 GB văn bản)</text>
    <text x="135" y="115" font-size="11" fill="#334155" text-anchor="middle">Từ w xuất hiện 10.000 lần</text>
    <rect x="55" y="130" width="160" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="135" y="150" font-size="11" font-weight="700" fill="#244bd6" text-anchor="middle">Đếm cục bộ: (w, 10000)</text>
    <text x="135" y="185" font-size="10" fill="#059669" text-anchor="middle">Chỉ gửi 16 byte thay vì 1 GB!</text>

    <!-- Worker B -->
    <rect x="530" y="65" width="190" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="625" y="90" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Máy trạm B (1 GB văn bản)</text>
    <text x="625" y="115" font-size="11" fill="#334155" text-anchor="middle">Từ w xuất hiện 5.000 lần</text>
    <rect x="545" y="130" width="160" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="625" y="150" font-size="11" font-weight="700" fill="#244bd6" text-anchor="middle">Đếm cục bộ: (w, 5000)</text>
    <text x="625" y="185" font-size="10" fill="#059669" text-anchor="middle">Chỉ gửi 16 byte qua mạng!</text>

    <!-- Network Center -->
    <path d="M 235 140 L 325 140" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>
    <path d="M 525 140 L 435 140" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>

    <rect x="330" y="95" width="100" height="90" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="2" filter="url(#shadow)"/>
    <text x="380" y="125" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">Tổng hợp</text>
    <text x="380" y="150" font-size="13" font-weight="700" fill="#047857" text-anchor="middle">(w, 15000)</text>
    <text x="380" y="172" font-size="9" fill="#065f46" text-anchor="middle">Giảm 99.9% mạng</text>
  `),

  // 22. danh-gia-do-tre.svg
  'danh-gia-do-tre.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Độ trễ truy vấn (Latency): Trải dài từ lúc nhận yêu cầu đến lúc trả kết quả</text>
    
    <!-- Timeline Stages -->
    <g transform="translate(40, 70)">
      <!-- Stage 1 -->
      <rect x="0" y="0" width="130" height="60" rx="6" fill="#f1f5f9" stroke="#94a3b8"/>
      <text x="65" y="28" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">1. Nhận truy vấn</text>
      <text x="65" y="48" font-size="10" fill="#64748b" text-anchor="middle">Phân giải &amp; Parse</text>

      <!-- Stage 2 -->
      <rect x="140" y="0" width="140" height="60" rx="6" fill="url(#softAmber)" stroke="#f59e0b"/>
      <text x="210" y="28" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">2. Xếp hàng / Chờ</text>
      <text x="210" y="48" font-size="10" fill="#78350f" text-anchor="middle">Tải hệ thống cao</text>

      <!-- Stage 3 -->
      <rect x="290" y="0" width="180" height="60" rx="6" fill="url(#softBlue)" stroke="#244bd6"/>
      <text x="380" y="28" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">3. Truy cập chỉ mục</text>
      <text x="380" y="48" font-size="10" fill="#1e40af" text-anchor="middle">Đọc RAM / Cache / Đĩa</text>

      <!-- Stage 4 -->
      <rect x="480" y="0" width="200" height="60" rx="6" fill="url(#softGreen)" stroke="#10b981"/>
      <text x="580" y="28" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">4. Tính toán &amp; Trả về</text>
      <text x="580" y="48" font-size="10" fill="#047857" text-anchor="middle">Xếp hạng &amp; Gửi socket</text>
    </g>

    <!-- Large latency bracket -->
    <path d="M 40 150 L 720 150" stroke="#244bd6" stroke-width="2"/>
    <path d="M 40 145 L 40 155" stroke="#244bd6" stroke-width="2"/>
    <path d="M 720 145 L 720 155" stroke="#244bd6" stroke-width="2"/>
    <text x="380" y="175" font-size="13" font-weight="700" fill="#244bd6" text-anchor="middle">Tổng độ trễ (Latency) = T_nhận + T_chờ + T_truy_cập + T_tính_toán</text>
    <text x="380" y="200" font-size="11" fill="#64748b" text-anchor="middle">Khác với Thông lượng (Throughput = số truy vấn xử lý trên một giây)</text>
  `),

  // 23. danh-gia-xay-dung.svg
  'danh-gia-xay-dung.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chi phí xây dựng chỉ mục (Offline Build) vs Hiệu quả truy vấn (Online Query)</text>
    
    <!-- Offline Step -->
    <rect x="50" y="60" width="300" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="200" y="85" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Giai đoạn Offline (1 Lần)</text>
    <text x="200" y="110" font-size="11" fill="#334155" text-anchor="middle">Kho 10 tỷ vector thô → Xây dựng chỉ mục HNSW/PQ</text>
    <rect x="70" y="125" width="260" height="40" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="200" y="145" font-size="11" font-weight="700" fill="#b45309" text-anchor="middle">Tốn nhiều giờ CPU, RAM đỉnh lớn</text>
    <text x="200" y="195" font-size="11" fill="#78350f" text-anchor="middle">Chấp nhận đầu tư chi phí chuẩn bị ban đầu</text>

    <!-- Arrow -->
    <path d="M 360 135 L 400 135" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Online Step -->
    <rect x="410" y="60" width="300" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="560" y="85" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Giai đoạn Online (Hàng triệu lần)</text>
    <text x="560" y="110" font-size="11" fill="#334155" text-anchor="middle">Mỗi truy vấn đến tái sử dụng cấu trúc chỉ mục</text>
    <rect x="430" y="125" width="260" height="40" rx="4" fill="#ffffff" stroke="#86efac"/>
    <text x="560" y="145" font-size="13" font-weight="700" fill="#047857" text-anchor="middle">Độ trễ cực thấp: &lt; 5 mili-giây</text>
    <text x="560" y="195" font-size="11" fill="#065f46" text-anchor="middle">Lợi ích lớn khi số truy vấn N_q rất lớn</text>
  `),

  // 24. danh-gia-cap-nhat.svg
  'danh-gia-cap-nhat.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chi phí cập nhật: Sửa bản ghi gốc và đồng bộ cấu trúc chỉ mục</text>
    
    <!-- Table Update -->
    <rect x="50" y="65" width="290" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="195" y="90" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">1. Sửa bản ghi trong Bảng</text>
    <rect x="70" y="110" width="250" height="35" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="195" y="132" font-size="11" fill="#1e293b" text-anchor="middle">Mã ID 101: Lương cũ 50.000 → Mới 65.000</text>
    <text x="195" y="175" font-size="11" fill="#1e40af" text-anchor="middle">Nếu chỉ sửa ở đây, truy vấn khoảng</text>
    <text x="195" y="192" font-size="11" fill="#1e40af" text-anchor="middle">sẽ đọc sai theo chỉ mục cũ!</text>

    <!-- Sync Arrow -->
    <path d="M 345 137 L 415 137" stroke="#ef4444" stroke-width="2.5" marker-end="url(#redArrow)"/>
    <text x="380" y="125" font-size="11" font-weight="700" fill="#ef4444" text-anchor="middle">Đồng bộ</text>

    <!-- Index Update -->
    <rect x="420" y="65" width="290" height="145" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="565" y="90" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">2. Sửa chỉ mục (B+-Tree)</text>
    <rect x="440" y="110" width="250" height="35" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="565" y="132" font-size="11" font-weight="600" fill="#92400e" text-anchor="middle">Xóa khóa 50k, Chèn khóa mới 65k</text>
    <text x="565" y="175" font-size="11" fill="#78350f" text-anchor="middle">Phát sinh tách/gộp nút lá cây B+</text>
    <text x="565" y="192" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">Phải đảm bảo tính nhất quán dữ liệu</text>
  `),

  // 25. danh-gia-luu-tru.svg
  'danh-gia-luu-tru.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Dung lượng lưu trữ: Dữ liệu mã hóa + Toàn bộ thông tin giải mã</text>
    
    <!-- File structure bar -->
    <g transform="translate(60, 75)">
      <rect x="0" y="0" width="640" height="60" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
      
      <!-- Meta / Dictionary part -->
      <rect x="0" y="0" width="220" height="60" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="2"/>
      <text x="110" y="28" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">Thông tin phụ trợ</text>
      <text x="110" y="46" font-size="11" fill="#78350f" text-anchor="middle">Cây mã, Từ điển, Header (H byte)</text>

      <!-- Compressed payload -->
      <rect x="220" y="0" width="420" height="60" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="2"/>
      <text x="430" y="28" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">Dữ liệu mã nén (Payload)</text>
      <text x="430" y="46" font-size="11" fill="#1e40af" text-anchor="middle">Chuỗi bit nén đã mã hóa (B byte)</text>
    </g>

    <text x="380" y="170" font-size="14" font-weight="700" fill="#1e293b" text-anchor="middle">Tổng kích thước lưu trữ = H (Phụ trợ) + B (Mã nén)</text>
    <text x="380" y="195" font-size="11" fill="#64748b" text-anchor="middle">Với tệp nhỏ hoặc dữ liệu ngẫu nhiên: H + B có thể LỚN HƠN tệp gốc ban đầu!</text>
  `),

  // 26. danh-gia-do-thu-hoi.svg
  'danh-gia-do-thu-hoi.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chất lượng kết quả gần đúng: Độ thu hồi recall@k (Ví dụ k = 5)</text>
    
    <!-- True ground truth -->
    <rect x="40" y="65" width="260" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="170" y="90" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Tập chuẩn đúng N₅(q)</text>
    <rect x="60" y="105" width="220" height="40" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="170" y="130" font-size="14" font-weight="700" fill="#1e293b" text-anchor="middle">{ a,  b,  c,  d,  e }</text>
    <text x="170" y="170" font-size="11" fill="#b91c1c" font-weight="600" text-anchor="middle">a, b: Hàng xóm thật bị bỏ sót</text>
    <text x="170" y="190" font-size="10" fill="#64748b" text-anchor="middle">(False Negatives)</text>

    <!-- Retrieved set -->
    <rect x="460" y="65" width="260" height="145" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="590" y="90" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Tập trả về N̂₅(q)</text>
    <rect x="480" y="105" width="220" height="40" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="590" y="130" font-size="14" font-weight="700" fill="#1e293b" text-anchor="middle">{ c,  d,  e,  f,  g }</text>
    <text x="590" y="170" font-size="11" fill="#b45309" font-weight="600" text-anchor="middle">f, g: Mục sai nằm ngoài tập đúng</text>
    <text x="590" y="190" font-size="10" fill="#64748b" text-anchor="middle">(False Positives)</text>

    <!-- Overlap Center Box -->
    <rect x="320" y="90" width="120" height="80" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="2" filter="url(#shadow)"/>
    <text x="380" y="115" font-size="11" font-weight="700" fill="#065f46" text-anchor="middle">Giao: { c, d, e }</text>
    <text x="380" y="135" font-size="15" font-weight="700" fill="#047857" text-anchor="middle">3 / 5</text>
    <text x="380" y="155" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">Recall = 60%</text>
  `),

  // 27. danh-gia-ung-vien.svg
  'danh-gia-ung-vien.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Lọc ứng viên và Nguy cơ bỏ sót: R̂ = A ∩ R ⊆ R</text>
    
    <!-- All pairs pool -->
    <rect x="40" y="60" width="180" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="130" y="85" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">Kho N(N-1)/2 cặp</text>
    <circle cx="100" cy="120" r="12" fill="#bfdbfe"/>
    <circle cx="150" cy="115" r="12" fill="#86efac"/>
    <circle cx="120" cy="160" r="12" fill="#fca5a5"/>
    <text x="130" y="195" font-size="10" fill="#64748b" text-anchor="middle">Chứa tập đúng R</text>

    <!-- Filter Arrow -->
    <path d="M 225 110 L 295 110" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="260" y="100" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Bộ lọc LSH</text>

    <!-- Candidates A -->
    <rect x="305" y="60" width="190" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="400" y="85" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">Tập ứng viên A</text>
    <rect x="320" y="105" width="160" height="30" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="400" y="125" font-size="11" font-weight="600" fill="#92400e" text-anchor="middle">Cặp được chọn vào A</text>
    <text x="400" y="160" font-size="10" fill="#78350f" text-anchor="middle">Cặp ngoài A: BỊ LOẠI HẲN</text>
    <text x="400" y="180" font-size="10" font-weight="700" fill="#b91c1c" text-anchor="middle">Không thể khôi phục!</text>

    <!-- Verify Arrow -->
    <path d="M 500 120 L 550 120" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>
    <text x="525" y="110" font-size="10" font-weight="600" fill="#10b981" text-anchor="middle">Hậu kiểm</text>

    <!-- Final Result -->
    <rect x="560" y="60" width="160" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="640" y="85" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">Đầu ra R̂ = A ∩ R</text>
    <rect x="575" y="105" width="130" height="40" rx="4" fill="#ffffff" stroke="#86efac"/>
    <text x="640" y="130" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">Đạt ngưỡng τ</text>
    <text x="640" y="168" font-size="10" fill="#065f46" text-anchor="middle">Hậu kiểm chỉ loại</text>
    <text x="640" y="184" font-size="10" fill="#065f46" text-anchor="middle">ứng viên sai trong A</text>
  `),

  // 28. ban-do-hoc-phan.svg
  'ban-do-hoc-phan.svg': svgWrapper(760, 260, `
    <text x="380" y="25" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bản đồ cấu trúc học phần: Giải thuật nền tảng của Khoa học dữ liệu (UET.DSE2053)</text>
    
    <!-- Central Node Bài 01 -->
    <rect x="40" y="90" width="130" height="80" rx="8" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="105" y="125" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">Bài 01: Nền tảng</text>
    <text x="105" y="145" font-size="10" fill="#e2ebfd" text-anchor="middle">Dữ liệu lớn &amp; Mô hình</text>

    <!-- 5 Branches -->
    <!-- Branch 1: Phân tán & Xếp hạng -->
    <path d="M 175 105 L 250 55" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="255" y="35" width="225" height="42" rx="6" fill="url(#softBlue)" stroke="#244bd6"/>
    <text x="367" y="52" font-size="11" font-weight="700" fill="#1e3a8a" text-anchor="middle">Nhánh 1: Phân tán &amp; Xếp hạng</text>
    <text x="367" y="68" font-size="10" fill="#334155" text-anchor="middle">Bài 02 MapReduce · 03 PageRank · 04 TrustRank</text>

    <!-- Branch 2: Tương đồng & Tìm gần -->
    <path d="M 175 120 L 250 95" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="255" y="80" width="225" height="42" rx="6" fill="url(#softGreen)" stroke="#10b981"/>
    <text x="367" y="97" font-size="11" font-weight="700" fill="#065f46" text-anchor="middle">Nhánh 2: Tương đồng &amp; Vector</text>
    <text x="367" y="113" font-size="10" fill="#334155" text-anchor="middle">Bài 05 Shingle/MinHash · 06 LSH · 07 HNSW/PQ</text>

    <!-- Branch 3: Dòng dữ liệu & Cửa sổ -->
    <path d="M 175 135 L 250 140" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="255" y="125" width="225" height="42" rx="6" fill="url(#softAmber)" stroke="#f59e0b"/>
    <text x="367" y="142" font-size="11" font-weight="700" fill="#b45309" text-anchor="middle">Nhánh 3: Dòng dữ liệu &amp; Cửa sổ</text>
    <text x="367" y="158" font-size="10" fill="#334155" text-anchor="middle">Bài 08 Sampling/Bloom · 09 Count-Min/DGIM</text>

    <!-- Branch 4: Nén dữ liệu -->
    <path d="M 175 150 L 250 185" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="255" y="170" width="225" height="42" rx="6" fill="#fdf4ff" stroke="#c084fc"/>
    <text x="367" y="187" font-size="11" font-weight="700" fill="#7e22ce" text-anchor="middle">Nhánh 4: Nén dữ liệu</text>
    <text x="367" y="203" font-size="10" fill="#334155" text-anchor="middle">Bài 10 Huffman · Bài 11 LZ77/LZ78/JPEG</text>

    <!-- Branch 5: Lưu trữ & Truy vấn -->
    <path d="M 175 165 L 250 230" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="255" y="215" width="225" height="42" rx="6" fill="#f8fafc" stroke="#64748b"/>
    <text x="367" y="232" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">Nhánh 5: Lưu trữ &amp; Truy vấn</text>
    <text x="367" y="248" font-size="10" fill="#475569" text-anchor="middle">Bài 12 Sắp ngoài · 13 B-Tree · 14 R-Tree · 15 Join</text>

    <!-- Connecting prerequisite lines to Bài 15 -->
    <path d="M 485 236 L 530 236" stroke="#64748b" stroke-width="1.5" marker-end="url(#grayArrow)"/>
    <rect x="535" y="165" width="185" height="92" rx="6" fill="url(#softBlue)" stroke="#244bd6"/>
    <text x="627" y="190" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">Bài 15: Nối bảng Join</text>
    <text x="627" y="210" font-size="10" fill="#334155" text-anchor="middle">• Nhận hỗ trợ từ Bài 12, 13</text>
    <text x="627" y="228" font-size="10" fill="#334155" text-anchor="middle">• Kết hợp phân tán Bài 02</text>
    <text x="627" y="245" font-size="10" fill="#244bd6" font-weight="600" text-anchor="middle">Tổng hợp toàn học phần</text>
  `),

  // 29. chuong-trinh-cap-ung-vien.svg
  'chuong-trinh-cap-ung-vien.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Quy trình tìm cặp tương đồng: Shingling → MinHash → LSH → Hậu kiểm Jaccard</text>
    
    <g transform="translate(30, 60)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="155" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
      <text x="77" y="28" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">1. Shingling</text>
      <text x="77" y="50" font-size="10" fill="#334155" text-anchor="middle">Tài liệu văn bản</text>
      <text x="77" y="70" font-size="13" fill="#244bd6" text-anchor="middle">↓</text>
      <text x="77" y="95" font-size="11" font-weight="600" fill="#1e3a8a" text-anchor="middle">Tập Shingle k ký tự</text>
      <text x="77" y="120" font-size="10" fill="#64748b" text-anchor="middle">(Tập hợp không lặp)</text>

      <!-- Arrow 1 -->
      <path d="M 160 72 L 180 72" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Step 2 -->
      <rect x="185" y="0" width="155" height="145" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
      <text x="262" y="28" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">2. MinHash</text>
      <text x="262" y="50" font-size="10" fill="#334155" text-anchor="middle">Hoán vị ngẫu nhiên</text>
      <text x="262" y="70" font-size="13" fill="#10b981" text-anchor="middle">↓</text>
      <text x="262" y="95" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">Chữ ký ngắn gọn</text>
      <text x="262" y="120" font-size="10" fill="#065f46" text-anchor="middle">Pr(h(A)=h(B)) = J(A,B)</text>

      <!-- Arrow 2 -->
      <path d="M 345 72 L 365 72" stroke="#10b981" stroke-width="2" marker-end="url(#greenArrow)"/>

      <!-- Step 3 -->
      <rect x="370" y="0" width="155" height="145" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="447" y="28" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">3. LSH Băm dải</text>
      <text x="447" y="50" font-size="10" fill="#334155" text-anchor="middle">Chia b dải, r hàng</text>
      <text x="447" y="70" font-size="13" fill="#f59e0b" text-anchor="middle">↓</text>
      <text x="447" y="95" font-size="11" font-weight="600" fill="#b45309" text-anchor="middle">Tập cặp ứng viên A</text>
      <text x="447" y="120" font-size="10" fill="#78350f" text-anchor="middle">Tránh xét C(N, 2)</text>

      <!-- Arrow 3 -->
      <path d="M 530 72 L 550 72" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Step 4 -->
      <rect x="555" y="0" width="145" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
      <text x="627" y="28" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">4. Hậu kiểm</text>
      <text x="627" y="50" font-size="10" fill="#334155" text-anchor="middle">Chỉ tính Jaccard</text>
      <text x="627" y="70" font-size="11" fill="#244bd6" text-anchor="middle">trên cặp trong A</text>
      <text x="627" y="95" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Kiểm tra: J ≥ τ</text>
      <text x="627" y="120" font-size="10" fill="#b91c1c" text-anchor="middle">Xuất kết quả R̂</text>
    </g>
  `),

  // 30. chuong-trinh-vec-to.svg
  'chuong-trinh-vec-to.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Hai hướng tối ưu truy vấn Vector quy mô lớn: HNSW vs Product Quantization (PQ)</text>
    
    <!-- HNSW Side -->
    <rect x="40" y="60" width="320" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="200" y="85" font-size="14" font-weight="700" fill="#1e3a8a" text-anchor="middle">HNSW (Đồ thị nhiều tầng)</text>
    <text x="200" y="110" font-size="11" fill="#334155" text-anchor="middle">• Tầng trên thưa: Nhảy bước lớn định vị</text>
    <text x="200" y="130" font-size="11" fill="#334155" text-anchor="middle">• Tầng dưới dày: Tìm kiếm cục bộ chính xác</text>
    <rect x="60" y="145" width="280" height="32" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="200" y="165" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Giảm số lượng vector cần so sánh</text>
    <text x="200" y="195" font-size="10" fill="#1e40af" text-anchor="middle">Thời gian truy vấn O(log N)</text>

    <!-- PQ Side -->
    <rect x="400" y="60" width="320" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="560" y="85" font-size="14" font-weight="700" fill="#065f46" text-anchor="middle">PQ (Lượng tử hóa tích)</text>
    <text x="560" y="110" font-size="11" fill="#334155" text-anchor="middle">• Cắt vector 3072 chiều thành m đoạn nhỏ</text>
    <text x="560" y="130" font-size="11" fill="#334155" text-anchor="middle">• Mỗi đoạn đại diện bằng 1 mã centroid (1 byte)</text>
    <rect x="420" y="145" width="280" height="32" rx="4" fill="#ffffff" stroke="#a7f3d0"/>
    <text x="560" y="165" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">Nén 97% RAM &amp; Bảng tra khoảng cách nhanh</text>
    <text x="560" y="195" font-size="10" fill="#065f46" text-anchor="middle">Vẫn quét toàn kho hoặc kết hợp IVF-PQ</text>
  `),

  // 31. chuong-trinh-mau-loc.svg
  'chuong-trinh-mau-loc.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Xử lý dòng dữ liệu: Phân biệt Mẫu đại diện và Bộ lọc thành viên</text>
    
    <!-- Sampling Box -->
    <rect x="50" y="60" width="300" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="200" y="85" font-size="14" font-weight="700" fill="#1e3a8a" text-anchor="middle">Lấy mẫu (Sampling)</text>
    <text x="70" y="115" font-size="11" fill="#334155">• Giữ lại một phần đại diện của dòng</text>
    <text x="70" y="135" font-size="11" fill="#334155">• Lấy mẫu theo khóa (User): đo mức lặp</text>
    <text x="70" y="155" font-size="11" fill="#334155">• Lấy mẫu hồ chứa (Reservoir): mẫu ngẫu nhiên</text>
    <text x="200" y="195" font-size="11" font-weight="600" fill="#244bd6" text-anchor="middle">Mục tiêu: Thống kê không chệch</text>

    <!-- Bloom Filter Box -->
    <rect x="410" y="60" width="300" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
    <text x="560" y="85" font-size="14" font-weight="700" fill="#065f46" text-anchor="middle">Bộ lọc Bloom (Membership Filter)</text>
    <text x="430" y="115" font-size="11" fill="#334155">• Kiểm tra phần tử x có thuộc tập S không</text>
    <text x="430" y="135" font-size="11" fill="#334155">• Trả lời: &quot;Chắc chắn KHÔNG&quot; (Không bỏ sót)</text>
    <text x="430" y="155" font-size="11" fill="#334155">• Trả lời: &quot;CÓ THỂ CÓ&quot; (Có sai số dương tính)</text>
    <text x="560" y="195" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">Mục tiêu: Tiết kiệm tối đa bộ nhớ tra cứu</text>
  `),

  // 32. hoc-tap-san-pham.svg
  'hoc-tap-san-pham.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Chu trình kỹ năng tạo sản phẩm học tập (CLO1 → CLO4)</text>
    
    <g transform="translate(35, 65)">
      <!-- Step 1 -->
      <rect x="0" y="0" width="150" height="120" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
      <text x="75" y="30" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">1. Đặc tả chặt chẽ</text>
      <text x="75" y="55" font-size="10" fill="#334155" text-anchor="middle">• Miền đầu vào</text>
      <text x="75" y="75" font-size="10" fill="#334155" text-anchor="middle">• Đầu ra chính xác</text>
      <text x="75" y="95" font-size="10" fill="#334155" text-anchor="middle">• Giả thiết &amp; sai số</text>

      <path d="M 155 60 L 175 60" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Step 2 -->
      <rect x="180" y="0" width="150" height="120" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5"/>
      <text x="255" y="30" font-size="12" font-weight="700" fill="#065f46" text-anchor="middle">2. Dry-run vết chạy</text>
      <text x="255" y="55" font-size="10" fill="#334155" text-anchor="middle">• Chạy tay ví dụ nhỏ</text>
      <text x="255" y="75" font-size="10" fill="#334155" text-anchor="middle">• Bảng biến trạng thái</text>
      <text x="255" y="95" font-size="10" fill="#334155" text-anchor="middle">• Trường hợp biên</text>

      <path d="M 335 60 L 355 60" stroke="#10b981" stroke-width="2" marker-end="url(#greenArrow)"/>

      <!-- Step 3 -->
      <rect x="360" y="0" width="150" height="120" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="435" y="30" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">3. Lập luận bất biến</text>
      <text x="435" y="55" font-size="10" fill="#334155" text-anchor="middle">• Bất biến vòng lặp</text>
      <text x="435" y="75" font-size="10" fill="#334155" text-anchor="middle">• Chứng minh dừng</text>
      <text x="435" y="95" font-size="10" fill="#334155" text-anchor="middle">• Tính đúng đắn</text>

      <path d="M 515 60 L 535 60" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Step 4 -->
      <rect x="540" y="0" width="150" height="120" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5" filter="url(#shadow)"/>
      <text x="615" y="30" font-size="12" font-weight="700" fill="#1e3a8a" text-anchor="middle">4. Cài đặt &amp; Đo đạc</text>
      <text x="615" y="55" font-size="10" fill="#334155" text-anchor="middle">• Code Python/C++</text>
      <text x="615" y="75" font-size="10" fill="#334155" text-anchor="middle">• Đo độ trễ, RAM</text>
      <text x="615" y="95" font-size="10" fill="#334155" text-anchor="middle">• Báo cáo trung thực</text>
    </g>
    <text x="380" y="215" font-size="11" fill="#64748b" text-anchor="middle">Mã chạy đúng 1 lần không thay thế chứng minh; chạy nhanh 1 lần không chứng minh độ phức tạp tiệm cận</text>
  `),

  // 33. suy-luan-mau-luu-tru.svg
  'suy-luan-mau-luu-tru.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bài toán hồ sơ lưu trú: Cặp người (u, v) trùng khách sạn trong 2 ngày khác nhau</text>
    
    <!-- Day s -->
    <rect x="60" y="60" width="280" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="200" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Ngày quan sát s</text>
    <rect x="80" y="105" width="240" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="200" y="125" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">Người u ở Khách sạn H₁</text>
    <rect x="80" y="145" width="240" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="200" y="165" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">Người v ở Khách sạn H₁ (TRÙNG)</text>
    <text x="200" y="195" font-size="10" fill="#1e40af" text-anchor="middle">Cùng ở khách sạn H₁ trong ngày s</text>

    <!-- AND connector -->
    <circle cx="380" cy="132" r="20" fill="#1e293b"/>
    <text x="380" y="137" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">VÀ</text>

    <!-- Day t -->
    <rect x="420" y="60" width="280" height="145" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="560" y="85" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Ngày quan sát t (t ≠ s)</text>
    <rect x="440" y="105" width="240" height="30" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="560" y="125" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">Người u ở Khách sạn H₂</text>
    <rect x="440" y="145" width="240" height="30" rx="4" fill="#ffffff" stroke="#fcd34d"/>
    <text x="560" y="165" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">Người v ở Khách sạn H₂ (TRÙNG)</text>
    <text x="560" y="195" font-size="10" fill="#78350f" text-anchor="middle">Khách sạn H₂ có thể KHÁC khách sạn H₁!</text>
  `),

  // 34. suy-luan-hai-ngay.svg
  'suy-luan-hai-ngay.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Tính xác suất trùng trong 2 ngày dưới giả thiết độc lập</text>
    
    <!-- Day 1 Calc -->
    <rect x="50" y="60" width="280" height="145" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="190" y="88" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Trùng trong 1 ngày bất kỳ</text>
    <text x="70" y="115" font-size="11" fill="#334155">• Cả 2 cùng đi: q² = (0.01)² = 10⁻⁴</text>
    <text x="70" y="135" font-size="11" fill="#334155">• Cùng chọn 1 trong H = 10⁵ khách sạn: 1/H</text>
    <rect x="70" y="150" width="240" height="35" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="190" y="172" font-size="13" font-weight="700" fill="#244bd6" text-anchor="middle">p = q² / H = 10⁻⁹</text>

    <!-- Multiplication Arrow -->
    <path d="M 335 132 L 420 132" stroke="#244bd6" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="377" y="120" font-size="11" font-weight="700" fill="#244bd6" text-anchor="middle">Độc lập</text>

    <!-- 2 Days Calc -->
    <rect x="430" y="60" width="280" height="145" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="570" y="88" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Trùng trong cả 2 ngày đã chọn</text>
    <text x="450" y="115" font-size="11" fill="#334155">• Do 2 ngày độc lập với nhau:</text>
    <text x="450" y="135" font-size="11" fill="#334155">• Pr(trùng s VÀ t) = Pr(s) × Pr(t)</text>
    <rect x="450" y="150" width="240" height="35" rx="4" fill="#ffffff" stroke="#86efac"/>
    <text x="570" y="172" font-size="14" font-weight="700" fill="#b91c1c" text-anchor="middle">p² = 10⁻⁹ × 10⁻⁹ = 10⁻¹⁸</text>
    <text x="570" y="198" font-size="10" fill="#065f46" text-anchor="middle">Xác suất 1 phép thử cực kỳ nhỏ!</text>
  `),

  // 35. phep-thu-va-duong-tinh-gia.svg
  'phep-thu-va-duong-tinh-gia.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bùng nổ số phép thử và Hiện tượng dương tính giả (Nguyên lý Bonferroni)</text>
    
    <!-- Trials Box -->
    <rect x="40" y="60" width="310" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="195" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Tổng số phép thử khổng lồ:</text>
    <text x="60" y="110" font-size="11" fill="#334155">• Chọn cặp người: C(10⁹, 2) ≈ 5 × 10¹⁷</text>
    <text x="60" y="130" font-size="11" fill="#334155">• Chọn cặp ngày: C(1000, 2) ≈ 5 × 10⁵</text>
    <rect x="55" y="145" width="280" height="35" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="195" y="167" font-size="12" font-weight="700" fill="#244bd6" text-anchor="middle">Số phép thử = C(P, 2) · C(T, 2) ≈ 2.5 × 10²³</text>
    <text x="195" y="198" font-size="10" fill="#64748b" text-anchor="middle">Mỗi phép thử có xác suất p² = 10⁻¹⁸</text>

    <!-- Arrow -->
    <path d="M 355 135 L 400 135" stroke="#ef4444" stroke-width="2.5" marker-end="url(#redArrow)"/>

    <!-- Expectation Box -->
    <rect x="410" y="60" width="310" height="150" rx="8" fill="url(#softAmber)" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="565" y="85" font-size="13" font-weight="700" fill="#b45309" text-anchor="middle">Kỳ vọng số cặp trùng ngẫu nhiên:</text>
    <rect x="425" y="102" width="280" height="50" rx="6" fill="#ffffff" stroke="#fcd34d"/>
    <text x="565" y="125" font-size="12" fill="#78350f" text-anchor="middle">E[X] = 2.5 × 10²³ × 10⁻¹⁸</text>
    <text x="565" y="144" font-size="16" font-weight="700" fill="#b91c1c" text-anchor="middle">≈ 249.750 CẶP TRÙNG!</text>
    <text x="565" y="175" font-size="11" font-weight="600" fill="#1e293b" text-anchor="middle">Trùng ngẫu nhiên lấn át dấu hiệu thật!</text>
    <text x="565" y="195" font-size="10" fill="#78350f" text-anchor="middle">Không thể kết luận họ cấu kết chỉ vì có trùng</text>
  `),

  // 36. bai-tap-quy-mo.svg
  'bai-tap-quy-mo.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bài tập 1.2.1: Thay đổi riêng từng quy mô (a) T=2000 ngày vs (b) P=2 tỷ người</text>
    
    <!-- Base model -->
    <rect x="40" y="90" width="170" height="80" rx="8" fill="url(#blueGrad)" filter="url(#shadow)"/>
    <text x="125" y="120" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">Mô hình gốc</text>
    <text x="125" y="142" font-size="11" fill="#e2ebfd" text-anchor="middle">E[X] ≈ 249.750 cặp</text>

    <!-- Branch A -->
    <path d="M 215 110 L 320 80" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="330" y="55" width="390" height="65" rx="6" fill="url(#softAmber)" stroke="#f59e0b"/>
    <text x="345" y="78" font-size="12" font-weight="700" fill="#b45309">(a) Tăng thời gian lên T = 2000 ngày:</text>
    <text x="345" y="98" font-size="11" fill="#78350f">C(2000, 2) tăng gần 4 lần → Kỳ vọng tăng 4 lần:</text>
    <text x="630" y="98" font-size="12" font-weight="700" fill="#b91c1c">E ≈ 999.500 cặp</text>

    <!-- Branch B -->
    <path d="M 215 150 L 320 175" stroke="#244bd6" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="330" y="145" width="390" height="65" rx="6" fill="url(#softGreen)" stroke="#10b981"/>
    <text x="345" y="168" font-size="12" font-weight="700" fill="#065f46">(b) Tăng P = 2 tỷ người, H = 200.000 khách sạn:</text>
    <text x="345" y="188" font-size="11" fill="#047857">C(P, 2) tăng gần 4 lần, nhưng p² giảm đúng 4 lần →</text>
    <text x="630" y="188" font-size="12" font-weight="700" fill="#047857">E ≈ 249.750 (Gần như không đổi)</text>
  `),

  // 37. bai-tap-ba-ngay.svg
  'bai-tap-ba-ngay.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bài tập 1.2.1(c): Nâng tiêu chuẩn lên TRÙNG TRONG CẢ 3 NGÀY (k = 3)</text>
    
    <!-- 3 days inspection -->
    <rect x="50" y="60" width="310" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="205" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Phép thử trên bộ 3 ngày:</text>
    <text x="70" y="110" font-size="11" fill="#334155">• Số bộ 3 ngày: C(1000, 3) ≈ 1.66 × 10⁸</text>
    <text x="70" y="130" font-size="11" fill="#334155">• Xác suất trùng 3 ngày độc lập:</text>
    <rect x="70" y="142" width="270" height="30" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="205" y="162" font-size="12" font-weight="700" fill="#244bd6" text-anchor="middle">p³ = (10⁻⁹)³ = 10⁻²⁷</text>
    <text x="205" y="195" font-size="10" fill="#1e40af" text-anchor="middle">Số mũ k=3 dập tắt xác suất cực mạnh</text>

    <!-- Arrow -->
    <path d="M 365 135 L 415 135" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>

    <!-- Result -->
    <rect x="425" y="60" width="285" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="567" y="85" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Kỳ vọng số cặp trùng ngẫu nhiên:</text>
    <rect x="440" y="105" width="255" height="40" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="567" y="130" font-size="16" font-weight="700" fill="#047857" text-anchor="middle">E[X_c] ≈ 0.0831</text>
    <text x="567" y="165" font-size="12" font-weight="600" fill="#065f46" text-anchor="middle">Kỳ vọng ngẫu nhiên GIẢM XUỐNG DƯỚI 1!</text>
    <text x="567" y="190" font-size="10" fill="#334155" text-anchor="middle">Dấu hiệu nếu xuất hiện ít bị chìm trong nhiễu</text>
  `),

  // 38. ung-dung-trung-gio-hang.svg
  'ung-dung-trung-gio-hang.svg': svgWrapper(760, 240, `
    <text x="380" y="28" font-size="15" font-weight="700" fill="#1e293b" text-anchor="middle">Bài tập 1.2.2: Trùng tập 10 mặt hàng giỏ hàng giữa 2 người khác nhau</text>
    
    <!-- Cart matching -->
    <rect x="40" y="60" width="310" height="150" rx="8" fill="url(#softBlue)" stroke="#244bd6" stroke-width="1.5"/>
    <text x="195" y="85" font-size="13" font-weight="700" fill="#1e3a8a" text-anchor="middle">Không gian giỏ hàng</text>
    <text x="60" y="110" font-size="11" fill="#334155">• Mua 10 trong 1000 mặt hàng</text>
    <text x="60" y="130" font-size="11" fill="#334155">• Số tập 10 món: C(1000, 10) ≈ 2.63 × 10²³</text>
    <rect x="55" y="145" width="280" height="32" rx="4" fill="#ffffff" stroke="#93c5fd"/>
    <text x="195" y="165" font-size="11" font-weight="700" fill="#244bd6" text-anchor="middle">Xác suất trùng 2 giỏ = 1 / C(1000, 10) ≈ 3.8 × 10⁻²⁴</text>
    <text x="195" y="195" font-size="10" fill="#64748b" text-anchor="middle">100 triệu người · Mỗi người đi 100 lần/năm</text>

    <!-- Arrow -->
    <path d="M 355 135 L 405 135" stroke="#10b981" stroke-width="2.5" marker-end="url(#greenArrow)"/>

    <!-- Cart Expectation -->
    <rect x="415" y="60" width="305" height="150" rx="8" fill="url(#softGreen)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="567" y="85" font-size="13" font-weight="700" fill="#065f46" text-anchor="middle">Kỳ vọng số cặp lượt trùng ngẫu nhiên:</text>
    <rect x="430" y="105" width="275" height="40" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="567" y="130" font-size="15" font-weight="700" fill="#047857" text-anchor="middle">E[Y] ≈ 1.90 × 10⁻⁴ (Rất nhỏ!)</text>
    <text x="567" y="165" font-size="11" font-weight="600" fill="#065f46" text-anchor="middle">Pr(Y ≥ 1) ≤ E[Y] ≈ 0.019%</text>
    <text x="567" y="190" font-size="10" fill="#334155" text-anchor="middle">Không bị ngập bởi trùng ngẫu nhiên như khách sạn</text>
  `)
}

console.log(`Generating ${Object.keys(diagrams).length} SVGs...`)
for (const [name, content] of Object.entries(diagrams)) {
  for (const dir of targets) {
    await writeFile(path.join(dir, name), content.trim(), 'utf8')
  }
}
console.log('All 38 SVGs generated successfully in both targets!')
