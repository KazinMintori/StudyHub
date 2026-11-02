import { writeFile } from 'node:fs/promises'
import { graphSearch, iterativeSearch } from '../../src/features/labs/services/uninformed-search.mjs'
const source = '// Generated from the executable search generators. Run node scripts/content/sync-uninformed-code.mjs after editing them.\n'
  + 'export const searchCode = ' + JSON.stringify(graphSearch.toString().split('\n'), null, 2) + '\n\n'
  + 'export const idsCode = ' + JSON.stringify(iterativeSearch.toString().split('\n'), null, 2) + '\n'
await writeFile(new URL('../../src/features/labs/services/uninformed-search-code.mjs', import.meta.url), source)
console.log('Updated stable, readable code for the production search viewer.')
