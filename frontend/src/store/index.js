import Vue from "vue";
import Vuex from "vuex";

import cookies from "vue-cookies";
import router from "@/router";
import axios from "axios";

import SERVER from "@/api/drf";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authToken: cookies.get("auth-token"),
    user: {},
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token;
      cookies.set("auth-token", token);
    },
    SET_USER(state, userInfo) {
      state.user = userInfo;
    },
  },
  actions: {
    signup({ commit }, signupData) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.signup, signupData)
        .then((res) => {
          console.log(res.data);
          commit("SET_TOKEN", res.data);
          router.push({ name: "BeforeEmailAuthView" });
        })
        .catch((err) => {
          for (const [key, value] of Object.entries(err.response.data)) {
            alert(`${key}: ${value}`);
          }
        });
    },
  },
  modules: {},
});
