<template>
  <v-card class="mx-auto mt-15" color="grey lighten-5" dark width="700">
    <v-card-title class="mx-2 my-2 text--primary">
      <h3>질문 관리</h3>
    </v-card-title>

    <v-card-actions v-for="script in kid.scripts" :key="script.id">
      <v-list-item class="grow blue-grey lighten-4">
        <v-list-item-content class="ml-5 text--primary">
          <v-list-item-title>질문</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
          <v-btn color="black" text @click="deleteScript(script.id)">삭제</v-btn>
        </v-row>
      </v-list-item>
    </v-card-actions>

    <v-card-actions>
      <v-btn color="black" text @click.stop="dialog=true">
        <v-icon class="mr-1">mdi-plus</v-icon>
      </v-btn>
    </v-card-actions>

    <v-dialog v-model="dialog" max-width="600">
      <v-card class="text-center px-5">
        <v-col>
          <h1>질문 등록</h1>
        </v-col>
        <form>
          <v-col>
            <v-text-field require prepend-icon="mdi-pencil" label="질문" v-model="script"></v-text-field>
          </v-col>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="green darken-1" text @click="addScript">add</v-btn>

            <v-btn color="green darken-1" text @click="dialog=false">close</v-btn>
          </v-card-actions>
        </form>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mapGetters, mapState } from "vuex";
// import axios from "axios";
// import SERVER from "@/api/drf";
// import Swal from "sweetalert2";

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
    addScript() {},
    deleteScript(scriptId) {
      console.log(scriptId);
    },
  },
};
</script>

<style>
</style>