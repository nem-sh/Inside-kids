<template>
  <div>
    <div :class="characterState"></div>
    <!-- <img
      class="character"
      src="../../assets/characters/talking.png"
      height="600px"
      width="500px"
      alt="character"
    />-->
    <div class="text-center">
      <div v-show="!result">
        <!-- <h4 class="title is-4">{{ timer.interval ? `${formatedTime}` : "00:00:00" }}</h4> -->
        <video v-show="false" ref="video"></video>
      </div>
      <div v-show="result">
        <video v-show="false" controls :src="blobUrl"></video>
      </div>
      <div>
        <!-- <v-btn @click="stop" v-if="recorder && recorder.getState() === 'recording'">
          <i class="fas fa-arrow-right"></i>
        </v-btn>-->
        <!-- <v-btn class="button is-primary" @click="record" v-else>말하기</v-btn> -->
        <div v-for="(script, index) in scripts" :key="script.id">
          <audio
            :id="`script` + index"
            :src="server + script.file_source"
          ></audio>
        </div>
        <audio id="reaction"></audio>
        <button v-show="characterState === 'stop'" @click="nextScript">
          <img src="../../assets/icons/scriptNext.png" alt="script-next" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import axios from "axios";
import SERVER from "@/api/drf";
import { mapGetters, mapState } from "vuex";
import RecordRTC from "recordrtc";

export default {
  name: "KidsTalking",
  data() {
    return {
      recorder: null,
      result: null,
      blobUrl: null,
      timer: {
        interval: null,
        value: 0,
      },
      scripts: [],
      index: 0,
      characterState: "stop",
      server: SERVER.URL,
      recordFlag: false,
      startFlag: false,
      scriptsLoaded: false,
      reactions: ["react1"],
    };
  },
  computed: {
    ...mapState(["authToken"]),
    ...mapGetters(["commonConfig"]),
    formatedTime() {
      let hour = Math.floor(this.timer.value / 3600);
      let minute = Math.floor((this.timer.value - hour * 3600) / 60);
      let seconds = this.timer.value - (hour * 3600 + minute * 60);
      return [hour, minute, seconds].map(this._fillzero).join(":");
    },
  },
  methods: {
    loaddata() {
      Swal.fire({
        position: "center",
        icon: "success",
        title: "서비스 준비 중 입니다!",
        showConfirmButton: false,
        timer: 2000,
      });
    },
    _fillzero(value) {
      return value < 9 ? "0" + value : value;
    },
    record() {
      this.recorder && this.recorder.startRecording();
      this.result = null;
      this.blobUrl && URL.revokeObjectURL(this.blobUrl);
      this.blobUrl = null;
      this.timer.interval = setInterval(() => ++this.timer.value, 1000);
    },
    stop() {
      var scriptId = this.scripts[this.index - 1].id;
      this.recorder.stopRecording(() => {
        this.result = this.recorder.getBlob();
        this.blobUrl = window.URL.createObjectURL(this.result);
        if (this.scripts[this.index - 1].state === 0) {
          var formData = new FormData();
          formData.append("file_source", this.result, "video");
          const axiosConfig = {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `jwt ${this.authToken}`,
            },
          };
          axios
            .post(
              SERVER.URL +
                "/contents/kids/" +
                this.$route.params.kidId +
                "/scripts/" +
                scriptId +
                "/videos/",
              formData,
              axiosConfig
            )
            .then(() => {})
            .catch((err) => {
              if (err.response.status == 403) {
                alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
                router.push({ name: "Home" });
              } else {
                console.log(err.response);
              }
            });
        }
        // console.log(this.result, "result");
        // console.log(this.blobUrl, "url");
        clearInterval(this.timer.interval);
        this.timer.value = 0;
        this.timer.interval = null;
      });
    },
    getScripts() {
      const hello = ["hello1"];
      const bye = ["bye1"];
      // 오디오 가져오는 axios & push
      axios
        .get(
          SERVER.URL +
            "/contents/kids/" +
            this.$route.params.kidId +
            "/scripts/",
          this.commonConfig
        )
        .then((res) => {
          // 랜덤으로 처음에 인사 넣기
          var rand1 = hello[Math.floor(Math.random() * hello.length)];
          this.scripts.push({
            id: 0,
            file_source: `/media/greeting/${rand1}.mp3`,
            state: 2,
          });
          // 준비한 질문 넣기
          res.data.forEach((script) => {
            this.scripts.push({
              id: script.id,
              file_source: `/media/audio/${script.id}.wav`,
              state: script.state,
            });
          });
          this.scripts.push();
          // 랜덤으로 끝에 인사 넣기
          var rand2 = bye[Math.floor(Math.random() * bye.length)];
          this.scripts.push({
            id: -1,
            file_source: `/media/greeting/${rand2}.mp3`,
            state: 2,
          });
          this.LoadCheck();
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
            router.push({ name: "Home" });
          } else {
            console.log(err.response);
          }
        });
    },
    LoadCheck() {
      if (document.getElementById("script0")) {
        if (this.index == 0) {
          this.nextScript();
        }
      } else {
        setTimeout(() => {
          this.LoadCheck();
        }, 1);
      }
    },

    nextScript() {
      // 녹화중이었다면 중지 & 저장
      if (this.recordFlag) {
        this.stop();
        this.recordFlag = false;
      }
      // 사용자가 등록한 질문 녹화
      if (this.scripts[this.index].state === 0 || this.index === 6) {
        this.record();
        this.recordFlag = true;
      }

      // 처음 질문과 끝 인사 제외하고 리액션 넣기
      var react_duration = 0;
      if (this.index > 1 && this.index < this.scripts.length) {
        react_duration = 2000;
        var react_audio = document.getElementById("reaction");
        var rand3 = this.reactions[
          Math.floor(Math.random() * this.reactions.length)
        ];
        react_audio.src = this.server + `/media/reaction/${rand3}.wav`;
        react_audio.play();
      }

      // 오디오 실행
      var audio = document.getElementById(`script${this.index}`);
      setTimeout(() => {
        audio.play();
      }, react_duration);
      // var audio = document.querySelector("audio").play();

      // if (audio !== undefined) {
      //   audio.then(function () {}).catch(function () {});
      // }

      this.characterState = "talking";

      // 입모양 움직이기
      setTimeout(() => {
        this.characterState = "stop";
        this.index += 1;
        if (this.index === this.scripts.length) {
          this.$router.push({
            name: "KidsMainView",
            params: { kidId: this.$route.params.kidId },
          });
        }
      }, react_duration + audio.duration * 1000);
    },
  },
  created() {
    this.getScripts();
  },
  mounted() {
    let self = this;
    let video = self.$refs.video;
    navigator.mediaDevices
      .getUserMedia({
        video: true,
        audio: true,
      })
      .then(async function (stream) {
        self.recorder = RecordRTC(stream, {
          type: "video",
        });
        video.srcObject = stream;
        video.volume = 0;
        video.play();
      });
  },
  beforeDestroy() {
    location.reload();
  },
};
</script>

<style scoped>
/* video {
  display: block;
  margin: 0 auto;
  box-shadow: 0 4px 8px 2px #999;
} */
.stop {
  width: 680px;
  height: 767px;
  background: url("../../assets/characters/talking.png") left center;
}
.talking {
  width: 680px;
  height: 767px;
  background: url("../../assets/characters/talkingIng.png") left center;
  animation: play-talking 0.6s steps(3);
  animation-iteration-count: infinite;
}

@keyframes play-talking {
  100% {
    background-position: -2040px;
  }
}
</style>
