import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueCookies from "vue-cookies";
import { Plugin } from "vue-responsive-video-background-player";
import GSignInButton from "vue-google-signin-button";
Vue.use(GSignInButton);
Vue.use(Plugin);
Vue.config.productionTip = false;
Vue.use(VueCookies);

window.Kakao.init("403d64d9441a610dd94481f81b3aed9b");

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
