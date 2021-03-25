<template>
    <div id="searchlist">

      <p class="plantscardtitle">식물 데이터</p>

      <PlantsCard v-for="(plants, idx) in plant_list" :key="idx" :plants="plants" />
    </div>
</template>

<script>
// import axios from "axios";

import PlantsCard from '@/components/Search/PlantsCard.vue';

export default {
  name: "SearchList",

  props: ['plant_list'],

  data: () => {
    return {
      
    }
  },
  components: {
    PlantsCard,
  },
  methods: {
    
  },
  created(){
    
  },
};
</script>
<style>
    .plantscardtitle {
        text-align: left;
        color: white;
        padding: 0 0 0 5%;
        font-weight: bold;
    }
</style>
