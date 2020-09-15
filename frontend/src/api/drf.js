export default {
  URL: "http://localhost:8000",
  ROUTES: {
    // auth
    login: "/accounts/login/",
    logout: "/accounts/logout/",
    signup: "/accounts/signup/",
    resetPwd: "/accounts/password/reset/",
    getUserInfo: '/accounts/user/',
    editUserInfo: '/accounts/user/',
    passwordChange: '/accounts/password/change/',
    deletAccount: '/accounts/delete/',
    getKidInfo: '/accounts/kids/',
  },
};
