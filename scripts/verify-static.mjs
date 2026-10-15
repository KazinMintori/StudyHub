// Check the current single build output served by a local static preview.
process.env.QA_URL ||= process.env.STATIC_QA_URL || 'http://127.0.0.1:8080'
await import('./verification/verify-content-model.mjs')
await import('./verification/verify-refactor-browser.mjs')
