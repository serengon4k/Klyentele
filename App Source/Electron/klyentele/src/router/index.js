import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  },
  {
    path: '/setup/start',
    name: 'SetupStart',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Setup/StartView.vue')
    }
  },
  {
    path: '/setup/legal',
    name: 'LicenseAgreement',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Setup/LicenseAgreementView.vue')
    }
  },
  {
    path: '/setup/licensekey',
    name: 'LicenseKeyEntry',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Setup/LicenseKeyEntryView.vue')
    }
  },
  {
    path: '/setup/pincreation',
    name: 'PinCreation',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Setup/SignUpView.vue')
    },
    props: true
  },
  {
    path: '/setup/finish',
    name: 'SetupFinish',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Setup/SetupFinishView.vue')
    },
    props: true
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
