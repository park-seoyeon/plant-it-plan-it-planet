<template>
  <div id="app">
    <router-view />
    <Navbar />
  </div>
</template>

<script>
import Navbar from '@/components/Nav/Navbar.vue';
export default {
  data: () => {
    return {};
  },
  components: {
    Navbar,
  },
};
</script>

<style>
@font-face {
  font-family: 'KyoboHand';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/KyoboHand.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'BMHANNAAir';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.0/BMHANNAAir.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'DungGeunMo';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Cafe24Oneprettynight';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Oneprettynight.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}

@import './assets/css/display.css';
@import './assets/css/intro.css';
@import './assets/css/login.css';
@import './assets/css/survey.css';
@import './assets/css/loading.css';
@import './assets/css/search.css';
@import './assets/css/plantCategory.css';
@import './assets/css/skyCategory.css';
@import './assets/css/leafCategory.css';
@import './assets/css/dungulCategory.css';
@import './assets/css/cactusCategory.css';
@import './assets/css/leafType.css';
@import './assets/css/searchDetail.css';
@import './assets/css/planit.css';
@import './assets/css/planit-myplant.css';
@import './assets/css/planit-foryou.css';
@import './assets/css/planit-magazine.css';
@import './assets/css/myplant.css';
@import './assets/css/modal.css';
@import './assets/css/myplant-detail.css';
@import './assets/css/myplant-cards.css';
@import './assets/css/mypage.css';
@import './assets/css/magazine.css';
@import './assets/css/nav-bar.css';

#app {
  font-family: 'NanumSquare', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  height: 100%;
  align-self: center;
}

html {
  margin: 0px;
  height: 100%;
}

body {
  background-color: #252525;
  font-family: 'NanumSquare', sans-serif;
  margin: 0px;
  height: 100%;
}
</style>
