let pending

/** Load the concept dictionary once and share the promise between callers. */
export function loadConceptData() {
  pending ??= import('./concept-data.mjs').catch(error => {
    pending = undefined
    throw error
  })
  return pending
}
