// Stable entry for existing authoring tools.
export * from '../../src/features/lecture/services/lecture-model.mjs'
// Cheatsheets import every physics data module, so the client lecture model
// does not re-export them. Node tools keep the synchronous helper here.
export { getLectureCheatsheet as lectureCheatsheet } from '../../src/features/lecture/services/cheatsheet-service.mjs'
