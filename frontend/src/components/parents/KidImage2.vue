<template>
  <v-avatar class="img-border" size="100px" color="black">
    <img
      v-if="!existImage"
      src="../../assets/default_kid.png"
      alt="kids-profile"
    />
    <img v-if="existImage" :src="imagePath" alt="kids-profile" />
  </v-avatar>
</template>

<script>
import SERVER from "@/api/drf";

export default {
  name: "KidImage2",
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

<style>
.img-border {
  border: 4px solid black;
}
</style>