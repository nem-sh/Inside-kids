<template>
  <v-row>
    <v-col offset="2" cols="8" class="mt-10">
      <h1 v-if="!kid.videos.length" class="text-center pt-10">
        <i class="fas fa-exclamation-triangle" style="color:orange"></i> 기록이 없습니다.
      </h1>
      <v-expansion-panels>
        <v-expansion-panel v-for="video in kid.videos" :key="video.id" cols="6" md="4">
          <v-expansion-panel-header>
            날짜?
            <template v-slot:actions>
              <v-icon color="primary">$expand</v-icon>
            </template>
          </v-expansion-panel-header>
          <v-expansion-panel-content>비디오 넣을 곳</v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "VideoList",
  computed: {
    ...mapState(["kid"]),
  },
};
</script>

<style>
</style>