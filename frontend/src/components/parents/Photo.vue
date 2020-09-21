<template>
  <v-row>
    <v-col offset="2" cols="8">
      <v-container fluid>
        <v-row>
          <v-col v-for="i in 6" :key="i" cols="6" md="4">
            <ContentImage />
          </v-col>
        </v-row>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import ContentImage from "@/components/parents/ContentImage.vue";

export default {
  name: "Photo",
  components: {
    ContentImage,
  },
};
</script>

<style>
</style>