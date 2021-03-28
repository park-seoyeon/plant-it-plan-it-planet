<template>
  <div id="searchname">
    <form v-on:submit.prevent="searchplant">
      <input id="plantname" type="text" ref="plantname">
      <button class="submitbutton" type="submit">검색</button>
    </form>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "SearchName",

  props: ['filter_list'],

  data: () => {
    return {
      
    }
  },
  components: {
    
  },
  methods: {
    searchplant() {
      this.$emit('callParent', this.$refs.plantname.value);
      document.getElementById('plantname').value='';
    }
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
    margin: 0 0 0 5%;
  }

  #searchname {
    margin: 0 0 0 5%;
    padding: 8% 0 0 0;
    width: 370px;
  }
</style>
