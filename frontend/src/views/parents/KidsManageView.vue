<template>
  <div>
    <Nav />
    <div class="kids-manage-body pt-15">
      <v-card class="mx-auto my-auto" color="#90A4AE" dark width="500">
        <v-card-title class="mx-2 my-2">
          <v-icon large left>fas fa-child</v-icon>
          <h1>아이 관리</h1>
        </v-card-title>
        <div v-if="!kidslist.length" class="text-center">
          <h2>
            <i class="fas fa-exclamation-circle"></i> 아이를 등록해주세요
          </h2>
        </div>
        <v-card-actions
          v-for="kid in kidslist"
          :key="kid.id"
          @click="goToDetail(kid.id)"
          class="kid-list"
        >
          <v-list-item class="grow blue-grey lighten-4">
            <v-list-item-avatar color="white">
              <KidImage :image="kid.image" />
            </v-list-item-avatar>

            <v-list-item-content class="ml-5 text--primary">
              <v-list-item-title>{{kid.name}}</v-list-item-title>
            </v-list-item-content>

            <v-row align="center" justify="end">
              <v-btn
                color="black"
                text
                @click.stop="(dialog=true),(addOrUpdate=true),(kidsId=kid.id)"
              >수정</v-btn>
              <v-btn color="black" text @click="deleteKids(kid.id)">삭제</v-btn>
            </v-row>
          </v-list-item>
        </v-card-actions>

        <v-card-actions>
          <v-btn color="white" text @click.stop="(dialog=true),(addOrUpdate=false)">
            <v-icon class="mr-1">mdi-plus</v-icon>
          </v-btn>
        </v-card-actions>

        <v-dialog v-model="dialog" max-width="400">
          <v-card class="text-center px-5">
            <v-col>
              <h1 v-if="!addOrUpdate">아이 등록</h1>
              <h1 v-if="addOrUpdate">아이 수정</h1>
            </v-col>

            <v-col>
              <v-file-input
                accept="image/png, image/jpeg, image/bmp"
                placeholder="아이 사진"
                prepend-icon="mdi-camera"
                v-model="kidsImage"
                ref="file"
                type="file"
              ></v-file-input>
            </v-col>
            <v-col>
              <v-text-field require prepend-icon="mdi-pencil" label="이름" v-model="kidsName"></v-text-field>
            </v-col>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn color="green darken-1" text @click="addKids" v-if="!addOrUpdate">add</v-btn>
              <v-btn color="green darken-1" text @click="updateKids()" v-if="addOrUpdate">update</v-btn>

              <v-btn color="green darken-1" text @click="dialog=false">close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card>
    </div>
    <Footer />
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";

import Nav from "@/components/Navigation";
import Footer from "@/components/Footer";
import KidImage from "@/components/parents/KidImage";
import Swal from "sweetalert2";
import router from "@/router";

export default {
  name: "KidsManageView",
  components: {
    Nav,
    Footer,
    KidImage,
  },
  data() {
    return {
      dialog: false,
      kidsName: "",
      kidsImage: null,
      addOrUpdate: false,
      kidsId: "",
    };
  },
  computed: {
    ...mapState(["kidslist", "authToken"]),
    ...mapGetters(["commonConfig"]),
  },
  methods: {
    ...mapActions(["getKidsList", "getUser"]),
    // fileSelect() {
    //   this.kidsImage = this.$refs.kidsimage.files[0];
    // },
    addKids() {
      if (this.kidsName) {
        var formData = new FormData();
        formData.append("name", this.kidsName);
        if (this.kidsImage) {
          formData.append("image", this.kidsImage);
        }
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
      } else {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "아이 이름을 입력해주세요.",
          showConfirmButton: false,
          timer: 1000,
        });
      }
    },
    updateKids() {
      if (this.kidsName || this.kidsImage) {
        var formData = new FormData();
        if (this.kidsName) {
          formData.append("name", this.kidsName);
        }
        if (this.kidsImage) {
          formData.append("image", this.kidsImage);
        }
        const axiosConfig = {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `jwt ${this.authToken}`,
          },
        };
        axios
          .put(
            SERVER.URL + SERVER.ROUTES.getKidInfo + this.kidsId + "/",
            formData,
            axiosConfig
          )
          .then(() => {
            this.dialog = false;
            this.getKidsList();
            this.kidsName = null;
            this.kidsImage = null;
          })
          .catch((err) => {
            console.error(err.response);
          });
      } else {
        Swal.fire({
          position: "center",
          icon: "warning",
          title: "변경할 이름을 입력해주세요.",
          showConfirmButton: false,
          timer: 1000,
        });
      }
    },
    deleteKids(kidId) {
      event.stopPropagation();
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
              SERVER.URL + SERVER.ROUTES.getKidInfo + kidId + "/",
              this.commonConfig
            )
            .then(() => {
              this.getKidsList();
            })
            .catch((err) => {
              console.error(err.response);
            });
        }
      });
    },
    goToDetail(kidId) {
      router.push({ name: "KidsDetailView", params: { kidId: kidId } });
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
  min-height: 100vh;
}
.kid-list:hover {
  cursor: pointer;
}
</style>