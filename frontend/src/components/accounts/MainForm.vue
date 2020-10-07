<template>
  <div>
    <v-btn @click="start" rounded large color="white" class="red--text ma-5 font-weight-bold">시작하기</v-btn>
    <v-dialog v-model="dialog" width="450">
      <v-card>
        <div class="d-flex justify-center">
          <v-btn-toggle
            v-if="!switchBoolean2"
            v-model="switchBoolean"
            tile
            color="green lighten-1"
            group
          >
            <v-btn :value="false">Login</v-btn>

            <v-btn :value="true">Signup</v-btn>
          </v-btn-toggle>
        </div>

        <div id="login-form">
          <Login />
        </div>

        <div id="signup-form" style="display:none">
          <Signup @signup="toLogin" />
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
import { mapState } from "vuex";
import router from "@/router";
import Login from "@/components/accounts/Login";
import Signup from "@/components/accounts/Signup";
import ResetPassword from "@/components/accounts/ResetPassword";
import Swal from "sweetalert2";

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
  computed: {
    ...mapState(["authToken"]),
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
    toLogin() {
      Swal.fire({
        position: "center",
        icon: "success",
        title:
          "가입하신 이메일로 인증 메일을 보냈습니다. 인증 후 로그인해주세요.",
      });
      this.switchBoolean = !this.switchBoolean;
    },
    start() {
      if (this.authToken) {
        router.push({ name: "KidsManageView" });
      } else {
        this.dialog = true;
      }
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
