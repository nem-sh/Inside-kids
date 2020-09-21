<template>
  <div class>
    <Nav />
    <div class="container kids-detail-body">
      <div class="text-center justify-center">
        <h1 class="font-weight-bold mt-5">{{kid.name}}</h1>
      </div>
      <KidProfile />
      <v-tabs fixed-tabs color="cyan accent-4">
        <v-tab>대화녹화</v-tab>
        <v-tab>그림</v-tab>
        <v-tab>사진</v-tab>
        <v-tab-item>
          <Recording />
        </v-tab-item>
        <v-tab-item>
          <Drawing />
        </v-tab-item>
        <v-tab-item>
          <Photo />
        </v-tab-item>
      </v-tabs>
    </div>
    <Footer />
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import KidProfile from "@/components/parents/KidProfile.vue";
import Recording from "@/components/parents/Recording.vue";
import Photo from "@/components/parents/Photo.vue";
import Drawing from "@/components/parents/Drawing.vue";
import Nav from "@/components/Navigation.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "kidsDetailView",
  components: {
    Nav,
    KidProfile,
    Drawing,
    Photo,
    Recording,
    Footer,
  },
  computed: {
    ...mapState(["kid"]),
  },
  methods: {
    ...mapActions(["getUser", "getKid"]),
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