export function exerciseAssetPath(chapter, file='index.json') {
 if(!Number.isInteger(chapter)||chapter<1||chapter>44)throw Error('Invalid chapter')
 if(!/^(?:index|(?:guided|discussion|numbered-[abcd]|bridge)-\d{2})\.json$/.test(file))throw Error('Invalid exercise asset')
 return '/physics-exercises/ch'+String(chapter).padStart(2,'0')+'/'+file
}
export function resolveExerciseHtml(html, base='/') {
 // Every local URL is emitted with root-relative paths by the trusted renderer.
 return html.replace(/\b(href|src)="\/(?!\/)/g,(_,attribute)=>attribute+'="'+base)
}
