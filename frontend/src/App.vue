<template>
  <v-app id="app">
    <div>
      <v-app-bar dense dark>
        <v-toolbar-title>
          <v-btn>
            <span>로고</span>
          </v-btn>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn>
          <span>도움말</span>
        </v-btn>
      <div class="text-center">
        <EditUser/>
      </div>
      </v-app-bar>
      <router-view></router-view>
    </div>
  </v-app>
</template>

<script>
  import EditUser from "@/components/navitem/EditUser.vue"
  export default {
    name: 'App',
    components:{
      EditUser,
    }
  }
</script>
<style>
#app {
  font-family: "Jua", sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  color: #2c3e50;
}
</style>