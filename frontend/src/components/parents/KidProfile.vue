<template>
  <div class="row my-5 mx-5">
    <!-- <div class="col-lg-2 col-md-3 col-4 box"> -->
    <div class="col-lg-12 text-center">
      <v-avatar v-if="imageLoaded" size="120px">
        <img
          v-if="!existImage"
          src="../../assets/default_kid.png"
          alt="kids-profile"
        />
        <img v-if="existImage" :src="imagePath" alt="kids-profile" />
      </v-avatar>
    </div>
    <div class="col-12 text-center my-auto">
      <v-btn @click="moveToChildPage">{{ kid.name }} 놀이터</v-btn>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import { mapState } from "vuex";
import SERVER from "@/api/drf";

// import axios from 'axios'
export default {
  name: "KidProfile",
  data: function () {
    return {
      imageLoaded: false,
      existImage: false,
    };
  },
  computed: {
    ...mapState(["kid"]),
    imagePath() {
      return SERVER.URL + this.kid.image;
    },
  },

  methods: {
    moveToChildPage() {
      router.push({ name: "KidsMainView", params: { kidId: this.kid.id } });
    },
  },
  watch: {
    kid: function () {
      this.imageLoaded = true;
      if (this.kid.image != "/media/default_image.jpg") {
        this.existImage = true;
      }
    },
  },
};
</script>

<style>
.box {
  width: 150px;
  height: 150px;
  border-radius: 70%;
  overflow: hidden;
}
</style>
