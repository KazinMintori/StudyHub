import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {
  configureStudyMarkdown,
  injectHtmlImgAttributes,
  hasExactAttribute
} from '../build/markdown-presentation.mjs'
import {
  generateFontPreloads,
  resolveFontPreloadAssets,
  PRELOAD_FONT_PATTERNS
} from '../build/font-preloads.mjs'

function createStudyMarkdown(base = '/') {
  const md = new MarkdownIt({ html: true }).use(mathjax)
  configureStudyMarkdown(md, { base })
  return md
}

// ---------------------------------------------------------------------------
// Image Loading & Decoding Tests
// ---------------------------------------------------------------------------

test('single standalone image becomes figure with eager loading and async decoding', () => {
  const md = createStudyMarkdown()
  const html = md.render('![Hình 1.1: Thí nghiệm Young](young-1/young-exp.png)')

  assert(html.includes('<figure class="lecture-figure">'), 'Should wrap standalone image in lecture-figure')
  assert(html.includes('<figcaption>Hình 1.1: Thí nghiệm Young</figcaption>'), 'Should render figcaption')
  assert(html.includes('loading="eager"'), 'First image must have loading="eager"')
  assert(html.includes('decoding="async"'), 'Image must have decoding="async"')
  assert(html.includes('src="young-1/young-exp.png"'), 'Must keep image src')
  assert(html.includes('alt="Hình 1.1: Thí nghiệm Young"'), 'Must keep image alt')
})

test('multiple images: first is eager and later images are lazy by default', () => {
  const md = createStudyMarkdown()
  const doc = [
    '![Hình 1](img1.png)',
    '',
    'Đoạn văn phân tích ở giữa.',
    '',
    '![Hình 2](img2.png)',
    '',
    '![Hình 3](img3.png)'
  ].join('\n')

  const html = md.render(doc)

  const imgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])
  assert.equal(imgTags.length, 3, 'Should render three image tags')

  // 1st image: eager, async
  assert(imgTags[0].includes('loading="eager"'), 'First image must be loading="eager"')
  assert(imgTags[0].includes('decoding="async"'), 'First image must be decoding="async"')

  // 2nd image: lazy, async
  assert(imgTags[1].includes('loading="lazy"'), 'Second image must be loading="lazy"')
  assert(imgTags[1].includes('decoding="async"'), 'Second image must be decoding="async"')

  // 3rd image: lazy, async
  assert(imgTags[2].includes('loading="lazy"'), 'Third image must be loading="lazy"')
  assert(imgTags[2].includes('decoding="async"'), 'Third image must be decoding="async"')
})

test('avoids eager-loading all figures: inline first image makes subsequent figure lazy', () => {
  const md = createStudyMarkdown()
  const doc = [
    'Quan sát ký hiệu ![icon](badge.png) trước khi vào bài.',
    '',
    '![Hình 1: Đồ thị thế năng](potential.png)'
  ].join('\n')

  const html = md.render(doc)
  const imgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])

  assert.equal(imgTags.length, 2)
  // First image is inline:
  assert(imgTags[0].includes('src="badge.png"'))
  assert(imgTags[0].includes('loading="eager"'), 'First content image (inline) must be eager')

  // Second image is a figure, but NOT the first content image -> MUST be lazy:
  assert(imgTags[1].includes('src="potential.png"'))
  assert(imgTags[1].includes('loading="lazy"'), 'Subsequent figure must NOT be eager; must be lazy')
  assert(imgTags[1].includes('decoding="async"'))
})

test('preserves explicit loading and decoding attributes on images', () => {
  const md = createStudyMarkdown()
  const doc = [
    '<img src="first-lazy.png" alt="First" loading="lazy" />',
    '',
    '<img src="second-eager.png" alt="Second" loading="eager" decoding="sync" />',
    '',
    '![Third](third.png)'
  ].join('\n')

  const html = md.render(doc)
  const imgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])

  assert.equal(imgTags.length, 3)

  // First image explicitly requested loading="lazy"
  assert(imgTags[0].includes('loading="lazy"'), 'Explicit loading="lazy" on first image must be preserved')
  assert(imgTags[0].includes('decoding="async"'), 'Default decoding="async" applied when missing')

  // Second image explicitly requested loading="eager" and decoding="sync"
  assert(imgTags[1].includes('loading="eager"'), 'Explicit loading="eager" on second image must be preserved')
  assert(imgTags[1].includes('decoding="sync"'), 'Explicit decoding="sync" on second image must be preserved')

  // Third image has no explicit attributes: gets lazy and async
  assert(imgTags[2].includes('loading="lazy"'), 'Third image gets loading="lazy"')
  assert(imgTags[2].includes('decoding="async"'), 'Third image gets decoding="async"')
})

test('preserves captions, bilingual labels and math markup intact', () => {
  const md = createStudyMarkdown()
  const doc = [
    'Phương trình sóng: $y(x, t) = A \\cos(kx - \\omega t)$.',
    '',
    '![Hình 35.1: Giao thoa hai khe Young](young-35/35-01.png)',
    '',
    '$$\\Delta r = d \\sin\\theta = m\\lambda$$'
  ].join('\n')

  const html = md.render(doc)

  // Check math markup presence (MathJax SVG/MathML wrapped in static-math container with v-html)
  assert(html.includes('class="static-math"'), 'MathJax static-math container must be present')
  assert(html.includes('v-html="'), 'MathJax rendered output must be preserved in v-html binding')
  assert(html.includes('data-mml-node='), 'MathJax SVG/MathML node must be present inside binding')

  // Check figure, caption and image loading attributes
  assert(html.includes('<figure class="lecture-figure">'))
  assert(html.includes('<figcaption>Hình 35.1: Giao thoa hai khe Young'))
  assert(html.includes('loading="eager"') && html.includes('decoding="async"'))
})

test('resets image count per document render', () => {
  const md = createStudyMarkdown()

  const htmlA = md.render('![Page 1 Img 1](p1-1.png)\n\n![Page 1 Img 2](p1-2.png)')
  const htmlB = md.render('![Page 2 Img 1](p2-1.png)\n\n![Page 2 Img 2](p2-2.png)')

  const imgsA = [...htmlA.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])
  const imgsB = [...htmlB.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])

  assert(imgsA[0].includes('loading="eager"'), 'Doc A first image eager')
  assert(imgsA[1].includes('loading="lazy"'), 'Doc A second image lazy')

  assert(imgsB[0].includes('loading="eager"'), 'Doc B first image must reset and be eager')
  assert(imgsB[1].includes('loading="lazy"'), 'Doc B second image lazy')
})

test('image captions render inline equations through the static math renderer', () => {
  const md = createStudyMarkdown()
  const html = md.render(String.raw`![Hình 1: Hình chiếu $L_z=2\hbar$ và độ lớn $L=\sqrt{6}\hbar$.](img.png)`)
  const caption = html.match(/<figcaption>([\s\S]*?)<\/figcaption>/)?.[1]
  assert(caption)
  assert.equal((caption.match(/class="static-math"/g) || []).length, 2)
  assert(caption.includes('v-html="'))
  assert(caption.includes('data-mml-node='))
  assert(!caption.includes('$L_z'))
  assert(!caption.includes('$L='))
})

test('math captions still escape literal HTML and keep bilingual labels', () => {
  const md = createStudyMarkdown()
  const html = md.render(String.raw`![Hình 1: <script>alert(1)</script> và $x<y$.](young-24/hinh-24-1.png)`)
  const caption = html.match(/<figcaption>([\s\S]*?)<\/figcaption>/)?.[1]
  assert(caption.includes('&lt;script&gt;alert(1)&lt;/script&gt;'))
  assert(!caption.includes('<script>'))
  assert(caption.includes('class="static-math"'))
  assert(caption.includes('figure-label-list'))
})

test('regression (1): preserves > inside quoted attributes and recognizes data-loading is not loading attribute', () => {
  const md = createStudyMarkdown()

  // Supervisor bug 1 case: > inside alt attribute and custom data-loading attribute
  const doc = '<img src="sample.png" data-loading="custom" alt="x > y">'
  const html = md.render(doc)

  // Must not be corrupted into alt="x decoding="async" > y">
  assert(!html.includes('alt="x decoding="async" > y">'), 'Must not truncate or corrupt attribute at > inside quotes')
  assert(html.includes('alt="x > y"'), 'Quoted attribute value with > must be preserved intact')
  assert(html.includes('data-loading="custom"'), 'data-loading attribute must be preserved')
  assert(html.includes('loading="eager"'), 'data-loading is not loading attribute; missing loading must be injected as eager')
  assert(html.includes('decoding="async"'), 'decoding="async" must be injected')
  assert.equal(
    html.trim(),
    '<img src="sample.png" data-loading="custom" alt="x > y" loading="eager" decoding="async">',
    'Resulting tag must have attributes properly appended before closing >'
  )

  // Verify self-closing variant
  const selfClosingDoc = '<img src="sample.png" data-loading="custom" alt="x > y" />'
  const selfClosingHtml = md.render(selfClosingDoc)
  assert.equal(
    selfClosingHtml.trim(),
    '<img src="sample.png" data-loading="custom" alt="x > y" loading="eager" decoding="async" />'
  )

  // Verify data-decoding is not decoding attribute
  const dataDecDoc = '<img src="sample.png" data-decoding="custom" alt="test">'
  const dataDecHtml = md.render(dataDecDoc)
  assert(dataDecHtml.includes('data-decoding="custom"'))
  assert(dataDecHtml.includes('decoding="async"'))

  // Unit-level exact attribute boundary checks
  assert.equal(hasExactAttribute(' src="sample.png" data-loading="custom"', 'loading'), false)
  assert.equal(hasExactAttribute(' src="sample.png" my-loading="custom"', 'loading'), false)
  assert.equal(hasExactAttribute(' src="sample.png" loading-mode="custom"', 'loading'), false)
  assert.equal(hasExactAttribute(' src="sample.png" alt="photo with loading spinner"', 'loading'), false)
  assert.equal(hasExactAttribute(' src="sample.png" loading="lazy"', 'loading'), true)
  assert.equal(hasExactAttribute(' src="sample.png" loading', 'loading'), true)
  assert.equal(hasExactAttribute(' src="sample.png" data-decoding="custom"', 'decoding'), false)
  assert.equal(hasExactAttribute(' src="sample.png" decoding="sync"', 'decoding'), true)
})

test('regression (2): script and style blocks remain byte-for-byte unchanged and do not consume first-image status', () => {
  const md = createStudyMarkdown()

  // Supervisor bug 2 case: script string must remain unchanged and not consume first-image status
  const scriptContent = `<script>const marker = '<img src="not-an-image.png">';</script>`
  const doc = [
    scriptContent,
    '',
    '![First Real Image](real.png)',
    '',
    '![Second Real Image](second.png)'
  ].join('\n')

  const html = md.render(doc)

  // Script block must remain byte-for-byte unchanged
  assert(html.includes(scriptContent), 'Script block must remain byte-for-byte unchanged')
  assert(!html.includes('not-an-image.png" loading='), 'Script string must not receive loading attribute')
  assert(!html.includes('not-an-image.png" decoding='), 'Script string must not receive decoding attribute')

  const imgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0])
  // Total real images should be 2 (real.png and second.png)
  const realImgTags = imgTags.filter(t => !t.includes('not-an-image.png'))
  assert.equal(realImgTags.length, 2, 'Should only render two content images')

  // First real image must be eager (script did NOT consume first-image status)
  assert(realImgTags[0].includes('src="real.png"'))
  assert(realImgTags[0].includes('loading="eager"'), 'First real image must be eager despite preceding script')
  assert(realImgTags[0].includes('decoding="async"'))

  // Second real image must be lazy
  assert(realImgTags[1].includes('src="second.png"'))
  assert(realImgTags[1].includes('loading="lazy"'), 'Second real image must be lazy')

  // Verify style tags also remain byte-for-byte unchanged
  const styleDoc = [
    '<style>/* <img src="not-an-image.png"> */</style>',
    '',
    '![Real After Style](real-style.png)'
  ].join('\n')
  const styleHtml = md.render(styleDoc)
  assert(styleHtml.includes('<style>/* <img src="not-an-image.png"> */</style>'), 'Style block must remain byte-for-byte unchanged')
  assert(styleHtml.includes('src="real-style.png"'))
  assert(styleHtml.includes('loading="eager"'), 'Real image after style must stay eager')
})

test('regression (3): HTML comments remain byte-for-byte unchanged and do not make the real image lazy', () => {
  const md = createStudyMarkdown()

  // Supervisor bug 3 case: comment must remain unchanged and real image must stay eager
  const commentContent = '<!-- <img src="comment.png"> -->'
  const doc = [
    commentContent,
    '',
    '![First Real Image](real.png)',
    '',
    '![Second Real Image](second.png)'
  ].join('\n')

  const html = md.render(doc)

  // Comment must remain byte-for-byte unchanged
  assert(html.includes(commentContent), 'HTML comment must remain byte-for-byte unchanged')
  assert(!html.includes('comment.png" loading='), 'Comment image must not receive loading attribute')
  assert(!html.includes('comment.png" decoding='), 'Comment image must not receive decoding attribute')

  const realImgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0]).filter(t => !t.includes('comment.png'))
  assert.equal(realImgTags.length, 2)

  // First real image must stay eager
  assert(realImgTags[0].includes('src="real.png"'))
  assert(realImgTags[0].includes('loading="eager"'), 'First real image must remain eager; comment must not make it lazy')
  assert(realImgTags[0].includes('decoding="async"'))

  // Second real image must be lazy
  assert(realImgTags[1].includes('src="second.png"'))
  assert(realImgTags[1].includes('loading="lazy"'), 'Second real image must be lazy')
})

test('regression (all 3 combined): mixed document with comments, scripts, custom attributes, and multiple images', () => {
  const md = createStudyMarkdown()

  const doc = [
    '<!-- <img src="comment.png"> -->',
    '',
    `<script>const marker = '<img src="not-an-image.png">';</script>`,
    '',
    '<img src="sample.png" data-loading="custom" alt="x > y">',
    '',
    '![Second Real Image](second.png)'
  ].join('\n')

  const html = md.render(doc)

  // Comment and script remain byte-for-byte unchanged
  assert(html.includes('<!-- <img src="comment.png"> -->'))
  assert(html.includes(`<script>const marker = '<img src="not-an-image.png">';</script>`))

  // Sample image has alt="x > y" preserved, data-loading preserved, and gets eager
  assert(html.includes('<img src="sample.png" data-loading="custom" alt="x > y" loading="eager" decoding="async">'))

  // Second image gets lazy
  assert(html.includes('src="second.png"'))
  assert(html.includes('loading="lazy"'))
})


// ---------------------------------------------------------------------------
// Font Preload Tests
// ---------------------------------------------------------------------------

const MOCK_EMITTED_ASSETS = [
  '/StudyHub/assets/source-serif-4-latin-standard-normal-CHw8sP2.woff2',
  '/StudyHub/assets/source-serif-4-latin-ext-standard-normal-B8q2K1.woff2',
  '/StudyHub/assets/source-serif-4-latin-standard-italic-F93jLa.woff2',
  '/StudyHub/assets/source-serif-4-vietnamese-standard-normal-D4k19A.woff2',
  '/StudyHub/assets/source-serif-4-vietnamese-standard-italic-M21aQ.woff2',
  '/StudyHub/assets/be-vietnam-pro-latin-400-normal-KL92a8.woff2',
  '/StudyHub/assets/be-vietnam-pro-latin-ext-400-normal-PL819.woff2',
  '/StudyHub/assets/be-vietnam-pro-latin-500-normal-O0192a.woff2',
  '/StudyHub/assets/be-vietnam-pro-latin-600-normal-JJ921a.woff2',
  '/StudyHub/assets/be-vietnam-pro-latin-700-normal-AA821b.woff2',
  '/StudyHub/assets/be-vietnam-pro-vietnamese-400-normal-MM981a.woff2',
  '/StudyHub/assets/be-vietnam-pro-vietnamese-700-normal-ZZ012a.woff2',
  '/StudyHub/assets/jetbrains-mono-latin-wght-normal-HH821a.woff2',
  '/StudyHub/assets/app.B91a02.js',
  '/StudyHub/assets/style.CC819.css'
]

test('bounds font preloads to primary normal-weight Latin and Vietnamese subsets', () => {
  const selected = resolveFontPreloadAssets(MOCK_EMITTED_ASSETS, '/StudyHub/')

  assert.equal(selected.length, 4, 'Must select exactly 4 font files')
  assert(selected.includes('/StudyHub/assets/source-serif-4-latin-standard-normal-CHw8sP2.woff2'))
  assert(selected.includes('/StudyHub/assets/source-serif-4-vietnamese-standard-normal-D4k19A.woff2'))
  assert(selected.includes('/StudyHub/assets/be-vietnam-pro-latin-400-normal-KL92a8.woff2'))
  assert(selected.includes('/StudyHub/assets/be-vietnam-pro-vietnamese-400-normal-MM981a.woff2'))

  // Verify non-target fonts are excluded
  assert(!selected.some(f => f.includes('latin-ext')), 'Must exclude latin-ext')
  assert(!selected.some(f => f.includes('italic')), 'Must exclude italics')
  assert(!selected.some(f => f.includes('500') || f.includes('600') || f.includes('700')), 'Must exclude other weights')
  assert(!selected.some(f => f.includes('jetbrains-mono')), 'Must exclude code fonts')
})

test('generateFontPreloads produces valid HeadConfig tuples with correct attributes', () => {
  const context = {
    assets: MOCK_EMITTED_ASSETS,
    siteConfig: { site: { base: '/StudyHub/' } }
  }

  const preloads = generateFontPreloads(context)
  assert.equal(preloads.length, 4)

  for (const tag of preloads) {
    assert.equal(tag[0], 'link')
    assert.equal(tag[1].rel, 'preload')
    assert.equal(tag[1].as, 'font')
    assert.equal(tag[1].type, 'font/woff2')
    assert.equal(tag[1].crossorigin, '')
    assert(tag[1].href.startsWith('/StudyHub/assets/'), `Href must have correct base: ${tag[1].href}`)
  }
})

test('supports development base (/) and production base (/StudyHub/)', () => {
  const devAssets = [
    '/assets/source-serif-4-latin-standard-normal-CHw8sP2.woff2',
    '/assets/source-serif-4-vietnamese-standard-normal-D4k19A.woff2',
    '/assets/be-vietnam-pro-latin-400-normal-KL92a8.woff2',
    '/assets/be-vietnam-pro-vietnamese-400-normal-MM981a.woff2'
  ]

  const devPreloads = generateFontPreloads({
    assets: devAssets,
    siteConfig: { site: { base: '/' } }
  })
  assert.equal(devPreloads.length, 4)
  for (const tag of devPreloads) {
    assert(tag[1].href.startsWith('/assets/'), `Dev href must start with /assets/: ${tag[1].href}`)
  }

  const prodPreloads = generateFontPreloads({
    assets: MOCK_EMITTED_ASSETS,
    siteConfig: { site: { base: '/StudyHub/' } }
  })
  assert.equal(prodPreloads.length, 4)
  for (const tag of prodPreloads) {
    assert(tag[1].href.startsWith('/StudyHub/assets/'), `Prod href must start with /StudyHub/assets/: ${tag[1].href}`)
  }
})

test('never manufactures font URLs when assets are empty or unavailable', () => {
  // Empty assets array
  assert.deepEqual(generateFontPreloads({ assets: [] }), [])

  // Missing assets property (e.g. dev server)
  assert.deepEqual(generateFontPreloads({}), [])
  assert.deepEqual(generateFontPreloads(null), [])
  assert.deepEqual(generateFontPreloads(undefined), [])

  // Only unrelated assets
  assert.deepEqual(generateFontPreloads({ assets: ['/assets/main.js', '/assets/style.css'] }), [])
})

test('deduplicates with existing head tags', () => {
  const existingHref = '/StudyHub/assets/source-serif-4-latin-standard-normal-CHw8sP2.woff2'
  const context = {
    assets: MOCK_EMITTED_ASSETS,
    siteConfig: { site: { base: '/StudyHub/' } },
    head: [
      ['link', { rel: 'preload', href: existingHref, as: 'font', type: 'font/woff2', crossorigin: '' }]
    ]
  }

  const preloads = generateFontPreloads(context)
  // Should have 3 new preloads instead of 4 (omits the already-existing one)
  assert.equal(preloads.length, 3)
  assert(!preloads.some(p => p[1].href === existingHref))
})
