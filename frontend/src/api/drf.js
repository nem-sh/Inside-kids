export default {
  URL: "http://localhost:8000",
  // URL: "https://j3b106.p.ssafy.io",
  ROUTES: {
    // auth
    login: "/api/accounts/login/",
    logout: "/api/accounts/logout/",
    signup: "/api/accounts/signup/",
    resetPwd: "/api/accounts/password/reset/",
    getUserInfo: "/api/accounts/user/",
    editUserInfo: "/api/accounts/user/",
    passwordChange: "/api/accounts/password/change/",
    deletAccount: "/api/accounts/delete/",
    getKidInfo: "/api/accounts/kids/",

    // contents
    getCharacterInfo: "/api/contents/characters/",
    deleteVideo: "/api/contents/videos/",
  },
};
