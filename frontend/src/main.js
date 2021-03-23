import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

const APP_KEY = process.env.VUE_APP_KAKAO_KEY;

const APP_KEY = process.env.VUE_APP_KAKAO_KEY;

Vue.config.productionTip = false;

window.Kakao.init(APP_KEY);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
