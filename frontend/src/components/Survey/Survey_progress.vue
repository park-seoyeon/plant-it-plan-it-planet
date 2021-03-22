<template>
    <div class="content">
        <div id="icons">
            <img :src='planticon'>
            <img :src='planicon'>
            <img :src='planeticon' style="margin-right: 0;">  
        </div>

        <!-- 상태바 찾아서 넣기 -->
        <!-- 임시로 css로 흰색 얇은 박스 하나 넣어놈 -->
        <div id="progressbar">
            
        </div>
                      
        <div id="ask">
          처음 만난 사람들에게 나는?
        </div>

        <div class="buttons">
            1번 답안
        </div>
        <div class="buttons">
            2번 답안
        </div>
        <div class="buttons">
            3번 답안
        </div>
        <div class="buttons">
            4번 답안
        </div>
    </div>
</template>
<script>
import planticon from '@/assets/img/plantit_icon.png'
import planicon from '@/assets/img/planit_icon.png'
import planeticon from '@/assets/img/planet_icon.png'

export default {
  name: "SurveyProgress",
  data: () => {
    return {
        planticon : planticon,
        planicon : planicon,
        planeticon : planeticon,
    }
  },
  methods : {
    
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

    .content #icons {
        padding: 20% 0 0 0;
    }

    .content #icons img {
        width: 15%;
        height: 15%;
        margin: 0 5% 0 0;
    }

    .content #progressbar {
        height: 5px;
        background: white;
        width: 80%;
        margin: 5% auto 0 auto;
    }

    .content #ask {
      color: white;
      margin: 10% 0 20% 0;
      font-size: 18px;
    }

    .content .buttons {
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