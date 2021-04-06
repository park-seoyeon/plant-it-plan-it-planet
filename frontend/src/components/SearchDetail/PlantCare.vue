<template>
  <div class="care">
    <div class="name">어떻게 키우나요?</div>
    <img src="@/assets/img/care_plant/light.png" />
    <div class="title">{{ care.sunlight_title }}</div>
    <div class="desc" v-html="handleNewLine(care.sunlight_desc)"></div>
    <img src="@/assets/img/care_plant/temperature.png" />
    <div class="title">{{ care.temperature_title }}</div>
    <div class="desc" v-html="handleNewLine(care.temperature_desc)"></div>
    <img src="@/assets/img/care_plant/humidity.png" />
    <div class="title">{{ care.humidity_title }}</div>
    <div class="desc" v-html="handleNewLine(care.humidity_desc)"></div>
    <img src="@/assets/img/care_plant/watering.png" />
    <div class="title">{{ care.water_title }}</div>
    <div class="desc" v-html="handleNewLine(care.water_desc)"></div>
    <img src="@/assets/img/care_plant/soil.png" />
    <div class="title">{{ care.soil_title }}</div>
    <div class="desc" v-html="handleNewLine(care.soil_desc)"></div>
    <img src="@/assets/img/care_plant/repotting.png" />
    <div class="title">{{ care.repotting_title }}</div>
    <div class="desc" v-html="handleNewLine(care.repotting_desc)"></div>
    <div id="dashed-division" style="width: 350px; margin: 4% auto"></div>
  </div>
</template>

<script>
export default {
  name: 'PlantCare',
  props: {
    care: Object,
  },
  methods: {
    // \n </br>로 바꾸기
    handleNewLine(str) {
      return String(str).replace(/(?:\r\n|\r|\n)/g, '</br>');
    },
  },
};
</script>

<style></style>
