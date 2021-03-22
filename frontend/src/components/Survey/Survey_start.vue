<template>
    <div>
        {{ this.name }}<br>
        {{ this.email }}<br>
        {{ this.jwt }}
        <div>
            <button @click="logOut">로그아웃</button>
        </div>
    </div>
</template>
<script>
export default {
  name: "SurveyStart",
  data: () => {
    return {
      name : localStorage.name,
      email : localStorage.email,
      jwt : localStorage.jwt,
    }
  },
  methods : {
      logOut() {
        localStorage.removeItem('jwt');
        localStorage.removeItem('name');
        localStorage.removeItem('email');
        this.isLogin = false;
        alert('로그아웃 되었습니다.');
      this.$router.push({ name: 'Home' });
    },
  },

};
</script>
<style>
</style>