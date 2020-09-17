<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn text dark v-bind="attrs" v-on="on">
          아이 선택
          <!-- {{kid.name}} -->
        </v-btn>
      </template>
      <v-list class="text-center">
        <v-list-item v-for="(kid, index) in kidslist" :key="index" @click="kidDetail(index)">
          <v-list-item-title>
            <v-avatar color="indigo" size="36">
              <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
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

export default {
  name: "SelectKid",
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
