import test from 'node:test'
import {verifyDataExamAdditions} from '../verify-data-exam-additions.mjs'
test('New Drive banks retain every question and exact code with detailed feedback',async()=>{
  await verifyDataExamAdditions()
})
