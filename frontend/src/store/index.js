import Vue from "vue";
import Vuex from "vuex";

import cookies from "vue-cookies";
import router from "@/router";
import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authToken: cookies.get("auth-token"),
    user: {},
    kid: {},
    kidslist: {},
  },
  getters: {
    isLoggedIn: (state) => !!state.authToken,
    config: (state) => ({
      headers: { Authorization: `jwt ${state.authToken}` },
    }),
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token;
      cookies.set("auth-token", token);
    },
    SET_USER(state, userInfo) {
      state.user = userInfo;
    },
    SET_KID(state, kidInfo) {
      state.kid = kidInfo;
    },
    SET_KIDSLIST(state, kids) {
      state.kidslist = kids;
    },
  },
  actions: {
    signup({ commit }, signupData) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.signup, signupData)
        .then((res) => {
          commit("SET_TOKEN", res.data.token);
          commit("SET_USER", res.data.user);
          router.push({ name: "BeforeEmailAuthView" });
        })
        .catch((err) => {
          if ("email" in err.response.data) {
            alert(err.response.data.email);
          } else if ("password1" in err.response.data) {
            alert(err.response.data.password1);
          } else {
            alert("이메일 혹은 비밀번호를 확인해주세요.");
          }
        });
    },
    login({ commit }, loginData) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.login, loginData)
        .then((res) => {
          commit("SET_TOKEN", res.data.token);
          commit("SET_USER", res.data.user);
          router.push({ name: "KidsDetailView", params: { kidId: 0 } });
        })
        .catch(() => {
          alert("아이디 혹은 비밀번호를 확인해주세요.");
        });
    },
    resetPwd(email) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.resetPwd, email)
        .then(() => {
          alert("비밀번호 초기화 메일을 전송했습니다.");
        })
        .catch(() => {
          alert("존재하지 않는 이메일입니다.");
        });
    },
    logout({ getters, commit }) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          commit("SET_TOKEN", null);
          cookies.remove("auth-token");
          Swal.fire({
            position: "center",
            icon: "success",
            title: "로그아웃 되었습니다!",
          });
          router.push({ name: "Home" });
        })
        .catch((err) => console.log(err));
    },
    // getUser({ getters, commit, state }) {
    getUser({ getters, commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.getUserInfo, getters.config)
        .then((res) => {
          commit("SET_USER", res.data);
          // if (state.authToken !== cookies.get('auth-token')) {
          //   commit('SET_TOKEN', null)
          //   cookies.remove('auth-token')
          //   Swal.fire({
          //     position: 'center',
          //     icon: 'warning',
          //     title: '로그인해 주세요.',
          //   })
          //   router.push({ name: "Home" })
          // }
        });
      // .catch((err) => {
      //   console.error(err)
      //   commit('SET_TOKEN', null)
      //   cookies.remove('auth-token')
      //   Swal.fire({
      //     position: 'center',
      //     icon: 'warning',
      //     title: '로그인해 주세요.',
      //   })
      //   router.push({ name: "Home" })
      // })
    },
    getKidsList({ getters, commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.getKidInfo, getters.config)
        .then((res) => {
          commit("SET_KIDSLIST", res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    getKid({ getters, commit, kidId }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.getKidInfo + kidId, getters.config)
        .then((res) => {
          commit("SET_KID", res.data);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    changePassword({ getters }, data) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.passwordChange, data, getters.config)
        .then(() => {
          alert("비밀번호 변경이 완료되었습니다.");
          location.reload();
        })
        .catch(() => {
          alert("일상적이거나, 아이디와 비슷한 비밀번호로 바꿀 수 없습니다.");
        });
    },
    deleteUser({ getters }) {
      Swal.fire({
        position: "center",
        icon: "warning",
        title: "회원 탈퇴하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: `Yes`,
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          axios
            .delete(SERVER.URL + SERVER.ROUTES.deletAccount, getters.config)
            .then(() => {
              alert("회원 탈퇴되었습니다.");
              router.push({ name: "Home" });
            })
            .catch((err) => {
              console.log(err.response);
            });
        }
      });
    },
  },
  modules: {},
});
