// Reviewed prose replacements, kept separate from plain-text foundation data.
const expressions = new Map([
  ['f(x+Δx)≈f(x)+∇f(x)·Δx', 'f(x+\\Delta x)\\approx f(x)+\\nabla f(x)\\cdot\\Delta x'],
  ['f: ℝⁿ→ℝ', 'f:\\mathbb{R}^n\\to\\mathbb{R}'],
  ['∇f(x)·u', '\\nabla f(x)\\cdot u'], ['∇f = (2x, 2y)', '\\nabla f=(2x,2y)'],
  ['f(x,y) = x²+y²', 'f(x,y)=x^2+y^2'], ['f(x)=x²', 'f(x)=x^2'],
  ['f(x) = x²', 'f(x)=x^2'], ['f′(x) = 2x', "f'(x)=2x"],
  ['f′(x)', "f'(x)"], ['f(x)=x³', 'f(x)=x^3'],
  ['E = −∇V', '\\mathbf{E}=-\\nabla V'],
  ['x mới=x cũ−η∇f(x cũ)', 'x_{k+1}=x_k-\\eta\\nabla f(x_k)'],
  ['x mới=(1−2η)x cũ', 'x_{k+1}=(1-2\\eta)x_k'],
  ['0<η<1', '0<\\eta<1'], ['η=1', '\\eta=1'], ['η>1', '\\eta>1'],
  ['−∇f', '-\\nabla f'], ['∇f', '\\nabla f'], ['Δx', '\\Delta x']
])
export function formatWikiMath(source) {
  // Existing math is opaque so edits never double-wrap or alter TeX.
  return source.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g).map((part, index) => {
    if (index % 2) return part
    // Work on individual non-math segments after every replacement.
    for (const [plain, tex] of expressions) part = part.split(/(\$[^$\n]+?\$)/g).map((segment, i) => i % 2 ? segment : segment.replaceAll(plain, `$${tex}$`)).join('')
    return part
  }).join('')
}
