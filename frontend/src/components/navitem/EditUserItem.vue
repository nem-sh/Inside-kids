<template>
  <!-- modal 정보수정 -->
  <v-list-item>
    <v-row justify="center">
      <v-dialog v-model="dialog" max-width="400px">
        <template v-slot:activator="{ on, attrs }">
          <v-list-item-title v-bind="attrs" v-on="on">계정설정</v-list-item-title>
        </template>
        <v-card>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <span class="h1 font-weight-bold">이메일: {{ user.email }}</span>
                </v-col>

                <v-col cols="12">
                  <v-text-field v-model="currentPwd" label="현재 비밀번호" type="password" required></v-text-field>
                  <v-text-field
                    v-model="changePwd"
                    label="변경할 비밀번호"
                    hint="At least 8 characters"
                    :error-messages="passwordErrors"
                    @input="$v.changePwd.$touch()"
                    @blur="$v.changePwd.$touch()"
                    type="password"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="repeatChangePwd"
                    label="변경할 비밀번호 확인"
                    hint="At least 8 characters"
                    :error-messages="repeatPasswordErrors"
                    @input="$v.repeatChangePwd.$touch()"
                    @blur="$v.repeatChangePwd.$touch()"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="chpwd">비밀번호 변경</v-btn>
            <v-btn color="red darken-1" text @click="deleteUser">회원 탈퇴</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </v-list-item>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";
import { validationMixin } from "vuelidate";
import { required, minLength, sameAs } from "vuelidate/lib/validators";

import Swal from "sweetalert2";

export default {
  mixins: [validationMixin],
  validations: {
    changePwd: {
      required,
      minLength: minLength(8),
    },
    repeatChangePwd: {
      sameAsPassword: sameAs("changePwd"),
    },
  },
  name: "EditUserItem",
  data() {
    return {
      dialog: false,
      currentPwd: "",
      changePwd: "",
      repeatChangePwd: "",
    };
  },
  methods: {
    ...mapActions(["changePassword", "deleteUser"]),
    chpwd() {
      const data = {
        old_password: this.currentPwd,
        new_password1: this.changePwd,
        new_password2: this.repeatChangePwd,
      };
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
        this.changePassword(data);
      }
    },
  },
  computed: {
    ...mapState(["user"]),
    ...mapGetters(["config"]),
    passwordErrors() {
      const errors = [];
      if (!this.$v.changePwd.$dirty) return errors;
      !this.$v.changePwd.minLength &&
        errors.push(
          `비밀번호는 최소 ${this.$v.changePwd.$params.minLength.min}자리 이상 입력해야 합니다.`
        );
      !this.$v.changePwd.required && errors.push("비밀번호를 입력해주세요.");
      return errors;
    },
    repeatPasswordErrors() {
      const errors = [];
      if (!this.$v.repeatChangePwd.$dirty) return errors;
      !this.$v.repeatChangePwd.sameAsPassword &&
        errors.push("비밀번호가 같지 않습니다.");
      return errors;
    },
  },
};
</script>
