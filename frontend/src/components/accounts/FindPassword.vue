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
      ></v-text-field>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="findPwd">Send email</v-btn>
    </v-card-actions>
  </div>
</template>

<script>
export default {
  name: "FindPassword",
  data() {
    return {
      email: "",
    };
  },
};
</script>

<style></style>
