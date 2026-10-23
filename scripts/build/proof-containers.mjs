// Classify proof containers after VitePress installs its details renderer.
export function setupProofRenderer(md) {
 let wrapped = false
 md.core.ruler.after('block', 'study_proof_containers', state => {
  for (const token of state.tokens) {
   if (token.type === 'container_details_open') {
    const source = token.map ? state.src.split('\n').slice(...token.map).join('\n') : ''
    token.meta = { ...token.meta,
     studyProof: /^details\s+Chứng minh(?:\s|:|$)/u.test(token.info.trim()),
     explicitQed: /\\(?:blacksquare|qed)\b|∎/.test(source)
    }
   }
  }
  if (wrapped || !md.renderer.rules.container_details_open) return
  wrapped = true
  const open = md.renderer.rules.container_details_open
  md.renderer.rules.container_details_open = (tokens, index, options, env, self) => {
   const html = open(tokens, index, options, env, self)
   return tokens[index].meta?.studyProof
    ? html.replace(/class="([^"]*)"/, (_, classes) => 'class="' + classes + ' proof' + (tokens[index].meta.explicitQed ? ' proof-has-qed' : '') + '"')
    : html
  }
 })
}
