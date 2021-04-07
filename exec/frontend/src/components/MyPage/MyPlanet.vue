<template>
  <div class="myplanet">
    <img id="planet-image" :src="getEarthImg()" />
  </div>
</template>

<script>
export default {
  name: 'MyPlanet',
  data: () => {
    return {
      mylevel: 0,
    };
  },
  props: ['level'],
  methods: {
    getEarthImg() {
      if (this.level == 0) {
        return require(`@/assets/img/planet/planet_0.png`);
      } else if (this.level == 1) {
        return require(`@/assets/img/planet/planet_1.png`);
      } else if (this.level == 2) {
        return require(`@/assets/img/planet/planet_2.png`);
      } else if (this.level == 3) {
        return require(`@/assets/img/planet/planet_3.png`);
      } else if (this.level == 4) {
        return require(`@/assets/img/planet/planet_4.png`);
      } else if (this.level == 5) {
        return require(`@/assets/img/planet/planet_5.png`);
      }
    },
  },
};
</script>
