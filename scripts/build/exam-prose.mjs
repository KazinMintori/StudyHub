// Apply the site's colon rule to prose tokens, never to code, URLs or TeX.
const identifiers = new Set(`np pd df s a b c x y z p q r m t u v gia phi loai
shape dtype dtypes ndim size itemsize nbytes strides offset ndarray nan NaN NaT
None True False int float str list dict set tuple range zip map filter sorted
sum len min max any all print repr type isinstance get items freeze pip venv
apply transform agg aggregate groupby sort reindex align copy assign to_numeric
explode dropna fillna isna notna replace strip contains fullmatch match search
findall extract extractall split join startswith endswith casefold upper lower
pandas numpy rolling resample asfreq shift pct_change tz_localize tz_convert
localize convert read_csv usecols validate observed query concat merge cut qcut
from import if else return`.split(/\s+/))

export function examProsePlugin(md) {
  md.core.ruler.after('inline', 'exam_prose_colons', state => {
    for (const block of state.tokens) {
      if (block.type !== 'inline' || !block.children) continue
      let afterColon = false
      const children = []
      for (const token of block.children) {
        if (token.type !== 'text') {
          children.push(token)
          if (['code_inline', 'math_inline', 'image', 'html_inline'].includes(token.type)) afterColon = false
          continue
        }
        let content = ''
        const flush = () => {
          if (!content) return
          const text = new state.Token('text', '', 0)
          text.content = content
          children.push(text)
          content = ''
        }
        for (let index = 0; index < token.content.length; index++) {
          const char = token.content[index]
          if (afterColon && !/\s/.test(char)) {
            if (char === '"' || char === "'") {
              const end = token.content.indexOf(char, index + 1)
              if (end > index) {
                flush()
                const code = new state.Token('code_inline', 'code', 0)
                code.content = token.content.slice(index, end + 1)
                children.push(code)
                index = end
                afterColon = false
                continue
              }
            }
            if (/[“‘(]/.test(char)) { content += char; continue }
            // ASCII identifiers must end at a full Unicode word boundary.
            // Otherwise “máy” can be misread as the identifier “m” + “áy”.
            const name = token.content.slice(index).match(/^[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*(?:\([^\n)]*\))?(?![\p{L}\p{M}\p{N}_])/u)
            if (name && (identifiers.has(name[0].split(/[.(]/)[0]) || /^\w+_\w/.test(name[0]))) {
              flush()
              const code = new state.Token('code_inline', 'code', 0)
              code.content = name[0]
              children.push(code)
              index += name[0].length - 1
            } else content += char.toLocaleUpperCase('vi-VN')
            afterColon = false
          } else content += char
          if (char === ':' && (index + 1 === token.content.length || /\s/.test(token.content[index + 1]))) afterColon = true
        }
        flush()
      }
      block.children = children
    }
  })
}
