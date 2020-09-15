<template>
  <div class="row my-5">
    <div class="col-lg-2 col-md-3 col-4 box">
      <v-avatar size="120px"
        ><img src="@/assets/default_image.jpg" alt=""
      /></v-avatar>
    </div>
    <div class="col-10 text-left my-auto">
      <v-btn><i class="fas fa-edit"></i> 정보 수정</v-btn>
      <v-btn><i class="far fa-trash-alt"></i> 계정 삭제</v-btn>
      <v-btn>대화하기</v-btn>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: "KidProfile",
};
</script>

<style>
.box {
  width: 150px;
  height: 150px;
  border-radius: 70%;
  overflow: hidden;
}
</style>
