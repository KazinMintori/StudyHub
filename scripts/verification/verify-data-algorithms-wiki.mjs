import { createMathValidator } from './math-validator.mjs'
import { dataAlgorithmsConcepts, dataAlgorithmsWikiDetails } from '../../docs/.vitepress/data-algorithms-foundations.mjs'
const validate = createMathValidator()
let count = 0
for (const source of [...Object.values(dataAlgorithmsWikiDetails), ...Object.values(dataAlgorithmsConcepts).flatMap(Object.values)].filter(x => typeof x === 'string')) {
  for (const match of source.matchAll(/\$([^$]+)\$/g)) { validate(match[1]); count++ }
}
console.log(`Validated ${count} equations in the data-algorithm Wiki definitions and articles`)
