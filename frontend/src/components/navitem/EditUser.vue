<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn dark v-bind="attrs" v-on="on">
            username
          <!-- {{user.username}} -->
        </v-btn>
      </template>
      <v-list class="text-center">
        <!-- modal 정보수정 -->
        <EditUserItem/>
        <!-- modal 비밀번호수정 -->
        <ChangePassword/>
        <!-- 로그아웃 -->
        <v-list-item>
          <v-list-item-title>로그아웃</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import EditUserItem from "@/components/navitem/EditUserItem.vue"
import ChangePassword from "@/components/navitem/ChangePassword.vue"

export default {
  name: "EditUser",
  components:{
    ChangePassword,
    EditUserItem,
  },
  computed: {
      ...mapState(['user']),
  },
};
</script>

<style></style>
