import {slides as a} from '../../src/content/courses/bieu-dien-tri-thuc/lectures/05-tim-kiem-cuc-bo/slides.mjs'
import {slides as b} from '../../src/content/courses/bieu-dien-tri-thuc/lectures/05-csp/slides.mjs'
import {localCspConcepts,localCspWikiDetails} from '../../docs/.vitepress/local-csp-foundations.mjs'
import {mathSegments} from '../../docs/.vitepress/math-text.mjs'
import {createMathValidator} from '../verification/math-validator.mjs'
const validate=createMathValidator();let count=0
for(const text of [...a,...b,...Object.values(localCspConcepts),localCspWikiDetails].flatMap(x=>Object.values(x).flat()).filter(x=>typeof x==='string'))for(const segment of mathSegments(text)){if(!segment.startsWith('$'))continue;const display=segment.startsWith('$$'),n=display?2:1;validate(segment.slice(n,-n),display,'local-csp support');count++}
console.log('PASS '+count+' formulas in accepted review cards and Wiki data')
