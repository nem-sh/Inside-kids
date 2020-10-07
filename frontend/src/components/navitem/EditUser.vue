<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn text dark v-bind="attrs" v-on="on">{{user.username}}님</v-btn>
      </template>
      <v-list class="text-center">
        <!-- modal 정보수정 -->
        <EditUserItem />
        <!-- 로그아웃 -->
        <v-list-item @click="logout">
          <v-list-item-title>로그아웃</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import EditUserItem from "@/components/navitem/EditUserItem.vue";

export default {
  name: "EditUser",
  components: {
    EditUserItem,
  },
  computed: {
    ...mapState(["user"]),
  },
  methods: {
    ...mapActions(["logout"]),
  },
};
</script>
