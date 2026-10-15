import { ref } from 'vue'

export const isCoffeeModalOpen = ref(false)

export function openCoffeeModal() {
  isCoffeeModalOpen.value = true
}

export function closeCoffeeModal() {
  isCoffeeModalOpen.value = false
}
