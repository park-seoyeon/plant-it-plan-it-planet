<template>
  <div id="leaftype">
    <div class="dashedline2"></div>
    <div class="leaftypefilter" id="select1" @click="select1">
      구멍
    </div>
    <div class="leaftypefilter" id="select2" @click="select2">
      넓은
    </div>
    <div class="leaftypefilter" id="select3" @click="select3">
      둥근
    </div>
    <div class="leaftypefilter" id="select4" @click="select4">
      뾰족한
    </div>
    <div class="leaftypefilter" id="select5" @click="select5">
      길쭉한
    </div>
    <div class="leaftypefilter" id="select6" @click="select6">
      갈라진
    </div>
    <div class="leaftypefilter" id="select7" @click="select7">
      하트모양
    </div>
    <div class="leaftypefilter" id="select8" @click="select8">
      별모양
    </div>
    <div class="leaftypefilter" id="select9" @click="select9">
      작은
    </div>
    <div class="leaftypefilter" id="select10" @click="select10">
      두꺼운
    </div>
    <div class="leaftypefilter" id="select11" @click="select11">
      무늬
    </div>
    <div class="leaftypefilter" id="select12" @click="select12">
      꽃 모양
    </div>
    <div class="leaftypefilter" id="select13" @click="select13">
      통통한
    </div>
    <div class="leaftypefilter" id="select14" @click="select14">
      납작한
    </div>
    <div class="leaftypefilter" id="select15" @click="select15">
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

  .dashedline2 {
    width: 330px;
    height: 0px;
    margin: -10px auto 0 auto;

    border: 0.25px dashed #FFFFFF;
  }

  #select1{
    width: 62px;
    float: left;
    margin-left: 5%;
    margin-top: 2%;
  }

  #select2{
    width: 62px;
    float: left;
    margin-top: 2%;
  }

  #select3{
    width: 62px;
    float: left;
    margin-top: 2%;
  }

  #select4{
    width: 72px;
    float: left;
    margin-top: 2%;
  }

  #select5{
    width: 72px;
    float: left;
    margin-left: 5%;
  }

  #select6{
    width: 72px;
    float: left;
  }

  #select7{
    width: 80px;
    float: left;
  }

  #select8{
    width: 72px;
    float: left;
  }

  #select9{
    width: 62px;
    float: left;
    margin-left: 5%;
  }

  #select10{
    width: 72px;
    float: left;
  }

  #select11{
    width: 62px;
    float: left;
  }

  #select12{
    width: 80px;
    float: left;
  }

  #select13{
    width: 72px;
    float: left;
    margin-left: 5%;
  }

  #select14{
    width: 72px;
    float: left;
  }

  #select15{
    width: 90px;
    float: left;
  }

</style>