import {slides} from '../../src/content/courses/bieu-dien-tri-thuc/lectures/08-logic-vi-tu/slides.mjs'
import {predicateConcepts,predicateWikiDetails} from '../../docs/.vitepress/predicate-foundations.mjs'
import {mathSegments} from '../../docs/.vitepress/math-text.mjs'
import {createMathValidator} from '../verification/math-validator.mjs'
const validate=createMathValidator();let count=0
for(const text of [...slides,...Object.values(predicateConcepts),predicateWikiDetails].flatMap(x=>Object.values(x).flat()).filter(x=>typeof x==='string'))for(const s of mathSegments(text)){if(!s.startsWith('$'))continue;const display=s.startsWith('$$'),n=display?2:1;validate(s.slice(n,-n),display,'predicate support');count++}
console.log(`PASS ${count} formulas in review cards and Wiki data`)
