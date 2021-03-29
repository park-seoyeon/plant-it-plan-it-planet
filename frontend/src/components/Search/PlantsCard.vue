<template>
    <div class="plants">
        <div class="plantscard">
            <img :src="plantImg" />
            <div class="plantsname">
                {{ this.plants.plant_name }}
            </div>
        </div>
    </div>
</template>

<script>
import firebase from "firebase";

import PlantsDefault from '@/assets/img/plantsdefault.png';

export default {
  name: "PlantsCard",

  props: ['plants'],

  data: () => {
    return {
        PlantsDefault : PlantsDefault,

        plantImg: null,
    }
  },
  components: {
    
  },
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
  },
  created(){
      this.Download();
  },
  beforeUpdate(){
      this.Download();
  },
};
</script>
<style>
    .plantscard {
        width: 50%;
        height: 200px;
        float: left;
        margin: 0 0 5% 0;
    }

    .plantscard img {
        float: left;
        width: 80%;
        height: 80%;
        margin: 0 0 5% 10%;
    }

    .plantscard .plantsname {
        width: 80%;
        height: 20%;
        padding: 0 0 0 10%;
        text-align: left;
        font-size: 14px;
        color: white;
        float: left;
    }
</style>
