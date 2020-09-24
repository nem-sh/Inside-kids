<template>
  <div
    class="kid-main"
    style="display: flex; justify-content: center; align-items: center"
  >
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
};
</script>

<style></style>
