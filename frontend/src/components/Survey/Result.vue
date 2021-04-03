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
      <div id="flower-description">{{ result.flower_description }}</div>
      <div id="division-bar"></div>
      <div id="recommend">
        <div id="title">이런 당신에게 어울리는 식물</div>
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
      <div class="restart">
        <span class="restart-btn" @click="restartSurvey()"
          >나와 맞는 식물 다시 찾기</span
        >
      </div>
      <div id="division-bar"></div>
      <div id="start-tool">
        <span id="start" @click="sendLink()">
          <img
            src="//developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_small.png"
            width="12px"
          />
          카카오로 공유하기</span
        ><span id="start" @click="goMain()" style="margin-left: 2%"
          >플랜잇 시작하기</span
        >
      </div>
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
      mbtiPlantImg: null,
    };
  },

  props: {
    result: Object,
  },

  methods: {
    Download_mbti_plants_img() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images

      var starsRef = storageRef.child(
        `mbti_plant_images/${this.result.mbti_name}.png`
      );
      starsRef.getDownloadURL().then((url) => {
        this.mbtiPlantImg = url;
      });
      return this.mbtiPlantImg;
    },

    restartSurvey() {
      this.$router.push({ name: 'SurveyProgress' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },

    sendLink() {
      // 카카오톡 공유하기
      this.Download_mbti_plants_img();
      setTimeout(() => {
        window.Kakao.Link.sendDefault({
          objectType: 'feed',
          content: {
            title: this.result.mbti_expression,
            description: this.result.flower_description,
            imageUrl: this.mbtiPlantImg,
            link: {
              mobileWebUrl: 'https://developers.kakao.com',
              androidExecParams: 'PlantIt',
            },
          },
          buttons: [
            {
              title: '웹으로 이동',
              link: {
                mobileWebUrl: 'https://developers.kakao.com',
              },
            },
          ],
        });
      }, 1000);
    },
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
    goMain() {
      this.$router.push({ name: 'Main' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
  },
};
</script>

<style></style>
