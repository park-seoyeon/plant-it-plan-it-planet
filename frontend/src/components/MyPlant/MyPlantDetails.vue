<template>
  <div class="detailscontent">

    <div class="myplant_details">
      <div class="more">
        <div class="detail" @click="goDetail()">
          + 자세히 보기
        </div>
        <div v-if="!nicknameOn">
          <div class="changenickname" @click="togglenickname()">
            + 닉네임 변경하기
          </div>
        </div>
        <div v-else>
          <div class="changenickname" @click="togglenickname()">
            - 닉네임 변경취소
          </div>
        </div>
      </div>
      <div class="information">
        <div class="img">
          <img :src="plantImg" />
        </div>
        <div class="text">
          <div class="top">
            <div class="title">
              <div v-if="nicknameOn">
                <form @submit.prevent="changenickname">
                  <input class="nickname"
                    type="text"
                    v-model="nickname.name"
                    placeholder="별명을 새로 정해보세요!"
                  />
                  <button class="nicknameconfirm" type="submit">
                    변경완료
                  </button>
                </form>
              </div>
              <div v-else>
                {{ this.myplant_detail.plant_nickname }}
                <div class="level">
                  Lv.{{ this.myplant_detail.level }}
                </div>
              </div>
            </div>
            <div class="date">
              {{ this.myplant_detail.add_date }} ~ 
            </div>
          </div>
          <div class="level">
            <div class="title">
              <div id="title">
                다음레벨까지
              </div>
              <div id="datepoint">
                {{ this.myplant_detail.point }}p / {{ this.myplant_detail.max_point }}p
              </div>
            </div>
            <div class="progressbar">
              <div id="level-bar">
                <div id="level-progress"
                  v-bind:style="{ width: myplant_detail.level_pc + '%' }"
                ></div>
              </div>
            </div>
          </div>
          <div class="water">
            <div class="title">
              <div id="title">
                물주기
              </div>
              <div id="datepoint">
                D-{{ this.myplant_detail.watering_d_day }}
              </div>
            </div>
            <div class="progressbar">
              <div id="water-bar">
                <div id="water-progress"
                  v-bind:style="{ width: myplant_detail.watering_pc + '%' }"
                ></div>
              </div>
            </div>
          </div>
          <div class="soil">
            <div class="title">
              <div id="title">
                분갈이
              </div>
              <div id="datepoint">
                D-{{ this.myplant_detail.repotting_d_day }}
              </div>
            </div>
            <div class="progressbar">
              <div id="soil-bar">
                <div id="soil-progress"
                  v-bind:style="{ width: myplant_detail.repotting_pc + '%' }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';

import firebase from 'firebase';

// const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'MyPlantDetails',
  
  props: ['myplant_detail'],

  data: () => {
    return {
      isAdd: false,
      plantImg: null,
      nicknameOn: false,
      nickname: {
        name: '',
      },
    };
  },
  components: {

  },
  methods: {

    changenickname() {
      this.$emit('callnickname', this.nickname );
    },

    togglenickname(){
      if(this.nicknameOn){
        this.nicknameOn = false;
      }
      else{
        this.nickname.name = this.myplant_detail.plant_nickname;
        this.nicknameOn = true;
      }
    },

    downloadPlantImg() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `plant_images/${this.myplant_detail.plant_id}_1.jpg`
      );
      starsRef.getDownloadURL().then((url) => {
        this.plantImg = url;
      });
    },

    downloadMyPlantImg() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `my_plant_images/${localStorage.getItem('user_number')}_${
          this.myplant_detail.id
        }.jpg`
      );
      if (starsRef != null) {
        starsRef.getDownloadURL().then((url) => {
          this.plantImg = url;
        });
      }
    },

    goDetail() {
      this.$router
        .push({
          name: 'SearchDetail',
          params: { searchnumber: this.myplant_detail.plant_id },
        })
        .catch((error) => {
          if (error.name === 'NavigationDuplicated') {
            location.reload();
          }
        });
    }, 

  },

  beforeUpdate() {
    if (this.myplant_detail.is_add == 1) {
      this.isAdd = true;
      if (this.myplant_detail.is_upload == 1) {
        this.downloadMyPlantImg();
      } else {
        this.downloadPlantImg();
      }
    } else {
      this.isAdd = false;
      this.downloadPlantImg();
    }
  },
};
</script>

<style></style>
