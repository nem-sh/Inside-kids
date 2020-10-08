<template>
  <div id="webcam-start">
    <div id="app-panel" class="app-panel md-content">
      <div id="webcam-container" class="webcam-container d-none">
        <video id="webcam" autoplay playsinline width="640" height="480"></video>
        <div id="selfie-container">
          <div :id="background[num]"></div>
          <canvas id="canvasPerson" ref="canvas" width="640" height="480"></canvas>
        </div>
      </div>

      <!-- // -->
      <img id="arrowLeft" alt="arrowLeft" src="../../assets/images/arrow-left.png" @click="left" />
      <img
        id="arrowRight"
        alt="arrowRight"
        src="../../assets/images/arrow-right.png"
        @click="right"
      />
      <!-- // -->
      <div id="cameraControls" class="cameraControls">
        <v-col class="text-center">
          <div style="display: flex; justify-content: center">
            <!-- 뒤로가기 -->
            <button v-if="!check" @click="gokidhome()" style="margin: 50px">
              <img
                class="back-btn"
                src="../../assets/icons/back.png"
                alt="back_btn"
                style="width: 120x; width: 120px"
              />
            </button>
            <button
              id="resume-camera"
              title="Resume Camera"
              class="d-none"
              style="margin: 50px"
              @click="changeCheck2()"
            >
              <img
                v-if="check"
                src="../../assets/icons/back.png"
                alt="back_btn"
                style="width: 120x; width: 120px"
              />
            </button>
            <!-- 사진찍기 -->
            <button
              v-if="!check"
              id="take-photo"
              title="Take Photo"
              style="margin: 50px"
              @click="changeCheck()"
            >
              <v-img
                class="phtoimg"
                src="../../assets/icons/camera2.png"
                alt="camera2"
                style="width: 120x; width: 120px"
              />
            </button>
            <button v-else style="margin: 50px" @click="download()">
              <img
                class="download-btn"
                src="../../assets/icons/save.png"
                alt="download"
                style="width: 120x; width: 120px"
              />
            </button>
            <!-- 사진 리스트 -->
            <button style="margin: 50px" @click="toPictureList()">
              <img
                class="back-btn"
                src="../../assets/icons/drawings.png"
                alt="picture"
                style="width: 120x; width: 120px"
              />
            </button>
          </div>
        </v-col>
        <!-- 이유는 모르지만 필수 -->
        <a id="download-photo" download="selfie.png" target="_blank" title="Save Photo"></a>
      </div>
    </div>
    <audio id="camera-sound" src="../../assets/characterSounds/camera.mp3"></audio>
  </div>
</template>
<script>
import { mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";
import Swal from "sweetalert2";

export default {
  name: "Home",
  data() {
    return {
      num: 0,
      background: ["taj", "desert", "moon", "beach", "christ"],
      check: false,
    };
  },
  components: {},
  computed: {
    ...mapState(["authToken"]),
  },
  methods: {
    toPictureList() {
      this.$router.push({
        name: "KidsPictureListView",
        params: { kidId: this.$route.params.kidId },
      });
    },
    changeCheck() {
      this.check = true;
      var camera_audio = document.getElementById(`camera-sound`);
      camera_audio.play();
    },
    changeCheck2() {
      this.check = false;
      this.$router.go();
    },
    gokidhome() {
      this.$router.push({
        name: "KidsMainView",
        params: { kidId: this.$route.params.kidId },
      });
    },
    right() {
      if (this.num == this.background.length - 1) {
        this.num = 0;
      } else {
        this.num = this.num + 1;
      }
    },

    left() {
      if (this.num == 0) {
        this.num = this.background.length - 1;
      } else {
        this.num = this.num - 1;
      }
    },
    download() {
      var imgBase64 = document.getElementById("download-photo");

      const decodImg = atob(imgBase64.href.split(",")[1]);
      let array = [];
      for (let i = 0; i < decodImg.length; i++) {
        array.push(decodImg.charCodeAt(i));
      }
      const file = new Blob([new Uint8Array(array)], { type: "image/png" });
      const fileName = "pictures_img_" + new Date().getMilliseconds() + ".jpg";
      let formData = new FormData();
      formData.append("file_source", file, fileName);

      const axiosConfig = {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `jwt ${this.authToken}`,
        },
      };
      axios
        .post(
          SERVER.URL + `/contents/kids/${this.$route.params.kidId}/pictures/`,
          formData,
          axiosConfig
        )
        .then(() => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "저장되었습니다!",
            showConfirmButton: false,
            timer: 1000,
          });
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
            this.$router.push({ name: "Home" });
          }
        });
    },
  },
  mounted() {
    var scripts = ["/js/selfie-anywhere.js"];
    scripts.forEach((scri) => {
      let tag = document.createElement("script");
      tag.setAttribute("src", scri);
      document.head.appendChild(tag);
    });
  },
  beforeDestroy() {
    location.reload();
  },
};
</script>

<style scoped>
#selfie-anywhere-app {
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: black;
  width: 100vw;
  height: 100vh;
}
.webcam-container {
  height: 100vh;
  width: 100vw;
}

#taj {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/images/taj.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: transparent;
}
#desert {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/images/desert.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: transparent;
}
#moon {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/images/moon.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: transparent;
}
#beach {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/images/beach.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: transparent;
}
#christ {
  height: 100vh;
  width: 100vw;
  background-image: url("../../assets/images/Christ.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: transparent;
}

@media screen and (min-width: 768px) {
  .webcam-container {
    background-attachment: fixed;
  }
}
/* .selfie-container {
  height: 100%;
  width: 100%;
} */
/* .selfie-container img {
  height: 100%;
  width: 100%;
  position: absolute;
  bottom: 0;
} */

.app-panel {
  height: 100vh;
  width: 100vw;
  text-align: center;
}

#selfie-container {
  height: 100%;
  width: 100%;
  z-index: 0;
  top: 0;
  left: 0;
  position: absolute;
}

#canvasPerson {
  background-color: transparent;
  position: absolute;
  width: 100vw;
  height: auto;
  z-index: 0;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin-left: auto;
  margin-right: auto;
  -moz-transform: scale(-1, 1);
  -webkit-transform: scale(-1, 1);
  -o-transform: scale(-1, 1);
  transform: scale(-1, 1);
  filter: FlipH;
}

#webcam {
  display: block;
  position: relative;
  width: auto;
  height: 100vh;
  z-index: -100;
  pointer-events: none;
  margin-left: -9999px;
}

#arrowLeft {
  position: absolute;
  left: 20px;
  top: 50%;
  z-index: 999999;
  opacity: 0.7;
  cursor: pointer;
}

@media screen and (min-width: 768px) {
  #arrowLeft {
    left: 100px;
  }
}

#arrowRight {
  position: absolute;
  right: 20px;
  top: 50%;
  z-index: 999999;
  opacity: 0.7;
  cursor: pointer;
}

.cameraControls {
  position: absolute;
  bottom: 5px;
  width: 100%;
  z-index: 9999;
  background: transparent;
  opacity: 0.7;
  padding: 10px;
}
</style>
