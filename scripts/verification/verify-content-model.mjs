import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import MarkdownIt from 'markdown-it'
import { courseCatalog } from '../../docs/.vitepress/course-catalog.mjs'
import { concepts } from '../../docs/.vitepress/concepts.mjs'
import { relatedConcepts,wikiDetails,wikiGroups } from '../../docs/.vitepress/wiki-content.mjs'
import { resolveConceptForCourse } from '../../docs/.vitepress/wiki-content.mjs'
import { lectureSlides,lectureConceptIds } from '../../docs/.vitepress/lecture-model.mjs'
import { lectureParts } from '../../docs/.vitepress/lecture-model.mjs'
import { termLinks } from '../../docs/.vitepress/term-links.mjs'
import { searchTrace,gradientTrace,bayesCounts,wordCountTrace } from '../../src/features/illustrations/services/illustrations.js'

const ids=Object.keys(concepts)
assert.equal(new Set(wikiGroups.flatMap(g=>g.ids)).size,ids.length)
for(const id of ids){assert(wikiDetails[id]);assert(relatedConcepts(id).length);for(const other of relatedConcepts(id))assert(concepts[other]&&other!==id);assert((await readFile(`docs/wiki/${id}.md`,'utf8')).includes('## Giải thích kỹ thuật'))}
for(const c of courseCatalog)for(const l of c.lessons){const source=await readFile(`docs/${c.id}/bai-giang/${l.slug}.md`,'utf8');assert(new RegExp(`lecture:\\s*["']?${l.slug}["']?`).test(source),`Missing lecture: ${l.slug} in docs/${c.id}/bai-giang/${l.slug}.md`);assert(/section:\s*["']?lecture["']?/.test(source),`Missing section: lecture in docs/${c.id}/bai-giang/${l.slug}.md`);if(l.status==='ready' && c.slides.length)assert(lectureSlides(c,l).length)}
const md=new MarkdownIt().use(termLinks,'/Study_UET/')
const rendered=md.render('Gradient và đạo hàm riêng. `gradient` [vector](https://example.com)',{relativePath:'toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.md'})
assert(rendered.includes('data-wiki="/wiki/gradient.html"'));assert(rendered.includes('aria-haspopup="dialog"'));assert(rendered.includes('<code>gradient</code>'))
const wiki=md.render('Gradient dùng vector và đạo hàm riêng.',{relativePath:'wiki/gradient.md'})
assert(!wiki.includes('data-wiki="/wiki/gradient.html"'));assert(wiki.includes('data-wiki="/wiki/vector.html"'))
const mathParameter=md.render('tham số',{relativePath:'toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu.md'})
const codeParameter=md.render('tham số',{relativePath:'xu-ly-du-lieu/bai-giang/bai-02-python-co-ban.md'})
assert(mathParameter.includes('data-term="tham-so-toan-hoc"'));assert(!mathParameter.includes('data-term="tham-so-lap-trinh"'))
assert(!codeParameter.includes('data-term="tham-so-toan-hoc"'))
assert.equal(resolveConceptForCourse(['tham-so-toan-hoc','tham-so-lap-trinh'],'xu-ly-du-lieu'),'tham-so-lap-trinh')
const mathParameterWiki=md.render('Tham số của mô hình.',{relativePath:'wiki/tham-so-toan-hoc.md'})
assert(!mathParameterWiki.includes('data-term="tham-so-lap-trinh"'))
assert((await readFile('docs/wiki/gradient.md','utf8')).includes(String.fromCharCode(92)+'nabla'))
assert.deepEqual(searchTrace({A:['B','C'],B:['D'],C:[],D:[]},'dfs').at(-1).visited,['A','B','D','C'])
assert.equal(gradientTrace(2,.5,1)[1],0);assert(Math.abs(bayesCounts(.2,.8,.3).posterior-.4)<1e-10);assert.deepEqual(wordCountTrace('UET học uet').counts,[['uet',2],['học',1]])

console.log('PASS course/Wiki metadata, scoped term linking and illustration models.')
