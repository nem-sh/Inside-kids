<template>
  <v-avatar class="img-border" size="100px" color="black">
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
.img-border {
  border: 4px solid black;
}
</style>