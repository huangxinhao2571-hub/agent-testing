<script setup>
import { useToast } from "../services/toast";

const { toastState } = useToast();
</script>

<template>
  <Transition name="toast">
    <div v-if="toastState.visible" class="toast" :data-type="toastState.type">
      <span class="toast__dot"></span>
      <span>{{ toastState.message }}</span>
    </div>
  </Transition>
</template>

<style scoped>
.toast {
  position: fixed;
  top: 22px;
  left: 50%;
  z-index: 99;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  max-width: min(520px, calc(100vw - 32px));
  padding: 13px 18px;
  border: 1px solid rgba(166, 196, 214, 0.18);
  border-radius: 14px;
  background: rgba(8, 20, 31, 0.92);
  color: #edf8ff;
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
  backdrop-filter: blur(18px);
  transform: translateX(-50%);
}

.toast__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #7bd2ff;
  box-shadow: 0 0 18px rgba(123, 210, 255, 0.64);
}

.toast[data-type="success"] .toast__dot {
  background: #35d39a;
  box-shadow: 0 0 18px rgba(53, 211, 154, 0.68);
}

.toast[data-type="error"] .toast__dot {
  background: #ff6d65;
  box-shadow: 0 0 18px rgba(255, 109, 101, 0.68);
}

.toast-enter-active,
.toast-leave-active {
  transition: opacity 180ms ease, transform 180ms ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translate(-50%, -10px);
}
</style>
