import {writeFile} from 'node:fs/promises'
import {informedSearch} from '../../src/features/labs/services/informed-search.mjs'
await writeFile(new URL('../../src/features/labs/services/informed-search-code.mjs',import.meta.url),'// Generated from the executable generator. Run node scripts/content/sync-informed-code.mjs.\nexport const informedCode = '+JSON.stringify(informedSearch.toString().split('\n'),null,2)+'\n')
console.log('Updated readable informed-search source.')
