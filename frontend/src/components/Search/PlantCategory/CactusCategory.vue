<template>
  <div id="cactuscategory">
    <div class="cactuscategoryfilter" @click="selectleaftype">
      잎 모양
    </div>
    <div class="cactuscategoryfilter" @click="selectair">
      공기정화
    </div>
    <div class="cactuscategoryfilter" @click="selectflower">
      꽃 피는
    </div>
    <div class="cactuscategoryfilter" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="cactuscategoryfilter" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="cactuscategoryfilter" @click="selectfruit">
      열매 맺는
    </div>
    <div class="cactuscategoryfilter" @click="selectstick">
      목대 있는
    </div>
    <div class="cactuscategoryfilter" @click="selectniddle">
      가시가 없는
    </div>
    <div class="cactuscategoryfilter" @click="selectbottom">
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
  .cactuscategoryfilter {
    width: 38px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 5px;
  }
</style>