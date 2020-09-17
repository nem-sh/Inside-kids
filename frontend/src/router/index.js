import Vue from "vue";
import VueRouter from "vue-router";

//도연
import KidsDetailView from "@/views/parents/KidsDetailView";

//수미
import Home from "@/views/Home";
import BeforeEmailAuthView from "@/views/accounts/BeforeEmailAuthView";
import KidsManageView from "@/views/parents/KidsManageView";
import KidsMainView from "@/views/kids/KidsMainView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/auth/before",
    name: "BeforeEmailAuthView",
    component: BeforeEmailAuthView,
  },
  {
    path: "/parents/kids/manage",
    name: "KidsManageView",
    component: KidsManageView,
  },
  {
    path: "/child",
    name: "KidsMainView",
    component: KidsMainView,
  },
  {
    path: "/:kidId",
    name: "KidsDetailView",
    component: KidsDetailView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
