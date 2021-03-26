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
      this.$router.push({ name: 'SurveyProgress' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
    goMain() {
      this.$router.push({ name: 'Main' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
  },

  // created 할 때 jwt가 없다면 home으로 보내기
  created() {
    const token = localStorage.getItem('jwt');
    if (token == null) {
      alert('로그인 하고 이용해주세요.');
      this.$router.push({ name: 'Home' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    }
  },
};
</script>
<style></style>
