export const relationPresets = {
  identity: { title: 'Mỗi người liên hệ với chính mình', matrix: [[true,false,false],[false,true,false],[false,false,true]] },
  universal: { title: 'Một người liên hệ với tất cả', matrix: [[true,true,true],[false,false,false],[false,false,false]] },
  empty: { title: 'Không có quan hệ nào', matrix: [[false,false,false],[false,false,false],[false,false,false]] },
  cycle: { title: 'Chu trình ba người', matrix: [[false,true,false],[false,false,true],[true,false,false]] }
}
export const quantifiedFormulas = {
  ae: { title: 'Mỗi người được ít nhất một người liên hệ', outer: 'all', inner: 'some', outerVariable:'y', text: '∀y ∃x R(x, y)' },
  ea: { title: 'Có một người liên hệ với mọi đối tượng', outer: 'some', inner: 'all', text: '∃x ∀y R(x, y)' },
  aa: { title: 'Mọi cặp đều có quan hệ', outer: 'all', inner: 'all', text: '∀x ∀y R(x, y)' },
  ee: { title: 'Có ít nhất một cặp liên hệ', outer: 'some', inner: 'some', text: '∃x ∃y R(x, y)' }
}
export function* quantifierSteps(matrix, id = 'ae') {
  if (!Array.isArray(matrix) || matrix.length < 1 || matrix.length > 4 || matrix.some(row => !Array.isArray(row) || row.length !== matrix.length || row.some(v=>typeof v!=='boolean')) || !quantifiedFormulas[id]) throw Error('Cần ma trận quan hệ vuông 1 đến 4 đối tượng, giá trị Đúng/Sai.')
  const { outer, inner,outerVariable='x' } = quantifiedFormulas[id], rows = []
  const snap = (phase, extra={}) => ({ phase, rows: rows.slice(), ...extra })
  yield snap('start')
  for (let index = 0; index < matrix.length; index++) {
    const values = []
    for (let other = 0; other < matrix.length; other++) {
      const x=outerVariable==='x'?index:other,y=outerVariable==='x'?other:index
      values.push(matrix[x][y])
      yield snap('pair', { x, y, value: matrix[x][y], values: values.slice() })
    }
    const value = inner === 'all' ? values.every(Boolean) : values.some(Boolean)
    rows.push(value)
    yield snap('row', { index,outerVariable,value, witness: inner==='some'?values.findIndex(Boolean):null, counterexample:inner==='all'?values.findIndex(v=>!v):null })
  }
  const value = outer === 'all' ? rows.every(Boolean) : rows.some(Boolean)
  yield snap('result', { value,outerVariable,witness:outer==='some'?rows.findIndex(Boolean):null, counterexample:outer==='all'?rows.findIndex(v=>!v):null })
}
