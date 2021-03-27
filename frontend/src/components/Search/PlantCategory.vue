<template>
  <div id="plantcategory">
    <div class="plantcategoryfilter" @click="selectleaf">
      잎이 있는 식물
    </div>
    <div class="plantcategoryfilter" @click="selectsky">
      공중식물
    </div>
    <div class="plantcategoryfilter" @click="selectdungul">
      덩굴식물
    </div>
    <div class="plantcategoryfilter" @click="selectcactus">
      선인장/다육식물
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "PlantCategory",

  data: () => {
    return {
      selectleafbutton : false,
    }
  },
  components: {
    
  },
  methods: {
    selectleaf(){
      this.$emit('callLeaf');
    },

    selectsky(){
      this.$emit('callSky');
    },

    selectdungul(){
      this.$emit('callDungul');
    },

    selectcactus(){
      this.$emit('callCactus');
    },
  },
  created(){
    
  },
};
</script>
<style>
  .plantcategoryfilter {
    width: 90px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 10px;
  }
</style>
