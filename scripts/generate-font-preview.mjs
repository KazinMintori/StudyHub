import puppeteer from 'puppeteer'
import { writeFile, mkdir } from 'node:fs/promises'
import path from 'node:path'

const html = `<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Thử nghiệm Font chữ tên web UETệ</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=JetBrains+Mono:wght@600;700&family=Lora:ital,wght@0,600;0,700;1,600&family=Playfair+Display:ital,wght@0,700;1,700&family=Plus+Jakarta+Sans:wght@700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #fbfbf8;
    color: #202521;
    font-family: 'Be Vietnam Pro', system-ui, sans-serif;
    padding: 40px;
  }
  .header {
    text-align: center;
    margin-bottom: 36px;
  }
  .header h1 {
    font-size: 26px;
    font-weight: 700;
    color: #1b3cac;
    margin-bottom: 8px;
  }
  .header p {
    font-size: 14px;
    color: #555d57;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
  }
  .card {
    background: #ffffff;
    border: 1px solid #dedfd8;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  }
  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f0f1ec;
    padding-bottom: 12px;
    margin-bottom: 18px;
  }
  .badge {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #244bd6;
    background: #edf1ff;
    padding: 4px 10px;
    border-radius: 20px;
  }
  .font-name {
    font-size: 13px;
    color: #727b74;
    font-weight: 500;
  }
  .preview-row {
    margin-bottom: 16px;
  }
  .preview-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #8c968f;
    margin-bottom: 6px;
  }
  .nav-mock {
    display: flex;
    align-items: center;
    background: #fbfbf8;
    border: 1px solid #e5e6e0;
    border-radius: 8px;
    padding: 10px 16px;
    gap: 12px;
  }
  .nav-icon {
    width: 32px;
    height: 32px;
    background: #244bd6;
    color: white;
    border-radius: 6px;
    display: grid;
    place-items: center;
    font-weight: 700;
    font-size: 18px;
  }
  .brand-text {
    font-size: 21px;
  }
  .nav-links {
    margin-left: auto;
    display: flex;
    gap: 16px;
    font-size: 12px;
    color: #626b65;
  }
  .dark-mock {
    background: #171b1a;
    border-color: #353e38;
    color: #eef1eb;
  }
  .dark-mock .nav-links {
    color: #a5afa7;
  }
  .dark-mock .nav-icon {
    background: #244bd6;
  }
  .notes {
    font-size: 12px;
    color: #555d57;
    line-height: 1.6;
    margin-top: 14px;
    padding-top: 10px;
    border-top: 1px dashed #e8eae3;
  }

  /* Specific font styles */
  .f-current { font-family: 'Be Vietnam Pro', sans-serif; font-weight: 700; letter-spacing: -0.6px; }
  .f-space { font-family: 'Space Grotesk', sans-serif; font-weight: 700; letter-spacing: -0.8px; }
  .f-lora { font-family: 'Lora', serif; font-weight: 600; letter-spacing: -0.3px; }
  .f-jetbrains { font-family: 'JetBrains Mono', monospace; font-weight: 700; letter-spacing: -0.5px; }
  .f-jakarta { font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; letter-spacing: -0.8px; }
  .f-playfair { font-family: 'Playfair Display', serif; font-weight: 700; letter-spacing: -0.4px; }
</style>
</head>
<body>

<div class="header">
  <h1>BẢNG THỬ NGHIỆM TYPOGRAPHY TÊN WEB: "UETệ" & "UET Study Hub"</h1>
  <p>So sánh hiển thị thực tế trên thanh điều hướng (Light Mode & Dark Mode) với đầy đủ hỗ trợ dấu tiếng Việt</p>
</div>

<div class="grid">
  <!-- Option 1 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 1: Hiện tại (Mặc định)</span>
      <span class="font-name">Be Vietnam Pro (Bold 700)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-current">U</div>
        <div class="brand-text f-current">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-current">U</div>
        <div class="brand-text f-current">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Sans-serif chuẩn mực, thanh thoát, trung tính và dễ đọc ở mọi kích cỡ.
    </div>
  </div>

  <!-- Option 2 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 2: Tech & Công nghệ</span>
      <span class="font-name">Space Grotesk (Bold 700)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-space">U</div>
        <div class="brand-text f-space">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-space">U</div>
        <div class="brand-text f-space">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Góc cạnh sắc sảo, phong cách kỹ thuật cao, rất hợp với bản sắc Đại học Công nghệ (UET).
    </div>
  </div>

  <!-- Option 3 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 3: Học thuật & Giáo trình</span>
      <span class="font-name">Lora (Semi-Bold 600)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-lora">U</div>
        <div class="brand-text f-lora">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-lora">U</div>
        <div class="brand-text f-lora">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Serif thanh lịch, mang cảm giác sách giáo khoa Oxford/Quarto cổ điển, uy tín và chuẩn mực học thuật.
    </div>
  </div>

  <!-- Option 4 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 4: Lập trình & Dân IT</span>
      <span class="font-name">JetBrains Mono (Bold 700)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-jetbrains">U</div>
        <div class="brand-text f-jetbrains">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-jetbrains">U</div>
        <div class="brand-text f-jetbrains">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Monospace sắc nét của môi trường lập trình IDE, cá tính mạnh, đậm chất Khoa học Máy tính và Dữ liệu.
    </div>
  </div>

  <!-- Option 5 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 5: Hiện đại & Cao cấp</span>
      <span class="font-name">Plus Jakarta Sans (Extra-Bold 800)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-jakarta">U</div>
        <div class="brand-text f-jakarta">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-jakarta">U</div>
        <div class="brand-text f-jakarta">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Nét chữ tròn trịa, chắc chắn, chuẩn phong cách các nền tảng công nghệ giáo dục quốc tế (EdTech) hàng đầu.
    </div>
  </div>

  <!-- Option 6 -->
  <div class="card">
    <div class="card-top">
      <span class="badge">Lựa chọn 6: Sang trọng & Điểm nhấn</span>
      <span class="font-name">Playfair Display (Bold 700)</span>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện sáng (Light Mode)</div>
      <div class="nav-mock">
        <div class="nav-icon f-playfair">U</div>
        <div class="brand-text f-playfair">UETệ</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="preview-row">
      <div class="preview-label">Giao diện tối (Dark Mode)</div>
      <div class="nav-mock dark-mock">
        <div class="nav-icon f-playfair">U</div>
        <div class="brand-text f-playfair">UET Study Hub</div>
        <div class="nav-links"><span>Trang chủ</span><span>Học phần</span><span>Wiki</span></div>
      </div>
    </div>
    <div class="notes">
      <strong>Đặc điểm:</strong> Tương phản nét thanh đậm rõ nét, mang phong thái ấn phẩm học thuật danh giá và sang trọng.
    </div>
  </div>
</div>

</body>
</html>
`

const outDir = 'qa'
await mkdir(outDir, { recursive: true })
const htmlPath = path.resolve(outDir, 'font-preview.html')
await writeFile(htmlPath, html, 'utf8')

console.log('Rendering font preview with Puppeteer...')
const executablePath = 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe'
const browser = await puppeteer.launch({ headless: true, executablePath })
const page = await browser.newPage()
await page.setViewport({ width: 1300, height: 1100, deviceScaleFactor: 2 })
await page.goto('file:///' + htmlPath.replace(/\\\\/g, '/'), { waitUntil: 'networkidle0' })
// Wait for Google Fonts to fully load
await page.evaluateHandle('document.fonts.ready')
await new Promise(r => setTimeout(r, 1500))

const screenshotPath = path.resolve(outDir, 'font-comparison.png')
await page.screenshot({ path: screenshotPath, fullPage: true })
await browser.close()

console.log('Screenshot saved to', screenshotPath)
