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
    character: {},
  },
  getters: {
    isLoggedIn: (state) => !!state.authToken,
    commonConfig: (state) => ({
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
    SET_CHARACTER(state, character) {
      state.character = character;
    },
  },
  actions: {
    login({ commit }, loginData) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.login, loginData)
        .then((res) => {
          commit("SET_TOKEN", res.data.token);
          commit("SET_USER", res.data.user);
          router.push({ name: "KidsManageView" });
        })
        .catch(() => {
          Swal.fire({
            position: "center",
            icon: "warning",
            title: "아이디 혹은 비밀번호를 확인해주세요.",
            showConfirmButton: false,
            timer: 1000,
          });
        });
    },
    kakaoSocialLogin({ commit }, loginData) {
      let token = { access_token: loginData.access_token }
      axios
        .post(SERVER.URL + "/accounts/kakao/", token)
        .then((res) => {
          commit("SET_TOKEN", res.data.token);
          commit("SET_USER", res.data.user);
          if (loginData.isParent) {
            router.push({ name: "KidsManageView" });
          }
          else {
            router.push({ name: "KidsSelectView" });
          }
        })
        .catch((err) => {
          if ("non_field_errors" in err.response.data) {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: err.response.data.non_field_errors,
              showConfirmButton: false,
              timer: 1000,
            });
          } else {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: "아이디 혹은 비밀번호를 확인해주세요.",
              showConfirmButton: false,
              timer: 1000,
            });
          }
        });
    },

    googleSocialLogin({ commit }, loginData) {
      let token = { access_token: loginData.access_token }
      axios
        .post(SERVER.URL + "/accounts/google/", token)
        .then((res) => {
          commit("SET_TOKEN", res.data.token);
          commit("SET_USER", res.data.user);
          if (loginData.isParent) {
            router.push({ name: "KidsManageView" });
          }
          else {
            router.push({ name: "KidsSelectView" });
          }
        })
        .catch((err) => {
          if ("non_field_errors" in err.response.data) {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: err.response.data.non_field_errors,
              showConfirmButton: false,
              timer: 1000,
            });
          } else {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: "아이디 혹은 비밀번호를 확인해주세요.",
              showConfirmButton: false,
              timer: 1000,
            });
          }
        });
    },

    resetPwd(context, emailData) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.resetPwd, emailData)
        .then(() => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "비밀번호 초기화 메일을 전송했습니다.",
            showConfirmButton: false,
            timer: 1000,
          });
        })
        .catch(() => {
          Swal.fire({
            position: "center",
            icon: "warning",
            title: "존재하지 않는 이메일입니다.",
            showConfirmButton: false,
            timer: 1000,
          });
        });
    },
    logout({ getters, commit }) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.logout, null, getters.commonConfig)
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
        .catch(() => { });
    },
    getUser({ getters, commit, state }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.getUserInfo, getters.commonConfig)
        .then((res) => {
          commit("SET_USER", res.data);
          if (state.authToken !== cookies.get("auth-token")) {
            commit("SET_TOKEN", null);
            cookies.remove("auth-token");
            Swal.fire({
              position: "center",
              icon: "warning",
              title: "로그인해 주세요.",
            });
            router.push({ name: "Home" });
          }
        })
        .catch(() => {
          commit("SET_TOKEN", null);
          cookies.remove("auth-token");
          Swal.fire({
            position: "center",
            icon: "warning",
            title: "로그인해 주세요.",
          });
          router.push({ name: "Home" });
        });
    },
    getKidsList({ getters, commit }) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.getKidInfo, getters.commonConfig)
        .then((res) => {
          commit("SET_KIDSLIST", res.data);
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.")
            router.push({ name: "Home" });
          }
        });
    },
    getKid({ getters, commit }, kidId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.getKidInfo + kidId + "/",
          getters.commonConfig
        )
        .then((res) => {
          commit("SET_KID", res.data);
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.")
            router.push({ name: "Home" });
          }
        });
    },
    changePassword({ getters }, data) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.passwordChange,
          data,
          getters.commonConfig
        )
        .then(() => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "비밀번호 변경이 완료되었습니다.",
            showConfirmButton: false,
            timer: 1000,
          });
          location.reload();
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.")
            router.push({ name: "Home" });
          }
          Swal.fire({
            position: "center",
            icon: "warning",
            title: "일상적이거나, 아이디와 비슷한 비밀번호로 바꿀 수 없습니다.",
            showConfirmButton: false,
            timer: 1000,
          });
        });
    },
    deleteUser({ getters, commit }) {
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
            .delete(
              SERVER.URL + SERVER.ROUTES.deletAccount,
              getters.commonConfig
            )
            .then(() => {
              Swal.fire({
                position: "center",
                icon: "success",
                title: "회원 탈퇴되었습니다.",
                showConfirmButton: false,
                timer: 1000,
              });
              commit("SET_TOKEN", null);
              cookies.remove("auth-token");
              router.push({ name: "Home" });
            })
            .catch((err) => {
              if (err.response.status == 403) {
                alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.")
                router.push({ name: "Home" });
              }
            });
        }
      });
    },
    getCharacter({ getters, commit }, kidId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.getCharacterInfo + kidId + "/",
          getters.commonConfig
        )
        .then((res) => {
          commit("SET_CHARACTER", res.data);
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.")
            router.push({ name: "Home" });
          }
        });
    },
  },
  modules: {},
});
