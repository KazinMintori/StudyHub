<script setup>
import { withBase } from 'vitepress'
import { openCoffeeModal } from './coffee-state'

defineEmits(['show-introduction'])
</script>

<template>
  <footer class="site-footer site-introduction" aria-label="Giới thiệu và liên kết website">
    <div class="site-introduction-inner">
      <div class="site-introduction-columns">
        <div class="site-introduction-brand">
          <img :src="withBase('/uet-polytechnic.png')" alt="UET Education — UET Polytechnic" class="site-introduction-logo" width="2109" height="746" loading="lazy" decoding="async" />
          <p>UETệ là không gian tự học dành cho sinh viên UET, tập hợp bài giảng theo học phần, kiến thức nền và công cụ hỗ trợ ôn tập.</p>
        </div>
        <nav class="site-introduction-column site-introduction-links" aria-labelledby="footer-about-title">
          <h2 id="footer-about-title">Giới thiệu</h2>
          <a :href="withBase('/guide/')">Hướng dẫn học</a>
          <a :href="withBase('/guide/contribute.html')">Đóng góp nội dung</a>
          <button @click="$emit('show-introduction')">Xem giới thiệu website</button>
        </nav>
        <nav class="site-introduction-column" aria-labelledby="footer-study-title">
          <h2 id="footer-study-title">Học tập</h2>
          <a :href="withBase('/#hoc-phan')">Danh sách học phần</a>
          <a :href="withBase('/wiki/')">Wiki kiến thức</a>
          <a :href="withBase('/goc-hoc-tap.html')">Góc học tập</a>
          <a :href="withBase('/goc-hoc-tap.html#flashcards')">Flashcard ôn tập</a>
          <a :href="withBase('/goc-hoc-tap.html#notes')">Sổ ghi chú</a>
        </nav>
        <section class="site-introduction-column site-introduction-support" aria-labelledby="footer-support-title">
          <h2 id="footer-support-title">Ủng hộ website</h2>
          <p>Website miễn phí. Nếu muốn ủng hộ, bạn có thể xem thông tin chuyển khoản tại đây.</p>
          <button class="coffee-footer-btn" @click="openCoffeeModal"><img :src="withBase('/coffee-logo.svg')" alt="" class="coffee-footer-icon" width="18" height="18" /><span>Buy me a coffee</span></button>
        </section>
      </div>
      <div class="site-introduction-bottom"><span>UETệ</span><span>Bài giảng · Wiki · Góc học tập</span></div>
    </div>
  </footer>
</template>

<style scoped>
.site-introduction { display: block; width: 100%; max-width: none; margin: var(--space-6) 0 0; padding: 0; border-top: 1px solid var(--rule); background: var(--canvas); position: relative; z-index: 10; }
.site-introduction-inner { max-width: 1184px; margin: 0 auto; padding: var(--space-7) var(--space-6) var(--space-5); }
.site-introduction-columns { display: grid; grid-template-columns: 1.25fr .85fr 1fr 1fr; gap: var(--space-7); }
.site-introduction-logo { display: block; width: 100%; max-width: 300px; height: auto; margin-bottom: var(--space-5); }
.site-introduction-brand p, .site-introduction-support p { color: var(--ink-2); font-size: var(--fs-ui); line-height: 1.7; }
.site-introduction-column h2 { position: relative; color: var(--ink); font-size: var(--fs-ui); font-weight: 700; text-transform: uppercase; margin: 0 0 var(--space-4); padding-bottom: var(--space-4); border-bottom: 1px solid var(--rule); }
.site-introduction-column h2::after { content: ''; position: absolute; left: 0; bottom: -1px; width: 40px; height: 2px; background: var(--tim); }
.site-introduction-column :is(a, button) { display: flex; width: fit-content; max-width: 100%; align-items: center; min-height: 44px; color: var(--ink-2); font-size: var(--fs-ui); text-align: left; }
.site-introduction-column :is(a, button):hover { color: var(--tim); text-decoration: underline; text-underline-offset: 3px; }
.site-introduction-support .coffee-footer-btn { color: var(--tim); gap: var(--space-2); margin-top: var(--space-4); }
.site-introduction-bottom { display: flex; justify-content: space-between; flex-wrap: wrap; gap: var(--space-3); border-top: 1px solid var(--rule); margin-top: var(--space-6); padding-top: var(--space-5); font-size: var(--fs-small); color: var(--ink-3); }
@media (min-width: 960px) {
  :global(.VPContent.has-sidebar ~ .site-introduction) { width: auto; margin-left: var(--vp-sidebar-width); }
  :global(.VPContent.has-sidebar ~ .site-introduction .site-introduction-columns) { gap: var(--space-5); }
}
@media (min-width: 1440px) {
  :global(.VPContent.has-sidebar ~ .site-introduction) {
    margin-left: calc((100vw - var(--vp-layout-max-width)) / 2 + var(--vp-sidebar-width));
    margin-right: calc((100vw - var(--vp-layout-max-width)) / 2);
  }
}
@media (max-width: 1199px) {
  .site-introduction-columns { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-6); }
  .site-introduction-logo { max-width: 280px; }
}
@media (max-width: 599px) {
  .site-introduction-inner { padding: var(--space-6) 20px var(--space-5); }
  .site-introduction-columns { grid-template-columns: 1fr; }
  .site-introduction-logo { max-width: 260px; }
}
</style>
