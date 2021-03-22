<template>
    <div class="content">
        <!-- {{ this.name }}<br>
        {{ this.email }}<br>
        {{ this.jwt }}
        <div>
            <button @click="logOut">로그아웃</button>
        </div> -->

        <div id="logo">
          <img :src='Logo'>
        </div>
        <div id="ask">
          설문 조사를 통해<br>나에게 맞는 식물을 알아볼까요?
        </div>
        <div id="ask_ok_button" @click="goSurvey">
          네, 그렇게 할게요
        </div>
        <div id="ask_no_button" @click="goMain">
          아니요, 괜찮아요
        </div>
    </div>
</template>
<script>
import Logo from '@/assets/img/Logo.png'

export default {
  name: "SurveyStart",
  data: () => {
    return {
      // name : localStorage.name,
      // email : localStorage.email,
      // jwt : localStorage.jwt,

      Logo : Logo,
    }
  },
  methods : {
      // logOut() {
      //   localStorage.removeItem('jwt');
      //   localStorage.removeItem('name');
      //   localStorage.removeItem('email');
      //   this.isLogin = false;
      //   alert('로그아웃 되었습니다.');
      // this.$router.push({ name: 'Home' });
    // },
    goSurvey() {
      this.$router.push({ name: 'SurveyProgress' });
    },
    goMain() {
      this.$router.push({ name: 'Main' });
    },
  },

};
</script>
<style>
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

    .content #ask {
      color: white;
      margin: 20% 0 0 0;
    }

    .content #ask_ok_button {
      border: 2px solid white;
      border-radius: 10px;
      width: 80%;
      height: 60px;
      margin: 15% auto 0 auto;
      color: white;
      font-size: 18px;
      vertical-align: middle;
      line-height: 60px;
    }

    .content #ask_no_button {
      border: 2px solid white;
      border-radius: 10px;
      width: 80%;
      height: 60px;
      margin: 10% auto 0 auto;
      color: white;
      font-size: 18px;
      vertical-align: middle;
      line-height: 60px;
    }
</style>