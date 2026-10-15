export const artifactPolicy = Object.freeze({
  generated: ['docs/.vitepress/cache', 'docs/.vitepress/.temp', 'dist'],
  protected: [
    'raw_materials', 'materials', 'docs/public', 'src',
    'qa/physics/chapter30', 'qa/physics/full-source',
    'qa/physics/release29-certified'
  ]
})
