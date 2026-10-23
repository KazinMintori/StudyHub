const searchable = value => String(value ?? '').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase()
export function filterParallelCheatsheet(cheatsheet, query = '') {
 const terms = searchable(query).trim().split(/\s+/).filter(Boolean)
 const sections = cheatsheet?.sections ?? []
 if (!terms.length) return sections
 const matches = text => terms.every(term => searchable(text).includes(term))
 return sections.flatMap(section => {
  if (matches(section.title)) return [section]
  const items = (section.items ?? []).filter(item => matches([
   item.name,item.description,item.note,item.formula,item.code,
   ...(item.bullets ?? []),...(item.variables ?? []),
   ...(item.formulaRows ?? []).flatMap(row => [row.label,row.formula])
  ].filter(Boolean).join(' ')))
  const table = section.table && {
   ...section.table,
   rows: (section.table.rows ?? []).filter(row => matches(row.join(' ')))
  }
  return items.length || table?.rows.length ? [{...section,items,table}] : []
 })
}
