<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue'
import { withBase } from 'vitepress'
import { isCoffeeModalOpen, closeCoffeeModal } from './coffee-state'

const dialog = ref(null)
const bankInfo = {
  bankName: 'Momo',
  accountName: 'MOMO - TKTH DO MINH TRI',
  accountNumber: '01MMTTT0060405229'
}
let previousFocus

watch(isCoffeeModalOpen, async open => {
  if (open) {
    previousFocus = document.activeElement
    await nextTick()
    dialog.value?.showModal()
  } else if (dialog.value?.open) {
    dialog.value.close()
    previousFocus?.focus?.()
  }
})

function hide() {
  closeCoffeeModal()
}

onUnmounted(() => {
  dialog.value?.close()
  closeCoffeeModal()
})
</script>

<template>
  <Teleport to="body">
    <dialog
      ref="dialog"
      class="coffee-dialog"
      aria-labelledby="coffee-dialog-title"
      @cancel.prevent="hide"
      @click="event => event.target === dialog && hide()"
    >
      <header>
        <div class="coffee-dialog-header">
          <img :src="withBase('/coffee-logo.svg')" alt="Logo cà phê" width="32" height="32" class="coffee-dialog-logo" />
          <h2 id="coffee-dialog-title">Buy me a coffee</h2>
        </div>
        <button class="study-button" @click="hide">Đóng</button>
      </header>
      <p>Site miễn phí. Nếu muốn ủng hộ, bạn có thể chuyển khoản theo thông tin dưới đây.</p>
      <img :src="withBase('/donate-qr.png')" alt="Mã QR chuyển khoản Momo" class="coffee-qr-img" />
      <dl>
        <dt>Ngân hàng</dt>
        <dd>{{ bankInfo.bankName }}</dd>
        <dt>Tên người nhận</dt>
        <dd>{{ bankInfo.accountName }}</dd>
        <dt>Số tài khoản</dt>
        <dd class="coffee-acc-val">{{ bankInfo.accountNumber }}</dd>
      </dl>
    </dialog>
  </Teleport>
</template>
