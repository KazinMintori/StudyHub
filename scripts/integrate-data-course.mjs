// Integrate authored bundles without rebuilding the site or rewriting other courses.
import { readFile, writeFile, mkdir, access } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = fileURLToPath(new URL('../', import.meta.url))
const contract = JSON.parse(await readFile(path.join(root, 'raw_materials/xu-ly-du-lieu/authoring-contract.json'), 'utf8'))
const entries = contract.lessons
const directory = path.join(root, 'src/content/courses/xu-ly-du-lieu')
const imports = entries.flatMap((entry, i) => [
  `import { lesson as lesson${i} } from './lectures/${entry.slug}/lesson.mjs'`,
  `import { slides as slides${i} } from './lectures/${entry.slug}/slides.mjs'`
])
for (const entry of entries) {
  for (const file of [path.join(directory, 'lectures', entry.slug, 'lesson.mjs'),
    path.join(root, 'docs/xu-ly-du-lieu/bai-giang', `${entry.slug}.md`)]) await access(file)
}
const parts = [
  ['Phần 1. Công cụ và ngôn ngữ Python', 'Từ môi trường làm việc đến cấu trúc dữ liệu, hàm và tệp.', ['1', '2', '3']],
  ['Phần 2. Mảng và bảng dữ liệu', 'Tính toán bằng NumPy và làm việc với nhãn trong pandas.', ['4', '5']],
  ['Phần 3. Nạp, làm sạch và tổ chức dữ liệu', 'Đọc đúng dữ liệu, kiểm tra chất lượng, ghép bảng và chuyển dạng.', ['6', '7', '8']],
  ['Phần 4. Biểu đồ, nhóm và thời gian', 'Quan sát phân phối, tổng hợp đúng đơn vị và phân tích theo lịch.', ['9', '10', '11']],
  ['Phần 5. Mô hình và các bài toán phân tích', 'Đưa dữ liệu vào mô hình và kiểm tra kết luận qua nhiều dạng bài toán.', ['12', '13']],
  ['Phụ lục', 'Tra cứu NumPy nâng cao và các công cụ của IPython.', ['A', 'B']]
].map(([title, description, chapters]) => ({ title, description, lessons: chapters.map(chapter => entries.find(e => e.chapter === chapter).slug) }))
const metadata = {
  id: 'xu-ly-du-lieu', code: '04', name: 'Lập trình xử lý dữ liệu', short: 'Xử lý dữ liệu', current: true,
  description: 'Mười ba chương và hai phụ lục: Python, NumPy, pandas, dữ liệu, biểu đồ, mô hình và kiểm tra kết luận.',
  foundations: ['bien-kieu', 'list', 'dictionary', 'ham-lap-trinh', 'vong-lap', 'mang', 'chi-muc', 'vector-hoa', 'broadcasting', 'gia-tri-thieu', 'dataframe', 'groupby', 'thong-ke-mo-ta'],
  parts, illustration: 'broadcast'
}
await writeFile(path.join(directory, 'course.mjs'), imports.join('\n') + '\n\nexport const course = {\n' +
  Object.entries(metadata).map(([key, value]) => `  ${key}: ${JSON.stringify(value, null, 2)}`).join(',\n') + ',\n' +
  `  lessons: [${entries.map((e, i) => `{ ...lesson${i}, number: ${JSON.stringify(e.chapter)} }`).join(', ')}],\n` +
  `  slides: [${entries.map((e, i) => `...slides${i}`).join(', ')}]\n}\n`)

const redirect = target => `---\nlayout: page\nsearch: false\nredirectTo: ${JSON.stringify(target)}\n---\n\n<OldCourseLink />\n`
const retired = {
  'bai-05-series-dataframe-chuyen-sau': 'bai-08-ghep-bang-chuyen-dang',
  'bai-07-xu-ly-chuoi': 'bai-10-lam-sach-du-lieu',
  'bai-11-llm-du-lieu-phi-cau-truc': 'bai-10-lam-sach-du-lieu',
  'bai-13-truc-quan-hoa-nang-cao': 'bai-12-truc-quan-hoa-co-ban'
}
for (const [slug, target] of Object.entries(retired)) {
  for (const folder of ['', 'notes', 'bai-giang']) {
    await writeFile(path.join(root, 'docs/xu-ly-du-lieu', folder, `${slug}.md`), redirect(`/xu-ly-du-lieu/bai-giang/${target}.html`))
  }
}
for (const entry of entries) {
  for (const folder of ['', 'notes']) {
    await mkdir(path.join(root, 'docs/xu-ly-du-lieu', folder), { recursive: true })
    await writeFile(path.join(root, 'docs/xu-ly-du-lieu', folder, `${entry.slug}.md`), redirect(`/xu-ly-du-lieu/bai-giang/${entry.slug}.html`))
  }
}
const links = entries.map(e => `- [${/^\d+$/.test(e.chapter) ? `Chương ${e.chapter}. ` : ''}${e.title}](/xu-ly-du-lieu/bai-giang/${e.slug}.md)`)
await writeFile(path.join(root, 'docs/xu-ly-du-lieu/slides.md'), redirect(`/xu-ly-du-lieu/bai-giang/${entries[0].slug}.html#slides`))
await writeFile(path.join(root, 'docs/xu-ly-du-lieu/notes/lo-trinh.md'), `---\ncourse: xu-ly-du-lieu\ntitle: "Lộ trình học xử lý dữ liệu"\n---\n\n# Lộ trình học xử lý dữ liệu\n\nHọc lần lượt từ môi trường Python đến các bài toán phân tích. Hai phụ lục giúp tra cứu sâu hơn về NumPy và IPython khi cần.\n\n${links.join('\n')}\n\n## Tài liệu tham khảo\n\n- Wes McKinney, [Python for Data Analysis, ấn bản 3](https://wesmckinney.com/book/).\n- [Tài liệu học tập IAI](https://courses.iaidev.com/programming-for-data-processing/2627-1/).\n`)
await writeFile(path.join(root, 'docs/xu-ly-du-lieu/bai-tap.md'), `---\ncourse: xu-ly-du-lieu\ntitle: "Bài tập xử lý dữ liệu theo chương"\n---\n\n# Bài tập xử lý dữ liệu theo chương\n\nBài tập nằm trong từng bài giảng, cạnh phần kiến thức cần dùng. Hãy tự giải trước khi mở lời giải. Với bài thực hành trên dữ liệu bên ngoài, kết quả còn phụ thuộc bản dữ liệu, thời điểm chụp và quy tắc chọn hàng.\n\n${links.join('\n')}\n`)
const inventory = JSON.parse(await readFile(path.join(root, 'raw_materials/xu-ly-du-lieu/source-inventory.json'), 'utf8'))
const sourceMap = {
  checkedOn: inventory.checkedOn,
  mainReference: { title: 'Python for Data Analysis, 3rd edition', author: 'Wes McKinney', url: 'https://wesmckinney.com/book/' },
  supplementaryCourse: 'https://courses.iaidev.com/programming-for-data-processing/2627-1/',
  sourceHandling: contract.mode,
  excluded: ['administrative course content', 'grading and oral examination', 'course project', 'AI closed/open policies', inventory.excludedNotebook],
  unavailable: { iaiLecture9: 'Not linked in the public timetable' },
  lessons: entries.map(e => ({ chapter: e.chapter, lesson: e.slug, title: e.title,
    primary: inventory.records.filter(r => r.source === 'wes' && r.chapter === e.chapter).map(r => r.resolvedUrl),
    coverage: `coverage-${e.group}.json`, verification: `scripts/verify-data-course-${e.group}.py` }))
}
await writeFile(path.join(root, 'raw_materials/xu-ly-du-lieu/source-map.json'), JSON.stringify(sourceMap, null, 2) + '\n')
console.log(`Integrated ${entries.length} chapter and appendix bundles; preserved legacy routes.`)
