<template>
  <nav>
    <v-app-bar dense class="deep-orange lighten-3">
      <div class="container d-flex">
        <v-toolbar-title>
          <v-btn text dark @click="moveToMain">
            <img src="../assets/logo.png" alt width="80" />
          </v-btn>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text dark @click="moveToInfo">
          <v-icon>fas fa-question-circle</v-icon>
        </v-btn>
        <div class="text-center">
          <SelectKid />
        </div>
        <div class="text-center">
          <EditUser />
        </div>
      </div>
    </v-app-bar>
  </nav>
</template>

<script>
import EditUser from "@/components/navitem/EditUser.vue";
import SelectKid from "@/components/navitem/SelectKid.vue";

export default {
  name: "Navigation",
  components: {
    EditUser,
    SelectKid,
  },
  methods: {
    moveToMain() {
      this.$router.push({
        name: "Home",
      });
    },
    moveToInfo() {
      this.$router.push({
        name: "NavInfoView",
        params: { kidId: this.$route.params.kidId },
      });
    },
  },
};
</script>

<style>
</style>