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
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["login"]),
    submit() {
      if (!this.email || !this.password) {
        alert("이메일 혹은 패스워드를 입력해주세요.");
      } else {
        const loginData = {
          email: this.email,
          password: this.password,
        };
        this.login(loginData);
      }
    },
  },
};
</script>

<style></style>
