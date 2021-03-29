<template>
  <div class="problem">
    <div v-if="isOpen" class="title-active" @click="openAccodian()">
      Q. {{ problem.title }}
      <i class="fas fa-angle-down"></i>
    </div>
    <div v-else class="title" @click="openAccodian()">
      Q. {{ problem.title }}
      <i class="fas fa-angle-up"></i>
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
