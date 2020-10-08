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
            .catch(() => {});
        }
      });
    },
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