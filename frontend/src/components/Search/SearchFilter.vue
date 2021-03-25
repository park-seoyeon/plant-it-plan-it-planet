<template>
  <div id="searchfilter">
    <FilterButton v-for="(buttons, idx) in filter_list" :key="idx" :buttons="buttons" @callParent="addfiltertolist"/>
  </div>
</template>

<script>
// import axios from "axios";

import FilterButton from '@/components/Search/FilterButton.vue';

export default {
  name: "SearchFilter",

  props: ['filter_list'],

  data: () => {
    return {
      idx : 0,
      selectedlist : [],
      last_selected : 0,
      result : [],
    }
  },
  components: {
    FilterButton,
  },
  methods: {
    addfiltertolist(getdata){
      if(this.selectedlist.includes(getdata)){
        const where =  this.selectedlist.indexOf(getdata);
        this.selectedlist.splice(where, 1);
        this.idx = this.idx - 1;
        this.last_selected = -1;
      }
      else{
        this.selectedlist[this.idx] = getdata;
        this.idx = this.idx + 1;
        this.last_selected = getdata;
      }

      this.result[0] = this.selectedlist;
      this.result[1] = this.last_selected;
      
      this.$emit('callParent', this.result);
    },
  },
  created(){
    
  },
};
</script>
