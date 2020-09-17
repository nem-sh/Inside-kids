<template>
  <div>
    <Nav />
    <div class="kids-manage-body pt-15">
      <v-card class="mx-auto my-auto" color="#90A4AE" dark width="500">
        <v-card-title class="mx-2 my-2">
          <v-icon large left>fas fa-child</v-icon>
          <h1>아이 관리</h1>
        </v-card-title>

        <v-card-actions v-for="kid in kidslist" :key="kid.id">
          <v-list-item class="grow blue-grey lighten-4">
            <v-list-item-avatar color="white">
              <v-img
                class="elevation-6"
                src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
              ></v-img>
            </v-list-item-avatar>

            <v-list-item-content class="ml-5 text--primary">
              <v-list-item-title>{{kid.name}}</v-list-item-title>
            </v-list-item-content>

            <v-row align="center" justify="end">
              <v-btn color="black" text @click="updateKids">수정</v-btn>
              <v-btn color="black" text @click="deleteKids(kid.id)">삭제</v-btn>
            </v-row>
          </v-list-item>
        </v-card-actions>

        <v-card-actions>
          <v-btn color="white" text @click.stop="dialog = true">
            <v-icon class="mr-1">mdi-plus</v-icon>
          </v-btn>
        </v-card-actions>

        <v-dialog v-model="dialog" max-width="400">
          <v-card class="text-center px-5">
            <v-col>
              <h1>아이 등록</h1>
            </v-col>
            <form>
              <v-col>
                <v-file-input
                  accept="image/png, image/jpeg, image/bmp"
                  placeholder="아이 사진"
                  prepend-icon="mdi-camera"
                  v-model="kidsImage"
                ></v-file-input>
              </v-col>
              <v-col>
                <v-text-field require prepend-icon="mdi-pencil" label="이름" v-model="kidsName"></v-text-field>
              </v-col>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn color="green darken-1" text @click="addKids">add</v-btn>

                <v-btn color="green darken-1" text @click="dialog = false">close</v-btn>
              </v-card-actions>
            </form>
          </v-card>
        </v-dialog>
      </v-card>
    </div>
    <Footer />
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";

import Nav from "@/components/Navigation";
import Footer from "@/components/Footer";

export default {
  name: "KidsManageView",
  components: {
    Nav,
    Footer,
  },
  data() {
    return {
      dialog: false,
      kidsName: "",
      kidsImage: [],
    };
  },
  computed: {
    ...mapState(["kidslist", "commonConfig", "authToken"]),
  },
  methods: {
    ...mapActions(["getKidsList", "getUser"]),
    fileSelect() {
      this.kidsImage = this.$refs.kidsimage.files[0];
    },
    addKids() {
      var formData = new FormData();
      formData.append("name", this.kidsName);
      formData.append("image", this.kidsImage);

      const axiosConfig = {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `jwt ${this.authToken}`,
        },
      };
      axios
        .post(SERVER.URL + SERVER.ROUTES.getKidInfo, formData, axiosConfig)
        .then(() => {
          this.dialog = false;
          this.getKidsList();
          this.kidsName = null;
          this.kidsImage = null;
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
    updateKids() {},
    deleteKids(kidId) {
      const axiosConfig = {
        headers: {
          Authorization: `jwt ${this.authToken}`,
        },
      };
      axios
        .delete(
          SERVER.URL + SERVER.ROUTES.getKidInfo + kidId + "/",
          axiosConfig
        )
        .then(() => {
          this.getKidsList();
        })
        .catch((err) => {
          console.error(err.response);
        });
    },
  },
  created() {
    this.getKidsList();
    this.getUser();
  },
};
</script>

<style>
.kids-manage-body {
  height: 90vh;
}
</style>