import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";

import SurveyStart from "../views/Survey/Survey_select.vue";
import SurveyProgress from "../components/Survey/Survey_progress.vue";
import SurveyResult from "../components/Survey/Survey_result.vue";

import Search from "../views/Search/Search.vue";

import Main from "../views/Main.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/survey_start",
    name: "SurveyStart",
    component: SurveyStart,
  },
  {
    path: "/main",
    name: "Main",
    component: Main,
  },
  {
    path: "/survey_progress",
    name: "SurveyProgress",
    component: SurveyProgress,
  },
  {
    path: "/survey_result",
    name: "SurveyResult",
    component: SurveyResult,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
