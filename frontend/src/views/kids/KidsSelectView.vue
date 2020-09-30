<template>
  <div class="bg-2 d-flex flex-column justify-center">
    <v-card class="mx-auto opacity-form pb-3" min-width="400" min-height="150" max-width="600">
      <v-card-title class="mx-2 my-2">
        <h2>Inside Kids를 이용할 프로필 선택</h2>
      </v-card-title>
      <div v-if="!kidslist.length" class="text-center">
        <h2>
          <i class="fas fa-exclamation-circle"></i> 등록된 프로필이 없습니다
        </h2>
      </div>
      <div class="d-flex justify-center flex-wrap">
        <v-card-actions v-for="kid in kidslist" :key="kid.id" class="kid-list">
          <v-list-item>
            <div class="text-center kids-select" @click="goToMain(kid.id)">
              <KidImage2 :image="kid.image" />
              <v-list-item-content class="text--primary">
                <v-list-item-title>{{kid.name}}</v-list-item-title>
              </v-list-item-content>
            </div>
          </v-list-item>
        </v-card-actions>
      </div>
    </v-card>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

import KidImage2 from "@/components/parents/KidImage2";
export default {
  name: "KidsSelectView",
  components: {
    KidImage2,
  },
  computed: {
    ...mapState(["kidslist"]),
  },
  methods: {
    ...mapActions(["getKidsList"]),
    goToMain(kidId) {
      this.$router.push({ name: "KidsMainView", params: { kidId: kidId } });
    },
  },
  created() {
    this.getKidsList();
  },
};
</script>

<style>
.kids-select {
  background-color: white;
  padding: 10px;
  border-radius: 20px;
  box-shadow: 10px 5px 5px grey;
}
.kids-select:hover {
  transform: scale(1.1);
}
</style>