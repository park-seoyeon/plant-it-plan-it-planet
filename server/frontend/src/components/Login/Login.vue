<template>
  <div class="content">
    <div id="login-logo">
      <img :src="Logo" />
    </div>
    <div id="login-title">Plant it Plan it Planet</div>
    <div id="login-logo-plantimg">
      <img :src="planticon" />
      <img :src="planicon" />
      <img :src="planeticon" style="margin-right: 0" />
    </div>
    <div id="login-division-bar"></div>
    <div id="login-logo-text">
      <b>"Plant it"</b> 나만의 식물을 추천받아 <br />
    </div>
    <div id="login-logo-text"><b>"Plan it"</b> 체계적으로 관리하고 <br /></div>
    <div id="login-logo-text"><b>"Planet"</b> 행성을 가꾸어 나가요 <br /></div>
    <div id="login-division-bar"></div>
    <div id="login-button" @click="requestKakao">
      <div id="login-button-kakao">
        <img :src="kakao" />
      </div>
      <div id="login-button-text">카카오 로그인</div>
    </div>
  </div>
</template>

<script>
import planticon from '@/assets/img/plantit_icon.png';
import planicon from '@/assets/img/planit_icon.png';
import planeticon from '@/assets/img/planet_icon.png';
import Logo from '@/assets/img/Logo.png';
import kakao from '@/assets/img/kakao.png';

export default {
  name: 'Login',
  data: () => {
    return {
      planticon: planticon,
      planicon: planicon,
      planeticon: planeticon,
      isLogin: false,
      Logo: Logo,

      kakao: kakao,
    };
  },
  methods: {
    requestKakao() {
      window.Kakao.Auth.authorize({
        redirectUri: `http://j4a101.p.ssafy.io`,
      });
    },
  },
};
</script>

<style></style>
