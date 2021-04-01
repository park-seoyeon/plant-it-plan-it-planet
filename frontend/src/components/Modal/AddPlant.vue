<template>
  <div class="modal">
    <div class="modal-head">
      <div id="close" @click="$emit('close')">
        <strong>X</strong>
      </div>
    </div>
    <div class="modal-body">
      <div id="upload-img">
        <!-- <img :src="plantImg" /> -->
        <div id="upload-btn">
          <form>
            <input
              type="file"
              id="upload"
              @change="selectedImg"
              style="display: none"
            />
          </form>
          <img id="upload-img" v-if="isImg" :src="isImg" @click="imgClick" />
          <img id="default-img" v-else :src="addImg" @click="imgClick" />
        </div>
      </div>
      <div id="plant-name">식물이름: {{ plant_name }}</div>
      <div id="plant-nickname">
        별명:
        <input
          id="plant-nickname-input"
          type="text"
          placeholder="별명을 입력해주세요"
          v-model="nickname"
        />
      </div>
      <div id="plant-date">키우기 시작한 날: {{ today_date }}</div>
    </div>
    <div class="modal-footer">
      <div id="add" @click="addPlant()">등록하기</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import firebase from 'firebase';
import addImg from '@/assets/img/add.png';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'AddPlant',
  data: () => {
    return {
      addImg: addImg,
      today_date: new Date().toJSON().slice(0, 10).replace(/-/g, '.'),
      nickname: '',
      isImg: '',
      isFile: '',
    };
  },
  props: ['myplant_id', 'plant_name', 'plant_img'],
  methods: {
    uploagImg() {},
    selectedImg(event) {
      // console.log(event);
      this.isFile = event.target.files[0];
      this.isImg = URL.createObjectURL(this.isFile);
    },
    imgClick() {
      const uploadBtn = document.querySelector('#upload');
      uploadBtn.click();
    },
    addPlant() {
      var is_upload = 0;
      if (this.isImg != '') {
        is_upload = 1;
        firebase
          .storage()
          .ref(
            `my_plant_images/${localStorage.getItem('user_number')}_${
              this.myplant_id
            }.jpg`
          )
          .put(this.isFile);
      }
      axios
        .put(`${SERVER_URL}/myplant/add/`, {
          user_number: localStorage.getItem('user_number'),
          myplant_id: this.myplant_id,
          plant_name: this.plant_name,
          plant_nickname: this.nickname,
          is_upload: is_upload,
        })
        .then(({ data }) => {
          let msg = '등록에 실패하였습니다.';
          if (data.message === 'success') {
            this.$emit('close');
            location.reload();
          } else {
            alert(msg);
            location.reload();
          }
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },
  },
  created() {
    // console.log(this.myplant_id);
  },
};
</script>

<style></style>
