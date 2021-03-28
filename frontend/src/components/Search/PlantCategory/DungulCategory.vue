<template>
  <div id="dungulcategory">
    <div class="dashedline"></div>
    <div class="dungulcategoryfilter" id="leaftype" @click="selectleaftype">
      잎 모양
    </div>
    <div class="dungulcategoryfilter" id="air3" @click="selectair">
      공기정화
    </div>
    <div class="dungulcategoryfilter" id="flower3" @click="selectflower">
      꽃 피는
    </div>
    <div class="dungulcategoryfilter" id="light3" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="dungulcategoryfilter" id="animal3" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="dungulcategoryfilter" id="fruit3" @click="selectfruit">
      열매 맺는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "DungulCategory",

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
  },
  created(){
    
  },
};
</script>
<style>
  #dungulcategory {
    width: 375px;
    height: 80px;
  }

  .dungulcategoryfilter {
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

  #air3 {
    width: 82px;
    float: left;
    margin-top: 2%;
  }

  #flower3 {
    width: 72px;
    float: left;
    margin-top: 2%;
    margin-right: 20px;
  }

  #light3 {
    width: 122px;
    float: left;
    margin-left: 5%;
  }

  #animal3 {
    width: 112px;
    float: left;
  }

  #fruit3 {
    width: 82px;
    float: left;
  }
</style>