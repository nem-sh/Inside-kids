<template>
  <div>
    <v-card-title
      class="text-h4 d-flex justify-center deep-orange--text font-weight-bold"
    >Find Password</v-card-title>
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
    <v-card-actions
      class="d-flex justify-center mx-5 my-2 form-btn"
      style="background-color:#FF8A65; cursor:pointer"
      @click="submit"
    >
      <div>
        <v-btn color="white" text>Send email</v-btn>
      </div>
    </v-card-actions>
  </div>
</template>

<script>
import { mapActions } from "vuex";

import Swal from "sweetalert2";

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
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "이메일을 입력해주세요.",
          showConfirmButton: false,
          timer: 1000,
        });
      } else {
        const emailData = {
          email: this.email,
        };
        this.resetPwd(emailData);
      }
    },
  },
};
</script>

