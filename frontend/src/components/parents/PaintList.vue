<template>
  <v-row>
    <v-col offset="2" cols="8">
      <v-container class="pa-4 text-center">
        <v-row class="fill-height" align="center">
          <h1 v-if="!kid.paints.length" class="mx-auto pt-10">
            <i class="fas fa-exclamation-triangle" style="color:orange"></i> 기록이 없습니다.
          </h1>
          <ContentItem v-for="paint in kid.paints" :key="paint.id" :content="paint" />
        </v-row>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";

import ContentItem from "@/components/parents/ContentItem";

export default {
  name: "PaintList",
  components: {
    ContentItem,
  },

  computed: {
    ...mapState(["kid"]),
  },
};
</script>

<style>
</style>