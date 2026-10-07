import { ref } from 'vue'

export const storageMessage = ref('')
export function readStored(key, fallback) {
  try { const value = localStorage.getItem(key); return value === null ? fallback : JSON.parse(value) }
  catch { return fallback }
}
export function writeStored(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); storageMessage.value = ''; return true }
  catch { storageMessage.value = 'Trình duyệt không cho phép lưu. Bạn có thể tải ghi chú để giữ lại dữ liệu.'; return false }
}
