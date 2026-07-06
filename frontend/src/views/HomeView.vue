<script setup>
import { reactive, ref } from "vue";
import { createProject } from "../services/project";
import { useToast } from "../services/toast";

const toast = useToast();
const isSubmitting = ref(false);
const createdProjects = ref([]);

const form = reactive({
  project_name: "",
  project_describe: "",
  project_password: ""
});

async function handleCreateProject() {
  if (isSubmitting.value) {
    return;
  }

  if (!form.project_name.trim() || !form.project_describe.trim() || !form.project_password.trim()) {
    toast.error("请填写项目名称、描述和密码");
    return;
  }

  isSubmitting.value = true;

  try {
    const result = await createProject({
      project_name: form.project_name.trim(),
      project_describe: form.project_describe.trim(),
      project_password: form.project_password.trim()
    });

    if (result?.status) {
      toast.success(result.msg || "创建成功");
      createdProjects.value.unshift(result.data);
      form.project_name = "";
      form.project_describe = "";
      form.project_password = "";
      return;
    }

    toast.error(result?.msg || "创建项目失败");
  } catch (error) {
    toast.error(error.message || "创建项目接口调用失败");
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<template>
  <main class="home-page">
    <header class="topbar">
      <div>
        <span class="eyebrow">Project Workspace</span>
        <h1>项目管理</h1>
      </div>
    </header>

    <section class="workspace-grid">
      <form class="panel project-form" @submit.prevent="handleCreateProject">
        <div class="panel__header">
          <span>Create</span>
          <strong>新建项目</strong>
        </div>

        <label>
          项目名称
          <input v-model="form.project_name" maxlength="10" type="text" placeholder="最多 10 位" />
        </label>

        <label>
          项目描述
          <textarea v-model="form.project_describe" maxlength="100" rows="5" placeholder="最多 100 位"></textarea>
        </label>

        <label>
          项目密码
          <input v-model="form.project_password" maxlength="8" type="password" placeholder="最多 8 位" />
        </label>

        <button type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? "创建中..." : "创建项目" }}
        </button>
      </form>

      <section class="panel project-list">
        <div class="panel__header">
          <span>Created</span>
          <strong>刚创建的项目</strong>
        </div>

        <div v-if="createdProjects.length" class="project-items">
          <article v-for="project in createdProjects" :key="project.project_id" class="project-item">
            <div>
              <strong>{{ project.project_name }}</strong>
              <span>ID: {{ project.project_id }}</span>
            </div>
            <p>{{ project.project_describe }}</p>
          </article>
        </div>

        <div v-else class="empty-state">
          <strong>暂无项目</strong>
          <span>创建成功后会显示在这里。</span>
        </div>
      </section>
    </section>
  </main>
</template>

<style scoped>
.home-page {
  min-height: 100vh;
  padding: 28px clamp(18px, 4vw, 54px) 42px;
  background:
    linear-gradient(120deg, rgba(7, 19, 30, 0.96), rgba(8, 26, 39, 0.98)),
    linear-gradient(90deg, rgba(116, 188, 224, 0.08) 1px, transparent 1px),
    linear-gradient(rgba(116, 188, 224, 0.08) 1px, transparent 1px);
  background-size: auto, 54px 54px, 54px 54px;
  color: #eaf7ff;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 22px;
}

.eyebrow,
.panel__header span {
  color: #7bd2ff;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

h1,
p {
  margin: 0;
}

h1 {
  margin-top: 8px;
  font-size: clamp(2rem, 4vw, 3.4rem);
  line-height: 1;
}

.workspace-grid {
  display: grid;
  grid-template-columns: minmax(320px, 440px) minmax(0, 1fr);
  gap: 16px;
  margin-top: 28px;
}

.panel {
  border: 1px solid rgba(145, 196, 224, 0.14);
  border-radius: 8px;
  background: rgba(8, 22, 34, 0.72);
  box-shadow: 0 28px 90px rgba(0, 0, 0, 0.22);
}

.project-form,
.project-list {
  padding: 24px;
}

.project-form {
  display: grid;
  gap: 18px;
}

.panel__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 4px;
}

.panel__header strong {
  color: #f5fbff;
  font-size: 1.4rem;
}

label {
  display: grid;
  gap: 8px;
  color: #b8d7ea;
  font-size: 0.94rem;
}

input,
textarea {
  width: 100%;
  padding: 0 14px;
  border: 1px solid rgba(135, 180, 207, 0.18);
  border-radius: 8px;
  outline: none;
  background: rgba(4, 15, 24, 0.82);
  color: #effaff;
  font: inherit;
  transition: border-color 160ms ease, box-shadow 160ms ease;
}

input {
  height: 48px;
}

textarea {
  min-height: 120px;
  padding-top: 12px;
  resize: vertical;
}

input:focus,
textarea:focus {
  border-color: #7bd2ff;
  box-shadow: 0 0 0 4px rgba(123, 210, 255, 0.12);
}

button {
  height: 50px;
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

.project-items {
  display: grid;
  gap: 14px;
  margin-top: 22px;
}

.project-item {
  display: grid;
  gap: 12px;
  padding: 16px;
  border: 1px solid rgba(145, 196, 224, 0.12);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.035);
}

.project-item div {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.project-item strong {
  color: #f3fbff;
}

.project-item span,
.project-item p,
.empty-state span {
  color: rgba(210, 232, 245, 0.66);
}

.project-item p {
  line-height: 1.7;
}

.empty-state {
  display: grid;
  place-items: center;
  min-height: 260px;
  gap: 8px;
  color: #f3fbff;
  text-align: center;
}

@media (max-width: 860px) {
  .workspace-grid {
    grid-template-columns: 1fr;
  }
}
</style>
