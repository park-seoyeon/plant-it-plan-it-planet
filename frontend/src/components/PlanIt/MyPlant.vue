<template>
  <div class="main_component_myplant">
      <div class="main_component_myplant_title">
          MY PLANT
      </div>
      <div class="main_component_myplant_sub">
          식물들을 관리해주세요
      </div>

      <carousel-3d>
        <slide class="myplant_slides" :index="0">
          Slide 1 Content
        </slide>
        <slide class="myplant_slides" :index="1">
          Slide 1 Content
        </slide>
        <slide class="myplant_slides" :index="2">
          Slide 1 Content
        </slide>
      </carousel-3d>

      <!-- <carousel-3d>
          <MyplantsCard
          v-for="(myplants, idx) in myplant_list"
          :key="idx"
          :myplants="myplants"
        />
      </carousel-3d> -->

    <MyplantsCard
      v-for="(myplants, idx) in myplant_list"
      :key="idx"
      :myplants="myplants"
    />  


  </div>
</template>

<script>
// import axios from "axios";

import MyplantsCard from '@/components/PlanIt/MyplantsCard.vue';

import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: "MainMyplant",

  props: ['myplant_list'],

  data: () => {
    return {
      where : 1,
      slides: 5,
    }
  },
  components: {
    MyplantsCard,
    Carousel3d,
    Slide,
  },
  methods: {
    
  },

  // Mount 이전에, localStorage값이 1인 경우 ( 로그인 안해서 storage에 정보가 들어가지 않은 경우 ) Intro로 돌아가라.
  created() {
    const token = localStorage.getItem('jwt');
    if (token == null) {
      alert('로그인 하고 이용해주세요.');
      this.$router.push({ name: 'Home' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    }
  },
};
</script>
