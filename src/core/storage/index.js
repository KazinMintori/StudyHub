import { ref } from 'vue'
import {
  readJson,
  writeJson,
  getStorage,
  createStorageAdapter,
  STORAGE_UNAVAILABLE_MESSAGE
} from './local-storage.js'

export const storageMessage = ref('')

export function readStored(key, fallback, storage = getStorage()) {
  return readJson(key, fallback, storage)
}

export function writeStored(key, value, storage = getStorage()) {
  const result = writeJson(key, value, storage)
  if (result.success) {
    storageMessage.value = ''
    return true
  }
  storageMessage.value = STORAGE_UNAVAILABLE_MESSAGE
  return false
}

export {
  readJson,
  writeJson,
  getStorage,
  createStorageAdapter,
  STORAGE_UNAVAILABLE_MESSAGE
}
