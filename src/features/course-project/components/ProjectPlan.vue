<script setup>
import plan from '../../../../src/content/courses/xu-ly-du-lieu/project/plan.json'
</script>

<template>
  <ol class="project-plan" aria-label="Các chặng thực hiện dự án độc lập">
    <li v-for="stage in plan.stages" :key="stage.id">
      <div class="plan-stage-heading"><span class="plan-stage-number">{{ stage.id }}</span><div><h3>{{ stage.title }}</h3><p>{{ stage.window }}</p></div></div>
      <p class="plan-stage-result">{{ stage.goal }}</p>
      <details>
        <summary>{{ stage.tasks.length }} việc cần làm và cách kiểm tra</summary>
        <ol class="plan-task-list">
          <li v-for="task in stage.tasks" :key="task.id">
            <h4><code>{{ task.id }}</code> {{ task.title }}</h4>
            <p>{{ task.action }}</p>
            <dl><div><dt>Bàn giao</dt><dd>{{ task.output }}</dd></div><div><dt>Đạt khi</dt><dd>{{ task.check }}</dd></div><div><dt>Làm sau</dt><dd>{{ task.after.length ? task.after.join(', ') : 'Có thể bắt đầu ngay' }}</dd></div></dl>
          </li>
        </ol>
      </details>
    </li>
  </ol>
</template>

<style scoped>
.project-plan { padding: 0; list-style: none; display: grid; gap: var(--space-4); font-family: var(--font-ui); }
.project-plan > li { border: 1px solid var(--rule); border-radius: var(--radius-lg); padding: var(--space-5); margin: 0; background: var(--paper); }
.plan-stage-heading { display: flex; align-items: center; gap: var(--space-4); }
.plan-stage-number { display: grid; place-items: center; flex: 0 0 44px; min-height: 44px; background: var(--tim-soft); color: var(--tim); font-size: var(--fs-lead); font-weight: 600; border-radius: var(--radius); }
.plan-stage-heading h3 { margin: 0; font-size: var(--fs-lead); line-height: 1.5; }
.plan-stage-heading p { margin: var(--space-1) 0 0; color: var(--ink-3); font-size: var(--fs-small); }
.plan-stage-result { font-size: var(--fs-ui); color: var(--ink-2); margin: var(--space-4) 0; }
summary { cursor: pointer; color: var(--tim); font-size: var(--fs-ui); padding: var(--space-2) 0; min-height: 44px; }
summary:focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
.plan-task-list { margin: var(--space-4) 0 0; padding: 0; list-style: none; }
.plan-task-list li { margin: var(--space-5) 0 0; padding-top: var(--space-4); border-top: 1px solid var(--rule); }
.plan-task-list h4 { font-size: var(--fs-ui); margin: 0 0 var(--space-3); line-height: 1.7; }
.plan-task-list p { font-size: var(--fs-ui); }
dl { margin: var(--space-3) 0 0; font-size: var(--fs-small); }
dl > div { display: grid; grid-template-columns: 78px minmax(0,1fr); gap: var(--space-3); margin: var(--space-2) 0; }
dt { font-weight: 600; color: var(--ink-2); }
dd { margin: 0; overflow-wrap: anywhere; }
@media(max-width:600px) { .project-plan > li { padding: var(--space-4); }dl > div { grid-template-columns: 1fr; gap: var(--space-1); } }
</style>
