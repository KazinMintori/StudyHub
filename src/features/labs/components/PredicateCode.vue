<script setup>
import {computed} from 'vue'
import {predicateCode} from '../services/predicate-code.mjs'
import SearchTraceCode from './SearchTraceCode.vue'
const props=defineProps({name:{type:String,required:true},phase:{type:String,default:'start'},derived:{type:Boolean,default:false}})
const code=computed(()=>predicateCode[props.name]||[])
</script>
<template><SearchTraceCode :listing="code" :name="name" :phase="phase" :needle="name==='resolutionPredicateSteps'&&phase==='success'&&derived?'if(result.clause?.length===0)':''"/></template>
