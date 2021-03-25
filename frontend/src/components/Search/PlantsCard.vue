<template>
    <div class="plants">
        <div class="plantscard">
            <img :src="PlantsDefault" />
            <div class="plantsname">
                {{ this.plants.plant_name }}
            </div>
        </div>
    </div>
</template>

<script>
// import axios from "axios";

import PlantsDefault from '@/assets/img/plantsdefault.png';

export default {
  name: "PlantsCard",

  props: ['plants'],

  data: () => {
    return {
        PlantsDefault : PlantsDefault,
    }
  },
  components: {
    
  },
  methods: {
    
  },
  created(){
    
  },
};
</script>
<style>
    .plantscard {
        width: 50%;
        height: 200px;
        float: left;
        margin: 0 0 5% 0;
    }

    .plantscard img {
        float: left;
        width: 80%;
        height: 80%;
        margin: 0 0 5% 10%;
    }

    .plantscard .plantsname {
        width: 80%;
        height: 20%;
        padding: 0 0 0 10%;
        text-align: left;
        font-size: 14px;
        color: white;
        float: left;
    }
</style>
