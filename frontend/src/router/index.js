import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '@/views/Home.vue';

import SurveyStart from '@/views/Survey/SurveyStart.vue';
import SurveyProgress from '@/views/Survey/SurveyProgress.vue';
import SurveyResult from '@/views/Survey/SurveyResult.vue';

import Search from "@/views/Search/Search.vue";

import Main from "@/views/Main.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/survey/start',
    name: 'SurveyStart',
    component: SurveyStart,
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
  },
  {
    path: '/survey/progress',
    name: 'SurveyProgress',
    component: SurveyProgress,
  },
  {
    path: '/survey/result',
    name: 'SurveyResult',
    component: SurveyResult,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
