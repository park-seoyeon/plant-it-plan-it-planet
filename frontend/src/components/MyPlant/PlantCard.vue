<template>
  <div class="plant-card">
    <div class="delete-plant">
      <div class="delete" @click="deletePlant()">ㅡ</div>
    </div>
    <div v-if="isAdd" class="myplant">
      <img :src="myPlantImg" />
      <div class="cont">
        <div id="day">함께한지 {{ myplant.add_day_count }}일</div>
        <div id="name">
          <div id="nickname">{{ myplant.plant_nickname }}</div>
          <span id="level">Lv.{{ myplant.level }}</span>
        </div>
        <div id="water-title">물주기</div>
        <div id="water-bar">
          <div
            id="water-progress"
            v-bind:style="{ width: myplant.watering_pc + '%' }"
          ></div>
        </div>
        <div id="repotting-title">분갈이</div>
        <div id="repotting-bar">
          <div
            id="repotting-progress"
            v-bind:style="{ width: myplant.repotting_pc + '%' }"
          ></div>
        </div>
      </div>
    </div>
    <div v-else class="wantplant">
      <img :src="plantImg" />
      <div class="cont">
        <div id="name">{{ myplant.plant_name }}</div>
        <div id="btn">
          <a v-bind:href="myplant.buy_link" target="_blank" id="buyit"
            >BUY IT</a
          >
          <div id="plantit" @click="addPlant()">PLANT IT</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import firebase from 'firebase';
import myPlantImg from '@/assets/img/default-img.png';
import AddPlant from '@/components/Modal/AddPlant.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'PlantCard',
  props: {
    myplant: Object,
  },
  data: () => {
    return {
      isAdd: false,
      plantImg: null,
      myPlantImg: myPlantImg,
    };
  },
  methods: {
    deletePlant() {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios
          .delete(`${SERVER_URL}/myplant/del/`, {
            data: {
              myplant_id: this.myplant.id,
            },
          })
          .then(({ data }) => {
            let msg = '삭제에 실패하였습니다.';
            if (data.message === 'success') {
              location.reload();
            } else {
              alert(msg);
              location.reload();
            }
          })
          .catch(() => {
            alert('서버와 통신할 수 없습니다.');
          });
      }
    },

    downloadPlantImg() {
      var storage = firebase.storage();
      var storageRef = storage.ref();
      // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      var starsRef = storageRef.child(
        `plant_images/${this.myplant.plant_id}_1.jpg`
      );
      starsRef.getDownloadURL().then((url) => {
        this.plantImg = url;
      });
    },

    downloadMyPlantImg() {
      // var storage = firebase.storage();
      // var storageRef = storage.ref();
      // // child안에 `불러오고 싶은 이미지 디렉토리/이미지 이름.jpg`로 불러오기
      // // 폴더명만 잘 설정해주세요. test -> plant_images, my_plant_images
      // var starsRef = storageRef.child(
      //   `my_plant_images/${this.myplant.user_number}_${this.myplant.id}.jpg`
      // );
      // if (starsRef != null) {
      //   starsRef.getDownloadURL().then((url) => {
      //     this.myPlantImg = url;
      //   });
      // }
    },
    addPlant() {
      this.$modal.show(
        AddPlant,
        {
          modal: this.$modal,
          myplant_id: this.myplant.id,
          plant_name: this.myplant.plant_name,
        },
        {
          name: 'dynamic-modal',
          width: '300px',
          height: '243px',
          draggable: false,
        },
        {
          closed: this.setLikes,
        }
      );
    },
  },
  created() {
    if (this.myplant.is_add == 1) {
      this.isAdd = true;
      this.downloadMyPlantImg();
    } else {
      this.isAdd = false;
      this.downloadPlantImg();
    }
  },
};
</script>

<style></style>
