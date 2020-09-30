<template>
  <div
    class="kid-main"
    style="display: flex; justify-content: center; align-items: center"
  >
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
      <div>
        <img
          @click="toPictureList"
          class="back-btn"
          src="../../assets/icons/drawings.png"
          alt="drawings"
        />
      </div>
    </div>
    <KidsPicture />
  </div>
</template>

<script>
import KidsPicture from "@/components/kids/KidsPicture.vue";
export default {
  name: "KidsPictureView",
  components: {
    KidsPicture,
  },
  methods: {
    toPictureList() {
      this.$router.push({
        name: "KidsPictureListView",
        params: { kidId: this.$route.params.kidId },
      });
    },
    gokidhome() {
      this.$router.push({
        name: "KidsMainView",
        params: { kidId: 1 },
      });
    },
  },
};
</script>

<style></style>
