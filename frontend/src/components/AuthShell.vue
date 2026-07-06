<script setup>
defineProps({
  mode: {
    type: String,
    default: "login"
  },
  eyebrow: {
    type: String,
    default: "AI Automation"
  },
  title: {
    type: String,
    default: ""
  },
  subtitle: {
    type: String,
    default: ""
  }
});

const pipelineItems = ["需求解析", "用例生成", "自动执行", "智能报告"];
</script>

<template>
  <main class="auth-shell" :data-mode="mode">
    <section class="auth-hero">
      <nav class="auth-nav">
        <span class="brand-mark">T</span>
        <span>Teamhelper AI Test</span>
      </nav>

      <div class="hero-copy">
        <p>{{ eyebrow }}</p>
        <h1>{{ title }}</h1>
        <span>{{ subtitle }}</span>
      </div>

      <div class="pipeline" aria-label="AI automation pipeline">
        <div v-for="(item, index) in pipelineItems" :key="item" class="pipeline__item">
          <span>{{ index + 1 }}</span>
          <strong>{{ item }}</strong>
        </div>
      </div>
    </section>

    <section class="auth-panel">
      <slot />
    </section>
  </main>
</template>

<style scoped>
.auth-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(380px, 500px);
  overflow: hidden;
  background:
    linear-gradient(120deg, rgba(10, 31, 47, 0.94), rgba(6, 15, 24, 0.98)),
    repeating-linear-gradient(90deg, rgba(124, 185, 217, 0.06) 0 1px, transparent 1px 72px);
}

.auth-hero {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 34px clamp(28px, 6vw, 76px);
}

.auth-hero::before {
  content: "";
  position: absolute;
  inset: 12% 8% auto auto;
  width: 34vw;
  max-width: 520px;
  aspect-ratio: 1;
  border: 1px solid rgba(124, 210, 255, 0.2);
  border-radius: 50%;
  background:
    linear-gradient(90deg, transparent 48%, rgba(124, 210, 255, 0.22) 49% 51%, transparent 52%),
    linear-gradient(0deg, transparent 48%, rgba(124, 210, 255, 0.22) 49% 51%, transparent 52%);
  filter: drop-shadow(0 0 42px rgba(72, 183, 255, 0.16));
  animation: scanSpin 18s linear infinite;
}

.auth-hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(137, 190, 220, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(137, 190, 220, 0.08) 1px, transparent 1px);
  background-size: 52px 52px;
  mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0.8), transparent 82%);
  pointer-events: none;
}

.auth-nav,
.hero-copy,
.pipeline {
  position: relative;
  z-index: 1;
}

.auth-nav {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  width: fit-content;
  color: #d9f3ff;
  font-weight: 700;
}

.brand-mark {
  display: inline-grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: linear-gradient(135deg, #31c8ff, #35d39a);
  color: #04111a;
}

.hero-copy {
  max-width: 660px;
  animation: floatIn 520ms ease both;
}

.hero-copy p {
  margin: 0 0 18px;
  color: #7bd2ff;
  font-size: 0.88rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.hero-copy h1 {
  max-width: 12ch;
  margin: 0;
  color: #f5fbff;
  font-size: clamp(3.4rem, 7vw, 6.6rem);
  line-height: 0.94;
}

.hero-copy span {
  display: block;
  max-width: 560px;
  margin-top: 22px;
  color: rgba(214, 235, 247, 0.72);
  font-size: 1.04rem;
  line-height: 1.9;
}

.pipeline {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  max-width: 760px;
}

.pipeline__item {
  min-height: 112px;
  padding: 18px;
  border: 1px solid rgba(145, 196, 224, 0.14);
  border-radius: 8px;
  background: rgba(8, 23, 35, 0.68);
  backdrop-filter: blur(14px);
  animation: riseIn 520ms ease both;
}

.pipeline__item:nth-child(2) {
  animation-delay: 80ms;
}

.pipeline__item:nth-child(3) {
  animation-delay: 160ms;
}

.pipeline__item:nth-child(4) {
  animation-delay: 240ms;
}

.pipeline__item span {
  color: #35d39a;
  font-weight: 800;
}

.pipeline__item strong {
  display: block;
  margin-top: 22px;
  color: #e9f7ff;
  font-size: 1.05rem;
}

.auth-panel {
  display: grid;
  place-items: center;
  padding: 28px;
  background: rgba(4, 12, 19, 0.42);
  border-left: 1px solid rgba(149, 197, 224, 0.12);
}

@keyframes floatIn {
  from {
    opacity: 0;
    transform: translateY(18px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes riseIn {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scanSpin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 980px) {
  .auth-shell {
    grid-template-columns: 1fr;
  }

  .auth-hero {
    min-height: 58vh;
    gap: 44px;
  }

  .auth-panel {
    border-left: 0;
  }
}

@media (max-width: 680px) {
  .auth-hero {
    padding: 26px 20px;
  }

  .pipeline {
    grid-template-columns: 1fr 1fr;
  }

  .pipeline__item {
    min-height: 92px;
  }
}
</style>
