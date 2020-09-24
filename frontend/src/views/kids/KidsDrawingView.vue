<template>
  <div
    class="kid-main show-area"
    style="display: flex; justify-content: center; align-items: center"
  >
    <KidsDrawing :width="640" :height="480" :outputName="'example'" />
  </div>
</template>

<script>
import KidsDrawing from "@/components/kids/KidsDrawing.vue";

export default {
  name: "KidsDrawingView",
  components: {
    KidsDrawing,
  },
};
</script>

<style scoped>

</style>
