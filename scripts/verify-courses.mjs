// Compatibility command for the current course model and interface.
process.env.QA_URL ||= 'http://127.0.0.1:8080'
await import('./verification/verify-content-model.mjs')
await import('./verification/verify-refactor-browser.mjs')
