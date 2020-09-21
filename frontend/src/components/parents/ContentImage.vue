<template>
  <img :src="contentImg" alt="content-image" />
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "contentImage",
  props: {
    image: String,
  },
  computed: {
    contentImg() {
      return SERVER.URL + this.image;
    },
  },
};
</script>

<style>
</style>