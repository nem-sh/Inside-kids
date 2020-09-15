import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import router from '@/router'
import axios from 'axios'
import SERVER from '@/api/drf'
import Swal from 'sweetalert2'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    user: {},
    kid: {},
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: state => ({ headers: { Authorization: `Token ${state.authToken}` } }),
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_USER(state, userInfo) {
      state.user = userInfo
    },
    SET_KID(state, kidInfo) {
      state.kid = kidInfo
    },
  },
  actions: {
    logout({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.logout, getters.config)
        .then(() => {
          commit('SET_TOKEN', null)
          cookies.remove('auth-token')
          Swal.fire({
            position: 'center',
            icon: 'success',
            title: '로그아웃 되었습니다!',
          })
          router.push({ name: 'Home' })
        })
        .catch(err => console.log(err))
    },
    // getUser({ getters, commit, state }) {
    getUser({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.getUserInfo, getters.config)
        .then(res => {
          commit('SET_USER', res.data)
          // if (state.authToken !== cookies.get('auth-token')) {
          //   commit('SET_TOKEN', null)
          //   cookies.remove('auth-token')
          //   Swal.fire({
          //     position: 'center',
          //     icon: 'warning',
          //     title: '로그인해 주세요.',
          //   })
          //   router.push({ name: "Home" })
          // }
        })
        // .catch((err) => {
        //   console.error(err)
        //   commit('SET_TOKEN', null)
        //   cookies.remove('auth-token')
        //   Swal.fire({
        //     position: 'center',
        //     icon: 'warning',
        //     title: '로그인해 주세요.',
        //   })
        //   router.push({ name: "Home" })
        // })
    },
    getKidsList({ getters, commit}) {
      axios.get(SERVER.URL + SERVER.ROUTES.getKidInfo, getters.config)
        .then(res => {
          commit('SET_KID', res.data)
        })
        .catch(err => { console.error(err) })
      },
    getKid({ getters, commit, kidId }) {
      axios.get(SERVER.URL + SERVER.ROUTES.getKidInfo+kidId, getters.config)
        .then(res => {
          commit('SET_KID', res.data)
        })
        .catch(err => { console.error(err) })
    },
  },
  modules: {
  }
})
