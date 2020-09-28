<template>
  <v-avatar tile size="100px" color="white">
    <img :src="kidImg" alt="kid-profile" />
  </v-avatar>
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "KidImage2",
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