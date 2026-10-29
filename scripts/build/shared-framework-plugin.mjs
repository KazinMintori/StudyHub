import { createHash } from 'node:crypto'
import { readFileSync } from 'node:fs'
import path from 'node:path'

const entry = 'virtual:studyhub-runtime-exports'
const resolvedEntry = '\0' + entry
const lock = readFileSync(new URL('../../package-lock.json', import.meta.url))
const namespace = 'studyhub.framework.' + createHash('sha256').update(lock).digest('hex').slice(0, 16)

export function sharedFrameworkProxy(file, exports, key = namespace) {
  if (exports.some(name => !/^[$A-Z_a-z][$\w]*$/.test(name))) throw Error('Unsupported runtime export name')
  return `const key = Symbol.for(${JSON.stringify(key)});
const runtime = globalThis[key] ||= await import(${JSON.stringify('./' + path.posix.basename(file))});
${exports.map((name, index) => `if (!(${JSON.stringify(name)} in runtime)) throw new Error(${JSON.stringify('Incompatible StudyHub runtime export: ' + name)});
const value${index} = runtime[${JSON.stringify(name)}];
export { value${index} as ${name} };`).join('\n')}
`
}

// Independently compiled VitePress batches can emit different framework
// hashes. A second framework creates different injection symbols and Vue
// effects. All page chunks must keep using the first document's runtime.
export function sharedFrameworkPlugin() {
  let clientBuild = false
  return {
    name: 'studyhub-shared-framework',
    enforce: 'post',
    configResolved(config) {
      clientBuild = config.command === 'build' && !config.build.ssr
      if (clientBuild) {
        const outputs = config.build.rollupOptions.output
        for (const output of Array.isArray(outputs) ? outputs : [outputs]) output.minifyInternalExports = false
      }
    },
    resolveId(id) { if (id === entry) return resolvedEntry },
    load(id) {
      // A fixed public export surface lets even a short first page initialize
      // every helper needed by a later page from another batch.
      if (id === resolvedEntry) return "export * from 'vue'; export * from 'vitepress'"
    },
    buildStart() {
      if (clientBuild) this.emitFile({ type: 'chunk', id: entry, name: 'studyhub-runtime-exports', preserveSignature: 'strict' })
    },
    generateBundle(_options, bundle) {
      if (!clientBuild) return
      const framework = Object.values(bundle).find(chunk => chunk.type === 'chunk' && chunk.name === 'framework')
      if (!framework) throw Error('VitePress framework chunk was not emitted')
      if (framework.imports.length) throw Error('The shared framework must remain self-contained')
      const name = path.posix.basename(framework.fileName)
      const proxyName = name.replace(/^framework\./, 'framework-shared.')
      for (const chunk of Object.values(bundle)) {
        if (chunk.type === 'chunk' && chunk !== framework) chunk.code = chunk.code.replaceAll(name, proxyName)
      }
      this.emitFile({ type: 'asset', fileName: path.posix.join(path.posix.dirname(framework.fileName), proxyName), source: sharedFrameworkProxy(framework.fileName, framework.exports) })
    }
  }
}
