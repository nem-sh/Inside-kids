<template>
  <v-app id="app">
    <div>
      <v-app-bar                  
        dense
        dark
      >
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
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              dark
              v-bind="attrs"
              v-on="on"
            >
              Dropdown
            </v-btn>
          </template>
          <v-list>
            <v-list-item
                      
              v-for="(item, index) in items"
              :key="index"
              @click="go"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              dark
              v-bind="attrs"
              v-on="on"
            >
              Dropdown
            </v-btn>
          </template>
          <v-list>
            <v-list-item
                      
              v-for="(item, index) in items"
              :key="index"
              @click="go"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      </v-app-bar>
      <router-view></router-view>
    </div>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data: () => ({
      items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' },
      ],
    }),
    methods:{
      go(){

      }
    },
  }
</script>
<style>
  #app {
    font-family: 'Jua', sans-serif !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
    color: #2c3e50;
  }
</style>