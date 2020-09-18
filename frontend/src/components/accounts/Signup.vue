<template>
  <div>
    <v-card-title class="text-h4 d-flex justify-center green--text font-weight-bold">SIGN UP</v-card-title>
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

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click="submit">Signup</v-btn>
    </v-card-actions>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, email, minLength, sameAs } from "vuelidate/lib/validators";
import { mapActions } from "vuex";

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
    };
  },
  methods: {
    ...mapActions(["signup"]),
    submit() {
      this.$v.$touch();
      if (this.$v.$invalid) {
        alert("입력한 내용을 다시 한번 확인해주세요.");
      } else {
        const signupData = {
          email: this.email,
          password1: this.password,
          password2: this.repeatPassword,
        };
        this.signup(signupData);
      }
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

<style></style>
