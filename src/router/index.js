import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '../views/LoginView.vue'
import RegView from '../views/RegView.vue'
import UserPage from "@/views/UserPageView.vue";
import UserReview from "@/views/userReviewView.vue";
import loadData from "@/views/loadDataView";
import uploadResult from "@/views/loadDataResultView";
import loadDataResultView from "@/views/loadDataResultView";
const routes = [
  {
    path: '/',
    name: 'userReview',
    component: UserReview,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginForm
    
  },
  {
    path: '/reg',
    name: 'reg',
    component: RegView
  },
  {
    path: '/user:id',
    name: 'user',
    component: UserPage,
    props: true
  },
  {
    path: '/upload',
    name: 'upload',
    component: loadData
  },
  {
    path: '/uploadResult',
    name: 'uploadResult',
    component: uploadResult
  },
  {
    path: '/checkData?:platform',
    name: 'checkData',
    component: loadDataResultView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
/* router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!user) {
      return({ name: 'login' })
    } else {
      next() // go to wherever I'm going
    }
  } else {
    next() // does not require auth, make sure to always call next()!
  }
}) */


export default router
