export const STORAGE_UNAVAILABLE_MESSAGE = 'Trình duyệt không cho phép lưu. Bạn có thể tải ghi chú để giữ lại dữ liệu.'

export function getStorage(customStorage) {
  if (customStorage !== undefined) return customStorage
  try {
    if (typeof window !== 'undefined' && window.localStorage) return window.localStorage
    if (typeof localStorage !== 'undefined') return localStorage
  } catch { /* Access itself can be denied before getItem is called. */ }
  return null
}

export function readJson(key, fallback, storage = getStorage()) {
  try {
    if (!storage) return fallback
    const value = storage.getItem(key)
    return value === null ? fallback : JSON.parse(value)
  } catch {
    return fallback
  }
}

export function writeJson(key, value, storage = getStorage()) {
  try {
    if (!storage) throw new Error('Storage is not available')
    storage.setItem(key, JSON.stringify(value))
    return { success: true, error: null }
  } catch (error) {
    return { success: false, error }
  }
}

export function readStored(key, fallback, storage = getStorage()) {
  return readJson(key, fallback, storage)
}

export function writeStored(key, value, storage = getStorage()) {
  const result = writeJson(key, value, storage)
  return result.success
}

export function createStorageAdapter(storage = getStorage()) {
  return {
    read(key, fallback) {
      return readJson(key, fallback, storage)
    },
    write(key, value) {
      return writeJson(key, value, storage)
    }
  }
}
