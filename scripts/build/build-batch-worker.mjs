import { readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { build, resolveConfig } from 'vitepress'
import { planBuild } from './page-batches.mjs'

const [command, root, planFile, batchIndex, destination] = process.argv.slice(2)
if (command === 'plan') {
  const config = await resolveConfig(root, 'build', 'production')
  await writeFile(planFile, JSON.stringify(await planBuild(config), null, 2))
} else if (command === 'batch') {
  const plan = JSON.parse(await readFile(planFile, 'utf8'))
  const batch = plan.batches[Number(batchIndex)]
  if (!batch?.pages?.length || !destination) throw new Error('Invalid build batch')
  await build(root, {
    onAfterConfigResolve(config) {
      config.pages = batch.pages
      config.outDir = path.resolve(destination)
      config.tempDir = path.resolve(destination, '../server-' + batchIndex)
      config.buildConcurrency = 1
    }
  })
  const memory = process.resourceUsage().maxRSS / 1024
  console.log(`Batch ${Number(batchIndex) + 1}: ${batch.pages.length} pages; peak RSS ${memory.toFixed(0)} MiB`)
} else throw new Error('Expected plan or batch command')
