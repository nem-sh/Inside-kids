<template>
  <div class="container mt-5">
    <img src="@/assets/404.jpg" alt="404" class="text-center col-lg" />
    <div class="text-center">
      <h1 class="btn--text2">
        <router-link to="/" class="btn--text">메인페이지</router-link>로 이동
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageNotFound",
};
</script>

<style>
</style>