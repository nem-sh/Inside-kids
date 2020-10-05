<template>
  <div
    class="kid-main"
    style="display: flex; justify-content: center; align-items: center"
  >
    <KidsTalking/>
  </div>
</template>

<script>
import KidsTalking from "@/components/kids/KidsTalking.vue"
export default {
    name:"KidsTalkingView",
    components:{
        KidsTalking,
    },
}
</script>

<style>

</style>