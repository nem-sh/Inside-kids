<template>
  <v-row>
    <v-col offset="2" cols="8" class="mt-10">
      <h1 v-if="!kid.videos.length" class="text-center pt-10">
        <i class="fas fa-exclamation-triangle" style="color:orange"></i> 기록이 없습니다.
      </h1>
      <v-expansion-panels>
        <VideoItem v-for="video in kid.videos" :key="video.id" :video="video" />
      </v-expansion-panels>
    </v-col>
  </v-row>
</template>

<script>
import { mapActions, mapState } from "vuex";

import VideoItem from "@/components/parents/VideoItem";

export default {
  name: "VideoList",
  components: {
    VideoItem,
  },
  computed: {
    ...mapState(["kid", "authToken"]),
  },
  methods: {
    ...mapActions(["getKid"]),
  },
};
</script>

<style>
</style>