<template>
  <div
    class="kid-music"
    style="
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    "
  >
    <div v-if="isStart" class="sun"></div>
    <v-row
      style="
        display: flex;
        justify-content: flex-end;
        align-items: center;
        flex-direction: column;
      "
    >
      <v-btn @click="back" class="blue" style="font-size: 2em" height="70" v-if="!isStart">
        <i class="fas fa-home"></i>
      </v-btn>
      <v-btn
        @click="music1"
        class="green mt-4"
        style="font-size: 2em"
        height="70"
        v-if="!isStart"
        width="100%"
      >싹이 싹이 나네요 ♪</v-btn>
      <v-btn
        @click="music2"
        class="orange mt-4"
        style="font-size: 2em"
        height="70"
        v-if="!isStart"
        width="100%"
      >하루 ♪</v-btn>

      <div>
        <h1 style="text-align: center">{{ text1 }}</h1>
      </div>
      <div>
        <h1 style="text-align: center">{{ text2 }}</h1>
      </div>
    </v-row>
    <v-row style="display: flex; justify-content: center; align-items: center">
      <div
        v-if="isStart"
        class="action-box"
        style="display: flex; justify-content: center; align-items: center"
      >
        <div class="dancing"></div>
        <img
          v-if="isMusic1"
          class="character"
          src="../../assets/characters/sprout.png"
          height="280px"
          width="350px"
          alt="character"
        />
      </div>
      <div v-else>
        <img
          class="character"
          src="../../assets/characters/character.png"
          height="480px"
          width="300px"
          alt="character"
        />
      </div>
    </v-row>

    <audio id="1" src="../../assets/music/1.wav"></audio>

    <audio id="2" src="../../assets/music/2.mp3"></audio>
  </div>
</template>

<script>
export default {
  name: "KidsMusicView",
  data: function () {
    return {
      text1: "",
      text2: "",
      isStart: false,
      isMusic1: false,
    };
  },
  methods: {
    music1: function () {
      this.isStart = true;
      var audio = document.getElementById("1");
      this.isMusic1 = true;
      audio.play();
      this.text1 = "싹이 싹이 나네요 ♪";

      this.text2 = "";
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

        this.isMusic1 = false;
      }, 70000);
    },
    music2: function () {
      this.isStart = true;
      var audio = document.getElementById("2");
      audio.play();
      this.text1 = "하루 ♪";
      this.text2 = "";
      setTimeout(() => {
        this.text1 = "해가 오면 날이 밝아";
        this.text2 = "아침이 되고";
      }, 5000);
      setTimeout(() => {
        this.text1 = "낮이되면 해가 ";
        this.text2 = "세상 가득 비추죠";
      }, 12000);
      setTimeout(() => {
        this.text1 = "붉게 물든 하늘도";
        this.text2 = "해가 떠나면";
      }, 20000);
      setTimeout(() => {
        this.text1 = "까만하늘위에";
        this.text2 = "달이 찾아오지요";
      }, 26000);
      setTimeout(() => {
        this.text1 = "전주 ♪";
        this.text2 = "";
      }, 35000);
      setTimeout(() => {
        this.text1 = "해가 오면 날이 밝아";
        this.text2 = "아침이 되고";
      }, 40000);
      setTimeout(() => {
        this.text1 = "낮이되면 해가 ";
        this.text2 = "세상 가득 비추죠";
      }, 47000);
      setTimeout(() => {
        this.text1 = "붉게 물든 하늘도";
        this.text2 = "해가 떠나면";
      }, 55000);
      setTimeout(() => {
        this.text1 = "까만하늘위에";
        this.text2 = "달이 찾아오지요";
      }, 61000);
      setTimeout(() => {
        this.text1 = "";
        this.text2 = "";
        this.isStart = false;
      }, 70000);
    },
    back: function () {
      this.$router.push(`/child/${this.$route.params.kidId}`);
    },
  },
  computed: {},
  created: function () {},
};
</script>

<style>
.kid-music {
  background-image: url("../../assets/backgrounds/music.jpeg");
  background-position: center center;
  background-size: cover;
  width: 100%;
  height: 100%;
}
.dancing {
  width: 480px;
  height: 480px;
  background: url("../../assets/characters/basicDanceX2.png") left center;
  animation: play-dancing 1.5s steps(10);
  animation-iteration-count: infinite;
}
@keyframes play-dancing {
  100% {
    background-position: -4800px;
  }
}
.sun {
  width: 180px;
  height: 180px;
  background: url("../../assets/characters/sun.png") left center;
  animation: play-sun 1.5s steps(8);
  animation-iteration-count: infinite;
  position: absolute;
  top: 100px;
  right: 100px;
}
@keyframes play-sun {
  100% {
    background-position: -1496px;
  }
}
h1 {
  font-size: 2.5em;
  text-shadow: -0.5px 0 white, 0 0.5px white, 0.5px 0 white, 0 -0.5px white;
}
</style>