import chapter1 from '../../../content/courses/triet-hoc-mac-lenin/exam/solutions/chuong-1.json' with { type: 'json' }
import chapter2a from '../../../content/courses/triet-hoc-mac-lenin/exam/solutions/chuong-2a.json' with { type: 'json' }
import chapter2b from '../../../content/courses/triet-hoc-mac-lenin/exam/solutions/chuong-2b.json' with { type: 'json' }
import chapter3 from '../../../content/courses/triet-hoc-mac-lenin/exam/solutions/chuong-3.json' with { type: 'json' }

const libraries = [chapter1, chapter2a, chapter2b, chapter3]

/** Resolve the authored conceptual explanation separately from the short option feedback. */
export function detailedSolution(questionId) {
  const library = libraries.find(item => Object.hasOwn(item.questions, questionId))
  const question = library?.questions[questionId]
  if (!question) return null
  return {
    contexts: question.contextIds.map(id => library.contexts[id]),
    reasoning: question.reasoning || '',
    example: question.example || '',
  }
}
