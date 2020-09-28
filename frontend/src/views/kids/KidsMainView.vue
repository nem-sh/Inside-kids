<template>
  <div
    class="kid-main"
    style="display: flex; justify-content: center; align-items: center"
  >
    <div>
      <!-- 윗 탭 -->
      <v-col class="text-center my-10">
        <div style="display: flex; justify-content: center">
          <!-- 그림그리기 -->
          <button
            v-if="!(hungry || dirty || sleep || actionOnOff)"
            @click="godrawing"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/draw.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/drawBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
          <!-- 사진찍기 -->
          <button
            v-if="!(hungry || dirty || sleep || actionOnOff)"
             @click="gopicture"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/photo.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/photoBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
          <!-- 동요부르기 -->
          <button
            v-if="!(hungry || dirty || sleep || actionOnOff)"
            @click="goMusic"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/sing.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/singBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
        </div>
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
        <div
          v-else
          style="display: flex; justify-content: center; align-items: center"
        >
          <div style="z-index: 2; position: absolute">
            <img
              v-if="!sleep && hungry && actionNum != 1 && actionNum != 2"
              src="../../assets/characters/wantEat.png"
              height="140px"
              width="150px"
              style="position: absolute; top: -200px; right: -250px"
            />
            <img
              v-if="
                !sleep && dirty && !hungry && actionNum != 1 && actionNum != 2
              "
              src="../../assets/characters/wantDirty.png"
              height="140px"
              width="150px"
              style="position: absolute; top: -200px; right: -250px"
            />
          </div>
          <div style="z-index: 2; position: absolute">
            <img
              v-if="actionNum == 2"
              src="../../assets/characters/bath.png"
              width="350px"
              style="position: absolute; top: -35px; right: -180px"
            />
          </div>
          <div class="action-box">
            <div :class="doAction" style="z-index: 1"></div>
          </div>
        </div>
      </v-col>

      <!-- 아랫 탭 -->
      <v-col class="text-center my-10">
        <div style="display: flex; justify-content: center">
          <!-- 먹기 -->
          <button
            v-if="!sleep && (!actionOnOff || hungry)"
            @click="eat"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/eat.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/eatBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
          <!-- 대화 -->
          <button
            v-if="!(hungry || dirty || sleep || actionOnOff)"
            @click="gotalking"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/talk.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/talkBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
          <!-- 씻기 -->
          <button
            v-if="!sleep && (!actionOnOff || dirty)"
            @click="wash"
            style="margin: 50px"
          >
            <v-img
              src="../../assets/icons/wash.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <div v-else style="margin: 50px">
            <v-img
              src="../../assets/icons/washBlack.png"
              alt
              style="width: 120x; width: 120px"
            />
          </div>
        </div>
      </v-col>

      <!-- 효과음 -->
      <audio
        id="eat-sound"
        src="../../assets/characterSounds/eating.mp3"
      ></audio>
      <audio
        id="wash-sound"
        src="../../assets/characterSounds/washing.mp3"
      ></audio>
      <audio
        id="hungry-sound"
        src="../../assets/characterSounds/hungry.mp3"
      ></audio>
      <audio
        id="door-sound"
        src="../../assets/characterSounds/door.mp3"
      ></audio>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import axios from "axios";
import SERVER from "@/api/drf";
import { mapActions, mapGetters, mapState, mapMutations } from "vuex";
export default {
  name: "KidsMainView",
  data: function () {
    return {
      actionOnOff: false,
      actionNum: 0,
      actionCnt: 0,
      hungry: false,
      dirty: false,
      sleep: false,
    };
  },
  methods: {
    ...mapMutations(["SET_CHARACTER"]),
    ...mapActions(["getCharacter"]),
    loaddata() {
      Swal.fire({
        position: "center",
        icon: "success",
        title: "서비스 준비 중 입니다!",
        showConfirmButton: false,
        timer: 1000,
      });
    },
    godrawing() {
      this.$router.push({ name: "KidsDrawingView" });
    },
    goMusic() {
      this.actionOnOff = true;
      this.actionNum = 99;
      var audio = document.getElementById("door-sound");
      audio.play();
      setTimeout(() => {
        this.$router.push(`/child/${this.$route.params.kidId}/music`);
      }, 1500);
    },
    gotalking() {
      this.$router.push({ name: "KidsTalkingView" });
    },
    gopicture() {
      this.$router.push({ name: "KidsPictureView" });
    },
    characterNonActionAlgo: function () {
      let now = new Date();
      let nowHours = now.getHours();
      if (nowHours > 19 || 7 > nowHours) {
        this.sleep = true;
      }
      if (new Date(this.character.eat_time) - now < -30000) {
        this.hungry = true;
      }
      if (new Date(this.character.wash_time) - now < -120000) {
        this.dirty = true;
      }
      if (!(this.hungry || this.dirty)) {
        let cnt = this.actionCnt;
        let nonActionList = [3, 4];
        let nonActionNum =
          nonActionList[Math.floor(Math.random() * nonActionList.length)];
        let rand = Math.random() * (10000 - 3000) + 10000;
        setTimeout(() => {
          if (cnt == this.actionCnt) {
            this.actionOnOff = true;
            this.actionNum = nonActionNum;
          }
        }, rand);
      } else {
        this.actionOnOff = true;
      }
    },
    actionTimer: function (ms) {
      let cnt = this.actionCnt;
      setTimeout(() => {
        if (cnt == this.actionCnt) {
          this.actionOnOff = false;
          this.actionNum = 0;
          this.characterNonActionAlgo();
        }
      }, ms);
    },
    wasAction: function () {
      this.actionCnt += 1;
    },
    eat: function () {
      this.actionNum = 1;
      this.actionOnOff = true;
      this.hungry = false;
      var audio1 = document.getElementById("hungry-sound");
      audio1.pause();
      var audio2 = document.getElementById("eat-sound");
      audio2.play();
      axios
        .put(
          SERVER.URL +
            SERVER.ROUTES.getCharacterInfo +
            this.$route.params.kidId +
            "/",
          { eat_time: new Date(), wash_time: this.character.wash_time },
          this.commonConfig
        )
        .then(() => {
          // this.SET_CHARACTER(null);

          this.getCharacter(this.$route.params.kidId);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    wash: function () {
      this.actionNum = 2;
      this.actionOnOff = true;
      var audio = document.getElementById("wash-sound");
      audio.play();
      setTimeout(() => {
        audio.pause();
      }, 3000);
      axios
        .put(
          SERVER.URL +
            SERVER.ROUTES.getCharacterInfo +
            this.$route.params.kidId +
            "/",
          { eat_time: this.character.eat_time, wash_time: new Date() },
          this.commonConfig
        )
        .then(() => {
          // this.SET_CHARACTER(null);
          this.dirty = false;
          this.getCharacter(this.$route.params.kidId);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    hungrySoundOn: function () {
      if (this.hungry) {
        var audio = document.getElementById("hungry-sound");
        audio.play();
        setTimeout(() => {
          this.hungrySoundOn();
        }, 10000);
      }
    },
  },
  computed: {
    ...mapState(["character"]),
    ...mapGetters(["commonConfig"]),
    doAction: function () {
      if (this.actionNum == 0) {
        if (this.sleep) {
          return "sleeping";
        }
        if (this.hungry) {
          this.hungrySoundOn();
          return "hungry";
        } else if (this.dirty) {
          return "dirty";
        }
      } else {
        this.wasAction();
        if (this.actionNum == 1) {
          this.actionTimer(3000);
          return "eating";
        } else if (this.actionNum == 2) {
          this.actionTimer(6000);
          return "washing";
        } else if (this.actionNum == 3) {
          this.actionTimer(3000);
          return "greeting";
        } else if (this.actionNum == 4) {
          this.actionTimer(3000);
          return "heart-dancing";
        }
      }
      return "non-action";
    },
  },
  watch: {
    character: function () {
      this.characterNonActionAlgo();
    },
  },

  created: function () {
    this.getCharacter(this.$route.params.kidId);
  },
};
</script>

<style>
.kid-main {
  background-image: url("../../assets/backgrounds/house.png");
  background-position: center center;
  background-size: cover;
  width: 100%;
  height: 100%;
}
.action-box {
  display: flex;
  justify-content: center;
}
.non-action {
  width: 240px;
  height: 240px;
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
  animation: play-washing 3s steps(19);
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
  animation: play-sleeping 3s steps(10);
  animation-iteration-count: infinite;
}
@keyframes play-sleeping {
  100% {
    background-position: -2400px;
  }
}
.hungry {
  width: 240px;
  height: 240px;
  background: url("../../assets/characters/hungry.png") left center;
  animation: play-hungry 8s steps(18);
  animation-iteration-count: infinite;
}
@keyframes play-hungry {
  100% {
    background-position: -4320px;
  }
}
.dirty {
  width: 145px;
  height: 240px;
  background: url("../../assets/characters/dirty.png") left center;
}
/* .character {
  position: relative;
  top: 45%;
  left: 40%;
} */
</style>