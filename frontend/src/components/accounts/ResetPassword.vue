<template>
  <div>
    <v-card-title class="text-h4 d-flex justify-center green--text font-weight-bold">FIND PASSWORD</v-card-title>
    <div class="pa-5">
      <v-text-field
        label="email"
        type="email"
        prepend-icon="mdi-account-circle"
        v-model="email"
        required
        @keyup.enter="submit"
      ></v-text-field>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="submit">Send email</v-btn>
    </v-card-actions>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ResetPassword",
  data() {
    return {
      email: "",
    };
  },
  methods: {
    ...mapActions(["resetPwd"]),
    submit() {
      if (!this.email) {
        alert("이메일을 입력해주세요.");
      } else {
        this.resetPwd(this.email);
      }
    },
  },
};
</script>

<style></style>
