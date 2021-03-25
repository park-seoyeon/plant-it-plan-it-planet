<template>
    <div class="filterbuttons">
        <div @click="selectfilter">
            {{ this.buttons.property_name }}
        </div>
    </div>
</template>

<script>
// import axios from "axios";

import PlantsDefault from '@/assets/img/plantsdefault.png';

export default {
  name: "FilterButton",

  props: ['buttons'],

  data: () => {
    return {
        PlantsDefault : PlantsDefault,
    }
  },
  components: {
    
  },
  methods: {
    selectfilter(){
        this.$emit('callParent', this.buttons.id);
    }
  },
  created(){
    
  },
};
</script>
<style>
    .filterbuttons {
        width: 50%;
        height: 30px;
        border: 2px solid white;
        color: white;
    }
</style>
