<template>
  <div class="plants">
    <div class="plantscard" @click="goDetail()">
      <img :src="plantImg" />
      <div class="plantsname">
        {{ this.plants.plant_name }}
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase';

import PlantsDefault from '@/assets/img/plantsdefault.png';

export default {
  name: 'PlantsCard',

  props: ['plants'],

  data: () => {
    return {
      PlantsDefault: PlantsDefault,

      plantImg: null,
    };
  },
  components: {},
  methods: {
    Download() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(`plant_images/${this.plants.id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg = url;
      });
    },
    goDetail() {
      document.documentElement.scrollTop = 0;
      this.$router
        .push({
          name: 'SearchDetail',
          params: { searchnumber: this.plants.id },
        })
        .catch((error) => {
          if (error.name === 'NavigationDuplicated') {
            location.reload();
          }
        });
    },
  },
  created() {
    this.Download();
  },
  beforeUpdate() {
    this.Download();
  },
};
</script>
<style></style>
