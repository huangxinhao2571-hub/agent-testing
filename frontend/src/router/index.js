import { createRouter, createWebHistory } from "vue-router";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      redirect: "/login"
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView
    },
    {
      path: "/login",
      name: "login",
      component: LoginView
    },
    {
      path: "/home",
      name: "home",
      component: HomeView
    }
  ]
});

export default router;
