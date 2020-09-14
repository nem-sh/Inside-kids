import Vue from 'vue'
import VueRouter from 'vue-router'

//도연
import KidsDetailView from '@/views/parents/KidsDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: "/:kidId",
    name: "KidsDetailView",
    component: KidsDetailView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
