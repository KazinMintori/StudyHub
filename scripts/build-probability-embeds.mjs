import assert from 'node:assert/strict'
import { readFile, writeFile, mkdir } from 'node:fs/promises'
import path from 'node:path'

const sourceRoot = process.argv[2] || 'raw_materials/xac-suat-thong-ke/stat20-spring-2026/full-course'
const targetRoot = process.argv[3] || '.'
const manifest = JSON.parse(await readFile(path.join(sourceRoot, 'manifest.json'), 'utf8'))
const base = manifest.base
const groups = [
  ['1-questions-and-data', 'Câu hỏi và dữ liệu'],
  ['2-summarizing-data', 'Thống kê mô tả'],
  ['3-generalization', 'Xác suất và suy luận thống kê'],
  ['4-causation', 'Nhân quả'],
  ['5-prediction', 'Dự đoán']
]
const titles = {
  '1-questions-and-data': 'Mở đầu: Câu hỏi và dữ liệu',
  '01-understanding-the-world': 'Hiểu thế giới bằng dữ liệu',
  '02-taxonomy-of-data': 'Phân loại dữ liệu',
  '2-summarizing-data': 'Mở đầu: Thống kê mô tả',
  '01-summarizing-categorical-data': 'Tóm tắt dữ liệu phân loại',
  '02-summarizing-numerical-data': 'Tóm tắt dữ liệu số',
  '03-a-grammar-of-graphics': 'Ngữ pháp của biểu đồ',
  '04-conditioning': 'Phân tích theo điều kiện',
  '05-summarizing-associations': 'Mối liên hệ giữa các biến số',
  '06-multiple-linear-regression': 'Hồi quy tuyến tính nhiều biến',
  '3-generalization': 'Mở đầu: Suy rộng thống kê',
  '01-prob-foundations': 'Cơ sở xác suất',
  '02-computing-probs': 'Tính xác suất',
  '03-probability-dsns': 'Các phân phối xác suất',
  '04-random-variables': 'Biến ngẫu nhiên',
  '05-ev-se': 'Kỳ vọng và phương sai',
  '06-normal-approx': 'Phân phối liên tục và xấp xỉ chuẩn',
  '07-from-samps-to-pops': 'Từ mẫu đến tổng thể',
  '08-confidence-intervals': 'Khoảng tin cậy',
  '09-bootstrapping': 'Bootstrap',
  '10-hypothesis-tests': 'Kiểm định giả thuyết',
  '11-hypothesis-tests-2': 'Kiểm định giả thuyết: phần tiếp theo',
  '12-wrong-by-design': 'Sai lầm trong thiết kế và suy luận',
  '4-causation': 'Mở đầu: Nhân quả',
  '01-defining-causality': 'Định nghĩa quan hệ nhân quả',
  '02-experiments': 'Thí nghiệm ngẫu nhiên',
  '03-matching': 'Tác động nhân quả trong nghiên cứu quan sát',
  '01-method-of-least-squares': 'Phương pháp bình phương tối thiểu',
  '02-improving-predictions': 'Đánh giá và cải thiện dự đoán',
  '03-overfitting': 'Quá khớp',
  '05-logistic-regression': 'Hồi quy logistic'
}
const records = manifest.records.filter(record => record.status === 'downloaded')
const noteRecords = records.filter(record => record.kind === 'notes').sort((a, b) => {
  const pa = a.url.slice(base.length).split('/'), pb = b.url.slice(base.length).split('/')
  return pa[0].localeCompare(pb[0]) || (pa.length === pb.length ? pa[1].localeCompare(pb[1]) : pa.length - pb.length)
})
assert.equal(noteRecords.length, 31)
const entries = noteRecords.map(record => {
  const relative = record.url.slice(base.length), parts = relative.split('/')
  const id = parts.slice(0, -1).join('--')
  const slide = records.find(item => item.url === record.url.replace('/notes.html', '/slides.html'))
  return { id, title: titles[parts.at(-2)], group: groups.find(([prefix]) => prefix === parts[0])[1], notes: record.url, slides: slide?.url || null }
})
entries.push({ id: 'quiz', title: 'Hướng dẫn kiểm tra', group: 'Tài liệu bổ sung', notes: null, slides: base + 'assets/quiz-slides.html' })
assert(entries.every(entry => entry.title))
assert.equal(entries.filter(entry => entry.slides).length, 28)
const urlMap = Object.fromEntries(entries.flatMap(entry => ['notes', 'slides'].filter(kind => entry[kind]).map(kind => [entry[kind], { id: entry.id, kind }])))
const publicDir = path.join(targetRoot, 'docs/public/materials/xac-suat-thong-ke/embedded')
await mkdir(publicDir, { recursive: true })

function removeBranding(text) {
  return text.replace(/(<script\b[\s\S]*?<\/script>|<style\b[\s\S]*?<\/style>|<pre\b[\s\S]*?<\/pre>|<code\b[\s\S]*?<\/code>|<[^>]+>)|([^<]+)/gi, (whole, tag, content) => {
    if (tag) return tag
    return content.replace(/\bSTAT\s*20\b/gi, 'this course').replace(/\b(?:UC\s+)?Berkeley\b/gi, 'the university')
  })
}
const notesStyle = `
html { color-scheme: light; scroll-behavior: auto; }
body { margin: 0; background: white; color: #202124; }
#quarto-content, #quarto-document-content { display: block !important; width: auto !important; max-width: 900px !important; margin: 0 auto !important; padding: 20px 24px !important; }
#quarto-document-content > * { grid-column: auto !important; }
.column-margin, .margin-caption { position: static !important; width: auto !important; max-width: 100% !important; }
.quarto-title .title { display: block !important; }
img, svg { max-width: 100%; }
pre, .cell-output, table, mjx-container[display=true] { max-width: 100%; overflow-x: auto; }
.studyhub-source-reference { border-top: 1px solid #ddd; margin-top: 40px; padding-top: 16px; font-size: 14px; }
@media(max-width:600px) { #quarto-document-content { padding: 16px !important; } body { font-size: 16px; } }
`
const frameScript = `
(() => {
  const entries = ${JSON.stringify(urlMap)};
  document.addEventListener('click', event => {
    const anchor = event.target.closest('a[href]');
    if (!anchor) return;
    const raw = anchor.getAttribute('href');
    if (raw.startsWith('#')) {
      const target = document.getElementById(decodeURIComponent(raw.slice(1)));
      if (target) { event.preventDefault(); target.scrollIntoView(); }
      return;
    }
    const url = new URL(anchor.href, document.baseURI);
    const key = url.origin + url.pathname;
    if (entries[key]) { event.preventDefault(); parent.postMessage({type:'studyhub-source-navigation', ...entries[key]}, '*'); }
    else { anchor.target = '_blank'; anchor.rel = 'noopener noreferrer'; }
  }, true);
})();`

const audit = []
for (const entry of entries) {
  for (const kind of ['notes', 'slides']) {
    if (!entry[kind]) continue
    const record = records.find(item => item.url === entry[kind])
    assert(record, entry[kind])
    const relative = record.url.slice(base.length)
    const original = await readFile(path.join(sourceRoot, relative), 'utf8')
    const head = original.match(/<head[^>]*>([\s\S]*?)<\/head>/i)?.[1]
    const body = original.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1]
    assert(head && body, relative)
    const main = kind === 'notes' ? body.match(/<main\b[^>]*>[\s\S]*?<\/main>/i)?.[0] : null
    assert(kind === 'slides' || main, relative)
    const references = `<section class="studyhub-source-reference"><h2>Tài liệu tham khảo</h2><p>Stat 20, UC Berkeley — <a href="${record.url}" target="_blank" rel="noopener noreferrer">Tài liệu gốc</a>. Chia sẻ theo <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a>. Nhúng toàn bộ nội dung; điều chỉnh điều hướng và tên hiển thị cho StudyHub.</p></section>`
    let content
    if (kind === 'notes') {
      const outside = body.replace(main, '')
      const scripts = outside.match(/<script\b[\s\S]*?<\/script>/gi) || []
      content = removeBranding(main).replace(/<\/main>/i, references + '</main>') + scripts.join('\n')
      assert.equal((main.match(/<p\b/gi) || []).length + 1, (content.match(/<p\b/gi) || []).length, `${entry.id}: preserve every paragraph`)
    } else {
      content = removeBranding(body).replace(/data-background-image="[^"\n]*stat20-hex[^"\n]*"/gi, '')
      content += `<details style="position:fixed;bottom:8px;left:8px;z-index:100;font-size:12px;background:white;color:black;padding:4px"><summary>Tài liệu tham khảo</summary>${references}</details>`
      assert.equal((body.match(/<section\b/gi) || []).length + 1, (content.match(/<section\b/gi) || []).length, `${entry.id}: preserve every slide section`)
    }
    const html = `<!DOCTYPE html><html lang="en"><head><base href="${record.url}">${removeBranding(head)}<style>${kind === 'notes' ? notesStyle : '.quarto-title-author,.quarto-title-affiliation{display:none!important}'}</style></head><body>${content}<script>${frameScript}</script></body></html>`
    const name = `${entry.id}.${kind}.html`
    await writeFile(path.join(publicDir, name), html)
    audit.push({ id: entry.id, kind, source: record.url, file: name, paragraphs: (main?.match(/<p\b/gi) || []).length, slideSections: (body.match(/<section\b/gi) || []).length })
  }
}
await writeFile(path.join(publicDir, 'coverage.json'), JSON.stringify(audit, null, 2))
const moduleDir = path.join(targetRoot, 'docs/.vitepress')
await mkdir(moduleDir, { recursive: true })
await writeFile(path.join(moduleDir, 'probability-source-library.mjs'), `// All public Notes and Slides linked from the source course indexes.\nexport const probabilitySourceLibrary = ${JSON.stringify(entries, null, 2)}\n`)
console.log(`Built ${audit.filter(item => item.kind === 'notes').length} complete Notes and ${audit.filter(item => item.kind === 'slides').length} complete slide decks.`)
