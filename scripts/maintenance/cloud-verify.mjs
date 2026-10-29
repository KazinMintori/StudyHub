import { spawnSync } from 'node:child_process'
const run = args => {
  const result = spawnSync('git', args, { encoding: 'utf8', windowsHide: true })
  if (result.status !== 0) throw Error(result.stderr || 'Git command failed')
  return result.stdout.trim()
}
const mode = process.argv[2] || 'fixture'
if (!['fixture', 'full'].includes(mode)) throw Error('Choose fixture or full')
if (run(['status', '--porcelain', '--untracked-files=normal'])) throw Error('Commit changes before cloud verification')
const branch = run(['branch', '--show-current'])
if (!branch) throw Error('Use a named branch for cloud verification')
const remote = run(['remote', 'get-url', 'origin'])
const match = remote.match(/github\.com[:/]([\w.-]+\/[\w.-]+?)(?:\.git)?$/)
if (!match) throw Error('Expected a GitHub origin')
const credential = spawnSync('git', ['credential', 'fill'], { input: 'protocol=https\nhost=github.com\n\n', encoding: 'utf8', windowsHide: true, env: {...process.env, GIT_TERMINAL_PROMPT:'0', GCM_INTERACTIVE:'never'} })
if (credential.status !== 0) throw Error('Sign in to GitHub with Git Credential Manager first')
const token = credential.stdout.split('\n').find(line => line.startsWith('password='))?.slice(9).trim()
if (!token) throw Error('GitHub credential unavailable')
run(['push', 'origin', `HEAD:refs/heads/${branch}`])
const response = await fetch(`https://api.github.com/repos/${match[1]}/actions/workflows/deploy.yml/dispatches`, {
  method:'POST', headers:{Authorization:`Bearer ${token}`,Accept:'application/vnd.github+json','Content-Type':'application/json'},
  body:JSON.stringify({ref:branch,inputs:{verify_only:true,fixture_only:mode==='fixture'}})
})
if (response.status !== 204) throw Error(`GitHub could not start verification (${response.status})`)
console.log(`Started ${mode} verification on GitHub. No local build or browser installation needed.`)
console.log(`https://github.com/${match[1]}/actions/workflows/deploy.yml?query=branch%3A${encodeURIComponent(branch)}`)
