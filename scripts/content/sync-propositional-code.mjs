import {writeFile} from 'node:fs/promises'
import {forwardChaining,sldResolution,resolutionRefutation} from '../../src/features/labs/services/propositional-inference.mjs'
const source='// Generated from executable generators. Run node scripts/content/sync-propositional-code.mjs.\n'+[["forwardCode",forwardChaining],["sldCode",sldResolution],["resolutionCode",resolutionRefutation]].map(([n,f])=>'export const '+n+'='+JSON.stringify(f.toString().split('\n'),null,2)).join('\n')+'\n'
await writeFile(new URL('../../src/features/labs/services/propositional-code.mjs',import.meta.url),source)
console.log('Updated stable propositional inference source.')
