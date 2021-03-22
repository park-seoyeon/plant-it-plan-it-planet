<template>
  <div class="content">
    <div id="Introimg">
        <img :src='Introimg'>
    </div>
    <div id="clicktostart">
        click to start
    </div>
  </div>
</template>

<script>
import Introimg from '@/assets/img/Introimg.gif'

export default {
  name: "Intro",
  data() {
      return {
          Introimg : Introimg,
      }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

    .content #Introimg img {
        height: 80%;
        width: 80%;
        margin: 50% 0 0 0;
    }

    .content #clicktostart {
        color: white;
        margin: 10% 0 0 0;
    }
    
</style>
