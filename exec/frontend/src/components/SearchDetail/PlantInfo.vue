<template>
  <div>
    <div class="detail-img">
      <img :src="plantImg" />
    </div>
    <div class="plant-name">{{ info.plant_name }}</div>
    <div class="plant-intro">{{ info.plant_intro }}</div>
    <div class="info">
      <div id="dashed-division"></div>
      <div class="info-icon">
        <img src="@/assets/img/info_icon/watering-can.png" />
      </div>
      <div class="info-cont">
        <div id="title">{{ info.summary_water_title }}</div>
        <div id="desc">{{ info.summary_water_desc }}</div>
      </div>
      <div id="dashed-division"></div>
      <div class="info-icon">
        <img src="@/assets/img/info_icon/sun.png" />
      </div>
      <div class="info-cont">
        <div id="title">{{ info.summary_sunlight_title }}</div>
        <div id="desc">{{ info.summary_sunlight_desc }}</div>
      </div>
      <div id="dashed-division"></div>
      <div class="info-icon">
        <img src="@/assets/img/info_icon/drop.png" />
      </div>
      <div class="info-cont">
        <div id="title">{{ info.summary_humidity_title }}</div>
        <div id="desc">{{ info.summary_humidity_desc }}</div>
      </div>
      <div id="dashed-division"></div>
      <div class="info-icon">
        <img src="@/assets/img/info_icon/pen.png" />
      </div>
      <div class="info-cont">
        <div id="title">{{ info.summary_scientific_name_title }}</div>
        <div id="desc">{{ info.summary_scientific_name_desc }}</div>
      </div>
      <div id="dashed-division"></div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase';

export default {
  name: 'PlantInfo',
  data: () => {
    return {
      plantImg: null,
    };
  },
  props: {
    info: Object,
  },
  methods: {
    Download() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(`plant_images/${this.info.id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg = url;
      });
    },
  },
  beforeUpdate() {
    this.Download();
  },
};
</script>

<style></style>
