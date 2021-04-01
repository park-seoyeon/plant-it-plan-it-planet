<template>
  <div class="detailscontent">
    <div class="myplant_diary">
      <div class="diary_title">
        <div class="title">
          식물 일지
        </div>
        <div class="write" @click="togglecreate()">
          + 일지쓰기
        </div>
      </div>

      <div v-if="iscreateopen" class="diary_create">
        <form @submit.prevent="creatediarys">
          <div class="title">
            <input class="titlename"
              id="diary_title"
              type="text"
              v-model="creatediary.creatediary_title"
              placeholder="일지 제목을 입력하세요."
            />
            <div class="cancel" @click="cancels">
              취소
            </div>
            <button class="create" type="submit">
              등록
            </button>
          </div>
          <input class="text"
            id="diary_contents"
            type="text"
            v-model="creatediary.creatediary_contents"
            placeholder="일지 내용을 입력하세요."
            style="white-space: pre-line"
          />
        </form>
      </div>
      <div class="diary_divisionbar"></div>
      <MyPlantsCard
        v-for="(myplants, idx) in diary"
        :key="idx"
        :myplants="myplants"
        @calldelete="deletediary"
      />
    </div>
  </div>
</template>

<script>
// import axios from 'axios';

// const SERVER_URL = process.env.VUE_APP_SERVER_URL;

import MyPlantsCard from '@/components/MyPlant/MyPlantsCard.vue';

export default {
  name: 'MyPlantDiary',

  props: ['diary'],

  data: () => {
    return {
      iscreateopen : false,
      creatediary: {
        creatediary_title: '',
        creatediary_contents: '',
      },
      creatediary_title : '',
      creatediary_contents : '',
    };
  },
  components: {
    MyPlantsCard,
  },
  methods: {
    togglecreate(){
      if(this.iscreateopen){
        this.iscreateopen = false;
      }
      else{
        this.iscreateopen = true;
      }
    },

    creatediarys() {
      // this.creatediary.creatediary_title = this.$refs.titlename.value;
      // this.creatediary.creatediary_contents = this.$refs.contents.value;

      this.$emit('callParent', this.creatediary );
      document.getElementById('diary_title').value = '';
      document.getElementById('diary_contents').value = '';
    },

    cancels(){
      document.getElementById('diary_title').value = '';
      document.getElementById('diary_contents').value = '';
    },

    deletediary(getdata){
      this.$emit('calldelete', getdata);
    },
  },

  created() {
    
  },
};
</script>

<style></style>
