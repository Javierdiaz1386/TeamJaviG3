import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import LogIn from './components/LogIn.vue'
import SignUpMedico from './components/SignUpMedico.vue'
import SignUpAuxiliar from './components/SignUpAuxiliar.vue'
import SignUpPaciente from './components/SignUpPaciente.vue'
import SignUpFamiliar from './components/SignUpFamiliar.vue'
import Home from './components/Home.vue'
import GlobalSearch from './components/GlobalSearch.vue'
import DetailedSearch from './components/DetailedSearch.vue'
import DetailedSearchIds from './components/DetailedSearchIds.vue'
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
    path: '/user/signUpMedico',
    name: "signUpMedico",
    component: SignUpMedico
  },
  {
    path: '/user/signUpAuxiliar',
    name: "signUpAuxiliar",
    component: SignUpAuxiliar
  },
  {
    path: '/user/signUpPaciente',
    name: "signUpPaciente",
    component: SignUpPaciente
  },
  {
    path: '/user/signUpFamiliar',
    name: "signUpFamiliar",
    component: SignUpFamiliar
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
    path: '/search/DetailedSearchIds/:id',
     name: "DetailedSearchIds",
    component: DetailedSearchIds
   },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;