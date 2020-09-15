<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn dark v-bind="attrs" v-on="on">
          kidname
          <!-- {{kid.name}} -->
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(kid, index) in kidslist"
          :key="index"
          @click="kidDetail(index)"
        >
          <v-list-item-title>{{ kid }}</v-list-item-title>
        </v-list-item>
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
  },
  created() {
    this.getKidsList();
  },
};
</script>

<style></style>
