<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { withBase, useData, useRoute } from 'vitepress'
import { isCoffeeModalOpen, openCoffeeModal, closeCoffeeModal } from './coffee-state'

const { frontmatter } = useData()
const route = useRoute()

const isHome = computed(() => {
  if (frontmatter.value?.layout === 'home') return true
  const cleanPath = (route.path || '').replace(/\/index(?:\.html)?$/, '/').replace(/\/+$/, '')
  return cleanPath === '' || cleanPath === '/'
})

const dialog = ref(null)
const copiedField = ref('')
const qrImageUrl = withBase('/donate-qr.png')

const bankInfo = {
  bankName: 'VPBank (Ngân hàng TMCP Việt Nam Thịnh Vượng)',
  bankShort: 'VPBank',
  service: 'Túi Thần Tài (MoMo)',
  accountName: 'MOMO - TKTH DO MINH TRI',
  accountNumber: '01MMTTT0060405229',
  defaultMemo: 'StudyHub - Moi ca phe',
  note: 'Không giới hạn số tiền nạp • Hỗ trợ chuyển 24/7'
}

let previousFocus = null

async function copyText(text, fieldName) {
  try {
    if (navigator?.clipboard?.writeText) {
      await navigator.clipboard.writeText(text)
    } else {
      const ta = document.createElement('textarea')
      ta.value = text
      ta.style.position = 'fixed'
      ta.style.opacity = '0'
      document.body.appendChild(ta)
      ta.select()
      document.execCommand('copy')
      document.body.removeChild(ta)
    }
    copiedField.value = fieldName
    setTimeout(() => {
      if (copiedField.value === fieldName) copiedField.value = ''
    }, 2200)
  } catch (err) {
    console.error('Không thể sao chép:', err)
  }
}

function copyAllInfo() {
  const allText = `THÔNG TIN CHUYỂN KHOẢN BUY ME A COFFEE (STUDYHUB)
Ngân hàng: ${bankInfo.bankName}
Dịch vụ: ${bankInfo.service}
Chủ tài khoản: ${bankInfo.accountName}
Số tài khoản: ${bankInfo.accountNumber}
Nội dung: ${bankInfo.defaultMemo}`
  copyText(allText, 'all')
}

async function show() {
  previousFocus = document.activeElement
  await nextTick()
  if (dialog.value && !dialog.value.open) {
    dialog.value.showModal()
    document.body.style.overflow = 'hidden'
  }
}

function hide() {
  if (dialog.value && dialog.value.open) {
    dialog.value.close()
  }
  document.body.style.overflow = ''
  closeCoffeeModal()
  if (window.location.hash === '#buy-me-a-coffee') {
    history.replaceState(null, '', window.location.pathname + window.location.search)
  }
  previousFocus?.focus?.()
}

function handleBackdrop(event) {
  if (event.target === dialog.value) {
    hide()
  }
}

function handleGlobalClick(event) {
  const link = event.target.closest?.('a[href*="#buy-me-a-coffee"]')
  if (link) {
    event.preventDefault()
    openCoffeeModal()
  }
}

function checkHash() {
  if (window.location.hash === '#buy-me-a-coffee') {
    openCoffeeModal()
  }
}

watch(isCoffeeModalOpen, (isOpen) => {
  if (isOpen) show()
  else hide()
})

onMounted(() => {
  document.addEventListener('click', handleGlobalClick, true)
  window.addEventListener('hashchange', checkHash)
  window.addEventListener('open-coffee-modal', openCoffeeModal)
  checkHash()
})

onUnmounted(() => {
  document.removeEventListener('click', handleGlobalClick, true)
  window.removeEventListener('hashchange', checkHash)
  window.removeEventListener('open-coffee-modal', openCoffeeModal)
  document.body.style.overflow = ''
})
</script>

<template>
  <div v-if="isHome" class="coffee-hub-wrapper">
    <!-- Floating Buy Me a Coffee Action Button -->
    <aside class="coffee-widget-container" aria-label="Khu vực ủng hộ Buy Me a Coffee">
    <button
      type="button"
      class="coffee-float-btn"
      aria-label="Buy me a coffee - Mời tác giả một ly cà phê"
      @click="openCoffeeModal"
    >
      <span class="coffee-icon-wrapper" aria-hidden="true">
        <svg viewBox="0 0 24 24" class="coffee-cup-svg" fill="none">
          <!-- Steam lines -->
          <path d="M7 2c0 1.2.6 1.8.6 2.6 0 .8-.6 1.4-.6 2.4M12 2c0 1.2.6 1.8.6 2.6 0 .8-.6 1.4-.6 2.4M17 2c0 1.2.6 1.8.6 2.6 0 .8-.6 1.4-.6 2.4" stroke="#d97706" stroke-width="1.8" stroke-linecap="round" />
          <!-- Cup body -->
          <path d="M4 8h13a1 1 0 0 1 1 1v6a6 6 0 0 1-6 6H9a6 6 0 0 1-5-6V9a1 1 0 0 1 1-1z" fill="#ffdd00" stroke="#1f2937" stroke-width="1.8" />
          <!-- Cup handle -->
          <path d="M18 10h1.8a2.8 2.8 0 0 1 0 5.6H18" stroke="#1f2937" stroke-width="1.8" stroke-linecap="round" />
          <!-- Heart in cup -->
          <path d="M10.5 13.2c-.8-.8-1.8-.1-1.8.8 0 1.2 1.8 2.4 1.8 2.4s1.8-1.2 1.8-2.4c0-.9-1-1.6-1.8-.8z" fill="#ef4444" />
        </svg>
      </span>
      <span class="coffee-float-text">Buy me a coffee</span>
      <span class="coffee-float-badge">☕</span>
    </button>
  </aside>

  <!-- Modal Dialog -->
  <dialog
    ref="dialog"
    class="coffee-modal"
    aria-labelledby="coffee-dialog-title"
    @cancel.prevent="hide"
    @click="handleBackdrop"
  >
    <div class="coffee-modal-inner">
      <!-- Modal Header -->
      <header class="coffee-modal-header">
        <div class="coffee-header-info">
          <div class="coffee-avatar" aria-hidden="true">
            <svg viewBox="0 0 48 48" class="coffee-modal-logo" fill="none">
              <!-- Steam -->
              <path d="M15 10c0-3 2.5-4 2.5-7M24 9c0-3 2.5-4 2.5-7M33 10c0-3 2.5-4 2.5-7" stroke="#f59e0b" stroke-width="2.6" stroke-linecap="round" />
              <!-- Cup body -->
              <path d="M8 15h26v16c0 6-4.5 10-10 10h-6c-5.5 0-10-4-10-10V15z" fill="#ffdd00" stroke="#111827" stroke-width="2.6" stroke-linejoin="round" />
              <path d="M8 19h26" stroke="#d97706" stroke-width="2.2" stroke-linecap="round" />
              <!-- Handle -->
              <path d="M34 19h4.5a5.5 5.5 0 0 1 0 11H34" stroke="#111827" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" />
              <!-- Heart -->
              <path d="M21 27.5c-1.5-1.5-3.5-.2-3.5 1.5 0 2.2 3.5 4.5 3.5 4.5s3.5-2.3 3.5-4.5c0-1.7-2-3-3.5-1.5z" fill="#ef4444" />
              <!-- Saucer -->
              <path d="M6 44h30" stroke="#111827" stroke-width="2.6" stroke-linecap="round" />
            </svg>
          </div>
          <div>
            <div class="coffee-badge-pill">Ủng hộ tác giả 💛</div>
            <h2 id="coffee-dialog-title" class="coffee-modal-title">Buy Me a Coffee</h2>
            <p class="coffee-modal-subtitle">Tiếp thêm năng lượng để StudyHub duy trì bài giảng & tài liệu ôn tập chất lượng cao</p>
          </div>
        </div>
        <button type="button" class="coffee-close-btn" aria-label="Đóng cửa sổ" @click="hide">
          <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </header>

      <!-- Modal Body -->
      <div class="coffee-modal-body">
        <!-- QR Code Section -->
        <div class="coffee-qr-column">
          <div class="coffee-qr-card">
            <div class="coffee-qr-badge">
              <span class="qr-dot"></span>
              <span>Quét mã VietQR / Napas 247</span>
            </div>
            <div class="coffee-qr-frame">
              <img
                :src="qrImageUrl"
                alt="Mã QR chuyển khoản Túi Thần Tài VPBank"
                class="coffee-qr-image"
                loading="eager"
              />
            </div>
            <div class="coffee-qr-footer">
              <span class="qr-subtext">Hỗ trợ tất cả ứng dụng Ngân hàng & MoMo</span>
              <a
                :href="qrImageUrl"
                download="StudyHub-VietQR-DoMinhTri.png"
                class="coffee-btn-secondary download-btn"
                title="Tải ảnh mã QR về máy để quét trong app"
              >
                <svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                  <polyline points="7 10 12 15 17 10" />
                  <line x1="12" y1="15" x2="12" y2="3" />
                </svg>
                <span>Tải ảnh mã QR</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Banking Information Section -->
        <div class="coffee-info-column">
          <div class="coffee-info-list">
            <!-- Bank item -->
            <div class="coffee-info-row">
              <div class="coffee-info-meta">
                <span class="coffee-label">Ngân hàng</span>
                <span class="coffee-value-highlight">{{ bankInfo.bankShort }}</span>
                <span class="coffee-sublabel">{{ bankInfo.bankName }}</span>
              </div>
              <span class="coffee-chip-tag">{{ bankInfo.service }}</span>
            </div>

            <!-- Account name item -->
            <div class="coffee-info-row">
              <div class="coffee-info-meta">
                <span class="coffee-label">Tên người nhận (Chủ TK)</span>
                <span class="coffee-value text-bold">{{ bankInfo.accountName }}</span>
              </div>
              <button
                type="button"
                class="coffee-copy-btn"
                :class="{ copied: copiedField === 'name' }"
                @click="copyText(bankInfo.accountName, 'name')"
              >
                <span v-if="copiedField === 'name'">✓ Đã chép</span>
                <span v-else>Sao chép</span>
              </button>
            </div>

            <!-- Account number item -->
            <div class="coffee-info-row highlight-box">
              <div class="coffee-info-meta">
                <span class="coffee-label">Số tài khoản chuyển khoản</span>
                <span class="coffee-account-number">{{ bankInfo.accountNumber }}</span>
                <span class="coffee-small-hint">Mã chuyển khoản vào Túi Thần Tài</span>
              </div>
              <button
                type="button"
                class="coffee-copy-btn primary"
                :class="{ copied: copiedField === 'acc' }"
                @click="copyText(bankInfo.accountNumber, 'acc')"
              >
                <span v-if="copiedField === 'acc'">✓ Đã sao chép!</span>
                <span v-else>
                  <svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
                  </svg>
                  <span>Sao chép STK</span>
                </span>
              </button>
            </div>

            <!-- Memo item -->
            <div class="coffee-info-row">
              <div class="coffee-info-meta">
                <span class="coffee-label">Nội dung chuyển khoản (gợi ý)</span>
                <span class="coffee-value code-font">{{ bankInfo.defaultMemo }}</span>
              </div>
              <button
                type="button"
                class="coffee-copy-btn"
                :class="{ copied: copiedField === 'memo' }"
                @click="copyText(bankInfo.defaultMemo, 'memo')"
              >
                <span v-if="copiedField === 'memo'">✓ Đã chép</span>
                <span v-else>Sao chép</span>
              </button>
            </div>
          </div>

          <!-- Quick Tip / Friendly Message -->
          <div class="coffee-gratitude-card">
            <div class="gratitude-icon">💝</div>
            <p class="gratitude-text">
              <strong>Cảm ơn bạn rất nhiều!</strong> Dù là 1 ly trà đá 10k, ly cà phê 25k hay chỉ là một lời nhắn, sự đồng hành của bạn đều là nguồn động lực quý giá để StudyHub ngày một hoàn thiện hơn.
            </p>
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <footer class="coffee-modal-footer">
        <button
          type="button"
          class="coffee-btn-secondary"
          :class="{ copied: copiedField === 'all' }"
          @click="copyAllInfo"
        >
          <span v-if="copiedField === 'all'">✓ Đã sao chép tất cả thông tin</span>
          <span v-else>📋 Sao chép toàn bộ thông tin</span>
        </button>
        <button type="button" class="study-button primary coffee-done-btn" @click="hide">
          Hoàn tất / Đóng
        </button>
      </footer>
    </div>
  </dialog>
  </div>
</template>

<style scoped>
/* Floating Widget Button */
.coffee-widget-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 800;
  display: block;
}

.coffee-float-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  height: 46px;
  padding: 0 18px 0 12px;
  border-radius: 9999px;
  background: #ffdd00;
  color: #1e232a;
  border: 1.5px solid #ebb800;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16), 0 2px 6px rgba(0, 0, 0, 0.08);
  font-family: var(--vp-font-family-base, sans-serif);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: -0.2px;
  cursor: pointer;
  transition: transform 0.22s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.22s ease, background-color 0.2s;
  user-select: none;
}

.coffee-float-btn:hover {
  transform: translateY(-3px) scale(1.02);
  background: #ffe326;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.22), 0 4px 10px rgba(0, 0, 0, 0.1);
}

.coffee-float-btn:active {
  transform: translateY(0) scale(0.98);
}

.coffee-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
}

.coffee-cup-svg {
  width: 24px;
  height: 24px;
}

.coffee-float-text {
  font-weight: 700;
  color: #1a1e24;
}

.coffee-float-badge {
  font-size: 14px;
  line-height: 1;
}

/* Modal Styling */
.coffee-modal {
  width: min(840px, 94vw);
  max-width: 94vw;
  max-height: 92vh;
  margin: auto;
  padding: 0;
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
  overflow: hidden;
}

.coffee-modal::backdrop {
  background: rgba(15, 23, 42, 0.72);
  backdrop-filter: blur(4px);
}

.coffee-modal-inner {
  display: flex;
  flex-direction: column;
  max-height: 92vh;
  overflow-y: auto;
}

/* Header */
.coffee-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 24px 28px 20px;
  border-bottom: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}

.coffee-header-info {
  display: flex;
  align-items: center;
  gap: 18px;
}

.coffee-avatar {
  flex-shrink: 0;
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: #fff8d6;
  border: 1px solid #ffdd00;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(255, 221, 0, 0.25);
}

.coffee-modal-logo {
  width: 38px;
  height: 38px;
}

.coffee-badge-pill {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  color: #b45309;
  background: #fef3c7;
  padding: 2px 10px;
  border-radius: 999px;
  margin-bottom: 4px;
}

.dark .coffee-badge-pill {
  color: #fef08a;
  background: #78350f44;
}

.coffee-modal-title {
  font-size: 22px;
  font-weight: 750;
  line-height: 1.25;
  margin: 0;
  letter-spacing: -0.5px;
}

.coffee-modal-subtitle {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 4px 0 0;
  line-height: 1.5;
}

.coffee-close-btn {
  background: transparent;
  border: none;
  color: var(--vp-c-text-2);
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.15s, color 0.15s;
}

.coffee-close-btn:hover {
  background: var(--vp-c-bg-alt);
  color: var(--vp-c-text-1);
}

/* Body */
.coffee-modal-body {
  display: grid;
  grid-template-columns: 310px 1fr;
  gap: 26px;
  padding: 24px 28px;
  align-items: start;
}

/* QR Code Column */
.coffee-qr-column {
  display: flex;
  flex-direction: column;
}

.coffee-qr-card {
  background: var(--study-card);
  border: 1px solid var(--vp-c-border);
  border-radius: 14px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.coffee-qr-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 600;
  color: #059669;
  margin-bottom: 12px;
}

.qr-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.coffee-qr-frame {
  width: 100%;
  max-width: 260px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  background: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
}

.coffee-qr-image {
  display: block;
  width: 100%;
  height: auto;
  object-fit: contain;
}

.coffee-qr-footer {
  width: 100%;
  margin-top: 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}

.qr-subtext {
  font-size: 11px;
  color: var(--vp-c-text-3);
  text-align: center;
}

.download-btn {
  width: 100%;
  font-size: 12px;
  text-decoration: none !important;
}

/* Info Column */
.coffee-info-column {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.coffee-info-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.coffee-info-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 12px 16px;
  border-radius: 10px;
  background: var(--study-card);
  border: 1px solid var(--vp-c-divider);
  transition: border-color 0.18s;
}

.coffee-info-row:hover {
  border-color: var(--vp-c-border);
}

.coffee-info-row.highlight-box {
  background: var(--study-blue-soft);
  border-color: var(--vp-c-brand-1);
  padding: 14px 18px;
}

.coffee-info-meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.coffee-label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--vp-c-text-3);
}

.coffee-value {
  font-size: 14px;
  color: var(--vp-c-text-1);
}

.coffee-value-highlight {
  font-size: 16px;
  font-weight: 700;
  color: var(--vp-c-brand-1);
}

.coffee-sublabel {
  font-size: 11.5px;
  color: var(--vp-c-text-2);
}

.coffee-account-number {
  font-family: var(--vp-font-family-mono, monospace);
  font-size: 19px;
  font-weight: 750;
  letter-spacing: 0.5px;
  color: var(--vp-c-brand-1);
}

.coffee-small-hint {
  font-size: 11px;
  color: var(--vp-c-text-2);
  margin-top: 2px;
}

.coffee-chip-tag {
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
  white-space: nowrap;
}

.text-bold {
  font-weight: 650;
}

.code-font {
  font-family: var(--vp-font-family-mono, monospace);
  font-weight: 600;
  font-size: 13.5px;
}

/* Copy Buttons */
.coffee-copy-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 34px;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-border);
  cursor: pointer;
  transition: all 0.16s ease;
  white-space: nowrap;
}

.coffee-copy-btn:hover {
  background: var(--vp-c-bg-alt);
  border-color: var(--vp-c-text-2);
}

.coffee-copy-btn.primary {
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  color: #fff;
  min-height: 38px;
  padding: 8px 16px;
  font-size: 13px;
}

.coffee-copy-btn.primary:hover {
  background: var(--vp-c-brand-2);
  border-color: var(--vp-c-brand-2);
}

.coffee-copy-btn.copied {
  background: #059669 !important;
  border-color: #059669 !important;
  color: #ffffff !important;
}

/* Gratitude Card */
.coffee-gratitude-card {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 16px;
  background: var(--vp-c-bg-soft);
  border-radius: 10px;
  border: 1px dashed var(--vp-c-border);
}

.gratitude-icon {
  font-size: 20px;
  line-height: 1.2;
}

.gratitude-text {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0;
}

.gratitude-text strong {
  color: var(--vp-c-text-1);
}

/* Modal Footer */
.coffee-modal-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  padding: 18px 28px;
  background: var(--vp-c-bg-soft);
  border-top: 1px solid var(--vp-c-divider);
}

.coffee-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 40px;
  padding: 8px 16px;
  font-size: 12.5px;
  font-weight: 550;
  border: 1px solid var(--vp-c-border);
  border-radius: 6px;
  background: var(--study-card);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.16s ease;
}

.coffee-btn-secondary:hover {
  background: var(--vp-c-bg-alt);
  border-color: var(--vp-c-text-2);
}

.coffee-btn-secondary.copied {
  background: #059669;
  border-color: #059669;
  color: #fff;
}

.coffee-done-btn {
  min-height: 40px;
}

/* Responsive */
@media (max-width: 720px) {
  .coffee-modal-body {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 18px 20px;
  }

  .coffee-modal-header {
    padding: 18px 20px 16px;
  }

  .coffee-modal-footer {
    padding: 16px 20px;
    flex-direction: column-reverse;
  }

  .coffee-btn-secondary,
  .coffee-done-btn {
    width: 100%;
  }

  .coffee-float-btn {
    height: 42px;
    padding: 0 14px 0 10px;
    font-size: 12.5px;
  }

  .coffee-widget-container {
    bottom: 18px;
    right: 18px;
  }
}
</style>
