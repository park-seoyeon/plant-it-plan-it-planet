<template>
  <div id="skycategory">
    <div class="skycategoryfilter" @click="selectleaftype">
      잎 모양
    </div>
    <div class="skycategoryfilter" @click="selectair">
      공기정화
    </div>
    <div class="skycategoryfilter" @click="selectflower">
      꽃 피는
    </div>
    <div class="skycategoryfilter" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="skycategoryfilter" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="skycategoryfilter" @click="selectfruit">
      열매 맺는
    </div>
    <div class="skycategoryfilter" @click="selectsoil">
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
  .skycategoryfilter {
    width: 50px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 5px;
  }
</style>