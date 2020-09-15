import Vue from "vue";
import VueRouter from "vue-router";

//도연
import KidsDetailView from "@/views/parents/KidsDetailView";

//수미
import Home from "@/views/Home";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
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
