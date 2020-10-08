<template>
  <v-col cols="6" md="4">
    <v-hover v-slot:default="{ hover }">
      <v-card
        @click.stop="dialog = true"
        class="custom-card"
        :elevation="hover ? 12 : 2"
        :class="{ 'on-hover': hover }"
      >
        <img :src="contentImg" alt="content-image" width="100%" height="150px" />
        <p>{{ content.created_at.slice(0, 10) }}</p>
      </v-card>
    </v-hover>
    <v-dialog v-model="dialog" max-width="40rem">
      <template>
        <v-card class="d-inline-block mx-auto">
          <v-container>
            <v-row justify="space-between">
              <v-col cols="9" class="mx-auto mt-5 swing">
                <img
                  class="content-image"
                  :src="contentImg"
                  alt="contentImage"
                  width="100%"
                  height="auto"
                />
              </v-col>

              <v-col cols="12" class="text-center pl-0">
                <div class="my-2 d-flex justify-end">
                  <div class="mr-5">
                    <v-btn color="cyan lighten-1" dark>
                      <a
                        style="text-decoration: none; color: white"
                        :download="content.file_source"
                        :href="`/api` + content.file_source"
                      >
                        <i class="fas fa-download"></i>다운로드
                      </a>
                    </v-btn>
                  </div>
                  <div>
                    <v-btn color="amber accent-2" dark @click="sendLink">
                      <i class="far fa-comment"></i>카카오톡 공유하기
                    </v-btn>
                  </div>
                  <div class="ml-3">
                    <v-btn color="red accent-2" dark @click="remove">
                      <i class="fas fa-trash-alt"></i>삭제하기
                    </v-btn>
                  </div>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </template>
    </v-dialog>
  </v-col>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";

export default {
  name: "ContentItem",
  props: {
    content: Object,
    flag: Boolean,
  },
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    ...mapState(["kid"]),
    ...mapGetters(["commonConfig"]),
    contentImg() {
      return SERVER.URL + this.content.file_source;
    },
  },
  methods: {
    sendLink() {
      window.Kakao.Link.sendCustom({
        templateId: 38029,
        templateArgs: {
          THU: this.contentImg,
        },
      });
    },
    remove() {
      if (this.flag === true) {
        // 사진 삭제
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
                SERVER.URL + "/contents/pictures/" + this.content.id + "/",
                this.commonConfig
              )
              .then(() => {
                this.$emit("pictureRemove", this.content.id);
                const newPictures = this.kid.pictures.filter((picture) => {
                  return picture.id !== this.content.id;
                });
                this.kid.pictures = newPictures;
              })
              .catch((err) => {
                if (err.response.status == 403) {
                  alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
                  this.$router.push({ name: "Home" });
                }
              });
          }
        });
      } else {
        // 그림 삭제
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
                SERVER.URL + "/contents/paints/" + this.content.id + "/",
                this.commonConfig
              )
              .then(() => {
                this.$emit("drawRemove", this.content.id);
                const newPaints = this.kid.paints.filter((paint) => {
                  return paint.id !== this.content.id;
                });
                this.kid.paints = newPaints;
              })
              .catch(() => {});
          }
        });
      }
    },
  },
};
</script>

<style scoped>
.custom-card {
  transition: opacity 0.4s ease-in-out;
}

.custom-card:not(.on-hover) {
  opacity: 0.6;
}
.custom-card:hover {
  transform: rotate(15deg);
  cursor: pointer;
}
/* .content-image {
  border: 4px dashed #bcbcbc;
} */
.swing {
  animation: swing ease-in-out 1s infinite alternate;
  transform-origin: center -20px;
  float: left;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
}
.swing img {
  border: 5px solid #f8f8f8;
  display: block;
}
.swing:after {
  content: "";
  position: absolute;
  width: 20px;
  height: 20px;
  border: 1px solid #999;
  top: -10px;
  left: 50%;
  z-index: 0;
  border-bottom: none;
  border-right: none;
  transform: rotate(45deg);
}
/* nail */
.swing:before {
  content: "";
  position: absolute;
  width: 5px;
  height: 5px;
  top: -14px;
  left: 51.5%;
  z-index: 5;
  border-radius: 50% 50%;
  background: #000;
}

@keyframes swing {
  0% {
    transform: rotate(3deg);
  }
  100% {
    transform: rotate(-3deg);
  }
}
</style>