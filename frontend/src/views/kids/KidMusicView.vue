<template>
  <div
    class="kid-main"
    style="display: flex; justify-content: center; align-items: center"
  >
    <v-row>
      <v-col
        cols="4"
        style="display: flex; justify-content: center; align-items: center"
        ><div v-if="isStart" class="action-box">
          <div class="dancing"></div>
        </div>
        <img
          v-else
          class="character"
          src="../../assets/characters/character.png"
          height="240px"
          width="150px"
          alt="character"
        />
      </v-col>

      <v-col
        cols="4"
        style="
          display: flex;
          justify-content: center;
          align-items: center;
          flex-direction: column;
        "
      >
        <v-btn @click="start" class="blue" v-if="!isStart">
          싹이 싹이 나네요 ♪
        </v-btn>

        <v-btn @click="back" class="red mt-4" v-if="!isStart"> 뒤로 </v-btn>

        <div>
          <h3 style="text-align: center">{{ text1 }}</h3>
        </div>
        <div>
          <h3 style="text-align: center">{{ text2 }}</h3>
        </div></v-col
      >
      <v-col
        cols="4"
        style="display: flex; justify-content: center; align-items: center"
        ><div v-if="isStart" class="action-box">
          <div class="dancing"></div>
        </div>
        <img
          v-else
          class="character"
          src="../../assets/characters/character.png"
          height="240px"
          width="150px"
          alt="character"
        />
      </v-col>
    </v-row>

    <audio id="1" src="../../assets/music/1.wav"></audio>
  </div>
</template>

<script>
export default {
  name: "KidMusicView",
  data: function () {
    return {
      text1: "",
      text2: "",
      isStart: false,
    };
  },
  methods: {
    start: function () {
      this.isStart = true;
      var audio = document.getElementById("1");
      audio.play();
      setTimeout(() => {
        this.text1 = "싹이 싹이 나네요 작은 새싹이나네요.";
        this.text2 = "둥근둥근 씨앗이 이쁜 새싹이 되어요.";
      }, 8000);
      setTimeout(() => {
        this.text1 = "싹이트고 자라서 커다란 나무가 되면";
        this.text2 = "새들의 놀이터 되지요~";
      }, 18000);
      setTimeout(() => {
        this.text1 = "싹이 싹이 나네요 작은 새싹이나네요";
        this.text2 = "어서어서 자라서 함께함께 놀아요";
      }, 28000);
      setTimeout(() => {
        this.text1 = "싹이 싹이 나네요 작은 새싹이나네요.";
        this.text2 = "둥근둥근 씨앗이 이쁜 새싹이 되어요.";
      }, 42000);
      setTimeout(() => {
        this.text1 = "싹이트고 자라서 커다란 나무가 되면";
        this.text2 = "새들의 놀이터 되지요~";
      }, 50000);
      setTimeout(() => {
        this.text1 = "싹이 싹이 나네요 작은 새싹이나네요";
        this.text2 = "어서어서 자라서 함께함께 놀아요";
      }, 60000);
      setTimeout(() => {
        this.text1 = "";
        this.text2 = "";
        this.isStart = false;
      }, 70000);
    },
  },
  computed: {},
  created: function () {},
};
</script>

<style>
.kid-main {
  background-image: url("../../assets/characters/house.png");
  background-position: center center;
  background-size: cover;
  width: 100%;
  height: 100%;
}
.dancing {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/basicDance.png") left center;
  animation: play-dancing 1.5s steps(10);
  animation-iteration-count: infinite;
}
@keyframes play-dancing {
  100% {
    background-position: -2400px;
  }
}
</style>