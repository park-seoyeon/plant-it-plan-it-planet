<template>
  <div id="cactuscategory">
    <div class="dashedline"></div>
    <div class="cactuscategoryfilter" id="leaftype" @click="selectleaftype">
      잎 모양
    </div>
    <div class="cactuscategoryfilter" id="air4" @click="selectair">
      공기정화
    </div>
    <div class="cactuscategoryfilter" id="flower4" @click="selectflower">
      꽃 피는
    </div>
    <div class="cactuscategoryfilter" id="light4" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="cactuscategoryfilter" id="animal4" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="cactuscategoryfilter" id="fruit4" @click="selectfruit">
      열매 맺는
    </div>
    <div class="cactuscategoryfilter" id="stick4" @click="selectstick">
      목대 있는
    </div>
    <div class="cactuscategoryfilter" id="niddle4" @click="selectniddle">
      가시가 없는
    </div>
    <div class="cactuscategoryfilter" id="bottom4" @click="selectbottom">
      밑이 통통한
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "CactusCategory",

  data: () => {
    return {
      
    }
  },
  components: {
    
  },
  methods: {
    selectleaftype(){
      this.$emit('callLeaftype');
    },

    selectair(){
      this.$emit('callAir');
    },

    selectflower(){
      this.$emit('callFlower');
    },

    selectlight(){
      this.$emit('callLight');
    },

    selectanimal(){
      this.$emit('callAnimal');
    },

    selectfruit(){
      this.$emit('callFruit');
    },

    selectstick(){
      this.$emit('callStick');
    },

    selectniddle(){
      this.$emit('callNiddle');
    },

    selectbottom(){
      this.$emit('callBottom');
    },
  },
  created(){
    
  },
};
</script>
<style>
  #cactuscategory {
    width: 375px;
    height: 80px;
  }

  .cactuscategoryfilter {
    width: 82px;
    height: 28px;

    background: #242424;
    border: 1px solid #FFFFFF;
    box-sizing: border-box;
    border-radius: 20px;

    font-family: Binggrae Melona;
    font-style: normal;
    font-weight: normal;
    font-size: 12px;
    line-height: 25px;

    color: #FFFFFF;

    float:left;
    vertical-align: center;
    margin: 0 0 2% 2%;
  }

  #air4 {
    width: 82px;
    float: left;
    margin-top: 2%;
  }

  #flower4 {
    width: 72px;
    float: left;
    margin-top: 2%;
    margin-right: 20px;
  }

  #light4 {
    width: 122px;
    float: left;
    margin-left: 5%;
  }

  #animal4 {
    width: 112px;
    float: left;
  }

  #fruit4 {
    width: 82px;
    float: left;
  }

  #stick4 {
    width: 82px;
    float: left;
    margin-left: 5%;
  }

  #niddle4 {
    width: 92px;
    float: left;
  }

  #bottom4 {
    width: 92px;
    float: left;
  }
</style>