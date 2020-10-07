<template>
  <v-card class="mx-auto my-15" color="grey lighten-5" dark width="700">
    <v-card-title class="mx-2 my-2 text--primary" v-if="kid.scripts">
      <h3>질문 관리 ({{ kid.scripts.length }}/3)</h3>
    </v-card-title>

    <p class="text--primary ml-5">** 아이의 답변이 등록된 질문은 대화녹화 탭에서 확인하실 수 있습니다.</p>

    <v-card-actions v-for="script in kid.scripts" :key="script.id">
      <v-list-item class="grow blue-grey lighten-5">
        <v-list-item-content class="ml-5 text--primary">
          <v-list-item-title>{{ script.content }}</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
          <v-btn color="red" text @click="deleteScript(script.id)">삭제</v-btn>
        </v-row>
      </v-list-item>
    </v-card-actions>

    <v-card-actions>
      <v-btn color="black" text @click.stop="cntCheck">
        <v-icon class="mr-1">mdi-plus</v-icon>
      </v-btn>
    </v-card-actions>

    <v-dialog v-model="dialog" max-width="600">
      <v-card class="text-center px-5">
        <v-col>
          <h1>질문 등록</h1>
        </v-col>
        <v-col>
          <v-text-field
            require
            prepend-icon="mdi-pencil"
            label="질문"
            v-model="script"
            @keyup.enter="addScript"
          ></v-text-field>
        </v-col>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="addScript">add</v-btn>

          <v-btn color="green darken-1" text @click="dialog = false">close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mapGetters, mapState } from "vuex";

import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";

export default {
  name: "ScriptList",
  data() {
    return {
      dialog: false,
      script: "",
    };
  },
  computed: {
    ...mapState(["kid"]),
    ...mapGetters(["commonConfig"]),
  },
  methods: {
    addScript() {
      if (this.kid.scripts.length >= 3) {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "질문은 최대 3개까지 등록 가능합니다.",
          showConfirmButton: false,
          timer: 1000,
        });
        this.dialog = false;
      } else {
        if (this.script) {
          const scriptData = {
            content: this.script,
          };
          axios
            .post(
              SERVER.URL + "/contents/kids/" + this.kid.id + "/scripts/",
              scriptData,
              this.commonConfig
            )
            .then((res) => {
              this.kid.scripts.push(res.data);
              this.script = "";
              this.dialog = false;
            })
            .catch((err) => {
              if (err.response.status == 403) {
                alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
                this.$router.push({ name: "Home" });
              } else {
                console.log(err.response);
              }
            });
        } else {
          Swal.fire({
            position: "center",
            icon: "warning",
            title: "질문을 작성해주세요.",
            showConfirmButton: false,
            timer: 1000,
          });
        }
      }
    },
    deleteScript(scriptId) {
      Swal.fire({
        position: "center",
        icon: "warning",
        title: "삭제하시겠습니까?",
        showCancelButton: true,
        confirmButtonText: `Yes`,
      }).then((result) => {
        if (result.isConfirmed) {
          axios
            .delete(
              SERVER.URL + "/contents/scripts/" + scriptId + "/",
              this.commonConfig
            )
            .then(() => {
              const newScripts = this.kid.scripts.filter((script) => {
                return script.id !== scriptId;
              });
              this.kid.scripts = newScripts;
            })
            .catch((err) => {
              if (err.response.status == 403) {
                alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
                this.$router.push({ name: "Home" });
              } else {
                console.log(err.response);
              }
            });
        }
      });
    },
    cntCheck() {
      if (this.kid.scripts.length >= 3) {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "질문은 최대 3개까지 등록 가능합니다.",
          showConfirmButton: false,
          timer: 1000,
        });
      } else {
        this.dialog = true;
      }
    },
  },
};
</script>

<style>
</style>