<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import AuthShell from "../components/AuthShell.vue";
import { loginUser } from "../services/auth";
import { useToast } from "../services/toast";

const router = useRouter();
const toast = useToast();
const form = reactive({
  username: "",
  password: ""
});

const isSubmitting = ref(false);

async function handleSubmit() {
  if (isSubmitting.value) {
    return;
  }

  if (!form.username.trim() || !form.password.trim()) {
    toast.error("请输入手机号和密码");
    return;
  }

  isSubmitting.value = true;

  try {
    const result = await loginUser({
      username: form.username.trim(),
      password: form.password.trim()
    });

    if (result?.status) {
      const token = result?.data?.token;
      if (token) {
        localStorage.setItem("teamhelper_token", token);
      }

      toast.success(result.msg || "登录成功");
      await router.push("/home");
      return;
    }

    toast.error(result?.msg || "登录失败，请检查账号密码");
  } catch (error) {
    toast.error(error.message || "登录接口调用失败");
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<template>
  <AuthShell
    mode="login"
    eyebrow="AI Automation Login"
    title="进入智能测试驾驶舱"
    subtitle="登录后查看任务编排、AI 用例生成、接口执行和回归质量报告。"
  >
    <form class="auth-card" @submit.prevent="handleSubmit">
      <div class="auth-card__header">
        <span>Access</span>
        <h2>登录平台</h2>
        <p>连接你的自动化测试任务流，继续推进质量交付。</p>
      </div>

      <label>
        手机号
        <input v-model="form.username" type="text" maxlength="11" placeholder="请输入注册手机号" />
      </label>

      <label>
        密码
        <input v-model="form.password" type="password" maxlength="10" placeholder="请输入登录密码" />
      </label>

      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? "登录中..." : "进入首页" }}
      </button>

      <router-link to="/register">还没有账号，立即注册</router-link>
    </form>
  </AuthShell>
</template>

<style scoped>
.auth-card {
  width: min(100%, 420px);
  display: grid;
  gap: 18px;
  padding: 30px;
  border: 1px solid rgba(154, 198, 224, 0.16);
  border-radius: 8px;
  background: rgba(8, 22, 33, 0.86);
  box-shadow: 0 30px 90px rgba(0, 0, 0, 0.32);
  backdrop-filter: blur(22px);
  animation: cardIn 420ms ease both;
}

.auth-card__header {
  margin-bottom: 8px;
}

.auth-card__header span {
  color: #7bd2ff;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.auth-card__header h2 {
  margin: 10px 0 8px;
  color: #f5fbff;
  font-size: 2rem;
}

.auth-card__header p {
  margin: 0;
  color: rgba(210, 232, 245, 0.68);
  line-height: 1.7;
}

label {
  display: grid;
  gap: 8px;
  color: #b8d7ea;
  font-size: 0.94rem;
}

input {
  width: 100%;
  height: 48px;
  padding: 0 14px;
  border: 1px solid rgba(135, 180, 207, 0.18);
  border-radius: 8px;
  outline: none;
  background: rgba(4, 15, 24, 0.82);
  color: #effaff;
  transition: border-color 160ms ease, box-shadow 160ms ease, transform 160ms ease;
}

input:focus {
  border-color: #7bd2ff;
  box-shadow: 0 0 0 4px rgba(123, 210, 255, 0.12);
  transform: translateY(-1px);
}

button {
  height: 50px;
  margin-top: 6px;
  border: 0;
  border-radius: 8px;
  background: linear-gradient(135deg, #7bd2ff, #35d39a);
  color: #03111a;
  font-weight: 800;
  cursor: pointer;
  transition: transform 160ms ease, opacity 160ms ease, box-shadow 160ms ease;
  box-shadow: 0 18px 38px rgba(53, 211, 154, 0.18);
}

button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 22px 46px rgba(53, 211, 154, 0.24);
}

button:disabled {
  cursor: wait;
  opacity: 0.72;
}

a {
  width: fit-content;
  color: #8bdcff;
  font-weight: 700;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

@keyframes cardIn {
  from {
    opacity: 0;
    transform: translateX(18px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
