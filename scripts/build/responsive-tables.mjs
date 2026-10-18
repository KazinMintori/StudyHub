// Keep semantic table headers available when a lab row becomes a mobile card.
export function responsiveTablesPlugin(md) {
  // VitePress's default table renderer emits a fixed tag and discards token attrs.
  md.renderer.rules.table_open = (tokens, index, options, env, renderer) => {
    if (tokens[index].attrIndex('tabindex') < 0) tokens[index].attrSet('tabindex', '0')
    return renderer.renderToken(tokens, index, options)
  }
  md.core.ruler.after('inline', 'study_table_labels', state => {
    const stack = []
    for (const token of state.tokens) {
      if (token.type === 'table_open') {
        token.attrJoin('class', 'study-data-table')
        stack.push({ headers: [], inHead: false, column: 0 })
        continue
      }
      if (token.type === 'table_close') { stack.pop(); continue }
      const table = stack.at(-1)
      if (!table) continue
      if (token.type === 'thead_open') table.inHead = true
      if (token.type === 'thead_close') table.inHead = false
      if (token.type === 'tr_open') table.column = 0
      if (token.type === 'th_open') token.attrSet('scope', 'col')
      if (table.inHead && token.type === 'inline') {
        const label = (token.children || []).map(child => {
          if (['text', 'code_inline'].includes(child.type)) return child.content
          if (child.type === 'softbreak') return ' '
          return ''
        }).join('').trim()
        table.headers.push(label)
      }
      if (token.type === 'td_open') {
        token.attrSet('data-label', table.headers[table.column] || '')
        table.column++
      }
    }
  })
}
