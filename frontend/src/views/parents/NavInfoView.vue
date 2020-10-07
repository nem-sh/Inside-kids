<template>
  <div>
    <Nav />
    <div class="py-5"></div>
    <v-container class="text-center">
      <h2 class="display-2 font-weight-bold mb-3">How to use</h2>

      <v-responsive class="mx-auto mb-8" width="56">
        <v-divider class="mb-1"></v-divider>

        <v-divider></v-divider>
      </v-responsive>
    </v-container>
    <p align="middle">
      <iframe
        src="https://www.youtube.com/embed/nNONgE0KWR4"
        frameborder="no"
        scrolling="no"
        width="50%"
        height="400"
        allow="autoplay"
        allowfullscreen
      ></iframe>
    </p>
    <div class="py-5"></div>
  </div>
</template>

<script>
import Nav from "@/components/Navigation";
export default {
  name: "NavInfoView",
  components: {
    Nav,
  },
};
</script>
