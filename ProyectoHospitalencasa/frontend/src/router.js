import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import GlobalSearch from './components/GlobalSearch.vue'
import DetailedSearch from './components/DetailedSearch.vue'
import Help from './components/Help.vue'


const routes = [{
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/user/logIn',
    name: "logIn",
    component: LogIn
  },
  {
    path: '/user/signUp',
    name: "signUp",
    component: SignUp
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
  },
  {
    path: '/user/help',
    name: "help",
    component: Help
  },
  {
    path: '/search/global',
    name: "GlobalSearch",
    component: GlobalSearch
  },
  {
    path: '/search/detailed',
    name: "DetailedSearch",
    component: DetailedSearch
  },
  {
    path: '/search/detailed/:id',
    name: "DetailedSearchidd",
    component: DetailedSearch
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;