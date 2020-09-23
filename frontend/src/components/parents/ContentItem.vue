<template>
  <v-col cols="6" md="4">
    <v-hover v-slot:default="{ hover }">
      <v-card
        @click.stop="dialog=true"
        class="custom-card"
        :elevation="hover ? 12 : 2"
        :class="{ 'on-hover': hover }"
      >
        <img :src="contentImg" alt="content-image" width="100%" height="150px" />
        <p>{{content.created_at.slice(0,10)}}</p>
      </v-card>
    </v-hover>
    <v-dialog v-model="dialog" max-width="40rem">
      <template>
        <v-card class="d-inline-block mx-auto">
          <v-container>
            <v-row justify="space-between">
              <v-col cols="10" class="mx-auto mt-5 swing">
                <img
                  class="content-image"
                  :src="contentImg"
                  alt="content-image"
                  width="100%"
                  height="auto"
                />
              </v-col>

              <v-col cols="12" class="text-center pl-0">
                <div class="my-2 d-flex justify-end">
                  <div class="mr-5">
                    <v-btn color="cyan lighten-1" dark>
                      <a
                        style="text-decoration:none; color:white"
                        :download="content.file_source"
                        :href="content.file_source"
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
import SERVER from "@/api/drf";

export default {
  name: "ContentItem",
  props: {
    content: Object,
  },
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    contentImg() {
      return SERVER.URL + this.content.file_source;
    },
  },
  methods: {
    sendLink() {
      window.Kakao.Link.sendCustom({
        templateId: 37115,
        templateArgs: {
          THU: this.contentImg,
        },
      });
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