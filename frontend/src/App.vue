<template>
  <div id="app">
    <img src="./assets/logo.png" @click="requestKakao">
    <div>
      {{ userInfo.name }}
      <br>
      {{ userInfo.email }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data: () => {
    return {
      userInfo: {
        name : "test_name",
        email : "test_email",
      },
      isLogin: false,

    }
  },
  methods: {
    requestKakao() {
      window.Kakao.Auth.authorize({
        redirectUri: `http://localhost:8080`,
        });
    },

  },
  created(){

    const token = localStorage.getItem('jwt');
    if (token) {
      this.isLogin = true;
      this.userInfo.name = localStorage.getItem('name');
    }

    this.code = this.$route.query.code;
    if (this.code != null || this.code != undefined) {
      axios
        .post(`http://localhost:8000/login/`, this.code)
        .then((response) => {
          history.pushState(null, '', `/`);
          // let userInfo = null;
          if (response.data['oauth-result'] === 'success') {
            userInfo = response.data['userInfo'];
            localStorage.setItem('jwt', response.data['access-token']);
            localStorage.setItem('name', response.data['userInfo'].name);
            localStorage.setItem('user_number', response.data['userInfo'].user_number);
            location.reload();
          } else {
            // const result = confirm('이미 존재하는 이메일입니다. 카카오 계정으로 통합하시겠습니까?');

            if (result) {
              userInfo = response.data['userInfo'];
              axios.post(`${SERVER_URL}/kakao/login/merge`, userInfo).then((response) => {
                history.pushState(null, '', `/`);
                if (response.data['oauth-result'] === 'success') {
                  userInfo = response.data['userInfo'];
                  localStorage.setItem('jwt', response.data['access-token']);
                  localStorage.setItem('name', response.data['userInfo'].name);
                  localStorage.setItem('user_number', response.data['userInfo'].user_number);
                  location.reload();
                } else {
                  alert('카카오 로그인에 실패하셨습니다');
                  this.$router.push({ name: 'Home' }).catch((error) => {
                    if (error.name === 'NavigationDuplicated') {
                      location.reload();
                    }
                  });
                }
              });
            }
          }
        })
        .catch(() => {
          alert('로그인중 오류가 발생했습니다. 다시 로그인 해주세요.');
          this.$router.push({ name: 'Home' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        });
    }
  }

}
</script>