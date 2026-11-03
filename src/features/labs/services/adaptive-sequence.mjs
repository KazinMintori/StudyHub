// Shared numerical trace for the Bài 6 gradient-memory illustration.
export function adaptiveSequence(gradients,{rate=0.1,beta=0.9,beta1=0.9,beta2=0.999,epsilon=1e-8}={}){
  let sum=0,rms=0,m=0,v=0
  return gradients.map((g,index)=>{
    const t=index+1
    sum+=g*g
    rms=beta*rms+(1-beta)*g*g
    m=beta1*m+(1-beta1)*g
    v=beta2*v+(1-beta2)*g*g
    const mean=m/(1-beta1**t)
    const square=v/(1-beta2**t)
    return {
      t,g,sum,rms,m,v,mean,square,
      adagrad:-rate*g/(Math.sqrt(sum)+epsilon),
      rmsprop:-rate*g/(Math.sqrt(rms)+epsilon),
      adam:-rate*mean/(Math.sqrt(square)+epsilon),
    }
  })
}
