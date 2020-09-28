<template>
  <div class="py-15 my-auto bg-1">
    <div class="controls">
      <div>
        <img
          class="back-btn"
          @click="gokidhome"
          src="../../assets/icons/back.png"
          alt="back_btn"
          width="80px"
        />
        <!-- <v-btn @click="gokidhome" class="red mb-2">
          <i class="fas fa-home fa-2x"></i>
        </v-btn>-->
      </div>
      <div class="controls__colors" id="jsColors">
        <div
          class="controls__color"
          :class="{ active: selectedToolIdx === 1 }"
          @click="changeTool(1)"
        >
          <img src="@/assets/icons/eraser.png" width="100%" />
        </div>
        <div
          class="controls__color jsColor"
          style="background-color: #2c2c2c"
          @click="chooseColor(colors.black);changeTool(0) "
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: white"
          @click="chooseColor(colors.white);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #ff3b30"
          @click="chooseColor(colors.red);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #ff9500"
          @click="chooseColor(colors.orange);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #ffcc00"
          @click="chooseColor(colors.yellow);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #4cd963"
          @click="chooseColor(colors.green);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #5ac8fa"
          @click="chooseColor(colors.skyBlue);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #0579FF"
          @click="chooseColor(colors.blue);changeTool(0)"
        ></div>
        <div
          class="controls__color jsColor"
          style="background-color: #5856D6"
          @click="chooseColor(colors.purple);changeTool(0)"
        ></div>
      </div>
    </div>
    <div class="content" ref="canvasWrapper">
      <canvas id="canvas" class="canvas" ref="canvas" :width="width" :height="height"></canvas>
      <!-- <canvas id="cursor" ref="cursor"></canvas> -->
    </div>
    <div class="d-flex justify-center mt-5">
      <img
        @click="toDrawingList()"
        class="drawings-btn"
        src="../../assets/icons/drawings.png"
        alt="drawings"
      />
      <img
        class="download-btn"
        @click="download()"
        src="../../assets/icons/save.png"
        alt="download"
      />
      <img class="save-btn" @click="reset()" src="../../assets/icons/trashcan.png" alt="save" />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";

import Swal from "sweetalert2";

export default {
  name: "KidsDrawingView",
  data() {
    return {
      brushSize: 12,
      width: "600rem",
      height: "500rem",
      outputName: "canvas",
      canvasContext: null,
      // cursorContext: null,
      isDrawing: false,
      lastX: 0,
      lastY: 0,
      tools: [
        {
          name: "Pencil",
          color: "#000000",
        },
        {
          name: "Eraser",
        },
      ],
      selectedToolIdx: 0,
      colors: {
        black: "#2c2c2c",
        white: "#ffffff",
        red: "#ff3b30",
        orange: "#ff9500",
        yellow: "#ffcc00",
        green: "#4cd963",
        skyBlue: "#5ac8fa",
        blud: "#0579FF",
        purple: "#5856D6",
      },
    };
  },
  computed: {
    ...mapState(["authToken"]),
  },
  methods: {
    gokidhome() {
      this.$router.push({
        name: "KidsMainView",
        params: { kidId: this.$route.params.kidId },
      });
    },
    setCanvas() {
      this.$refs.canvasWrapper.style.gridTemplateColumns = `${this.width}px 30px`;
      this.$refs.canvasWrapper.style.width = `${this.width + 30}px`;
      this.$refs.canvasWrapper.style.height = `${this.height}px`;
      this.canvasContext = this.$refs.canvas.getContext("2d");
      this.canvasContext.lineJoin = "round";
      this.canvasContext.lineCap = "round";
      this.canvasContext.lineWidth = this.brushSize;
      this.canvasContext.strokeStyle = this.tools[this.selectedToolIdx].color;
      // this.cursorContext = this.$refs.cursor.getContext("2d");
    },
    bindEvents() {
      this.$refs.canvas.addEventListener("mousedown", (event) => {
        this.isDrawing = true;
        [this.lastX, this.lastY] = [event.offsetX, event.offsetY];
      });
      this.$refs.canvas.addEventListener("mousemove", this.draw);
      this.$refs.canvas.addEventListener(
        "mouseup",
        () => (this.isDrawing = false)
      );
      this.$refs.canvas.addEventListener(
        "mouseout",
        () => (this.isDrawing = false)
      );

      const canvasContext = this.$refs.canvas.getContext("2d");
      var mode = this.tools[this.selectedToolIdx];

      // 아이패드, 모바일 붓 위치
      var canvas = this.$refs.canvas;
      // var rect = this.$refs.canvas.getBoundingClientRect();
      this.$refs.canvas.addEventListener("touchstart", function (event) {
        event.preventDefault();
        canvasContext.beginPath();
        if (mode.name === "Eraser") {
          canvasContext.strokeStyle = "rgb(255,255,255)";
          canvasContext.lineWidth = this.brushSize;
        } else {
          canvasContext.strokeStyle = mode.color;
          canvasContext.lineWidth = this.brushSize;
        }
        canvasContext.moveTo(
          event.touches[0].clientX - canvas.offsetLeft,
          event.touches[0].clientY - canvas.offsetTop
        );
      });
      // touch move
      this.$refs.canvas.addEventListener("touchmove", function (event) {
        event.preventDefault();
        canvasContext.lineTo(
          event.touches[0].clientX - canvas.offsetLeft,
          event.touches[0].clientY - canvas.offsetTop
        );
        canvasContext.stroke();
      });
      // touch end
      this.$refs.canvas.addEventListener("touchend", function () {
        canvasContext.closePath();
        canvasContext.save();
      });
      // touch cancel
      this.$refs.canvas.addEventListener("touchcancel", function () {
        canvasContext.closePath();
        canvasContext.save();
      });
    },
    changeTool(tool) {
      this.selectedToolIdx = tool;
    },
    draw(event) {
      if (!this.isDrawing) return;
      if (this.tools[this.selectedToolIdx].name === "Eraser") {
        this.canvasContext.globalCompositeOperation = "destination-out";
      } else {
        this.canvasContext.globalCompositeOperation = "source-over";
        this.canvasContext.strokeStyle = this.tools[this.selectedToolIdx].color;
      }
      this.canvasContext.beginPath();
      this.canvasContext.moveTo(this.lastX, this.lastY);
      this.canvasContext.lineTo(event.offsetX, event.offsetY);
      this.canvasContext.stroke();
      [this.lastX, this.lastY] = [event.offsetX, event.offsetY];
    },
    chooseColor(color) {
      this.tools[0].color = color;
    },
    download() {
      const imgBase64 = this.$refs.canvas.toDataURL("image/png");
      const decodImg = atob(imgBase64.split(",")[1]);
      let array = [];
      for (let i = 0; i < decodImg.length; i++) {
        array.push(decodImg.charCodeAt(i));
      }

      const file = new Blob([new Uint8Array(array)], { type: "image/png" });
      const fileName = "canvas_img_" + new Date().getMilliseconds() + ".jpg";
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
          SERVER.URL + `/contents/kids/${this.$route.params.kidId}/paints/`,
          formData,
          axiosConfig
        )
        .then(() => {
          this.reset();
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
    reset() {
      this.canvasContext.clearRect(
        0,
        0,
        this.$refs.canvas.width,
        this.$refs.canvas.height
      );
    },
    toDrawingList() {
      this.$router.push({
        name: "KidsDrawingListView",
        params: { kidId: this.$route.params.kidId },
      });
    },
  },
  mounted() {
    this.setCanvas();
    this.bindEvents();
  },
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.canvas {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  max-width: 100%;
  cursor: url("../../assets/icons/brush.png"), pointer;
  margin-top: 20px;
  background-color: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}
.controls {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.controls__width,
.controls__height {
  color: 1px solid rgba(0, 0, 0, 0.8);
  font-size: 15px;
  height: 18px;
  width: 50px;
  margin-right: 10px;
  padding-left: 5px;
}
.controls__btns {
  margin-top: 20px;
}
button {
  all: unset;
  cursor: pointer;
  background-color: white;
  padding: 5px 0px;
  width: 80px;
  text-align: center;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.2);
  color: 1px solid rgba(0, 0, 0, 0.8);
  text-transform: uppercase;
  font-weight: 600;
  font-size: 12px;
}
button:active {
  transform: scale(0.98);
}
.controls__size {
  display: flex;
}
.controls__colors {
  margin-top: 20px;
  display: flex;
}
.controls__color {
  margin-left: 5px;
  width: 50px;
  cursor: url("../../assets/icons/brush.png"), pointer;
  border-radius: 25px;
  height: 50px;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
  color: 1px solid rgba(0, 0, 0, 0.8);
  text-transform: uppercase;
  font-weight: 600;
  font-size: 12px;
  text-align: center;
  line-height: 50px;
}
.controls__color:active {
  transform: scale(0.98);
}
.controls__color__clicked {
  border-color: #4195fc;
  box-shadow: 0px 0px 15px #4195fc;
}
.download-btn,
.save-btn,
.drawings-btn {
  cursor: pointer;
  display: inline-block;
  padding: 0 20px;
}
</style>