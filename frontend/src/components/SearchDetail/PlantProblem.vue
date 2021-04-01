<template>
  <div class="problem">
    <div v-if="isOpen" class="title-active" @click="openAccodian()">
      Q. {{ problem.title }}
      <img src="@/assets/img/arrows/up-arrow.png" />
    </div>
    <div v-else class="title" @click="openAccodian()">
      Q. {{ problem.title }}
      <img src="@/assets/img/arrows/down-arrow.png" />
    </div>
    <div v-if="isOpen" class="desc">{{ problem.detail }}</div>
    <div class="problem-division"></div>
  </div>
</template>

<script>
export default {
  name: 'PlantProblem',
  props: {
    problem: Object,
  },
  data: () => {
    return {
      isOpen: false,
    };
  },
  methods: {
    openAccodian() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style></style>
