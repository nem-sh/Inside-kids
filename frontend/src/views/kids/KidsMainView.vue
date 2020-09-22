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
.action-box {
  display: flex;
  justify-content: center;
}
.non-action {
}
.eating {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/eat.png") left center;
  animation: play-eating 1.5s steps(12);
  animation-iteration-count: infinite;
}
@keyframes play-eating {
  100% {
    background-position: -2880px;
  }
}
.washing {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/wash.png") left center;
  animation: play-washing 1.5s steps(19);
  animation-iteration-count: infinite;
}
@keyframes play-washing {
  100% {
    background-position: -4560px;
  }
}
.greeting {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/greet.png") left center;
  animation: play-greeting 1.5s steps(4);
  animation-iteration-count: 2;
}
@keyframes play-greeting {
  100% {
    background-position: -960px;
  }
}
.heart-dancing {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/heartDance.png") left center;
  animation: play-heart-dancing 1.5s steps(8);
  animation-iteration-count: 2;
}
@keyframes play-heart-dancing {
  100% {
    background-position: -1920px;
  }
}
.basic-dancing {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/basicDance.png") left center;
  animation: play-basic-dancing 1.5s steps(8);
  animation-iteration-count: 2;
}
@keyframes play-basic-dancing {
  100% {
    background-position: -2400px;
  }
}
.sleeping {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/sleep.png") left center;
  animation: play-sleeping 1.5s steps(8);
  animation-iteration-count: 2;
}
@keyframes play-sleeping {
  100% {
    background-position: -2400px;
  }
}
/* .character {
  position: relative;
  top: 45%;
  left: 40%;
} */
</style>
