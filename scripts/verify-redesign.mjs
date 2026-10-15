// Compatibility command; verify the interface that is currently published.
process.env.QA_URL ||= 'http://127.0.0.1:5181'
await import('./verification/verify-refactor-browser.mjs')
