<template>
  <div class="kid-main">
    <v-col class="text-center my-10">
      <v-btn color="error mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-image fa-4x"></i>
      </v-btn>

      <v-btn color="cyan mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-camera fa-4x"></i>
      </v-btn>

      <v-btn color="green mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-music fa-4x"></i>
      </v-btn>
    </v-col>

    <v-col class="text-center my-10">
      <img class="character" src="../../assets/character3.png" height="300px" alt="character" />
    </v-col>

    <v-col class="text-center my-10">
      <v-btn color="error mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-utensils fa-4x"></i>
      </v-btn>

      <v-btn color="cyan mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-phone fa-4x"></i>
      </v-btn>

      <v-btn color="green mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-shower fa-4x"></i>
      </v-btn>
    </v-col>
  </div>
</template>

<script>
export default {
  name: "KidsMainView",
};
</script>

<style>
.kid-main {
  height: 100vh;
  background-image: url("../../assets/room.png");
  background-size: 100vw 100vh;
  background-position: center center;
}
/* .character {
  position: relative;
  top: 45%;
  left: 40%;
} */
</style>