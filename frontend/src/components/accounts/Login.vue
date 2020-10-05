<template>
  <div>
    <v-card-title class="text-h4 d-flex justify-center green--text font-weight-bold">LOG IN</v-card-title>
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
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="submit">Login</v-btn>
    </v-card-actions>
    <div>
      <div style="display: flex; justify-content: center" class="my-3">
        <g-signin-button
          style="cursor: pointer; max-width: 350px"
          :params="googleSignInParams"
          @success="onGoogleSignInSuccess"
          @error="onGoogleSignInError"
        >
          <img src="../../assets/google.png" alt style="max-width: 220px; max-height: 50px" />
        </g-signin-button>
        <button @click="kakaoLogin">
          <img src="../../assets/kakao.png" alt style="max-width: 220px; max-height: 50px" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import Swal from "sweetalert2";

export default {
  name: "Login",
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
    ...mapActions(["login", "googleSocialLogin", "kakaoSocialLogin"]),
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
        this.login(loginData);
      }
    },
    onGoogleSignInSuccess(resp) {
      const token = resp.wc.access_token;
      console.log(resp);
      this.googleSocialLogin({
        access_token: token,
      });
    },
    onGoogleSignInError(error) {
      console.log("OH NOES", error);
    },
    kakaoLogin() {
      window.Kakao.Auth.login({
        success: this.kakaoLoginSuccess,
        fail: function (error) {
          console.log(error);
        },
      });
    },
    kakaoLoginSuccess(response) {
      console.log(response);
      const token = response.access_token;
      this.kakaoSocialLogin({
        access_token: token,
      });
    },
  },
};
</script>

<style></style>
