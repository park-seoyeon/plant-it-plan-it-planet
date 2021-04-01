<template>
  <div class="content">
    <div class="head">
      <img :src="Plantitimg" />
    </div>
    <div class="division"></div>
    <div class="myplant_functions">
        icons
    </div>
    <div class="myplant_divisionbar"></div>
    <div class="myplant_details" id="myplant_details_content">
        <MyPlantDetails :myplant_detail="myplant_detail" />
    </div>
    <div class="myplant_divisionbar"></div>
    <div class="myplant_diarydetails">
        <MyPlantDiary :diary="diary" 
          @callParent="getdiarycreate"
          @calldelete="deletediary"
        />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import Plantitimg from '@/assets/img/PLANTIT.png';

import MyPlantDetails from '@/components/MyPlant/MyPlantDetails.vue';
import MyPlantDiary from '@/components/MyPlant/MyPlantDiary.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'MyPlantDetail',

  data: () => {
    return {
        Plantitimg : Plantitimg,
        myplant_detail : '',
        diary: '',
    };
  },
  components: {
    MyPlantDetails,
    MyPlantDiary,
  },
  methods: {
    async getDetail() {
      await axios
        .get(`${SERVER_URL}/myplant/detail/${this.$route.params.detailnumber}`)
        .then((response) => {
          this.myplant_detail = response.data.result;
        })
        .catch(() => {
          alert('결과를 가져오는 중에 오류가 발생했습니다');
          // this.$router.push({ name: 'Home' }).catch((error) => {
          //   if (error.name === 'NavigationDuplicated') {
          //     location.reload();
          //   }
          // });
        });

      await axios
        .post(`${SERVER_URL}/diary/`, {
            myplant_id: 2,
         })

        .then((response) => {
          this.diary = response.data.diary_list;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

    },

    getdiarycreate(getdata){
      axios
        .post(`${SERVER_URL}/diary/add/`, {
          user_number : localStorage.getItem('user_number'),
          myplant_id : 2,
          title : getdata.creatediary_title,
          content : getdata.creatediary_contents,
        })

        .then((response) => {
          console.log(response);
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },

    deletediary(getdata){
      alert(getdata);
      axios
        .delete(`${SERVER_URL}/diary/del/`, {
          diary_id : getdata,
        })

        .then((response) => {
          console.log(response);
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },

  },

  // created 할 때 jwt가 없다면 home으로 보내기
  created() {
    const token = localStorage.getItem('jwt');
    if (token == null) {
      alert('로그인 하고 이용해주세요.');
      this.$router.push({ name: 'Home' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    } else {
      this.getDetail();
    }
  },
};
</script>

<style></style>
