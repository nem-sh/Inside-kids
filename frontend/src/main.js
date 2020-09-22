import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueCookies from "vue-cookies";

Vue.config.productionTip = false;
Vue.use(VueCookies);

window.Kakao.init("a34e5d49a0ab57f173e9785c3ca7a8c3");

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
