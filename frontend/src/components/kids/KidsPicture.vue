<template>
  <div>
    <div class="form-control webcam-start" id="webcam-control">
      <label class="form-switch">
        <input type="checkbox" id="webcam-switch" />
        <i></i>
        <span id="webcam-caption">Click to Start Camera</span>
      </label>
    </div>
    <div class="md-modal md-effect-12">
      <div id="app-panel" class="app-panel md-content">
        <div id="webcam-container" class="webcam-container d-none">
          <video
            id="webcam"
            autoplay
            playsinline
            width="640"
            height="480"
          ></video>
          <div id="selfie-container">
            <div :id="background[num]">
              <div class="spinner-border d-none" role="status">
                <span class="sr-only">Loading...</span>
              </div>
            </div>
            <canvas
              id="canvasPerson"
              ref="canvas"
              width="640"
              height="480"
            ></canvas>
          </div>
          <div class="flash"></div>
        </div>
        <img
          id="arrowLeft"
          src="../../assets/images/arrow-left.png"
          @click="left"
        />
        <img
          id="arrowRight"
          src="../../assets/images/arrow-right.png"
          @click="right"
        />
        <div id="cameraControls" class="cameraControls">
          <v-btn id="exit-app" title="Exit App" class="d-none">
            <i class="material-icons">exit_to_app</i>
          </v-btn>
          <button id="take-photo" title="Take Photo">
            <v-img
              class="phtoimg"
              src="../../assets/icons/camera2.png"
              alt
              style="width: 120x; width: 120px"
            />
          </button>
          <a
            id="download-photo"
            download="selfie.png"
            target="_blank"
            title="Save Photo"
            class="d-none"
            ><i class="material-icons">file_download</i></a
          >
          <img
            class="back-btn"
            @click="gokidhome"
            src="../../assets/icons/back.png"
            alt="back_btn"
            width="80px"
          />
          <img
            class="download-btn"
            @click="download()"
            src="../../assets/icons/save.png"
            alt="download"
          />
          <v-btn id="resume-camera" title="Resume Camera" class="d-none">
            <i class="material-icons">camera_front</i>
          </v-btn>
        </div>
      </div>
    </div>
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
    };
  },
  components: {},
  computed: {
    ...mapState(["authToken"]),
  },
  methods: {
    gokidhome() {
      this.$router.push({
        name: "KidsMainView",
        params: { kidId: 1 },
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
      const imgBase64 = this.$refs.canvas.toDataURL("image/png");
      console.log(imgBase64);
      const decodImg = atob(imgBase64.split(",")[1]);
      let array = [];
      for (let i = 0; i < decodImg.length; i++) {
        array.push(decodImg.charCodeAt(i));
      }
      console.log(array);
      const file = new Blob([new Uint8Array(array)], { type: "image/png" });
      console.log(file);
      const fileName = "canvas_img_" + new Date().getMilliseconds() + ".jpg";
      console.log(fileName);
      let formData = new FormData();
      formData.append("file_source", file, fileName);
      console.log(formData);

      const axiosConfig = {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `jwt ${this.authToken}`,
        },
      };
      console.log(axiosConfig);
      axios
        .post(SERVER.URL + `/contents/kids/1/paints/`, formData, axiosConfig)
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
          console.error(err.response);
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

.form-control.webcam-start {
  margin-top: 20%;
  left: 30%;
  position: absolute;
  background: black;
  opacity: 0.8;
  padding: 10px 20px;
  border: none;
  color: white;
  text-shadow: 1px 1px #000;
  font-size: 1.2rem;
  width: auto;
  height: 55px;
  z-index: 9999;
}

.form-control.webcam-on {
  position: fixed;
  left: 8vw;
  top: 0;
  transition: all 700ms;
}
.form-control.webcam-off {
  left: 30%;
  transition: all 700ms;
}
@media screen and (max-width: 576px) {
  #selfie-anywhere-app {
    height: 100vh;
  }
  .form-control.webcam-start {
    left: 10%;
    width: auto;
    margin-top: 40%;
  }
  .form-control.webcam-on {
    position: fixed;
    margin-top: 0;
    top: 20vw;
    left: 0;
    transition: all 700ms;
  }
  .form-control.webcam-off {
    left: 10%;
    margin-top: 40%;
    transition: all 700ms;
  }
}

.form-switch {
  display: inline-block;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.form-switch i {
  position: relative;
  display: inline-block;
  margin-right: 0.5rem;
  width: 60px;
  height: 30px;
  background-color: #e6e6e6;
  border-radius: 25px;
  vertical-align: text-bottom;
  transition: all 0.3s linear;
}

.form-switch i::before {
  content: "";
  position: absolute;
  left: 0;
  width: 56px;
  height: 25px;
  background-color: #fff;
  border-radius: 15px;
  transform: translate3d(2px, 2px, 0) scale3d(1, 1, 1);
  transition: all 0.25s linear;
}

.form-switch i::after {
  content: "";
  position: absolute;
  left: 0;
  width: 26px;
  height: 26px;
  background-color: #fff;
  border: 1px solid grey;
  border-radius: 15px;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.25);
  transform: translate3d(2px, 2px, 0);
  transition: all 0.2s ease-in-out;
}

.form-switch:active i::after {
  width: 60px;
  transform: translate3d(2px, 2px, 0);
}

.form-switch:active input:checked + i::after {
  transform: translate3d(16px, 2px, 0);
}

.form-switch input {
  display: none;
}

.form-switch input:checked + i {
  background-color: #4bd763;
}

.form-switch input:checked + i::before {
  transform: translate3d(18px, 2px, 0) scale3d(0, 0, 0);
}

.form-switch input:checked + i::after {
  transform: translate3d(30px, 2px, 0);
}

.form-switch input:disabled + i {
  background-color: #eeeeee;
  cursor: not-allowed;
}

.form-switch input:disabled + i::after {
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}

.selfie-container {
  height: 100%;
}
.selfie-container img {
  width: 100%;
  position: absolute;
  bottom: 0;
}

.app-panel {
  height: 100vh;
  width: 100vw;
  text-align: center;
}

#selfie-container {
  height: 100vh;
  width: 100vw;
  z-index: 100;
  top: 0;
  left: 0;
  position: absolute;
}

#canvasPerson {
  background-color: transparent;
  position: absolute;
  width: 100vw;
  height: auto;
  z-index: 9999;
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
.md-modal {
  margin: auto;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  z-index: 2000;
  visibility: hidden;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  backface-visibility: hidden;
}

.md-show {
  visibility: visible;
}

.md-overlay {
  position: fixed;
  width: 100%;
  height: 100%;
  visibility: hidden;
  top: 0;
  left: 0;
  z-index: 1000;
  opacity: 0;
  background: rgba(#e4f0e3, 0.8);
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
}

.md-show ~ .md-overlay {
  opacity: 1;
  visibility: visible;
}

.md-effect-12 .md-content {
  -webkit-transform: scale(0.8);
  -moz-transform: scale(0.8);
  -ms-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
}

.md-show.md-effect-12 ~ .md-overlay {
  background-color: #e4f0e3;
}

.md-effect-12 .md-content h3,
.md-effect-12 .md-content {
  background: transparent;
}

.md-show.md-effect-12 .md-content {
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  transform: scale(1);
  opacity: 1;
}

.spinner-border {
  position: relative;
  top: 35%;
  width: 200px;
  height: 200px;
  color: white;
  z-index: 300000;
  filter: alpha(opacity=80);
  -moz-opacity: 0.8;
  opacity: 0.8;
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
  bottom: 150px;
  width: 100%;
  z-index: 9999;
  background: transparent;
  opacity: 0.7;
  padding: 10px;
}

.material-icons {
  width: 100px;
  font-size: 50px !important;
  color: white;
  width: 80px;
  height: 80px;
  background-color: black;
  border-radius: 50%;
  padding-top: 15px;
  margin: 0 10px;
}

.flash {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #fff;
  z-index: 99999999;
}

#errorMsg {
  position: fixed;
  top: 20vh;
  left: 0;
  padding: 20px;
  z-index: 999999;
}

@media screen and (min-width: 768px) {
  #errorMsg {
    position: fixed;
    top: 30vh;
    left: 20vw;
    padding: 20px;
    z-index: 999999;
  }
}
</style>
