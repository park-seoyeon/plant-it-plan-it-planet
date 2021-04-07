<template>
  <div class="main_component_myplant">
    <div class="main_component_myplant_title">MY PLANT</div>
    <div class="main_component_myplant_sub">식물들을 관리해주세요</div>
    <div v-if="myplant_list != undefined">
      <div>
        <flickity
          v-if="Object.keys(myplant_list).length > 0"
          ref="flickity"
          class="carousel"
          :options="flickityOptions"
        >
          <MyplantsCard
            class="carousel-cell"
            v-for="(myplants, idx) in myplant_list"
            :key="idx"
            :myplants="myplants"
          />
        </flickity>
      </div>
      <div v-if="myplant_list.length == 0">
        <div class="gotosearch" @click="gosearch()">
          나만의 식물 추가하러 가기
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyplantsCard from "@/components/PlanIt/MyplantsCard.vue";

import Flickity from "vue-flickity";

export default {
  name: "MainMyplant",

  props: ["myplant_list"],

  data: () => {
    return {
      where: 1,
      flickityOptions: {
        prevNextButtons: false,
        pageDots: false,
        wrapAround: true,
      },
    };
  },
  components: {
    MyplantsCard,
    Flickity,
  },

  methods: {
    gosearch() {
      this.$router.push({ name: "Search" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
  },

  // Mount 이전에, localStorage값이 1인 경우 ( 로그인 안해서 storage에 정보가 들어가지 않은 경우 ) Intro로 돌아가라.
  created() {
    const token = localStorage.getItem("jwt");
    if (token == null) {
      this.$swal.fire({
        icon: "error",
        title: "로그인 하고 이용해주세요.",
      });
      this.$router.push({ name: "Home" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    }
  },
};
</script>