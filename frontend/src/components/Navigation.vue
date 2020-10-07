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
        <!-- <v-btn  @click="moveToInfo">
          <v-icon>fas fa-question-circle</v-icon>
        </v-btn>-->
        <div class="text-center">
          <SelectKid />
        </div>
        <div class="text-center">
          <EditUser />
        </div>

        <v-dialog v-model="dialog" width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn text dark v-bind="attrs" v-on="on">
              <i class="fas fa-question-circle mr-1"></i>
              도움말
            </v-btn>
          </template>
          <v-card class="mx-auto my-auto">
            <v-card-title class="text-center">
              <h2>서비스 사용 안내</h2>
            </v-card-title>
            <div class="p-5">
              <iframe
                v-if="dialog"
                :src="require(`@/assets/videos/service_tutorial.mp4`)"
                frameborder="no"
                scrolling="no"
                width="600px"
                height="400px"
                allowfullscreen
              ></iframe>
            </div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    moveToMain() {
      this.$router.push({
        name: "Home",
      });
    },
    // moveToInfo() {
    //   this.$router.push({
    //     name: "NavInfoView",
    //     params: { kidId: this.$route.params.kidId },
    //   });
    // },
  },
};
</script>
