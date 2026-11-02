<script setup>
import { useCollections, getSourceHostname, getMaterialKindLabel, getAvailableChapterCount } from '../controllers/useCollections.js'
import { studyLink } from '../../../core/routing/links.js'
import SpotArt from '../../illustrations/components/SpotArt.vue'

const {
  query,
  selectedType,
  materialTypes,
  filteredCourses,
  totalCount,
  filteredCount,
  resetFilters,
  getStartAction
} = useCollections()
</script>

<template>
  <main class="extended-library">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn">
      <a :href="studyLink('/')">Trang chủ</a>
      <span aria-hidden="true">/</span>
      <span>Học liệu mở rộng</span>
    </nav>

    <header class="library-hero">
      <div class="library-hero-copy">
        <span class="library-eyebrow">Ngoài chương trình UET</span>
        <h1 class="library-title">Thư viện học liệu mở rộng</h1>
        <p class="library-lead">
          Sách và học phần ngoài chương trình UET, bao gồm giáo trình chuyên sâu và sách chuyên khảo phục vụ học tập và tra cứu.
        </p>
      </div>
      <div class="library-hero-art">
        <SpotArt name="tools" tone="lam" />
      </div>
    </header>

    <section class="library-toolbar" aria-label="Bộ lọc và tìm kiếm tài liệu">
      <div class="library-search-wrap">
        <label for="library-search-input" class="sr-only">Tìm kiếm tài liệu</label>
        <span class="library-search-field">
          <svg class="search-icon" viewBox="0 0 20 20" width="16" height="16" aria-hidden="true">
            <circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.8" />
            <path d="M13 13l4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
          </svg>
          <input
            id="library-search-input"
            v-model="query"
            type="search"
            placeholder="Tìm theo tên sách, tác giả hoặc từ khóa..."
          >
          <button
            v-if="query"
            type="button"
            class="search-clear-btn"
            title="Xóa tìm kiếm"
            aria-label="Xóa tìm kiếm"
            @click="query = ''"
          >
            ✕
          </button>
        </span>
      </div>

      <nav class="library-type-pills" aria-label="Phân loại tài liệu">
        <button
          v-for="t in materialTypes"
          :key="t.id"
          type="button"
          class="type-pill-btn"
          :class="{ active: selectedType === t.id }"
          :aria-pressed="selectedType === t.id"
          @click="selectedType = t.id"
        >
          {{ t.label }}
        </button>
      </nav>
    </section>

    <div class="library-status-bar" role="status" aria-live="polite" aria-atomic="true">
      <span>Hiển thị <strong>{{ filteredCount }}</strong> / {{ totalCount }} tài liệu</span>
    </div>

    <section v-if="filteredCourses.length" class="library-grid" aria-label="Danh sách tài liệu học thuật">
      <article
        v-for="course in filteredCourses"
        :key="course.id"
        class="academic-book-card"
      >
        <div class="book-card-header">
          <div class="book-badges">
            <span class="badge-kind">{{ getMaterialKindLabel(course.source?.kind) }}</span>
            <span v-if="course.source?.edition" class="badge-edition">Ấn bản {{ course.source.edition }} ({{ course.source?.year }})</span>
          </div>
          <h2 class="book-card-title">
            <a :href="studyLink(`/${course.id}/`)">{{ course.name }}</a>
          </h2>
        </div>

        <div v-if="course.source" class="book-source-panel">
          <div class="book-source-header">
            <span class="book-source-kicker">Tài liệu gốc</span>
            <a
              v-if="course.source.url"
              :href="course.source.url"
              target="_blank"
              rel="noopener noreferrer"
              class="book-source-link"
              :title="`Mở website bản gốc (${getSourceHostname(course.source.url)}) trong tab mới`"
            >
              <span>{{ getSourceHostname(course.source.url) }}</span>
              <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                <polyline points="15 3 21 3 21 9" />
                <line x1="10" y1="14" x2="21" y2="3" />
              </svg>
            </a>
          </div>
          <p class="book-original-title"><em>{{ course.source.title }}</em></p>
          <p class="book-authors">
            <strong>Tác giả:</strong> {{ Array.isArray(course.source.authors) ? course.source.authors.join(', ') : course.source.authors }}
            <template v-if="course.source.edition"> · Ấn bản {{ course.source.edition }}</template>
            <template v-if="course.source.year"> ({{ course.source.year }})</template>
            <template v-if="course.source.publisher"> · {{ course.source.publisher }}</template>
          </p>
        </div>

        <p class="book-card-summary">{{ course.description }}</p>

        <div class="book-card-meta">
          <div class="book-meta-item">
            <span class="meta-label">Đã phát hành</span>
            <span class="meta-value">{{ getAvailableChapterCount(course) }} chương</span>
          </div>
          <div v-if="course.parts" class="book-meta-item">
            <span class="meta-label">Phân chia</span>
            <span class="meta-value">{{ course.parts.length }} phần</span>
          </div>
          <div class="book-meta-item">
            <span class="meta-label">Định dạng</span>
            <span class="meta-value">Notes · Cheatsheet · Bài tập</span>
          </div>
        </div>

        <div class="book-card-actions">
          <a
            class="study-button primary book-action-btn"
            :href="studyLink(getStartAction(course).link)"
          >
            <span>{{ getStartAction(course).label }}</span>
            <span class="cta-arrow" aria-hidden="true">→</span>
          </a>
          <a
            class="study-button secondary book-action-btn"
            :href="studyLink(`/${course.id}/notes/lo-trinh`)"
          >
            <span>Lộ trình &amp; Tài liệu</span>
          </a>
          <a
            class="study-button secondary book-action-btn"
            :href="studyLink(`/${course.id}/bai-tap`)"
          >
            <span>Bài tập</span>
          </a>
        </div>
      </article>
    </section>

    <div v-else class="library-empty-state" role="status">
      <SpotArt name="empty" />
      <h2 class="empty-title">Không tìm thấy tài liệu học thuật</h2>
      <p class="empty-desc">Không có học liệu nào khớp với từ khóa "{{ query }}" hoặc bộ lọc đã chọn.</p>
      <button type="button" class="study-button primary" @click="resetFilters">
        Đặt lại bộ lọc
      </button>
    </div>
  </main>
</template>
