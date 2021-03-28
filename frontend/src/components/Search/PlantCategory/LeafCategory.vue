<template>
  <div id="leafcategory">
    <div class="dashedline"></div>
    <div class="leafcategoryfilter" id="leaftype" @click="selectleaftype">
      잎 모양
    </div>
    <div class="leafcategoryfilter" id="air" @click="selectair">
      공기정화
    </div>
    <div class="leafcategoryfilter" id="smell" @click="selectsmell">
      향기나는
    </div>
    <div class="leafcategoryfilter" id="animal" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="leafcategoryfilter" id="light" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="leafcategoryfilter" id="fruit" @click="selectfruit">
      열매 맺는
    </div>
    <div class="leafcategoryfilter" id="stick" @click="selectstick">
      목대 있는
    </div>
    <div class="leafcategoryfilter" id="bottom" @click="selectbottom">
      밑이 통통한
    </div>
    <div class="leafcategoryfilter" id="flower" @click="selectflower">
      꽃이 피는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "LeafCategory",

  data: () => {
    return {
      filter : 0,
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

    selectsmell(){
      this.$emit('callSmell');
    },

    selectanimal(){
      this.$emit('callAnimal');
    },

    selectlight(){
      this.$emit('callLight');
    },

    selectfruit(){
      this.$emit('callFruit');
    },

    selectstick(){
      this.$emit('callStick');
    },

    selectbottom(){
      this.$emit('callBottom');
    },

    selectflower(){
      this.$emit('callFlower');
    },
  },
  created(){
    
  },
};
</script>
<style>
  #leafcategory {
    width: 375px;
    height: 115px;
  }

  .leafcategoryfilter {
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

  .dashedline {
    width: 330px;
    height: 0px;
    margin: 4% auto 0 auto;

    border: 0.25px dashed #FFFFFF;
  }

  #leaftype {
    /* width: 66px; */
    float: left;
    margin-left: 5%;
    margin-top: 2%;
  }

  #air {
    width: 82px;
    float: left;
    margin-top: 2%;
  }

  #smell {
    width: 82px;
    float: left;
    margin-top: 2%;
  }

  #animal {
    width: 109px;
    float: left;
    margin-left: 5%;
  }

  #light {
    width: 109px;
    float: left;
  }

  #fruit {
    width: 82px;
    float: left;
  }

  #stick {
    width: 82px;
    float: left;
    margin-left: 5%;
  }

  #bottom {
    width: 82px;
    float: left;
  }

  #flower {
    width: 82px;
    float: left;
  }
</style>