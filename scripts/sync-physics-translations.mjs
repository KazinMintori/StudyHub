// Integrate only authored, source-linked translations. Never manufacture missing text.
import { readFile, writeFile, mkdir, access } from 'node:fs/promises'
import path from 'node:path'
import { physics1Course, physics2Course } from '../docs/.vitepress/physics-courses.mjs'
import { physicsMotionSlides } from '../docs/.vitepress/physics-motion-course.mjs'

const root=process.cwd()
const chapterTitles=[
  'Đơn vị, đại lượng vật lý và vector','Chuyển động trên đường thẳng','Chuyển động trong hai hoặc ba chiều',
  'Các định luật chuyển động của Newton','Áp dụng các định luật Newton','Công và động năng',
  'Thế năng và bảo toàn năng lượng','Động lượng, xung lượng và va chạm','Chuyển động quay của vật rắn',
  'Động lực học chuyển động quay','Cân bằng và đàn hồi','Cơ học chất lưu','Hấp dẫn','Chuyển động tuần hoàn',
  'Sóng cơ','Âm thanh và sự nghe','Nhiệt độ và nhiệt','Tính chất nhiệt của vật chất',
  'Nguyên lý thứ nhất của nhiệt động lực học','Nguyên lý thứ hai của nhiệt động lực học',
  'Điện tích và điện trường','Định luật Gauss','Điện thế','Điện dung và điện môi',
  'Dòng điện, điện trở và suất điện động','Mạch điện một chiều','Từ trường và lực từ','Nguồn của từ trường',
  'Cảm ứng điện từ','Điện cảm','Dòng điện xoay chiều','Sóng điện từ','Bản chất và sự truyền ánh sáng',
  'Quang hình học','Giao thoa','Nhiễu xạ','Thuyết tương đối','Photon: tính hạt của sóng ánh sáng',
  'Tính sóng của hạt','Cơ học lượng tử I: Hàm sóng','Cơ học lượng tử II: Cấu trúc nguyên tử',
  'Phân tử và vật chất ngưng tụ','Vật lý hạt nhân','Vật lý hạt và vũ trụ học'
]
const manifestFile=path.join(root,'raw_materials/physics/translation-manifest.json')
const exists=async p=>{try{await access(p);return true}catch{return false}}
let manifest
if(await exists(manifestFile)) manifest=JSON.parse(await readFile(manifestFile,'utf8'))
else {
  const audit=JSON.parse(await readFile('qa/physics/full-source/manifest.json','utf8'))
  manifest={source:'Young & Freedman, University Physics with Modern Physics, 15th edition',
    sourceSha256:audit.sourceSha256,language:'vi',policy:'full-source-translation',
    onlyPermittedAddition:'experimental-simulation',chapters:audit.chapters.map(ch=>({...ch,
      status:'pending',fragments:[],pendingSourceUnits:['chapter-opening',...ch.sections.map(s=>s.id),
        'all-original-figures-and-captions','chapter-summary','guided-practice',
        'discussion-questions','all-end-of-chapter-exercises-and-problems']}))}
}
const chapter1=manifest.chapters.find(c=>c.chapter===1)
const translated=[
  ['chapter-opening','00-mo-dau.md',[1,1]],
  ['1.1','01-ban-chat-vat-ly.md',[1,2]],
  ['1.2','02-giai-bai-toan.md',[2,3]],
  ['1.3','03-chuan-va-don-vi.md',[3,6]],
  ['1.4','04-su-dung-doi-don-vi.md',[6,7]],
  ['1.5','05-do-bat-dinh-chu-so.md',[8,9]],
  ['1.6','06-uoc-luong.md',[10,10]],
  ['1.7','07-vector-cong-vector.md',[10,14]],
  ['1.8','08-thanh-phan-vector.md',[14,18]],
  ['1.9','09-vector-don-vi.md',[18,19]],
  ['1.10','10-tich-vector.md',[19,24]],
  ['chapter-summary','11-tom-tat.md',[25,25]],
  ['guided-practice','12-luyen-tap-huong-dan.md',[26,26]],
  ['discussion-questions','13-cau-hoi-thao-luan.md',[27,27]],
  ['exercises-1.1-1.48','14-bai-tap-01-48.md',[27,29]],
  ['problems-1.49-1.89','15-bai-tap-49-89.md',[29,32]],
  ['challenge-and-mcat-1.90-1.94','16-bai-nang-cao-mcat.md',[32,33]],
  ['chapter-answers','17-dap-an-cua-sach.md',[33,33]],
]
chapter1.fragments=[]
for(const [unit,file,pages] of translated) {
  const relative=`raw_materials/physics/translations/chapter-01/${file}`
  if(!await exists(relative))continue
  chapter1.fragments.push({sourceUnit:unit,file:relative,printedPages:pages,status:'translated',
    semanticReview:'self-reviewed-against-source',independentReview:'not-performed'})
}
chapter1.status='in-progress'
chapter1.pendingSourceUnits=chapter1.pendingSourceUnits.filter(unit=>!chapter1.fragments.some(f=>f.sourceUnit===unit))
if(chapter1.fragments.some(f=>f.sourceUnit==='exercises-1.1-1.48') &&
   chapter1.fragments.some(f=>f.sourceUnit==='problems-1.49-1.89') &&
   chapter1.fragments.some(f=>f.sourceUnit==='challenge-and-mcat-1.90-1.94')) {
  chapter1.pendingSourceUnits=chapter1.pendingSourceUnits.filter(unit=>unit!=='all-end-of-chapter-exercises-and-problems')
  chapter1.pendingSourceUnits.push('appendix-odd-answers-source-errors')
  chapter1.pendingSourceUnits=[...new Set(chapter1.pendingSourceUnits)]
}
const chapter2=manifest.chapters.find(c=>c.chapter===2)
chapter2.fragments=[]
for(const [unit,file,pages] of [
  ['chapter-opening','00-mo-dau.md',[34,34]],
  ['2.1','01-do-doi-van-toc-trung-binh.md',[34,37]],
  ['2.2','02-van-toc-tuc-thoi.md',[37,40]],
  ['2.3','03-gia-toc.md',[40,44]],
  ['2.4','04-gia-toc-khong-doi.md',[44,49]],
  ['2.5','05-roi-tu-do.md',[50,53]],
  ['2.6','06-tich-phan-van-toc-vi-tri.md',[53,55]],
  ['chapter-summary','07-tom-tat.md',[56,56]],
  ['guided-practice','08-luyen-tap-huong-dan.md',[57,58]],
  ['discussion-questions','09-cau-hoi-thao-luan.md',[58,59]],
  ['exercises-2.1-2.26','10-bai-tap-01-26.md',[59,60]],
  ['exercises-2.27-2.52','11-bai-tap-27-52.md',[60,62]],
  ['problems-2.53-2.77','12-bai-tong-hop-53-77.md',[62,63]],
  ['problems-challenge-mcat-2.78-2.92','13-bai-tong-hop-nang-cao-mcat.md',[64,65]],
  ['chapter-answers','14-dap-an-cua-sach.md',[65,65]],
  ['appendix-odd-answers','15-dap-so-bai-le.md',['A-9','A-9']],
]) {
  const relative=`raw_materials/physics/translations/chapter-02/${file}`
  if(!await exists(relative))continue
  chapter2.fragments.push({sourceUnit:unit,file:relative,printedPages:pages,status:'translated',
    semanticReview:'self-reviewed-against-source',independentReview:'not-performed'})
}
chapter2.status=chapter2.fragments.length?'in-progress':'pending'
chapter2.pendingSourceUnits=chapter2.pendingSourceUnits.filter(unit=>!chapter2.fragments.some(f=>f.sourceUnit===unit))
const chapter2ReviewFile='raw_materials/physics/chapter-02-completion-review.json'
if(chapter2.fragments.length===16 && await exists(chapter2ReviewFile)) {
  const review=JSON.parse(await readFile(chapter2ReviewFile,'utf8'))
  if(review.status==='complete' && review.figuresAndCaptionsReviewed && review.exercises===92 && review.discussionQuestions===22) {
    chapter2.pendingSourceUnits=[]
    chapter2.status='complete'
    chapter2.theoryStatus='translated-2.1-through-2.6'
    chapter2.mainChapterTextStatus='translated-including-all-92-problems'
    chapter2.appendixAnswersStatus='translated-with-explicit-source-error-notes'
    chapter2.completionReview=chapter2ReviewFile
  }
}
// Keep reviews and source errors explicit instead of silently certifying completeness.
await writeFile(manifestFile,JSON.stringify(manifest,null,2)+'\n')
const backup=path.join(root,'qa/physics/previous-summaries')
await mkdir(backup,{recursive:true})
for(const course of [physics1Course,physics2Course]) {
  const moduleBackup=path.join(backup,'physics-courses.mjs')
  if(!await exists(moduleBackup))await writeFile(moduleBackup,await readFile('docs/.vitepress/physics-courses.mjs'))
  course.contentPolicy='full-source-translation'
  course.description=course.id==='vat-ly-1'
    ?'Bản dịch tiếng Việt theo chương 1–20 của Young & Freedman, từ cơ học đến hết nhiệt học. Đang dịch và đối chiếu từng mục, hình, ví dụ và bài tập nguyên tác.'
    :'Bản dịch tiếng Việt theo chương 21–44 của Young & Freedman, từ điện học đến hết vật lý hiện đại. Đang dịch và đối chiếu từng mục, hình, ví dụ và bài tập nguyên tác.'
  course.slides=course.id==='vat-ly-1' && chapter2.status==='complete' ? physicsMotionSlides : []
  for(const lesson of course.lessons) {
    const ch=manifest.chapters.find(ch=>ch.chapter===lesson.sourceChapter)
    lesson.title=chapterTitles[ch.chapter-1]
    lesson.status=ch.status==='complete'?'ready':'draft'
    if(ch.chapter===2) {
      lesson.prerequisites=['do-doi','thanh-phan-vector']
      lesson.supportingConcepts=['van-toc-vat-ly','toc-do-chuyen-dong','gia-toc','roi-tu-do','dao-ham','tich-phan']
    }
    const file=path.join('docs',course.id,'bai-giang',`${lesson.slug}.md`)
    const oldBackup=path.join(backup,`${course.id}-${lesson.slug}.md`)
    if(!await exists(oldBackup))await writeFile(oldBackup,await readFile(file))
    const unitLabels={'chapter-opening':'lời mở chương','chapter-summary':'tóm tắt của sách','guided-practice':'luyện tập có hướng dẫn và bài tổng hợp','discussion-questions':'câu hỏi thảo luận','chapter-answers':'đáp án cuối chương'}
    const notice=ch.status==='complete'
      ?'Đã dịch toàn bộ chương, gồm lời mở, mục 2.1–2.6, tóm tắt, luyện tập có hướng dẫn, bài tổng hợp, câu hỏi thảo luận, 92 bài tập và đáp án có trong sách. Đáp số bài lẻ trong phụ lục được đặt ở cuối trang; những lỗi nhận diện trong nguyên tác có ghi chú đối chiếu riêng. Hình gốc được giữ cùng bản dịch chú giải và nhãn ngay bên dưới.'
      :ch.fragments.length
      ?`Đã có bản dịch các phần: ${ch.fragments.map(f=>unitLabels[f.sourceUnit] || `mục ${f.sourceUnit}`).join(', ')}. Chương chưa hoàn tất; các phần còn thiếu được ghi ở cuối trang.`
      :'Chương này đang được dịch đầy đủ từ nguyên tác. Bản tóm lược cũ và các bài tập tự đặt đã được rút khỏi trang để không bị nhầm với nội dung sách.'
    const front=`---\ncourse: ${course.id}\nlecture: ${lesson.slug}\nsection: lecture\ntitle: ${JSON.stringify(lesson.title)}\nprerequisites: ${JSON.stringify(lesson.prerequisites)}\nlessonStatus: ${lesson.status}\nsourceTranslation: full\ndescription: ${JSON.stringify(ch.status==='complete'?`Bản dịch đầy đủ chương ${ch.chapter} của Young & Freedman, gồm lý thuyết, ví dụ và toàn bộ bài tập nguyên tác.`:`Bản dịch chương ${ch.chapter} của Young & Freedman; đang đối chiếu, chưa hoàn tất.`)}\n---\n\n`
    let body=`::: info Tiến độ bản dịch\n${notice}\n:::\n\n`
    for(const fragment of ch.fragments)body+=`<!--@include: ../../../${fragment.file}-->\n\n`
    if(ch.pendingSourceUnits.length) body+='## Phần nguyên tác đang tiếp tục dịch\n\n'
    for(const unit of ch.pendingSourceUnits) {
      const names={'chapter-opening':'Lời mở chương và mục tiêu học.','all-original-figures-and-captions':'Đối chiếu hoàn tất toàn bộ hình, chữ trong hình và chú thích của chương.','chapter-summary':'Tóm tắt chương của sách.','guided-practice':'Phần luyện tập có hướng dẫn (Guided Practice).','discussion-questions':'Toàn bộ câu hỏi thảo luận (Discussion Questions).','all-end-of-chapter-exercises-and-problems':'Toàn bộ bài tập cuối chương, bài tổng hợp, bài nâng cao và các phần bài tập khác có trong nguyên tác.','appendix-odd-answers-source-errors':'Đáp số bài lẻ trong phụ lục: đang đối chiếu những dòng nguyên tác có đơn vị hoặc hướng không khớp đề.'}
      const section=ch.sections.find(s=>s.id===unit)
      body+=`- ${names[unit] || `${unit} — ${section?.title || unit} (từ trang ${section?.page ?? ch.printedStart}).`}\n`
    }
    body+=`\n## Nguồn của bản dịch\n\nHugh D. Young và Roger A. Freedman, *University Physics with Modern Physics*, ấn bản 15, chương ${ch.chapter}, trang in ${ch.printedStart}–${ch.printedEnd}, tương ứng trang PDF ${ch.pdfStart}–${ch.pdfEnd} của bản được cung cấp. Phạm vi này bao gồm cả phần bài tập cuối chương.${ch.chapter===2?' Đáp số bài lẻ: phụ lục trang A-9, trang PDF 1554.':''}\n\nBản dịch giữ số mục, số hiệu công thức, ví dụ, bảng và hình để đối chiếu với sách. Các phần chưa dịch không được xem là đã hoàn tất.\n`
    await writeFile(file,front+body)
  }
  const roadmap=path.join('docs',course.id,'notes/lo-trinh.md')
  const oldRoadmap=await readFile(roadmap,'utf8')
  const roadmapBackup=path.join(backup,`${course.id}-lo-trinh.md`)
  if(!await exists(roadmapBackup))await writeFile(roadmapBackup,oldRoadmap)
  await writeFile(roadmap,`---\ncourse: ${course.id}\ntitle: "Lộ trình bản dịch giáo trình"\n---\n\n# Lộ trình bản dịch giáo trình\n\n${course.description}\n\nBài học giữ đầy đủ lời dẫn, nội dung, ứng dụng, công thức, lập luận, hình, ví dụ và bài tập của nguyên tác. Chỉ được thêm mô phỏng thí nghiệm có nhãn riêng. Có thể rút gọn diễn đạt nhưng phải giữ ý nghĩa và câu văn đầy đủ theo quy tắc ngôn ngữ của dự án.\n\nMỗi chương chỉ chuyển sang hoàn tất sau khi được dịch và đối chiếu toàn bộ, kể cả bài tập cuối chương. Các thẻ Slides cũ đã được rút vì chứa nội dung tự đặt và không phản ánh đủ nguyên tác.\n\n| Chương | Bài giảng | Trang in, kể cả bài tập | Trạng thái |\n| --- | --- | --- | --- |\n`+course.lessons.map(l=>{const ch=manifest.chapters.find(ch=>ch.chapter===l.sourceChapter);return `| ${ch.chapter} | [${l.title}](/${course.id}/bai-giang/${l.slug}.md) | ${ch.printedStart}–${ch.printedEnd} | ${ch.status==='complete'?'Đã dịch đầy đủ':ch.fragments.length?'Đang dịch':'Chưa dịch'} |`}).join('\n')+'\n')
  const exercisePath=path.join('docs',course.id,'bai-tap.md')
  const exerciseBackup=path.join(backup,`${course.id}-bai-tap.md`)
  if(!await exists(exerciseBackup))await writeFile(exerciseBackup,await readFile(exercisePath))
  await writeFile(exercisePath,`---\ncourse: ${course.id}\ntitle: "Bài tập trong giáo trình"\n---\n\n# Bài tập trong giáo trình\n\nBài tập được dịch nguyên vẹn trong chương tương ứng, giữ số hiệu và dữ kiện của sách. Các bài tập tự đặt của bản cũ đã được rút. Chỉ hiển thị lời giải hoặc đáp án của nguyên tác khi đã đối chiếu nguồn, không thêm lời giải mới vào phần dịch.\n\n`+course.lessons.map(l=>`- [Chương ${l.sourceChapter}: ${l.title}](/${course.id}/bai-giang/${l.slug}.md).`).join('\n')+'\n')
}
await writeFile('docs/.vitepress/physics-courses.mjs','// Bản dịch nguyên tác đang được đối chiếu. Không đánh dấu ready khi còn đơn vị nguồn chưa dịch.\nexport const physics1Course = '+JSON.stringify(physics1Course,null,2)+'\n\nexport const physics2Course = '+JSON.stringify(physics2Course,null,2)+'\n')
console.log(`Translation integrated: ${manifest.chapters.reduce((n,ch)=>n+ch.fragments.length,0)} authored fragments; ${manifest.chapters.filter(ch=>ch.status==='complete').length} complete chapters.`)
