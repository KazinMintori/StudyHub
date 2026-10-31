import { buildThemeConfig } from '../../src/features/course/services/build-navigation.mjs'
import { configureStudyMarkdown } from '../../scripts/build/markdown-presentation.mjs'
import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { courseCatalog } from './course-catalog.mjs'
import { wikiGroups } from './wiki-content.mjs'
import { concepts } from './concepts.mjs'
import { readFileSync, mkdirSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { mathTextPlugin } from '../../scripts/math-text-plugin.mjs'
import { generateFontPreloads } from '../../scripts/build/font-preloads.mjs'
import { liteCatalogPlugin } from '../../scripts/build/lite-catalog-plugin.mjs'
import { dropUnusedPreloads } from '../../scripts/build/page-preloads.mjs'
import { physicsExercisesDevPlugin } from '../../scripts/build/physics-exercises-dev.mjs'
import { applyCourseTimestamp } from '../../scripts/build/course-timestamps.mjs'
import { sharedFrameworkPlugin } from '../../scripts/build/shared-framework-plugin.mjs'
import { vietnameseMathOptions } from '../../scripts/math-fonts/vietnamese.mjs'

const tokenSource = readFileSync(new URL('./theme/tokens.css', import.meta.url), 'utf8')
const colorToken = name => tokenSource.match(new RegExp(`--${name}:\\s*([^;]+)`))[1].trim()

const base=process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? `/${process.env.GITHUB_REPOSITORY?.split('/')[1] || 'StudyHub'}/` : '/')
export default withMermaid(defineConfig({
  srcExclude: ['agy-plans/**'],
  buildConcurrency: 1,
  base, title:'UETệ', description:'Bài giảng UET và Wiki thuật ngữ', lang:'vi-VN',
  ignoreDeadLinks: true, lastUpdated: true,
  scrollOffset: { selector: '.reading-scroll-offset', padding: 0 },
  head:[
    ['link',{rel:'icon',href:`${base}favicon.svg`}],
    ['link',{rel:'icon',type:'image/png',href:`${base}favicon.png`}],
    ['meta',{name:'theme-color',content:colorToken('paper')}]
  ],
  // Keep SPA navigation, but avoid fetching every linked lecture in advance.
  router:{ prefetchLinks:false },
  transformHead(context) {
    return generateFontPreloads(context)
  },
  transformHtml(html) {
    return dropUnusedPreloads(html)
  },
  transformPageData: applyCourseTimestamp,
  markdown:{
    // A local font cache lets each formula reuse its repeated glyph paths
    // through <use>, which shrinks long lecture pages considerably.
    math:{ svg:{ ...vietnameseMathOptions.svg, fontCache:'local' } },
    lineNumbers:false,
    config:md => configureStudyMarkdown(md, { base })
  },
  mermaid:{theme:'base',themeVariables:{fontSize:'15px',fontFamily:'Be Vietnam Pro, sans-serif',primaryColor:colorToken('tim-soft'),primaryBorderColor:colorToken('tim'),primaryTextColor:colorToken('ink')},flowchart:{htmlLabels:true,padding:18,curve:'basis'}},
  appearance:true,
  vite:{
    server:{watch:{ignored:['**/.vitepress/dist/**','**/.vitepress/.temp/**']}},
    build:{
      chunkSizeWarningLimit: 2000,
      rollupOptions:{
        cache: false,
        maxParallelFileOps: 2
      }
    },
    plugins:[physicsExercisesDevPlugin({base,root:fileURLToPath(new URL('../../',import.meta.url))}),liteCatalogPlugin(),mathTextPlugin(),sharedFrameworkPlugin(),{name:'ensure-dist-chunks-dir',apply:'build',generateBundle(outputOptions){if(outputOptions.dir){mkdirSync(resolve(outputOptions.dir,'assets/chunks'),{recursive:true})}}}],
    resolve:{alias:{'vitepress-plugin-mermaid/Mermaid.vue':fileURLToPath(new URL('../../src/core/diagrams/components/StudyMermaid.vue',import.meta.url))}},
    optimizeDeps:{include:['mermaid','fastdom','fastdom/extensions/fastdom-promised.js']}
  },
  themeConfig:buildThemeConfig({ courseCatalog, wikiGroups, concepts })
}))
