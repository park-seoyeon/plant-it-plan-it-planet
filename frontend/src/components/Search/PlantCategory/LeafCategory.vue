<template>
  <div id="leafcategory">
    <div class="leafcategoryfilter" @click="selectleaftype">
      잎 모양
    </div>
    <div class="leafcategoryfilter" @click="selectair">
      공기정화
    </div>
    <div class="leafcategoryfilter" @click="selectsmell">
      향기나는
    </div>
    <div class="leafcategoryfilter" @click="selectanimal">
      반려동물 안전한
    </div>
    <div class="leafcategoryfilter" @click="selectlight">
      빛이 적어도 되는
    </div>
    <div class="leafcategoryfilter" @click="selectfruit">
      열매 맺는
    </div>
    <div class="leafcategoryfilter" @click="selectstick">
      목대 있는
    </div>
    <div class="leafcategoryfilter" @click="selectbottom">
      밑이 통통한
    </div>
    <div class="leafcategoryfilter" @click="selectflower">
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
  .leafcategoryfilter {
    width: 38px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 5px;
  }
</style>