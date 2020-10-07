<template>
  <v-avatar size="40px">
    <img v-if="!existImage" src="../../assets/default_kid.png" alt="kids-profile" />
    <img v-if="existImage" :src="imagePath" alt="kids-profile" />
  </v-avatar>
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "KidImage",
  data: function () {
    return {
      existImage: false,
    };
  },
  props: {
    image: String,
  },
  computed: {
    imagePath() {
      return SERVER.URL + this.image;
    },
  },
  created: function () {
    if (this.image != "/media/default_image.jpg") {
      this.existImage = true;
    }
  },
};
</script>
