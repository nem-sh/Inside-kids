<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn text dark v-bind="attrs" v-on="on">
          <i class="fas fa-user-check pr-1"></i>아이 선택
          <!-- {{kid.name}} -->
        </v-btn>
      </template>
      <v-list class="text-center">
        <v-list-item
          class="text-left"
          v-for="(kid, index) in kidslist"
          :key="index"
          @click="kidDetail(kid.id)"
        >
          <v-list-item-title>
            <KidImage :image="kid.image" />
            {{ kid.name }}
          </v-list-item-title>
        </v-list-item>
        <v-btn @click="movePage">
          <v-icon>fas fa-cog</v-icon>설정
        </v-btn>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

import KidImage from "@/components/parents/KidImage";

export default {
  name: "SelectKid",
  components: {
    KidImage,
  },
  computed: {
    ...mapState(["kidslist"]),
    ...mapState(["kid"]),
  },
  methods: {
    ...mapActions(["getKidsList"]),
    kidDetail(index) {
      this.$router.push({ name: "KidsDetailView", params: { kidId: index } });
    },
    movePage() {
      this.$router.push({ name: "KidsManageView" });
    },
  },
  created() {
    this.getKidsList();
  },
};
</script>

<style></style>
