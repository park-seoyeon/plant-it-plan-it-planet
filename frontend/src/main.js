import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import firebase from "firebase";

const APP_KEY = process.env.VUE_APP_KAKAO_KEY;

const FIREBASE_KEY = process.env.VUE_APP_FIREBASE_KEY;
const FIREBASE_DOMAIN = process.env.VUE_APP_FIREBASE_DOMAIN;
const FIREBASE_PROJECTID = process.env.VUE_APP_FIREBASE_PROJECTID;
const FIREBASE_STORAGEBUCKET = process.env.VUE_APP_FIREBASE_STORAGEBUCKET;
const FIREBASE_SENDERID = process.env.VUE_APP_FIREBASE_SENDERID;
const FIREBASE_APPID = process.env.VUE_APP_FIREBASE_APPID;
const FIREBASE_MEASUREMENTID = process.env.VUE_APP_FIREBASE_MEASUREMENTID;

Vue.config.productionTip = false;

window.Kakao.init(APP_KEY);

new Vue({
  router,
  store,
  render: (h) => h(App),
  created() {
      // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      var firebaseConfig = {
        apiKey: FIREBASE_KEY,
        authDomain: FIREBASE_DOMAIN,
        projectId: FIREBASE_PROJECTID,
        storageBucket: FIREBASE_STORAGEBUCKET,
        messagingSenderId: FIREBASE_SENDERID,
        appId: FIREBASE_APPID,
        measurementId: FIREBASE_MEASUREMENTID,
      };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      firebase.analytics();
  },
}).$mount('#app');
