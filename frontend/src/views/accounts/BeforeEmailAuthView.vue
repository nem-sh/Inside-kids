<template>
  <div class="text-center mt-15">
    <h1>가입하신 이메일로 인증 요청 메일 보냈습니다.</h1>
    <h1>인증 후 아래의 버튼을 눌러주세요.</h1>
    <br />
    <v-btn @click="goToKidsDetail">Start</v-btn>
  </div>
</template>

<script>
export default {
  name: "BeforeEmailAuth",
  methods: {
    goToKidsDetail() {
      //   router.push({ name: "KidsDetailView", params: { kidId: 1 } });
    },
  },
};
</script>

<style>
</style>