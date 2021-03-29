<template>
  <div id="searchname">
    <form v-on:submit.prevent="searchplant">
      <img :src="Searchname" />
      <input id="plantname" type="text" ref="plantname" placeholder='검색어를 입력해주세요'>
      <button class="submitbutton" type="submit">검색</button>
    </form>
  </div>
</template>

<script>
// import axios from "axios";
import Searchname from '@/assets/img/searchinput.png';

export default {
  name: "SearchName",

  props: ['filter_list'],

  data: () => {
    return {
      Searchname : Searchname,
    }
  },
  components: {
    
  },
  methods: {
    searchplant() {
      this.$emit('callParent', this.$refs.plantname.value);
      document.getElementById('plantname').value='';
    },

    resetfilters(){

    },
  },
  created(){
    
  },
};
</script>
<style>
  .submitbutton {
    width: 51px;
    height: 31px;
    border: 1px solid white;
    color: white;
    border-radius: 5px;
    vertical-align: middle;
    line-height: 25px;
    font-size: 15px;
    background: rgb(36, 36, 36);
    margin: 0 0 0 3%;
  }

  #searchname {
    margin: 0 0 0 5%;
    padding: 5% 0 0 0;
    width: 500px;
    text-align: left;
  }

  #searchname img {
    width: 3%;
    height: 3%;
    margin: 0 1% 0 0;
    padding: 1% 0 0 0;
  }

  #plantname {
    background: rgb(36, 36, 36);
    border-bottom: 2px solid white;
    border-top: 0px;
    border-left: 0px;
    border-right: 0px;
    color: white;
    width: 240px;
  }
</style>
