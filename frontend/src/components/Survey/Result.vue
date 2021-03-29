<template>
  <div>
    <div id="resulticons">
      <img :src="planticon" />
      <img :src="planicon" />
      <img :src="planeticon" style="margin-right: 0" />
    </div>

    <div id="resultbar"></div>
    <div class="result-detail">
      <div id="expression">
        {{ result.mbti_expression }}
      </div>
      <div id="division-bar"></div>
      <div id="result-img"><img :src="getMbtiImgPath()" /></div>
      <div id="division-bar"></div>
      <div id="recommend">
        <div id="title">당신에게 어울리는 식물</div>
        <div id="desc" @click="plantDetail(result.recommanded_plant_1_id)">
          <img :src="Download_1()" />
          <div id="text">
            <div id="name">
              {{ result.recommanded_plant_1_name }}
            </div>
            <div id="division"></div>
            <div id="intro">
              {{ result.recommanded_plant_1_intro }}
            </div>
          </div>
        </div>
        <div id="desc" @click="plantDetail(result.recommanded_plant_2_id)">
          <img :src="Download_2()" />
          <div id="text">
            <div id="name">
              {{ result.recommanded_plant_2_name }}
            </div>
            <div id="division"></div>
            <div id="intro">
              {{ result.recommanded_plant_2_intro }}
            </div>
          </div>
        </div>
        <div id="desc" @click="plantDetail(result.recommanded_plant_3_id)">
          <img :src="Download_3()" />
          <div id="text">
            <div id="name">
              {{ result.recommanded_plant_3_name }}
            </div>
            <div id="division"></div>
            <div id="intro">
              {{ result.recommanded_plant_3_intro }}
            </div>
          </div>
        </div>
      </div>
      <div id="division-bar"></div>
      <div id="friend">
        <div id="partner">
          <img :src="getBestImgPath()" />
          <div id="cont">
            <div id="title">최고의 궁합</div>
            <div id="division"></div>
            <div id="mbti">
              {{ result.best_expression }}
            </div>
          </div>
        </div>
        <div id="partner">
          <img :src="getWorstImgPath()" />
          <div id="cont">
            <div id="title">최악의 궁합</div>
            <div id="division"></div>
            <div id="mbti">
              {{ result.worst_expression }}
            </div>
          </div>
        </div>
      </div>
      <div id="start-tool"><span id="start">플랜잇 시작하기</span></div>
    </div>
  </div>
</template>

<script>
import planticon from '@/assets/img/plantit_icon.png';
import planicon from '@/assets/img/planit_icon.png';
import planeticon from '@/assets/img/planet_icon.png';
import firebase from 'firebase';

export default {
  name: 'Result',
  data: () => {
    return {
      planticon: planticon,
      planicon: planicon,
      planeticon: planeticon,
      plantImg_1: null,
      plantImg_2: null,
      plantImg_3: null,
    };
  },

  props: {
    result: Object,
  },

  methods: {
    getMbtiImgPath() {
      return require(`@/assets/img/mbti/${this.result.mbti_name}.png`);
    },
    getBestImgPath() {
      return require(`@/assets/img/mbti/${this.result.best_partner}.png`);
    },
    getWorstImgPath() {
      return require(`@/assets/img/mbti/${this.result.worst_partner}.png`);
    },
    Download_1() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `plant_images/${this.result.recommanded_plant_1_id}_1.jpg`
      );
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_1 = url;
      });
      return this.plantImg_1;
    },
    Download_2() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `plant_images/${this.result.recommanded_plant_2_id}_1.jpg`
      );
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_2 = url;
      });
      return this.plantImg_2;
    },
    Download_3() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `plant_images/${this.result.recommanded_plant_3_id}_1.jpg`
      );
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_3 = url;
      });
      return this.plantImg_3;
    },
    plantDetail(id) {
      this.$router
        .push({ name: 'SearchDetail', params: { searchnumber: id } })
        .catch((error) => {
          if (error.name === 'NavigationDuplicated') {
            location.reload();
          }
        });
    },
  },
};
</script>

<style></style>
