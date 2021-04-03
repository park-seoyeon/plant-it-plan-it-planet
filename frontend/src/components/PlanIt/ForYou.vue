<template>
  <div class="main_component_foryou">
    <div class="main_component_foryou_title">FOR YOU</div>
    <div class="main_component_foryou_sub">
      당신의 성향에 맞는 식물을 추천합니다
    </div>
    <div class="main_component_foryou_content">
      <div v-if="isSurvey">
        <div
          class="main_component_foryou_recommands"
          @click="plantDetail(recommend_list.recommanded_plant_1_id)"
        >
          <img :src="plantImg_1" />
          <div class="main_component_foryou_name">
            {{ this.recommend_list["recommanded_plant_1_name"] }}
          </div>
        </div>
        <div
          class="main_component_foryou_recommands"
          @click="plantDetail(recommend_list.recommanded_plant_2_id)"
        >
          <img :src="plantImg_2" />
          <div class="main_component_foryou_name">
            {{ this.recommend_list["recommanded_plant_2_name"] }}
          </div>
        </div>
        <div
          class="main_component_foryou_recommands"
          @click="plantDetail(recommend_list.recommanded_plant_3_id)"
        >
          <img :src="plantImg_3" />
          <div class="main_component_foryou_name">
            {{ this.recommend_list["recommanded_plant_3_name"] }}
          </div>
        </div>
      </div>
      <div v-else>MBTI 설문조사를 해주세여 니마</div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  name: "MainForyou",

  props: ["recommend_list"],

  data: () => {
    return {
      plantImg_1: null,
      plantImg_2: null,
      plantImg_3: null,
      recommend_plant_1_id_check: "",
      isSurvey: false,
    };
  },
  components: {},

  methods: {
    start() {
      this.recommend_plant_1_id_check = this.recommend_list[
        "recommanded_plant_1_id"
      ];
    },

    Download_1() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var input_plant_id = this.recommend_list["recommanded_plant_1_id"];
      var starsRef = storageRef.child(`plant_images/${input_plant_id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_1 = url;
      });
    },

    Download_2() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var input_plant_id = this.recommend_list["recommanded_plant_2_id"];
      var starsRef = storageRef.child(`plant_images/${input_plant_id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_2 = url;
      });
    },

    Download_3() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var input_plant_id = this.recommend_list["recommanded_plant_3_id"];
      var starsRef = storageRef.child(`plant_images/${input_plant_id}_1.jpg`);
      starsRef.getDownloadURL().then((url) => {
        this.plantImg_3 = url;
      });
    },

    plantDetail(id) {
      this.$router
        .push({ name: "SearchDetail", params: { searchnumber: id } })
        .catch((error) => {
          if (error.name === "NavigationDuplicated") {
            location.reload();
          }
        });
    },
  },

  // Mount 이전에, localStorage값이 1인 경우 ( 로그인 안해서 storage에 정보가 들어가지 않은 경우 ) Intro로 돌아가라.
  created() {
    const token = localStorage.getItem("jwt");
    if (token == null) {
      alert("로그인 하고 이용해주세요.");
      this.$router.push({ name: "Home" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    } else {
      this.start();
      if (localStorage.getItem("is_survey") == 1) {
        this.isSurvey = true;
      }
    }
  },

  beforeUpdate() {
    this.Download_1();
    this.Download_2();
    this.Download_3();
  },
};
</script>