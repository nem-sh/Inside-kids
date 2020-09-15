<template>
  <div>
    <v-card-title
      class="text-h4 d-flex justify-center green--text font-weight-bold"
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
      ></v-text-field>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="login">Login</v-btn>
    </v-card-actions>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
};
</script>

<style></style>
