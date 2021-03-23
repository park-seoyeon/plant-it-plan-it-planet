<template>
  <div class="content">
    <div id="logo">
      <img :src="Logo" />
    </div>
    <div id="logo_text">
      플랜잇과<br /><br />
      식물친구 만들기
    </div>
    <div id="logo_plantimg">
      <img :src="Plantimg" />
    </div>
    <div id="login_button" @click="requestKakao">
      <div id="login_button_kakao">
        <img :src="kakao" />
      </div>
      <div id="login_button_text">카카오 로그인</div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

import Logo from '@/assets/img/Logo.png';
import Plantimg from '@/assets/img/Login_plantimg.png';
import kakao from '@/assets/img/kakao.png';

export default {
  name: 'Login',
  data: () => {
    return {
      isLogin: false,
      Logo: Logo,
      Plantimg: Plantimg,
      kakao: kakao,
    };
  },
  methods: {
    requestKakao() {
      window.Kakao.Auth.authorize({
        redirectUri: `http://localhost:8080`,
      });
      //   this.$router.push({ name: 'SurveyStart' })
    },
    // loginKakao(){
    //   axios
    //     .post(`http://localhost:8000/login/`, {'code':this.code})
    //     .then((response)=>{
    //       console.log(response)

    //       // localStorage 또는 vuex 사용해서 jwt 토큰 저장 가능한데,
    //       // 일단 localStorage 사용해서 추후에 기능들 개발할 때 jwt가 필요한 경우 꺼내서 사용
    //       // 로그인 기능에서는 저장만 해줍니다.
    //       localStorage.setItem('email', response.data['email']);
    //       localStorage.setItem('name', response.data['name']);
    //       localStorage.setItem('jwt', response.data['access_token']);

    //       history.pushState(null, '', `/`);
    //     })
    // },
  },
  created() {
    // this.code = this.$route.query.code;
    // if (this.code != null || this.code != undefined) {
    //   this.loginKakao();
    // }
  },
};
</script>

<style></style>
