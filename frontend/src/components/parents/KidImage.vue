<template>
  <v-avatar size="40px">
    <img :src="kidImg" alt="kid-profile" />
  </v-avatar>
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "KidImage",
  props: {
    image: String,
  },
  computed: {
    kidImg() {
      return SERVER.URL + this.image;
    },
  },
};
</script>

<style>
</style>