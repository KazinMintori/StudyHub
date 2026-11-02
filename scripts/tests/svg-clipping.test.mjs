import test from 'node:test'
import assert from 'node:assert/strict'
import {clipSegment,clipPolyline} from '../../src/features/labs/services/svg-clipping.mjs'
const box={x0:0,x1:4,y0:0,y1:3}
test('display clipping keeps crossings and rejects wholly external or invalid segments',()=>{
 assert.deepEqual(clipSegment([[-2,1],[6,1]],box),[[0,1],[4,1]])
 assert.deepEqual(clipSegment([[2,-2],[2,5]],box),[[2,0],[2,3]])
 assert.equal(clipSegment([[-2,-1],[6,-1]],box),null)
 assert.equal(clipSegment([[NaN,1],[2,3]],box),null)
 assert.deepEqual(clipSegment([[0,1],[0,2]],box),[[0,1],[0,2]])
})
test('a curve leaving and reentering the frame has no fabricated connecting edge',()=>{
 const result=clipPolyline([[1,1],[2,4],[3,4],[4,1]],box)
 assert.equal(result.length,2)
 const expected=[[[1,1],[5/3,3]],[[10/3,3],[4,1]]]
 for(const [i,line]of result.entries())for(const [j,point]of [line[0],line.at(-1)].entries())assert(Math.hypot(...point.map((v,k)=>v-expected[i][j][k]))<1e-12)
 for(const line of result)for(const [x,y]of line)assert(x>=0&&x<=4&&y>=0&&y<=3)
})
