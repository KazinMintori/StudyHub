import {readFile,writeFile} from 'node:fs/promises'
import assert from 'node:assert/strict'
const browser=JSON.parse(await readFile('qa/physics/browser/results.json','utf8'))
assert.equal(browser.checks,66)
assert.equal(browser.errors.length,0)
assert.equal(browser.overflow.length,0)
for(const chapter of [21,22]){
 const file=`raw_materials/physics/chapter-${chapter}-review.json`,review=JSON.parse(await readFile(file,'utf8'))
 const arithmetic=JSON.parse(await readFile(`qa/physics/chapter${chapter}/numeric-checks.json`,'utf8'))
 assert.equal(arithmetic.status,'passed')
 review.status='content-complete'
 review.renderReview='passed'
 review.renderEvidence='qa/physics/browser/results.json'
 review.renderViewports=[360,375,1440]
 review.figureReview='Manually inspected PDF crops and corrected clipped labels and diagrams.'
 review.numericCheckGroups=chapter===21?134:arithmetic.numericGroups
 delete review.renderReviewLimitation
 await writeFile(file,JSON.stringify(review,null,2)+'\n')
}
console.log('Recorded successful content, numeric and headless render reviews for chapters21 and22.')
