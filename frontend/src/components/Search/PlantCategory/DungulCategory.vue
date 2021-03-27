<template>
  <div id="dungulcategory">
    <div class="dungulcategoryfilter" @click="selectleaftype">
      잎 모양
    </div>
    <div class="dungulcategoryfilter" @click="selectair">
      공기정화
    </div>
    <div class="dungulcategoryfilter" @click="selectflower">
      꽃 피는
    </div>
    <div class="dungulcategoryfilter" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="dungulcategoryfilter" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="dungulcategoryfilter" @click="selectfruit">
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
  .dungulcategoryfilter {
    width: 60px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 5px;
  }
</style>