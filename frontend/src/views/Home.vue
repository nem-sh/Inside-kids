<template>
  <div class="home">
    <section id="main">
      <video-background
        :src="require(`@/assets/videos/kidtalk.mp4`)"
        style="max-height: 500px; height: 100vh;"
        overlay="linear-gradient(45deg,#2a4ae430,#fb949e6b)"
      >
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <v-row align="center" justify="center">
          <v-col class="text-center" cols="12">
            <v-flex>
              <h1 class="display-2 mb-4" style="color: white;">
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
      </video-background>
    </section>
    <!-- <section id="main">
      <v-parallax dark src="https://t1.daumcdn.net/cfile/tistory/275FCF3656A1F6E428">
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
    </section>-->

    <section id="info-video">
      <div class="py-10"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">Service Info</h2>

        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1"></v-divider>

          <v-divider></v-divider>
        </v-responsive>
      </v-container>
      <p align="middle">
        <iframe
          :src="require(`@/assets/videos/service_intro.mp4`)"
          frameborder="no"
          scrolling="no"
          width="50%"
          height="400"
          allowfullscreen
        ></iframe>
      </p>
      <div class="py-10"></div>
    </section>

    <v-parallax id="parents" src="https://cdn.vuetifyjs.com/images/parallax/material.jpg">
      <div class="py-12"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-5">For Parents</h2>
        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1 p-5"></v-divider>

          <v-divider></v-divider>
        </v-responsive>
        <v-row>
          <v-col col="12" sm="6">
            <img width="45%" height="300px" src="../assets/characters/family.png" alt="info_parent" />
          </v-col>
          <v-col class="my-auto" col="12" sm="6">
            <h2>묻고 싶은 질문을 등록 하세요!</h2>
            <h2>AI 캐릭터 '시송이' 가 아이에게 대신 물어봐줄거에요</h2>
          </v-col>
        </v-row>
      </v-container>
      <div class="py-12"></div>
    </v-parallax>

    <section id="child">
      <div class="py-8"></div>
      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-5">For Children</h2>
        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1"></v-divider>
          <v-divider></v-divider>
        </v-responsive>
        <div class="mb-5">
          <h2>
            <a href="http://j3b106.p.ssafy.io/child">http://j3b106.p.ssafy.io/child</a> (아이 전용 페이지)
          </h2>
          <h2>
            아이가 사용할 수 있게
            <strong style="color:orange">즐겨찾기</strong> 해주세요 :)
          </h2>
        </div>
        <v-row class="mb-5">
          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5"
              >fas fa-utensils</v-icon
            >-->
            <img width="20%" height="50%" src="../assets/icons/eat.png" alt="info_parent" />
            <h1>밥 먹이기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5">fas fa-phone</v-icon> -->
            <img width="20%" height="50%" src="../assets/icons/talk.png" alt="info_parent" />
            <h1>대화하기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5"
              >fas fa-shower</v-icon
            >-->
            <img width="20%" height="50%" src="../assets/icons/wash.png" alt="info_parent" />
            <h1>씻기기</h1>
          </v-col>

          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5">fas fa-image</v-icon> -->
            <img width="20%" height="50%" src="../assets/icons/draw.png" alt="info_parent" />
            <h1>그림 그리기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5"
              >fas fa-camera</v-icon
            >-->
            <img width="20%" height="50%" src="../assets/icons/photo.png" alt="info_parent" />
            <h1>사진 찍기</h1>
          </v-col>
          <v-col cols="6" sm="4">
            <!-- <v-icon x-large color="blue-grey" class="mb-5">fas fa-music</v-icon> -->
            <img width="20%" height="50%" src="../assets/icons/sing.png" alt="info_parent" />
            <h1>노래 부르기</h1>
          </v-col>
        </v-row>

        <v-btn color="black" class="align-self-end" fab outlined @click="$vuetify.goTo('#main')">
          <v-icon>mdi-chevron-double-up</v-icon>
        </v-btn>
      </v-container>
      <div class="py-8"></div>
    </section>

    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import MainForm from "@/components/accounts/MainForm";
import Footer from "@/components/Footer";
import VideoBackground from "vue-responsive-video-background-player";

export default {
  name: "Home",
  components: {
    MainForm,
    Footer,
    VideoBackground,
  },
};
</script>
