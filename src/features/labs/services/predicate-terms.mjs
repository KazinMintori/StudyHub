export function parseTerm(source) {
  if (typeof source !== 'string' || source.length > 300) throw Error('Hạng thức dài tối đa 300 ký tự.')
  const tokens = source.match(/\?[A-Za-z][A-Za-z0-9_]*|[A-Za-z][A-Za-z0-9_]*|[(),]/g) || []
  if (tokens.join('') !== source.replace(/\s/g, '') || tokens.length > 100) throw Error('Dùng tên Latin, ?x cho biến, dấu phẩy và ngoặc tròn. Tối đa 100 token.')
  let position = 0
  function read(depth) {
    if (depth > 15) throw Error('Hạng thức lồng tối đa 15 tầng.')
    const name = tokens[position++]
    if (!name || /^[(),]$/.test(name)) throw Error('Thiếu tên hạng thức.')
    if (name.startsWith('?')) return { type: 'variable', name: name.slice(1) }
    if (tokens[position] !== '(') return { type: 'constant', name }
    position++
    const args = []
    if (tokens[position] !== ')') {
      args.push(read(depth + 1))
      while (tokens[position] === ',') { position++; args.push(read(depth + 1)) }
    }
    if (tokens[position++] !== ')') throw Error('Thiếu ngoặc đóng.')
    if (!args.length) throw Error('Hàm không đối số được viết như hằng, không dùng cặp ngoặc rỗng.')
    return { type: 'function', name, args }
  }
  const term = read(0)
  if (position !== tokens.length) throw Error('Có dữ liệu thừa sau hạng thức.')
  return term
}
export function formatTerm(t) {
  return t.type === 'variable' ? '?' + t.name : t.name + (t.args ? '(' + t.args.map(formatTerm).join(', ') + ')' : '')
}
export function termVariables(t) {
  return t.type === 'variable' ? [t.name] : [...new Set((t.args || []).flatMap(termVariables))]
}
export function applyTerm(t, theta, active = new Set()) {
  if (t.type === 'variable' && Object.hasOwn(theta, t.name)) {
    if (active.has(t.name)) throw Error('Phép thế có chu trình, không biểu diễn hạng thức hữu hạn.')
    return applyTerm(theta[t.name], theta, new Set([...active, t.name]))
  }
  return t.args ? { ...t, args: t.args.map(x => applyTerm(x, theta, active)) } : { ...t }
}
export function formatTheta(theta) {
  return Object.fromEntries(Object.keys(theta).map(v => ['?' + v, formatTerm(applyTerm(theta[v], theta))]))
}
export function* unifySteps(left, right, initial = {}) {
  const theta = { ...initial }
  let equations = [[left, right]]
  const snap = (phase, extra = {}) => ({ phase, theta: structuredClone(theta), equations: equations.map(pair => pair.map(x => formatTerm(applyTerm(x, theta)))), ...extra })
  yield snap('start')
  while (equations.length) {
    let [a, b] = equations.shift()
    a = applyTerm(a, theta); b = applyTerm(b, theta)
    yield snap('equation', { left: formatTerm(a), right: formatTerm(b) })
    if (formatTerm(a) === formatTerm(b)) { yield snap('delete'); continue }
    if (b.type === 'variable' && a.type !== 'variable') [a, b] = [b, a]
    if (a.type === 'variable') {
      if (termVariables(b).includes(a.name)) { yield snap('occurs', { variable: a.name, term: formatTerm(b) }); return null }
      theta[a.name] = b
      for (const name of Object.keys(theta)) theta[name] = applyTerm(theta[name], theta)
      yield snap('bind', { variable: a.name, term: formatTerm(b) })
    } else {
      if (a.type !== b.type || a.name !== b.name || (a.args?.length || 0) !== (b.args?.length || 0)) { yield snap('failure', { left: formatTerm(a), right: formatTerm(b) }); return null }
      equations = [...a.args.map((x, i) => [x, b.args[i]]), ...equations]
      yield snap('decompose')
    }
  }
  yield snap('success')
  return theta
}
export function unify(left, right, initial = {}) {
  const iterator = unifySteps(left, right, initial)
  let step = iterator.next()
  while (!step.done) step = iterator.next()
  return step.value
}
export function parseAtom(source) {
  if (typeof source !== 'string') throw Error('Câu nguyên tử phải là chuỗi.')
  const term = parseTerm(source)
  if (term.type === 'variable') throw Error('Tên vị từ không thể là biến.')
  return { name: term.name, args: term.args || [] }
}
export const formatAtom = atom => atom.name + (atom.args.length ? '(' + atom.args.map(formatTerm).join(', ') + ')' : '')
export const applyAtom = (atom, theta) => ({ name: atom.name, args: atom.args.map(t => applyTerm(t, theta)) })
export const atomVariables = atom => [...new Set(atom.args.flatMap(termVariables))]
export function unifyAtoms(a, b, theta = {}) {
  if (a.name !== b.name || a.args.length !== b.args.length) return null
  let result = { ...theta }
  for (let i = 0; i < a.args.length; i++) { result = unify(a.args[i], b.args[i], result); if (result === null) return null }
  return result
}
export function standardizeAtoms(atoms, prefix) {
  const names = [...new Set(atoms.flatMap(atomVariables))], mapping = Object.fromEntries(names.map((v, i) => [v, prefix + i]))
  return renameAtoms(atoms, mapping)
}
export function renameAtoms(atoms, mapping) {
  const rename = t => t.type==='variable'?{...t,name:mapping[t.name]??t.name}:t.args?{...t,args:t.args.map(rename)}:{...t}
  return atoms.map(a=>({...a,args:a.args.map(rename)}))
}
export const unificationExamples = {
  simple: { title: 'Một biến nhận một hằng', left: 'Knows(John, ?x)', right: 'Knows(John, Jane)' },
  join: { title: 'Hai biến cùng được ràng buộc', left: 'Knows(John, ?x)', right: 'Knows(?y, Bill)' },
  nested: { title: 'Truyền phép thế vào hàm lồng', left: 'Knows(John, ?x)', right: 'Knows(?y, Mother(?y))' },
  shared: { title: 'Cùng biến, buộc cùng hạng thức', left: 'P(?x, ?x)', right: 'P(An, Binh)' },
  occurs: { title: 'Kiểm tra xuất hiện trực tiếp', left: '?x', right: 'f(?x)' },
  indirect: { title: 'Kiểm tra xuất hiện sau truyền phép thế', left: 'Pair(?x, ?y)', right: 'Pair(?y, f(?x))' },
  apart: { title: 'Hai biến đã chuẩn hóa tách biệt', left: 'Knows(John, ?x)', right: 'Knows(?x17, Elizabeth)' },
  general: { title: 'Giữ tính tổng quát', left: 'P(?x)', right: 'P(?y)' }
}
