// Feedback is posted straight from the page to a form service, so readers do not
// need a GitHub account. `endpoint` accepts any service that takes a JSON POST
// and answers 2xx, for example Web3Forms (https://api.web3forms.com/submit, with
// `accessKey`) or Formspree (https://formspree.io/f/<id>, no key). While
// `endpoint` is empty the dialog still works: it lets the reader copy the message
// or, as a last resort, open a prefilled GitHub issue.
export const feedbackConfig = Object.freeze({
  endpoint: '',
  accessKey: '',
  repository: 'KazinMintori/StudyHub',
  maxDescriptionLength: 1000,
  maxContactLength: 120,
  maxIssueUrlLength: 8000,
  requestTimeoutMs: 15000,
  categories: [
    { id: 'content', label: 'Nội dung sai hoặc khó hiểu', short: 'Nội dung' },
    { id: 'display', label: 'Lỗi hiển thị hoặc chức năng', short: 'Hiển thị' },
    { id: 'suggestion', label: 'Ý tưởng hoặc góp ý khác', short: 'Ý tưởng' }
  ]
})
