import Vue from "vue";
import VueRouter from "vue-router";

//도연
import KidsDetailView from "@/views/parents/KidsDetailView";
import KidsTalkingView from "@/views/kids/KidsTalkingView";
import KidsPictureView from "@/views/kids/KidsPictureView";
import KidsDrawingView from "@/views/kids/KidsDrawingView";

//수미
import Home from "@/views/Home";
import BeforeEmailAuthView from "@/views/accounts/BeforeEmailAuthView";
import KidsManageView from "@/views/parents/KidsManageView";
import KidsMainView from "@/views/kids/KidsMainView";
import KidsDrawingListView from "@/views/kids/KidsDrawingListView";
import KidsLoginView from "@/views/kids/KidsLoginView";

//시성
import KidMusicView from "@/views/kids/KidMusicView";

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
    path: "/child/talking",
    name: "KidsTalkingView",
    component: KidsTalkingView,
  },
  {
    path: "/child/picture",
    name: "KidsPictureView",
    component: KidsPictureView,
  },
  {
    path: "/child/:kidId/drawing",
    name: "KidsDrawingView",
    component: KidsDrawingView,
  },
  {
    path: "/child/:kidId/drawing/list",
    name: "KidsDrawingListView",
    component: KidsDrawingListView,
  },
  {
    path: "/child",
    name: "KidsLoginView",
    component: KidsLoginView,
  },
  {
    path: "/child/:kidId",
    name: "KidsMainView",
    component: KidsMainView,
  },
  {
    path: "/child/:kidId/music",
    name: "KidMusicView",
    component: KidMusicView,
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
