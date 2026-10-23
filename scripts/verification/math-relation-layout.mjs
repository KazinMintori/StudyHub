// A display can fit its container and still separate a new left-hand side
// from its relation. Reject that malformed layout before publishing groups.
export function mathRelationLayoutIssues(source) {
 const text=source.replace(/```[^\n]*\n[\s\S]*?```/g,block=>block.replace(/[^\n]/g,' '))
 const issues=[]
 for(const block of text.matchAll(/\$\$([\s\S]*?)\$\$/g)) {
  const rules=[
   ['dangling-secondary-lhs',/\\(?:implies|iff|qquad|quad)\s*[^\n]+?\\\\\s*\n\s*&\s*(?:=|\\(?:approx|leq?|geq?))/g],
   ['empty-right-side-before-break',/(?:=|\\(?:approx|leq?|geq?))\s*&?\s*\\\\\s*\n/g]
  ]
  for(const [kind,pattern]of rules)for(const match of block[1].matchAll(pattern)) {
   const offset=block.index+2+match.index
   issues.push({kind,line:source.slice(0,offset).split('\n').length})
  }
 }
 return issues
}
