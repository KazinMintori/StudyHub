<script setup>
import { computed } from 'vue'
const props = defineProps({ rows: { type: Array, default: () => [] }, matrices: { type: Array, default: null }, operators: { type: Array, default: () => [] }, label: { type: String, required: true } })
const operands = computed(() => props.matrices || [props.rows])
</script>

<template>
  <math class="math-matrix" :aria-label="label">
    <mrow>
      <template v-for="(matrix, operand) in operands" :key="operand">
        <mo v-if="operand" lspace="0.5em" rspace="0.5em">{{ operators[operand - 1] }}</mo>
        <mrow>
          <mo stretchy="true">[</mo>
          <mtable columnspacing="0.8em" rowspacing="0.3em">
            <mtr v-for="(row, i) in matrix" :key="i">
              <mtd v-for="(value, j) in row" :key="j"><mrow><mo v-if="Number(value) < 0" lspace="0em" rspace="0em">−</mo><mn>{{ Math.abs(Number(value)) }}</mn></mrow></mtd>
            </mtr>
          </mtable>
          <mo stretchy="true">]</mo>
        </mrow>
      </template>
    </mrow>
  </math>
</template>

<style scoped>
.math-matrix { font-family: math; font-size: 1.25em; margin: .5em 0; color: inherit; }
</style>
