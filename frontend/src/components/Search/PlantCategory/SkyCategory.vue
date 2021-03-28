<template>
  <div id="skycategory">
    <div class="dashedline"></div>
    <div class="skycategoryfilter" id="leaftype" @click="selectleaftype">
      잎 모양
    </div>
    <div class="skycategoryfilter" id="air2" @click="selectair">
      공기정화
    </div>
    <div class="skycategoryfilter" id="flower2" @click="selectflower">
      꽃 피는
    </div>
    <div class="skycategoryfilter" id="light2" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="skycategoryfilter" id="animal2" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="skycategoryfilter" id="fruit2" @click="selectfruit">
      열매 맺는
    </div>
    <div class="skycategoryfilter" id="soil2" @click="selectsoil">
      흙이 필요 없는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "SkyCategory",

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

    selectsoil(){
      this.$emit('callSoil');
    },
  },
  created(){
    
  },
};
</script>
<style>
  #skycategory {
    width: 375px;
    height: 115px;
  }

  .skycategoryfilter {
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

  /* .dashedline {
    width: 330px;
    height: 0px;
    margin: 4% auto 0 auto;

    border: 0.25px dashed #FFFFFF;
  } */

  /* #leaftype {
    float: left;
    margin-left: 5%;
    margin-top: 2%;
  } */

  #air2 {
    width: 82px;
    float: left;
    margin-top: 2%;
  }

  #flower2 {
    width: 72px;
    float: left;
    margin-top: 2%;
    margin-right: 20px;
  }

  #light2 {
    width: 122px;
    float: left;
    margin-left: 5%;
  }

  #animal2 {
    width: 112px;
    float: left;
  }

  #fruit2 {
    width: 82px;
    float: left;
  }

  #soil2 {
    width: 112px;
    float: left;
    margin-left: 5%;
  }
</style>