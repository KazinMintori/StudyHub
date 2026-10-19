<script setup>
import cities from '../../../content/courses/xu-ly-du-lieu/project/cities.json'
</script>

<template>
  <details class="project-cities">
    <summary>Tra cứu 26 thành phố và bốn mốc chụp bắt buộc</summary>
    <div class="project-city-grid">
      <article v-for="city in cities" :key="city.dataRoot" class="project-city">
        <h4>{{ city.name }}</h4>
        <p class="project-city-region">{{ city.region }}<span v-if="city.monthly"> · Có dữ liệu hằng tháng</span></p>
        <code>{{ city.dataRoot }}</code>
        <ol aria-label="Bốn mốc chụp bắt buộc">
          <li v-for="date in city.snapshots" :key="date"><time :datetime="date">{{ date }}</time></li>
        </ol>
      </article>
    </div>
  </details>
</template>

<style scoped>
.project-cities { margin: 24px 0; border: 1px solid var(--rule); border-radius: 10px; }
.project-cities summary { padding: 16px; cursor: pointer; color: var(--ink); font-weight: 600; line-height: 1.5; }
.project-cities summary:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.project-city-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; padding: 0 14px 14px; }
.project-city { min-width: 0; padding: 16px; border: 1px solid var(--rule); border-radius: 8px; }
.project-city h4 { margin: 0 0 6px; font-size: 17px; }
.project-city p { margin: 0 0 10px; font-size: 13px; line-height: 1.5; }
.project-city-region { color: var(--ink-3); }
.project-city code { display: block; white-space: normal; overflow-wrap: anywhere; font-size: 14px; line-height: 1.65; }
.project-city ol { margin: 12px 0 0; padding-left: 22px; }
.project-city li { margin: 2px 0; font-size: 14px; font-variant-numeric: tabular-nums; }
@media (max-width: 600px) { .project-city-grid { grid-template-columns: 1fr; } }
</style>
