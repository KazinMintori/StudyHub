// Lazy entry for the concept dictionary and Wiki helpers. The data carries
// pre-rendered math for every term, so client code reaches it through
// concept-loader.mjs (term hover, Kiến thức nền, cheatsheet synthesis)
// instead of bundling it with the theme.
export { concepts } from '../../../../docs/.vitepress/concepts.mjs'
export { conceptField, relatedConcepts } from '../../../../docs/.vitepress/wiki-content.mjs'
