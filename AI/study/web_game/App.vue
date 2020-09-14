<template>
  <div id="app">
    <iframe src="./assets/silence.mp3" allow="autoplay" id="audio" style="display:none"></iframe>
    <audio v-if="on" id="audio" autoplay>
      <source src="./assets/b.mp3" />
    </audio>

    <div>
      <div class="monster" :class="changeClass"></div>
    </div>
    <button @click="on= !on">엉덩이 춤 온!!</button>
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/phaser@3.15.1/dist/phaser-arcade-physics.min.js">
</script>
    <script>
</script>
<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  data() {
    return {
      on: false,
    };
  },
  components: {
    HelloWorld,
  },

  methods: {},
  computed: {
    changeClass: function () {
      if (this.on) {
        return "sprite1";
      } else {
        return "sprite2";
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.monster {
  width: 480px;
  height: 480px;
}

.sprite1 {
  background: url("./assets/1.png") left center;
  animation: play 1.5s steps(12);

  animation-iteration-count: infinite;
}
.sprite2 {
  background: url("./assets/2.png") left center;
  animation: play2 1.5s steps(6);

  animation-iteration-count: 3;
}
@keyframes play {
  100% {
    background-position: -5760px;
  }
}
@keyframes play2 {
  100% {
    background-position: -2880px;
  }
}
</style>
