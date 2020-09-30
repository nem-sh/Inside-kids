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
  methods:{
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
