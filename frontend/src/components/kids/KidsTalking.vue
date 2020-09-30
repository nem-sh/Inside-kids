<template>
  <div>
        <img
          class="character"
          src="../../assets/characters/talking.png"
          height="600px"
          width="500px"
          alt="character"
        />
    <div class="text-center">
      <div v-show="!result">
        <h4 class="title is-4">
          {{ timer.interval ? `${formatedTime}` : "00:00:00" }}
        </h4>
        <video v-show="false" ref="video"></video>
      </div>
      <div v-show="result">
        <video v-show="false" controls :src="blobUrl"></video>
      </div>
      <div>
        <v-btn
          class="button is-danger"
          @click="stop"
          v-if="recorder && recorder.getState() === 'recording'"
        >
          <i class="fas fa-arrow-right"></i>
        </v-btn>
        <v-btn class="button is-primary" @click="loaddata" v-else>
          말하기
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import axios from "axios";
import SERVER from "@/api/drf";
import { mapActions, mapState } from "vuex";
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
    };
  },
  computed: {
    ...mapState(["kid", "authToken"]),
    ...mapActions(["getKid"]),
    formatedTime() {
      let hour = Math.floor(this.timer.value / 3600);
      let minute = Math.floor((this.timer.value - hour * 3600) / 60);
      let seconds = this.timer.value - (hour * 3600 + minute * 60);
      return [hour, minute, seconds].map(this._fillzero).join(":");
    },
  },
  methods: {
    loaddata(){
      Swal.fire({
        position: 'center',
        icon: 'success',
        title: '서비스 준비 중 입니다!',
        showConfirmButton: false,
        timer: 2000
      })
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
      this.recorder.stopRecording(() => {
        this.result = this.recorder.getBlob();
        this.blobUrl = window.URL.createObjectURL(this.result);
        var formData = new FormData();
        formData.append("file_source", this.result, "video");
        console.log(formData);
        const axiosConfig = {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `jwt ${this.authToken}`,
          },
        };
        console.log(444444444);
        axios
          .post(
            SERVER.URL + "/contents/kids/" + this.kid.id + "/videos/",
            formData,
            axiosConfig
          )
          .then((res) => {
            console.log(res);
            console.log(12345699999999999999999);
          })
          .catch((err) => {
            console.error(err);
            console.log(123456);
          });
        console.log(this.result, "result");
        console.log(this.blobUrl, "url");
        clearInterval(this.timer.interval);
        this.timer.value = 0;
        this.timer.interval = null;
      });
    },
  },
  mounted() {
    let self = this;
    let video = self.$refs.video;
    navigator.mediaDevices
      .getUserMedia({
        video: true,
        audio: true,
      })
      .then(async function(stream) {
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
</style>
