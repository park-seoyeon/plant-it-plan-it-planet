<template>
  <div class="myplants">


    <div class="myplantscard">
      <img :src="plantImg" />
      <div class="plantsname" id="myplants_name">
        {{ this.myplants.plant_nickname }}
      </div>
      <div class="plantsname_detail">
          관리하러 가기
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase';

import PlantsDefault from '@/assets/img/plantsdefault.png';

// import { Slide } from 'vue-carousel-3d';

export default {
  name: 'MyplantsCard',

  props: ['myplants'],

  data: () => {
    return {
      PlantsDefault: PlantsDefault,

      plantImg: null,
    };
  },
  components: {
    // Slide,
  },
  methods: {
    Download() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(`plant_images/${this.myplants.plant_id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg = url;
      });
    },
    // goDetail() {
    //   this.$router
    //     .push({
    //       name: 'SearchDetail',
    //       params: { searchnumber: this.plants.id },
    //     })
    //     .catch((error) => {
    //       if (error.name === 'NavigationDuplicated') {
    //         location.reload();
    //       }
    //     });
    // },
  },

  created(){
      this.Download();
  },
};
</script>
<style></style>
