<template>
  <v-expansion-panel cols="6" md="4">
    <v-expansion-panel-header>
      {{ video.script.content }}
      <template v-slot:actions>
        <v-icon color="primary">$expand</v-icon>
      </template>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <video :src="videoUrl" controls width="100%" height="400px"></video>
      <div style="display: flex; justify-content: center" class="mt-5">
        <p v-if="lieDetectResult" style="line-height: 36px">
          아이가 <b :class="resultColor">{{ lieDetectResult }}</b> 답변하고
          있어요.
        </p>
        <p v-else>영상을 분석하고 있어요.</p>
      </div>
      <div class="text-right">
        <a style="color: red" @click="deleteVideo">삭제</a>
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";

import Swal from "sweetalert2";

export default {
  name: "VideoItem",
  data() {
    return {
      lieDetectResult: "",
      resultColor: "",
    };
  },
  props: {
    video: Object,
    key2: Number,
  },
  computed: {
    ...mapState(["kid"]),
    ...mapGetters(["commonConfig"]),
    videoUrl() {
      return SERVER.URL + this.video.file_source;
    },
  },
  methods: {
    deleteVideo() {
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
              SERVER.URL + SERVER.ROUTES.deleteVideo + this.video.id + "/",
              this.commonConfig
            )
            .then(() => {
              const newVideos = this.kid.videos.filter((video) => {
                return video.id !== this.video.id;
              });
              this.kid.videos = newVideos;
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
    getLieDetectResult: function () {
      let result = this.video.analysis;
      if (result == "true") {
        this.lieDetectResult = "솔직히";
        this.resultColor = "greenfont";
      } else if (result == "lie") {
        this.lieDetectResult = "상상해서";
        this.resultColor = "redfont";
      } else if (result == "nature") {
        this.lieDetectResult = "부담없이";
        this.resultColor = "bluefont";
      } else {
        this.lieDetectResult = "";
      }
    },
  },
  created() {
    this.getLieDetectResult();
    console.log(this.video);
  },
};
</script>

<style>
.redfont {
  color: red;
}
.bluefont {
  color: blue;
}
.greenfont {
  color: green;
  margin-top: 10px;
}
</style>