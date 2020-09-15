<template>
  <div class="home">
    <section id="main">
      <v-parallax dark src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
        <v-row align="center" justify="center">
          <v-col class="text-center" cols="12">
            <v-flex>
              <h1 class="display-2 mb-4">
                <strong>우리 아이의 속마음이 궁금하신가요?</strong>
              </h1>
            </v-flex>
            <div class="mb-5">
              <MainForm />
            </div>

            <v-btn
              color="white"
              class="align-self-end"
              fab
              outlined
              @click="$vuetify.goTo('#info-video')"
            >
              <v-icon>mdi-chevron-double-down</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-parallax>
    </section>

    <section id="info-video">
      <div class="py-12"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">How to use</h2>

        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1"></v-divider>

          <v-divider></v-divider>
        </v-responsive>
      </v-container>
      <p align="middle">
        <iframe
          src="https://www.youtube.com/embed/nNONgE0KWR4"
          frameborder="no"
          scrolling="no"
          width="50%"
          height="400"
          allow="autoplay"
          allowfullscreen
        ></iframe>
      </p>
      <div class="py-12"></div>
    </section>

    <section id="parents" class="grey lighten-3">
      <div class="py-12"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-5">For parents</h2>
        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1 p-5"></v-divider>

          <v-divider></v-divider>
        </v-responsive>
        <v-row>
          <v-col col="12" sm="6">
            <img width="100%" height="300px" src="../assets/info_parent.png" alt="info_parent" />
          </v-col>
          <v-col class="my-auto" col="12" sm="6">
            <h1>AI 캐릭터가 되어 아이와 대화할 수 있어요!</h1>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias
              corporis repellat eaque accusantium porro placeat reprehenderit,
              corrupti omnis nam eos ducimus, sapiente laudantium nemo possimus
              ipsum perspiciatis vero! Accusamus, tempora?
            </p>
          </v-col>
        </v-row>
      </v-container>
      <div class="py-12"></div>
    </section>

    <section id="child">
      <div class="py-12"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-5">For children</h2>
        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1"></v-divider>
          <v-divider></v-divider>
        </v-responsive>
        <v-row class="mb-5">
          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-utensils</v-icon>
            <h1>밥 먹이기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-phone</v-icon>
            <h1>통화하기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-shower</v-icon>
            <h1>씻기기</h1>
          </v-col>

          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-image</v-icon>
            <h1>그림 그리기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-camera</v-icon>
            <h1>사진 찍기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <v-icon x-large color="blue-grey" class="mb-5">fas fa-music</v-icon>
            <h1>노래 부르기</h1>
          </v-col>
        </v-row>

        <v-btn color="black" class="align-self-end" fab outlined @click="$vuetify.goTo('#main')">
          <v-icon>mdi-chevron-double-up</v-icon>
        </v-btn>
      </v-container>
      <div class="py-12"></div>
    </section>

    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import MainForm from "@/components/accounts/MainForm";
import Footer from "@/components/Footer";

export default {
  name: "Home",
  components: {
    MainForm,
    Footer,
  },
};
</script>
