import { findCourse } from './course-catalog.mjs'
import { findLecture, lectureSlides } from './lecture-model.mjs'
import { concepts } from './concepts.mjs'

export function renderStudySearch(source,env,md) {
  const html=md.render(source,env)
  if(env.frontmatter?.search===false)return ''
  const course=findCourse(env.frontmatter?.course), lesson=findLecture(env.frontmatter?.course,env.frontmatter?.lecture)
  if(!course||!lesson)return html
  const escape=value=>md.utils.escapeHtml(value)
  const heading=(title,id)=>`<h2 id="${id}">${escape(title)} <a class="header-anchor" href="#${id}">Permalink</a></h2>`
  const title=`<h1>${escape(lesson.title)} <a class="header-anchor" href="#notes">Permalink</a></h1>`
  const slides=lectureSlides(course,lesson)
  return title+html+heading('Slides · '+lesson.title,'slides')+`<p>${escape(slides.map(s=>`${s.title} ${s.bullets.join(' ')} ${s.formula||''}`).join(' '))}</p>`+heading('Kiến thức nền · '+lesson.title,'kien-thuc-can-co')+`<p>${escape(lesson.prerequisites.map(id=>`${concepts[id].name}: ${concepts[id].definition}`).join(' '))}</p>`
}
