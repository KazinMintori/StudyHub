export const PRACTICE_TARGET_SIZE = 60

/** Balance a chapter so the final test is not a very short remainder. */
export function chapterPracticeTests(chapter, targetSize = PRACTICE_TARGET_SIZE) {
  const count = Number.isInteger(chapter?.count) ? chapter.count : chapter?.questions?.length || 0
  if (count <= 0 || !Number.isInteger(targetSize) || targetSize < 1) return []
  const numberOfTests = Math.ceil(count / targetSize)
  const base = Math.floor(count / numberOfTests)
  const remainder = count % numberOfTests
  let start = 0
  return Array.from({ length: numberOfTests }, (_, index) => {
    const size = base + (index < remainder ? 1 : 0)
    const test = {
      id: `${chapter.id}-bai-${index + 1}`,
      parentBankId: chapter.id,
      chapter: chapter.chapter,
      testNumber: index + 1,
      totalTests: numberOfTests,
      title: `Bài kiểm tra ${index + 1}`,
      count: size,
      start,
      end: start + size,
      path: `/triet-hoc-mac-lenin/on-thi/${chapter.id}/bai-${index + 1}`,
    }
    start += size
    return test
  })
}

export function createPracticeBank(chapter, testNumber, cleanQuestion = question => question) {
  const test = chapterPracticeTests(chapter).find(item => item.testNumber === testNumber)
  if (!test || !Array.isArray(chapter.questions)) throw new Error(`Unknown practice test: ${chapter?.id}/${testNumber}`)
  return {
    schemaVersion: chapter.schemaVersion,
    id: test.id,
    parentBankId: test.parentBankId,
    chapter: test.chapter,
    testNumber: test.testNumber,
    totalTests: test.totalTests,
    title: test.title,
    questions: chapter.questions.slice(test.start, test.end).map(question => {
      const { sourceReference, knowledgeIds, level, questionType, ...practice } = cleanQuestion(question)
      return practice
    }),
  }
}
