<template>
  <div class="main">
    Main page
  </div>

</template>

<script>
// import axios from "axios";

export default {
  name: "Main",
  data: () => {
    return {
      
    }
  },
  components: {
    
  },
  methods: {
    
  },
  created(){
    
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
