<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
@import './assets/css/display.css';
@import './assets/css/intro.css';
@import './assets/css/login.css';
@import './assets/css/survey.css';
@import './assets/css/loading.css';

#app {
  font-family: 'Noto Sans KR', sans-serif;
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
  margin: 0px;
  height: 100%;
}
</style>
