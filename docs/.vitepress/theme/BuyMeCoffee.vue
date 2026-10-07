<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue'
import { withBase } from 'vitepress'
import { isCoffeeModalOpen, closeCoffeeModal } from './coffee-state'
const dialog = ref(null), copied = ref(false), message = ref('')
const bankInfo = { bankName: 'VPBank (Túi Thần Tài)', accountName: 'MOMO - TKTH DO MINH TRI', accountNumber: '01MMTTT0060405229' }
let previousFocus, copyTimeout
watch(isCoffeeModalOpen, async open => { if (open) { previousFocus = document.activeElement; await nextTick(); dialog.value.showModal() } else if (dialog.value?.open) { dialog.value.close(); previousFocus?.focus?.() } })
function hide() { closeCoffeeModal() }
async function copy() { try { await navigator.clipboard.writeText(bankInfo.accountNumber); copied.value = true; clearTimeout(copyTimeout); copyTimeout = setTimeout(() => copied.value = false, 2000) } catch { message.value = 'Không thể chép tự động. Bạn có thể chọn và chép số tài khoản.' } }
onUnmounted(() => { clearTimeout(copyTimeout); dialog.value?.close(); closeCoffeeModal() })
</script>
<template><Teleport to="body"><dialog ref="dialog" class="coffee-dialog" aria-labelledby="coffee-dialog-title" @cancel.prevent="hide" @click="event => event.target === dialog && hide()"><header><h2 id="coffee-dialog-title">Ủng hộ người biên soạn</h2><button class="study-button" @click="hide">Đóng</button></header><p>Site miễn phí. Nếu muốn ủng hộ, bạn có thể chuyển khoản theo thông tin dưới đây.</p><img :src="withBase('/donate-qr.png')" alt="Mã QR chuyển khoản"><dl><dt>Ngân hàng</dt><dd>{{ bankInfo.bankName }}</dd><dt>Tên tài khoản</dt><dd>{{ bankInfo.accountName }}</dd><dt>Số tài khoản</dt><dd><span>{{ bankInfo.accountNumber }}</span><button class="study-button" @click="copy">{{ copied ? 'Đã chép' : 'Chép' }}</button></dd></dl><p v-if="copied || message" role="status">{{ message || 'Đã chép số tài khoản.' }}</p></dialog></Teleport></template>
