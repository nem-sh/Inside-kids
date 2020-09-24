<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="border">
          <vue-web-cam
            ref="webcam"
            :device-id="deviceId"
            width="100%"
            @started="onStarted"
            @stopped="onStopped"
            @error="onError"
            @cameras="onCameras"
            @camera-change="onCameraChange"
          />
        </div>

        <div class="row text-center">
          <div class="col-md-12">
            <v-btn class="button is-primary" @click="onCapture">
              사진찍기
            </v-btn>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <figure class="figure">
          <img :src="img" class="img-responsive" />
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
import { WebCam } from "vue-web-cam";
import Swal from 'sweetalert2'
export default {
  name: "App",
  components: {
    "vue-web-cam": WebCam,
  },
  data() {
    return {
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
    };
  },
  computed: {
    device: function() {
      return this.devices.find((n) => n.deviceId === this.deviceId);
    },
  },
  watch: {
    camera: function(id) {
      this.deviceId = id;
    },
    devices: function() {
      // Once we have a list select the first one
      const [first] = this.devices;
      if (first) {
        this.camera = first.deviceId;
        this.deviceId = first.deviceId;
      }
    },
  },
  methods: {
    loaddata(){
      Swal.fire({
        position: 'center',
        icon: 'success',
        showConfirmButton: false,
        timer: 1000
      })
    },
    onCapture() {
      this.img = this.$refs.webcam.capture();
    },
    onStarted(stream) {
      console.log("On Started Event", stream);
    },
    onStopped(stream) {
      console.log("On Stopped Event", stream);
    },
    onStop() {
      this.$refs.webcam.stop();
    },
    onStart() {
      this.$refs.webcam.start();
    },
    onError(error) {
      console.log("On Error Event", error);
    },
    onCameras(cameras) {
      this.devices = cameras;
      console.log("On Cameras Event", cameras);
    },
    onCameraChange(deviceId) {
      this.deviceId = deviceId;
      this.camera = deviceId;
      console.log("On Camera Change Event", deviceId);
    },
  },
created(){
    this.loaddata()
  },
};
</script>
