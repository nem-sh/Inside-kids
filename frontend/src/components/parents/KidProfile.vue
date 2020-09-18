<template>
  <div class="row my-5 mx-5">
    <!-- <div class="col-lg-2 col-md-3 col-4 box"> -->
    <div class="col-lg-12 text-center">
      <v-avatar size="120px">
        <img src="@/assets/default_image.jpg" alt />
      </v-avatar>
    </div>
    <div class="col-12 text-center my-auto">
      <v-btn>대화하기</v-btn>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: "KidProfile",
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
