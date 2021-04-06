<template>
  <div id="searchlist">
    <p class="plantscardtitle">식물 데이터</p>

    <PlantsCard
      v-for="(plants, idx) in (plant_list || '').slice(start_point, end_point)"
      :key="idx"
      :plants="plants"
    />
    <div v-if="isend" class="morewidth" style="padding-bottom: 30px">
      <div class="morebutton" style="border: 0px"></div>
    </div>
    <div v-else>
      <div class="morewidth">
        <button class="morebutton" @click="morelist">더보기</button>
      </div>
    </div>
  </div>
</template>

<script>
import PlantsCard from "@/components/Search/PlantsCard.vue";

export default {
  name: "SearchList",

  props: ["plant_list"],

  data: () => {
    return {
      start_point: 0,
      end_point: 20,
      isend: false,
    };
  },
  components: {
    PlantsCard,
  },
  methods: {
    resetlists() {
      this.end_point = 20;
      if (this.plant_list.length < 20) {
        this.isend = true;
      } else {
        this.isend = false;
      }
    },

    morelist() {
      this.end_point = this.end_point + 20;
      if (this.end_point >= this.plant_list.length) {
        this.isend = true;
      }
    },

    start() {
      if (this.plant_list.length < 20) {
        this.isend = true;
      }
    },
  },

  beforeUpdate() {
    this.start();
  },

  computed: {},
};
</script>
<style></style>
