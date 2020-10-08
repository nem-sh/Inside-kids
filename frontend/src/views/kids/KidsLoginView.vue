<template>
  <div class="bg-2 d-flex flex-column justify-center">
    <v-card class="mx-auto opacity-form" min-width="400">
      <div>
        <v-card-title
          class="text-h4 d-flex justify-center deep-orange--text font-weight-bold"
          >LOG IN</v-card-title
        >
        <div class="pa-5">
          <v-text-field
            label="email"
            prepend-icon="mdi-account-circle"
            type="email"
            v-model="email"
            required
          ></v-text-field>
          <v-text-field
            label="password"
            type="password"
            v-model="password"
            prepend-icon="mdi-lock"
            hint="At least 8 characters"
            required
            @keyup.enter="submit"
          ></v-text-field>
        </div>
        <v-card-actions
          @click="submit"
          class="d-flex justify-center mx-5 my-2 form-btn"
          style="background-color: #ff8a65; cursor: pointer"
        >
          <div>
            <v-btn color="white" text>Login</v-btn>
          </div>
        </v-card-actions>
        <div style="display: flex; justify-content: center" class="my-3">
          <g-signin-button
            style="cursor: pointer; max-width: 350px"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError"
          >
            <img
              src="../../assets/google.png"
              alt="google"
              style="max-width: 180px; height: 55px"
            />
          </g-signin-button>

          <button @click="kakaoLogin">
            <img
              src="../../assets/kakao.png"
              alt="kakao"
              style="max-width: 180px; height: 55px"
            />
          </button>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
import router from "@/router";
import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";
import { mapMutations, mapActions } from "vuex";

export default {
  name: "KidsLoginView",
  data() {
    return {
      email: "",
      password: "",
      googleSignInParams: {
        client_id:
          "692091835929-e5bhto8anq0j3v7k21kb4f87gfn2gt6s.apps.googleusercontent.com",
      },
    };
  },
  methods: {
    ...mapActions(["googleSocialLogin", "kakaoSocialLogin"]),

    ...mapMutations(["SET_TOKEN", "SET_USER"]),
    submit() {
      if (!this.email || !this.password) {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "이메일 혹은 패스워드를 입력해주세요.",
          showConfirmButton: false,
          timer: 1000,
        });
      } else {
        const loginData = {
          email: this.email,
          password: this.password,
        };
        axios
          .post(SERVER.URL + SERVER.ROUTES.login, loginData)
          .then((res) => {
            this.SET_TOKEN(res.data.token);
            this.SET_USER(res.data.user);
            router.push({
              name: "KidsSelectView",
            });
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
      }
    },
    onGoogleSignInSuccess(resp) {
      const token = resp.wc.access_token;
      this.googleSocialLogin({
        access_token: token,
        isParent: false,
      });
    },
    onGoogleSignInError(error) {
      console.error(error);
    },
    kakaoLogin() {
      window.Kakao.Auth.login({
        success: this.kakaoLoginSuccess,
        fail: function (error) {
          console.error(error);
        },
      });
    },
    kakaoLoginSuccess(response) {
      const token = response.access_token;
      this.kakaoSocialLogin({
        access_token: token,
        isParent: false,
      });
    },
  },
};
</script>

<style>
.bg-2 {
  width: 100%;
  height: 100%;
  background-image: url("../../assets/characters/outdoor.jpg");
  background-position: center center;
  background-size: cover;
}
.opacity-form {
  background-color: rgba(255, 255, 255, 0.8) !important;
}
</style>
