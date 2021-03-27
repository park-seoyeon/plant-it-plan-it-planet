<template>
  <div id="leaftype">
    <div class="leaftypefilter" @click="select1">
      구멍
    </div>
    <div class="leaftypefilter" @click="select2">
      넓은
    </div>
    <div class="leaftypefilter" @click="select3">
      둥근
    </div>
    <div class="leaftypefilter" @click="select4">
      뾰족한
    </div>
    <div class="leaftypefilter" @click="select5">
      길쭉한
    </div>
    <div class="leaftypefilter" @click="select6">
      갈라진
    </div>
    <div class="leaftypefilter" @click="select7">
      하트모양
    </div>
    <div class="leaftypefilter" @click="select8">
      별모양
    </div>
    <div class="leaftypefilter" @click="select9">
      작은
    </div>
    <div class="leaftypefilter" @click="select10">
      두꺼운
    </div>
    <div class="leaftypefilter" @click="select11">
      무늬
    </div>
    <div class="leaftypefilter" @click="select12">
      꽃 모양
    </div>
    <div class="leaftypefilter" @click="select13">
      통통한
    </div>
    <div class="leaftypefilter" @click="select14">
      납작한
    </div>
    <div class="leaftypefilter" @click="select15">
      잎이 없음
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "LeafType",

  data: () => {
    return {
      
    }
  },
  components: {
    
  },
  methods: {
    select1(){
      this.$emit('call1');
    },
    select2(){
      this.$emit('call2');
    },
    select3(){
      this.$emit('call3');
    },
    select4(){
      this.$emit('call4');
    },
    select5(){
      this.$emit('call5');
    },
    select6(){
      this.$emit('call6');
    },
    select7(){
      this.$emit('call7');
    },
    select8(){
      this.$emit('call8');
    },
    select9(){
      this.$emit('call9');
    },
    select10(){
      this.$emit('call10');
    },
    select11(){
      this.$emit('call11');
    },
    select12(){
      this.$emit('call12');
    },
    select13(){
      this.$emit('call13');
    },
    select14(){
      this.$emit('call14');
    },
    select15(){
      this.$emit('call15');
    },
  },
  created(){
    
  },
};
</script>
<style>
  .leaftypefilter {
    width: 80px;
    height: 20px;
    border: 1px solid white;
    color: white;
    float: left;
    font-size: 5px;
  }
</style>