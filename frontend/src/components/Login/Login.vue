<template>
  <div class="content">
    <div id="logo">
        <img :src='Logo'>
    </div>
    <div id="logo_text">
        플랜잇과<br><br> 식물친구 만들기
    </div>
    <div id="logo_plantimg">
        <img :src='Plantimg'>
    </div>
    <div id="login_button" @click="requestKakao">
        <div id="login_button_kakao">
            <img :src='kakao'>
        </div>
        <div id="login_button_text">
            카카오 로그인
        </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

import Logo from '@/assets/img/Logo.png'
import Plantimg from '@/assets/img/Login_plantimg.png'
import kakao from '@/assets/img/kakao.png'

export default {
  name: "Login",
  data: () => {
    return {
      isLogin: false,
      Logo : Logo,
      Plantimg : Plantimg,
      kakao : kakao,
    }
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

<style scoped>
    .content {
        /* background-color: black; */
        background: rgb(36, 36, 36) no-repeat center center fixed; 
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
        text-align: center;
        background-size: 100%;
        min-height: 800px;
    }

    .content #logo img {
        margin: 30% 0 0 0;
    }

    .content #logo_text {
        color: white;
        text-align: left;
        margin: 20% 0 0 20%;
        font-size: 20px;
    }

    .content #logo_plantimg {
        margin: 20% 0 0 0;
    }

    .content #login_button {
        border: 2px solid white;
        border-radius: 10px;
        width: 80%;
        height: 60px;
        margin: 10% auto 0 auto;
        color: white;
    }

    .content #login_button #login_button_kakao {
        float: left;
        margin: 8px 0 0 -40px;
    }

    .content #login_button #login_button_kakao img {
        width: 30%;
        height: 30%;
    }

    .content #login_button #login_button_text {
        width: 150px;
        float: left;
        margin: 15px 0 0 -10px;
        font-size: 20px;
    }
</style>
