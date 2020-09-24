<template>
  <v-expansion-panel cols="6" md="4">
    <v-expansion-panel-header>
      날짜
      <template v-slot:actions>
        <v-icon color="primary">$expand</v-icon>
      </template>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <video :src="videoUrl" controls></video>
    </v-expansion-panel-content>
    <a href="">삭제</a>
  </v-expansion-panel>
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "VideoItem",
  props: {
    video: Object,
    key2:Number,
  },
  computed: {
    videoUrl() {
      return SERVER.URL + this.video.file_source;
    },
  },
};
</script>

<style>
</style>