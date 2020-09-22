<template>
  <div class="kid-main">
    <!-- 윗 탭 -->
    <v-col class="text-center my-10">
      <!-- 그림그리기 -->
      <v-btn color="error mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-image fa-4x"></i>
      </v-btn>
      <!-- 사진찍기 -->
      <v-btn color="cyan mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-camera fa-4x"></i>
      </v-btn>
      <!-- 동요부르기 -->
      <v-btn color="green mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-music fa-4x"></i>
      </v-btn>
    </v-col>

    <!-- 캐릭터 -->
    <v-col class="text-center my-10">
      <!-- 기본 -->
      <img
        v-if="!actionOnOff"
        class="character"
        src="../../assets/characters/character.png"
        height="240px"
        width="150px"
        alt="character"
      />
      <!-- 행동 -->
      <div v-else class="action-box">
        <div :class="doAction"></div>
      </div>
    </v-col>

    <!-- 아랫 탭 -->
    <v-col class="text-center my-10">
      <!-- 식사하기 -->
      <v-btn
        @click="actionNum = 1; actionOnOff = true;"
        color="error mx-15 px-14 py-14"
        fab
        x-large
        dark
      >
        <i class="fa fa-utensils fa-4x"></i>
      </v-btn>

      <!-- 대화하기 -->
      <v-btn color="cyan mx-15 px-14 py-14" fab x-large dark>
        <i class="fa fa-phone fa-4x"></i>
      </v-btn>

      <!-- 씻기 -->
      <v-btn
        @click="actionNum = 2; actionOnOff = true;"
        color="green mx-15 px-14 py-14"
        fab
        x-large
        dark
      >
        <i class="fa fa-shower fa-4x"></i>
      </v-btn>
    </v-col>
  </div>
</template>

<script>
export default {
  name: "KidsMainView",
  data: function () {
    return {
      actionOnOff: false,
      actionNum: 0,
      actionCnt: 0,
    };
  },
  methods: {
    characterNonActionAlgo: function () {
      let cnt = this.actionCnt;
      let nonActionList = [3, 4];
      let nonActionNum =
        nonActionList[Math.floor(Math.random() * nonActionList.length)];
      let rand = Math.random() * (10000 - 3000) + 3000;
      setTimeout(() => {
        if (cnt == this.actionCnt) {
          this.actionOnOff = true;
          this.actionNum = nonActionNum;
        }
      }, rand);
    },
    actionTimer: function (ms) {
      setTimeout(() => {
        this.actionOnOff = false;
        this.actionNum = 0;
        this.characterNonActionAlgo();
      }, ms);
    },
    wasAction: function () {
      this.actionCnt += 1;
    },
  },
  computed: {
    doAction: function () {
      if (this.actionNum == 0) {
        return "non-action";
      } else {
        this.wasAction();
        this.actionTimer(3000);
        if (this.actionNum == 1) {
          return "eating";
        } else if (this.actionNum == 2) {
          return "washing";
        } else if (this.actionNum == 3) {
          return "greeting";
        } else if (this.actionNum == 4) {
          return "heart-dancing";
        }
      }
      return "non-action";
    },
  },
  created: function () {
    this.characterNonActionAlgo();
  },
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