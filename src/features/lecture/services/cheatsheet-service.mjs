import {physics1RemainingChapter15Parent} from '../../../../docs/.vitepress/physics1-remaining-ch15-course.mjs'
import {physics1RemainingChapter14Parent} from '../../../../docs/.vitepress/physics1-remaining-ch14-course.mjs'
import {physics1RemainingChapter13Parent} from '../../../../docs/.vitepress/physics1-remaining-ch13-course.mjs'
import {physics1RemainingChapter12Parent} from '../../../../docs/.vitepress/physics1-remaining-ch12-course.mjs'
import {physics1RemainingChapter1Parent} from '../../../../docs/.vitepress/physics1-remaining-ch01-course.mjs'
import {physics1RemainingChapter5Parent} from '../../../../docs/.vitepress/physics1-remaining-ch05-course.mjs'
import {physics1RemainingChapter8Parent} from '../../../../docs/.vitepress/physics1-remaining-ch08-course.mjs'
import {physics1RemainingChapter7Parent} from '../../../../docs/.vitepress/physics1-remaining-ch07-course.mjs'
import {physics1RemainingChapter6Parent} from '../../../../docs/.vitepress/physics1-remaining-ch06-course.mjs'
import {physics1PriorityCourseData} from '../../../../docs/.vitepress/physics1-priority-course.mjs'
import {physics1RemainingChapter4Parent} from '../../../../docs/.vitepress/physics1-remaining-ch04-course.mjs'
import {physics1RemainingChapter3Parent} from '../../../../docs/.vitepress/physics1-remaining-ch03-course.mjs'
import {particlesCosmologyCheatsheet} from '../../../../docs/.vitepress/physics-particles-cosmology-course.mjs'
import {nuclearCheatsheet} from '../../../../docs/.vitepress/physics-nuclear-course.mjs'
import {moleculesCheatsheet} from '../../../../docs/.vitepress/physics-molecules-course.mjs'
import {atomicStructureCheatsheet} from '../../../../docs/.vitepress/physics-atomic-structure-course.mjs'
import {quantumWaveCheatsheet} from '../../../../docs/.vitepress/physics-quantum-wave-course.mjs'
import {matterWavesCheatsheet} from '../../../../docs/.vitepress/physics-matter-waves-course.mjs'
import {photonCheatsheet} from '../../../../docs/.vitepress/physics-photon-course.mjs'
import {relativityCheatsheet} from '../../../../docs/.vitepress/physics-relativity-course.mjs'
import {diffractionCheatsheet} from '../../../../docs/.vitepress/physics-diffraction-course.mjs'
import {interferenceCheatsheet} from '../../../../docs/.vitepress/physics-interference-course.mjs'
import {geometricOpticsCheatsheet} from '../../../../docs/.vitepress/physics-geometric-optics-course.mjs'
import {opticsCheatsheet} from '../../../../docs/.vitepress/physics-optics-course.mjs'
import {emWaveCheatsheet} from '../../../../docs/.vitepress/physics-emwave-course.mjs'
import {acCheatsheet} from '../../../../docs/.vitepress/physics-ac-course.mjs'
import {inductanceCheatsheet} from '../../../../docs/.vitepress/physics-inductance-course.mjs'
import {inductionCheatsheet} from '../../../../docs/.vitepress/physics-induction-course.mjs'
import { sourcesCheatsheet } from '../../../../docs/.vitepress/physics-sources-course.mjs'
import { magneticCheatsheet } from '../../../../docs/.vitepress/physics-magnetic-course.mjs'
import { dcCheatsheet } from '../../../../docs/.vitepress/physics-dc-course.mjs'
import { currentCheatsheet } from '../../../../docs/.vitepress/physics-current-course.mjs'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { buildLectureCheatsheet } from './cheatsheet-builder.mjs'
import { physicsMotionCheatsheet } from '../../../../docs/.vitepress/physics-motion-course.mjs'
import { electrostaticsCheatsheet } from '../../../../docs/.vitepress/physics-electrostatics-course.mjs'
import { gaussCheatsheet } from '../../../../docs/.vitepress/physics-gauss-course.mjs'
import { potentialCheatsheet } from '../../../../docs/.vitepress/physics-potential-course.mjs'
import { capacitanceCheatsheet } from '../../../../docs/.vitepress/physics-capacitance-course.mjs'
import { mathAiReviewCheatsheet } from '../../../content/courses/toan-cho-ai/lectures/on-luyen/review-course.mjs'

import {
  unitsVectorsCheatsheet,
  newtonApplicationsCheatsheet,
  workEnergyCheatsheet,
  potentialEnergyCheatsheet,
  momentumCheatsheet,
  rotationKinematicsCheatsheet,
  rotationDynamicsCheatsheet,
  equilibriumElasticityCheatsheet,
  fluidMechanicsCheatsheet,
  gravitationCheatsheet,
  oscillationsCheatsheet,
  mechanicalWavesCheatsheet,
  acousticsCheatsheet,
  temperatureHeatCheatsheet,
  kineticTheoryCheatsheet,
  firstLawThermoCheatsheet,
  secondLawEntropyCheatsheet
} from '../../../../docs/.vitepress/physics1-cheatsheets.mjs'

export const cheatsheets = { 'vat-ly-2/18-photon': photonCheatsheet, 'vat-ly-2/17-thuyet-tuong-doi': relativityCheatsheet, 'vat-ly-2/16-nhieu-xa': diffractionCheatsheet, 'vat-ly-2/15-giao-thoa': interferenceCheatsheet, 'vat-ly-2/14-quang-hinh-hoc': geometricOpticsCheatsheet, 'vat-ly-2/13-truyen-anh-sang': opticsCheatsheet, 'vat-ly-2/12-song-dien-tu': emWaveCheatsheet, 'vat-ly-2/11-dong-dien-xoay-chieu': acCheatsheet, 'vat-ly-2/10-tu-cam': inductanceCheatsheet, 'vat-ly-2/09-cam-ung-dien-tu': inductionCheatsheet, 'vat-ly-2/08-nguon-tu-truong': sourcesCheatsheet, 'vat-ly-2/07-tu-truong-luc-tu': magneticCheatsheet, 'vat-ly-2/06-mach-dien-mot-chieu': dcCheatsheet, 'vat-ly-2/05-dong-dien-dien-tro': currentCheatsheet, 'vat-ly-2/04-tu-dien-dien-moi': capacitanceCheatsheet, 'vat-ly-1/02-chuyen-dong-thang': physicsMotionCheatsheet, 'vat-ly-2/01-dien-truong-coulomb': electrostaticsCheatsheet, 'vat-ly-2/03-dinh-luat-gauss': gaussCheatsheet, 'vat-ly-2/02-dien-the': potentialCheatsheet, 'toan-cho-ai/on-luyen': mathAiReviewCheatsheet,
  'vat-ly-2/19-song-vat-chat': matterWavesCheatsheet,
  'vat-ly-2/20-ham-song-schrodinger': quantumWaveCheatsheet,
  'vat-ly-2/21-cau-truc-nguyen-tu': atomicStructureCheatsheet,
  'vat-ly-2/22-chat-ran-ban-dan': moleculesCheatsheet,
  'vat-ly-2/23-vat-ly-hat-nhan': nuclearCheatsheet,
  'vat-ly-2/24-hat-co-ban-vu-tru': particlesCosmologyCheatsheet,
  'vat-ly-1/01-don-vi-vector': physics1RemainingChapter1Parent.cheatsheet,
  'vat-ly-1/03-chuyen-dong-khong-gian': physics1RemainingChapter3Parent.cheatsheet,
  'vat-ly-1/04-dinh-luat-newton': physics1RemainingChapter4Parent.cheatsheet,
  'vat-ly-1/05-ung-dung-newton': physics1RemainingChapter5Parent.cheatsheet,
  'vat-ly-1/06-cong-dong-nang': physics1RemainingChapter6Parent.cheatsheet,
  'vat-ly-1/07-the-nang-bao-toan-co-nang': physics1RemainingChapter7Parent.cheatsheet,
  'vat-ly-1/08-dong-luong-va-cham': physics1RemainingChapter8Parent.cheatsheet,
  'vat-ly-1/09-dong-hoc-vat-ran': physics1PriorityCourseData[9].cheatsheet,
  'vat-ly-1/10-dong-luc-hoc-quay': physics1PriorityCourseData[10].cheatsheet,
  'vat-ly-1/11-can-bang-dan-hoi': physics1PriorityCourseData[11].cheatsheet,
  'vat-ly-1/12-co-hoc-chat-luu': physics1RemainingChapter12Parent.cheatsheet,
  'vat-ly-1/13-hap-dan': physics1RemainingChapter13Parent.cheatsheet,
  'vat-ly-1/14-dao-dong': physics1RemainingChapter14Parent.cheatsheet,
  'vat-ly-1/15-song-co': physics1RemainingChapter15Parent.cheatsheet,
  'vat-ly-1/16-am-hoc': acousticsCheatsheet,
  'vat-ly-1/17-nhiet-do-nhiet-luong': physics1PriorityCourseData[17].cheatsheet,
  'vat-ly-1/18-thuyet-dong-hoc-chat-khi': physics1PriorityCourseData[18].cheatsheet,
  'vat-ly-1/19-nguyen-ly-thu-nhat': physics1PriorityCourseData[19].cheatsheet,
  'vat-ly-1/20-nguyen-ly-thu-hai-entropy': physics1PriorityCourseData[20].cheatsheet,
}

export function getLectureCheatsheet(course, lesson) {
  if (!course || !lesson) return null
  return buildLectureCheatsheet(course, lesson, { explicit: cheatsheets[`${course.id}/${lesson.slug}`], concepts })
}
