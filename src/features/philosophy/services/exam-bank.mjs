/** Adapt plain philosophy text to the shared exam renderer without interpreting it as HTML. */
import { detailedSolution } from './detailed-solutions.mjs'

const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, character => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character])
const paragraph = value => value ? `<p>${escapeHtml(value).replace(/\n/g, '<br>')}</p>` : ''

function fullAnswer(question) {
  const solution = detailedSolution(question.id)
  return [
    `<p><strong>Đáp án ${escapeHtml(question.correctKey)}.</strong></p>`,
    ...(solution?.contexts || []).flatMap(context => [
      `<h3>${escapeHtml(context.title)}</h3>`,
      ...context.paragraphs.map(paragraph),
    ]),
    paragraph(solution?.reasoning || question.explanation),
    paragraph(solution?.example),
  ].join('\n')
}

export function toExamBank(bank) {
  return {
    id: bank.id,
    title: bank.title,
    questions: (bank.questions || []).map(question => ({
      id: question.id,
      kind: 'quiz',
      correctKey: question.correctKey,
      promptHtml: paragraph(question.prompt),
      options: question.options.map(option => ({
        key: option.key,
        html: paragraph(option.text),
        explanationHtml: paragraph(option.key === question.correctKey
          ? question.explanation
          : question.distractors?.find(item => item.key === option.key)?.explanation),
      })),
      answerHtml: fullAnswer(question),
    })),
  }
}
