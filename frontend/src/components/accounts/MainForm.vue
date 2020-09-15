<template>
  <div>
    <v-dialog v-model="dialog" width="450">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-bind="attrs"
          v-on="on"
          rounded
          large
          color="white"
          class="red--text ma-5 font-weight-bold"
        >시작하기</v-btn>
      </template>

      <v-card>
        <div class="d-flex justify-center">
          <v-switch v-if="!switchBoolean2" v-model="switchBoolean" inset color="secondary"></v-switch>
        </div>

        <div id="login-form">
          <Login />
        </div>

        <div id="signup-form" style="display:none">
          <Signup />
        </div>

        <div id="find-pwd-form" style="display:none">
          <ResetPassword />
        </div>

        <a v-if="!switchBoolean2" class="ml-2" @click="findPwdForm">비밀번호를 잊으셨나요?</a>
        <a v-else class="ml-2" @click="switchForm">로그인/회원가입하기</a>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Login from "@/components/accounts/Login";
import Signup from "@/components/accounts/Signup";
import ResetPassword from "@/components/accounts/ResetPassword";

export default {
  name: "MainForm",
  components: {
    Login,
    Signup,
    ResetPassword,
  },
  data() {
    return {
      dialog: false,
      switchBoolean: false,
      switchBoolean2: false,
    };
  },
  methods: {
    switchForm() {
      var loginForm = document.getElementById("login-form");
      var signupForm = document.getElementById("signup-form");
      var findPwdForm = document.getElementById("find-pwd-form");
      if (this.switchBoolean) {
        loginForm.style.display = "none";
        signupForm.style.display = "block";
      } else {
        loginForm.style.display = "block";
        signupForm.style.display = "none";
      }
      findPwdForm.style.display = "none";
      this.switchBoolean2 = false;
    },
    findPwdForm() {
      var loginForm = document.getElementById("login-form");
      var signupForm = document.getElementById("signup-form");
      var findPwdForm = document.getElementById("find-pwd-form");
      loginForm.style.display = "none";
      signupForm.style.display = "none";
      findPwdForm.style.display = "block";
      this.switchBoolean2 = true;
    },
  },
  watch: {
    switchBoolean() {
      this.switchForm();
    },
  },
};
</script>

<style></style>
