<template>
  <v-row class="bg-1 pt-15">
    <v-col cols="12" class="text-center">
      <img
        class="back-btn"
        @click="back"
        src="../../assets/icons/back.png"
        alt="back_btn"
        width="80px"
      />
    </v-col>
    <v-col offset="2" cols="8">
      <v-container class="pa-4 text-center">
        <v-row class="fill-height" align="center">
          <h1 v-if="!drawings.length" class="mx-auto pt-10">
            <i class="fas fa-exclamation-triangle" style="color: orange"></i>
            기록이 없습니다.
          </h1>
          <ContentItem
            v-for="drawing in drawings"
            :key="drawing.id"
            :content="drawing"
            :flag="false"
            @drawRemove="refresh"
          />
        </v-row>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import axios from "axios";
import SERVER from "@/api/drf";

import ContentItem from "@/components/parents/ContentItem";

export default {
  name: "KidsDrawingListView",
  components: {
    ContentItem,
  },
  data() {
    return {
      drawings: [],
    };
  },
  computed: {
    ...mapState(["kid"]),
    ...mapGetters(["commonConfig"]),
  },
  methods: {
    fetchDrawings() {
      axios
        .get(
          SERVER.URL + `/contents/kids/${this.$route.params.kidId}/paints/`,
          this.commonConfig
        )
        .then((res) => {
          this.drawings = res.data;
        })
        .catch((err) => {
          if (err.response.status == 403) {
            alert("잘못된 접근입니다. 메인페이지로 돌아갑니다.");
            this.$router.push({ name: "Home" });
          }
        });
    },
    back() {
      history.back();
    },
    refresh(contentId) {
      const newPaints = this.drawings.filter((paint) => {
        return paint.id !== contentId;
      });
      this.drawings = newPaints;
    },
  },
  created() {
    this.fetchDrawings();
  },
};
</script>

<style>
.bg-1 {
  width: 100%;
  height: 100%;
  background-image: url("../../assets/characters/house.png");
  background-position: center center;
  background-size: cover;
}
.back-btn {
  cursor: pointer;
}
</style>