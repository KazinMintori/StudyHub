// A separate output and SSR directory lets this QA build coexist with another
// StudyHub task building the same checkout. It never changes the release config.
import {build} from 'vitepress'
import {resolve} from 'node:path'
import {access} from 'node:fs/promises'
const root=resolve('qa/physics/preview')
await build('docs',{
 onAfterConfigResolve(config){
  config.outDir=resolve(root,'dist')
  config.tempDir=resolve(root,'ssr')
  config.cacheDir=resolve(root,'cache')
 }
})
for(const file of ['index.html','vat-ly-2/bai-giang/01-dien-truong-coulomb.html','vat-ly-2/bai-giang/03-dinh-luat-gauss.html','vat-ly-2/bai-giang/02-dien-the.html']){
 await access(resolve(root,'dist',file))
}
console.log('Physics preview build and required HTML outputs verified.')
