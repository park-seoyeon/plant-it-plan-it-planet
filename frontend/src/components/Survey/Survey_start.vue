<template>
  <div class="content">
    <!-- {{ this.name }}<br>
        {{ this.email }}<br>
        {{ this.jwt }}
        <div>
            <button @click="logOut">로그아웃</button>
        </div> -->

    <div id="logo">
      <img :src="Logo" />
    </div>
    <div id="ask_start">
      설문 조사를 통해<br />나에게 맞는 식물을 알아볼까요?
    </div>
    <div id="ask_ok_button" @click="goSurvey">네, 그렇게 할게요</div>
    <div id="ask_no_button" @click="goMain">아니요, 괜찮아요</div>
  </div>
</template>
<script>
import Logo from '@/assets/img/Logo.png';

export default {
  name: 'SurveyStart',
  data: () => {
    return {
      // name : localStorage.name,
      // email : localStorage.email,
      // jwt : localStorage.jwt,

      Logo: Logo,
    };
  },
  methods: {
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

  // Mount 이전에, localStorage값이 1인 경우 ( 로그인 안해서 storage에 정보가 들어가지 않은 경우 ) Intro로 돌아가라.
  beforeMount(){
    if(localStorage.length == 1){
      alert("로그인 하고 이용해주세요.")
      this.$router.push({ name: 'Home' });
    }
  },
};
</script>
<style></style>
