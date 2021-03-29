<template>
  <div id="plantcategory">
    <div class="plantcategoryfilter" id="leaf" @click="selectleaf">
      잎이 있는 식물
    </div>
    <div class="plantcategoryfilter" id="sky" @click="selectsky">
      공중식물
    </div>
    <div class="plantcategoryfilter" id="dungul" @click="selectdungul">
      덩굴식물
    </div>
    <div class="plantcategoryfilter" id="cactus" @click="selectcactus">
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
  /* #leaf:hover {
    border: 2px solid #00b564;
    color: #00b564;
    font-size: 12px;
    line-height: 25px;
    vertical-align: middle;
  } */

  #plantcategory {
    width: 375px;
    height: 56px;
  }

  #leaf {
    width: 106px;
    float: left;
    margin-left: 5%;
  }

  #sky {
    width: 82px;
    float: left;
    margin-right: 100px;
  }

  #dungul {
    width: 82px;
    float: left;
    margin-top: 2%;
    margin-left: 5%;
  }

  #cactus {
    width: 106px;
    float: left;
    margin-top: 2%;
  }

  .plantcategoryfilter {
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
    vertical-align: middle;
    margin: 0 0 0 2%;
  }
</style>
