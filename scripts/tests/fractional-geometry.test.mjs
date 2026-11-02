import test from 'node:test'
import assert from 'node:assert/strict'
import {fractionalVertices as vertices,fractionalValue,cooperTransform,cooperInverse,fractionalSection,cooperFromScreen} from '../../src/features/labs/services/fractional-geometry.mjs'
import {project3} from '../../src/features/labs/services/foundation-geometry.mjs'

test('the threshold oracle retains singleton optima and excludes impossible levels',()=>{
 assert.deepEqual(fractionalSection(2.75),[[1,4]])
 assert.deepEqual(fractionalSection(8/7,'min'),[[6,0]])
 assert.equal(fractionalSection(2.76).length,0)
 assert.equal(fractionalSection(1.14,'min').length,0)
 assert.equal(fractionalSection(.6).length,4)
})
test('normalization, objective equality and projected-plane input hold across the whole polygon',()=>{
 for(const yaw of [32,50])for(let a=0;a<=10;a++)for(let b=0;b<=10-a;b++){
  // Convex combinations in each of the two triangles cover the quadrilateral.
  for(const triangle of [[vertices[0],vertices[1],vertices[2]],[vertices[0],vertices[2],vertices[3]]]){
   const weights=[a/10,b/10,1-(a+b)/10],x=[0,1].map(i=>triangle.reduce((s,p,j)=>s+p[i]*weights[j],0))
   const lifted=cooperTransform(x),back=cooperInverse(lifted)
   assert(Math.abs(lifted[0]+lifted[1]/2+lifted[2]-1)<1e-12)
   assert(Math.abs(lifted[0]+2*lifted[1]+2*lifted[2]-fractionalValue(x))<1e-12)
   const P=p=>project3(p,{yaw,pitch:32,scale:170,origin:[170,184]})
   const dragged=cooperFromScreen(P(lifted),P)
   for(let i=0;i<2;i++){assert(Math.abs(back[i]-x[i])<1e-10);assert(Math.abs(dragged[i]-x[i])<1e-9)}
  }
 }
 assert.equal(cooperInverse([1,0,0]),null)
})
