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
        ><v-btn @click="back" class="blue" v-if="!isStart"
          ><i class="fas fa-home"></i>
        </v-btn>
        <v-btn @click="music1" class="green mt-4" v-if="!isStart" width="140">
          싹이 싹이 나네요 ♪
        </v-btn>
        <v-btn @click="music2" class="orange mt-4" v-if="!isStart" width="140">
          하루 ♪
        </v-btn>

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

    <audio id="2" src="../../assets/music/2.mp3"></audio>
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
    music1: function () {
      this.isStart = true;
      var audio = document.getElementById("1");
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