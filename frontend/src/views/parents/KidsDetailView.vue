<template>
  <div class>
    <Nav />
    <div class="container kids-detail-body">
      <div class="d-flex justify-center">
        <div>
          <KidProfile />
          <div class="text-center justify-center">
            <h1 class="font-weight-bold mb-5">
              <i class="fas fa-house-user"></i>
              {{kid.name}}
            </h1>
          </div>
        </div>
        <div class="my-auto" style="cursor:pointer">
          <img
            @click="moveToChildPage"
            width="50px"
            src="../../assets/characters/character.png"
            alt="playroom"
          />
          <!-- <v-btn @click="moveToChildPage">{{kid.name}} 놀이터</v-btn> -->
        </div>
      </div>
      <v-tabs fixed-tabs color="cyan accent-4">
        <v-tab>질문관리</v-tab>
        <v-tab>대화녹화</v-tab>
        <v-tab>그림</v-tab>
        <v-tab>사진</v-tab>
        <v-tab-item>
          <ScriptList />
        </v-tab-item>
        <v-tab-item>
          <VideoList />
        </v-tab-item>
        <v-tab-item>
          <PaintList />
        </v-tab-item>
        <v-tab-item>
          <PictureList />
        </v-tab-item>
      </v-tabs>
    </div>
    <Footer />
  </div>
</template>

<script>
import router from "@/router";
import { mapActions, mapState } from "vuex";
import KidProfile from "@/components/parents/KidProfile";
import VideoList from "@/components/parents/VideoList";
import PictureList from "@/components/parents/PictureList";
import PaintList from "@/components/parents/PaintList";
import ScriptList from "@/components/parents/ScriptList";
import Nav from "@/components/Navigation";
import Footer from "@/components/Footer";

export default {
  name: "kidsDetailView",
  components: {
    Nav,
    KidProfile,
    PictureList,
    PaintList,
    VideoList,
    ScriptList,
    Footer,
  },
  computed: {
    ...mapState(["kid"]),
  },
  methods: {
    ...mapActions(["getUser", "getKid"]),
    moveToChildPage() {
      router.push({ name: "KidsMainView", params: { kidId: this.kid.id } });
    },
  },
  created() {
    this.getUser();
    this.getKid(this.$route.params.kidId);
  },
};
</script>

<style>
.kids-detail-body {
  min-height: 100vh;
}
</style>