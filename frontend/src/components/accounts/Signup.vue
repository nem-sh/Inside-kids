<template>
  <div>
    <v-card-title
      class="text-h4 d-flex justify-center deep-orange--text font-weight-bold"
      >SIGN UP</v-card-title
    >
    <div class="pa-5">
      <v-text-field
        label="email"
        prepend-icon="mdi-account-circle"
        type="email"
        v-model="email"
        :error-messages="emailErrors"
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
        required
      ></v-text-field>
      <v-text-field
        label="password"
        type="password"
        v-model="password"
        :error-messages="passwordErrors"
        @input="$v.password.$touch()"
        @blur="$v.password.$touch()"
        prepend-icon="mdi-lock"
        hint="At least 8 characters"
        required
      ></v-text-field>
      <v-text-field
        label="password confirm"
        type="password"
        v-model="repeatPassword"
        :error-messages="repeatPasswordErrors"
        @input="$v.repeatPassword.$touch()"
        @blur="$v.repeatPassword.$touch()"
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
      <v-btn color="white" text>Signup</v-btn>
    </v-card-actions>
    <div>
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
            style="max-width: 220px; max-height: 50px"
          />
        </g-signin-button>
        <button @click="kakaoLogin">
          <img
            src="../../assets/kakao.png"
            alt="kakao"
            style="max-width: 220px; max-height: 50px"
          />
        </button>
      </div>
    </div>

    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { validationMixin } from "vuelidate";
import { required, email, minLength, sameAs } from "vuelidate/lib/validators";

import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";

export default {
  mixins: [validationMixin],
  validations: {
    email: { required, email },
    password: {
      required,
      minLength: minLength(8),
    },
    repeatPassword: {
      sameAsPassword: sameAs("password"),
    },
  },
  name: "Signup",
  data() {
    return {
      email: "",
      password: "",
      repeatPassword: "",
      overlay: false,
      googleSignInParams: {
        client_id:
          "692091835929-e5bhto8anq0j3v7k21kb4f87gfn2gt6s.apps.googleusercontent.com",
      },
    };
  },
  methods: {
    ...mapActions(["login", "googleSocialLogin", "kakaoSocialLogin"]),
    submit() {
      this.$v.$touch();
      if (this.$v.$invalid) {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "입력한 내용을 다시 한번 확인해주세요.",
          showConfirmButton: false,
          timer: 1000,
        });
      } else {
        const signupData = {
          email: this.email,
          password1: this.password,
          password2: this.repeatPassword,
        };
        this.signup(signupData);
      }
    },
    signup(signupData) {
      this.overlay = true;
      axios
        .post(SERVER.URL + SERVER.ROUTES.signup, signupData)
        .then(() => {
          this.overlay = false;
          this.email = null;
          this.password = null;
          this.repeatPassword = null;
          this.$emit("signup");
        })
        .catch((err) => {
          this.overlay = false;
          if ("email" in err.response.data) {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: err.response.data.email,
              showConfirmButton: false,
              timer: 1000,
            });
          } else if ("password1" in err.response.data) {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: err.response.data.password1,
              showConfirmButton: false,
              timer: 1000,
            });
          } else {
            Swal.fire({
              position: "center",
              icon: "warning",
              title: "이메일 혹은 비밀번호를 확인해주세요.",
              showConfirmButton: false,
              timer: 1000,
            });
          }
        });
    },
    onGoogleSignInSuccess(resp) {
      const token = resp.wc.access_token;
      this.googleSocialLogin({
        access_token: token,
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
      });
    },
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("이메일 형식을 바르게 입력헤주세요.");
      !this.$v.email.required && errors.push("이메일을 입력해주세요.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.minLength &&
        errors.push(
          `비밀번호는 최소 ${this.$v.password.$params.minLength.min}자리 이상 입력해야 합니다.`
        );
      !this.$v.password.required && errors.push("비밀번호를 입력해주세요.");
      return errors;
    },
    repeatPasswordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.repeatPassword.sameAsPassword &&
        errors.push("비밀번호가 같지 않습니다.");
      return errors;
    },
  },
};
</script>

