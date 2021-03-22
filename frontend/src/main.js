import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

window.Kakao.init('676c5fa31785f08e2ce866bd98c4c645');

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");