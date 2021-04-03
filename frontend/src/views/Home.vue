<template>
  <div class="home">
    <div v-if="isStatusOn" @click="toggleOnOff" style="height: 100%">
      <Intro />
    </div>
    <div v-else style="height: 100%">
      <Login />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Login from '@/components/Login/Login.vue';
import Intro from '@/components/Intro/Intro.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Home',
  data: () => {
    return {
      isStatusOn: true,
      isLogin: false,
    };
  },
  components: {
    Login,
    Intro,
  },
  methods: {
    toggleOnOff: function () {
      if (this.isLogin) {
        this.isStatusOn = true;
        if (localStorage.getItem('is_survey') == 1) {
          this.$router.push({ name: 'Main' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        } else {
          this.$router.push({ name: 'SurveyStart' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        }
      } else {
        this.isStatusOn = false;
        // this.$router.push({ name: 'Login' })
      }
    },
    loginKakao() {
      axios
        .post(`${SERVER_URL}/login/`, { code: this.code })
        .then((response) => {
          history.pushState(null, '', `/`);
          // console.log(response)

          // localStorage 또는 vuex 사용해서 jwt 토큰 저장 가능한데,
          // 일단 localStorage 사용해서 추후에 기능들 개발할 때 jwt가 필요한 경우 꺼내서 사용
          // 로그인 기능에서는 저장만 해줍니다.
          localStorage.setItem('email', response.data['email']);
          localStorage.setItem('name', response.data['name']);
          localStorage.setItem('jwt', response.data['access_token']);
          localStorage.setItem('user_number', response.data['user_number']);
          localStorage.setItem('is_survey', response.data['is_survey']);

          location.reload();
          // this.$router.push({ name: 'SurveyStart' });
        })
        .catch(() => {
          alert('로그인중 오류가 발생했습니다. 다시 로그인 해주세요.');
          this.$router.push({ name: 'Home' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        });
    },
  },
  created() {
    const token = localStorage.getItem('jwt');

    if (token) {
      this.isLogin = true;
    }
    this.code = this.$route.query.code;
    if (this.code != null || this.code != undefined) {
      this.loginKakao();
    }
  },
};
</script>
