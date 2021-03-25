<template>
  <div id="searchname">
    <form v-on:submit.prevent="searchplant">
        <div>
            <input id="plantname" type="text" ref="plantname">
        </div>
        <div>
            <button type="submit">검색</button>
        </div>
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
