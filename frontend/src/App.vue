<template>
  <v-app id="app">
    <router-view :key="$route.fullPath"></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App",
};
</script>
<style>
#app {
  font-family: "Jua", sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  color: #2c3e50;
}
</style>