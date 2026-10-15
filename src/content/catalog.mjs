import { course as course0 } from './courses/bieu-dien-tri-thuc/course.mjs'
import { course as course1 } from './courses/toan-cho-ai/course.mjs'
import { course as course2 } from './courses/xac-suat-thong-ke/course.mjs'
import { course as course3 } from './courses/xu-ly-du-lieu/course.mjs'
import { course as course4 } from './courses/vat-ly-1/course.mjs'
import { course as course5 } from './courses/vat-ly-2/course.mjs'
import { course as course6 } from './courses/giai-thuat-du-lieu/course.mjs'
import { course as course7 } from './courses/dsa/course.mjs'
import { course as course8 } from './courses/discrete-math/course.mjs'

export const courseCatalog = [course0, course1, course2, course3, course4, course5, course6, course7, course8]
export const findCourse = id => courseCatalog.find(course => course.id === id)
