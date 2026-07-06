import { reactive } from "vue";

const toastState = reactive({
  visible: false,
  type: "info",
  message: "",
  timer: null
});

function showToast(message, type = "info") {
  if (toastState.timer) {
    window.clearTimeout(toastState.timer);
  }

  toastState.type = type;
  toastState.message = message;
  toastState.visible = true;
  toastState.timer = window.setTimeout(() => {
    toastState.visible = false;
  }, 2600);
}

export function useToast() {
  return {
    toastState,
    success: (message) => showToast(message, "success"),
    error: (message) => showToast(message, "error"),
    info: (message) => showToast(message, "info")
  };
}
