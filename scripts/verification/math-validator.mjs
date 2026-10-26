import { mathjax } from 'mathjax-full/js/mathjax.js'
import { TeX } from 'mathjax-full/js/input/tex.js'
import { SVG } from 'mathjax-full/js/output/svg.js'
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js'
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js'
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js'
import { AssistiveMmlHandler } from 'mathjax-full/js/a11y/assistive-mml.js'
import { mathRenderError, physicsEquationTag } from '../math-integrity.mjs'

// Use the site's TeX/SVG options without the per-expression HTML/CSS inliner.
// The full renderer is covered separately; this check discards each SVG after
// validating it so a site-wide source audit does not retain an HTML bundle.
export function createMathValidator(options = {}) {
  const adaptor = liteAdaptor()
  AssistiveMmlHandler(RegisterHTMLHandler(adaptor))
  const document = mathjax.document('', {
    InputJax: new TeX({ packages: AllPackages, ...options.tex }),
    OutputJax: new SVG({ fontCache: 'none', ...options.svg })
  })
  return (source, display = false, relativePath = '') => {
    // The Notes renderer extracts this tag into a separate responsive label.
    const numbered = display && physicsEquationTag(source, relativePath)
    if (numbered) source = source.replace(numbered[0], '')
    const html = adaptor.outerHTML(document.convert(source, { display }))
    if (mathRenderError.test(html)) throw new Error(`Invalid TeX: ${source.slice(0, 240)}`)
  }
}
