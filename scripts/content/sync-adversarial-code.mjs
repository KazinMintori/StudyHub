import {readFile,writeFile} from 'node:fs/promises'
import {adversarialSearch} from '../../src/features/labs/services/adversarial-search.mjs'
await writeFile(new URL('../../src/features/labs/services/adversarial-code.mjs',import.meta.url),'// Generated from executable search. Run node scripts/content/sync-adversarial-code.mjs.\nexport const adversarialCode='+JSON.stringify(adversarialSearch.toString().split('\n'),null,2)+'\n')
const ticTacToeSource=await readFile(new URL('../../src/features/labs/services/tic-tac-toe.mjs',import.meta.url),'utf8')
await writeFile(new URL('../../src/features/labs/services/tic-tac-toe-code.mjs',import.meta.url),'// Generated from the exact executable module. Run node scripts/content/sync-adversarial-code.mjs.\nexport const ticTacToeCode='+JSON.stringify(ticTacToeSource.split('\n'),null,2)+'\n')
console.log('Updated stable adversarial search code.')
