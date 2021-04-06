<template>
  <div class="content">
    <div class="head">
      <img :src="Plantitimg" />
    </div>
    <div class="division"></div>
    <div class="myplant_functions">
      <div class="watering">
        <div class="button" @click="watering">
          <div class="img">
            <img :src="Wateringimg" />
          </div>
          <div class="text">물주기</div>
          <div class="point">+10p</div>
        </div>
      </div>
      <div class="repotting">
        <div class="button" @click="repotting">
          <div class="img">
            <img :src="Repottingimg" />
          </div>
          <div class="text">분갈이</div>
          <div class="point">+100p</div>
        </div>
      </div>
      <div class="chatting" @click="chatting">
        <div class="button">
          <div class="img">
            <img :src="Chattingimg" />
          </div>
          <div class="text">말걸기</div>
        </div>
      </div>
    </div>
    <div class="myplant_divisionbar"></div>
    <div class="myplant_details" id="myplant_details_content">
      <MyPlantDetails
        :myplant_detail="myplant_detail"
        @callnickname="changenickname"
      />
    </div>
    <div class="myplant_divisionbar"></div>
    <div class="myplant_diarydetails">
      <MyPlantDiary
        :diary="diary"
        @callParent="getdiarycreate"
        @calldelete="deletediary"
        @callmodify="modifydiary"
      />
    </div>
    <div
      class="morewidth"
      style="width: 100%; height: 50px; float: left; padding-bottom: 30px"
    >
      <div class="morebutton" style="border: 0px"></div>
      <div class="back">
        <div class="back-icon" @click="goBack()"><img :src="Backimg" /></div>
      </div>
      <div style="padding-bottom: 75px"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import Plantitimg from '@/assets/img/PLANTIT.png';
import Wateringimg from '@/assets/img/myplant-watering.png';
import Repottingimg from '@/assets/img/myplant-repotting.png';
import Chattingimg from '@/assets/img/myplant-chatting.png';
import backicon from '@/assets/img/arrows/left-arrow.png';

import MyPlantDetails from '@/components/MyPlant/MyPlantDetails.vue';
import MyPlantDiary from '@/components/MyPlant/MyPlantDiary.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'MyPlantDetail',

  data: () => {
    return {
      Plantitimg: Plantitimg,
      Wateringimg: Wateringimg,
      Repottingimg: Repottingimg,
      Chattingimg: Chattingimg,
      Backimg: backicon,
      myplant_detail: '',
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
          this.$router.push({ name: 'Home' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        });

      await axios
        .post(`${SERVER_URL}/diary/`, {
          myplant_id: this.myplant_detail.id,
        })

        .then((response) => {
          this.diary = response.data.diary_list;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },

    watering() {
      if (this.myplant_detail.watering_d_day != 0) {
        alert('지금 물을 주면 배가 터져버릴 거에요..');
      } else {
        axios
          .put(`${SERVER_URL}/myplant/watering/`, {
            user_number: localStorage.getItem('user_number'),
            myplant_id: this.myplant_detail.id,
          })

          .then((response) => {
            let msg = '물주기에 실패하였습니다.';
            if (response.data.message === 'success') {
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

    repotting() {
      if (this.myplant_detail.repotting_d_day != 0) {
        alert('지금 분갈이해버리면 집을 잃어서 슬플 거에요..');
      } else {
        axios
          .put(`${SERVER_URL}/myplant/repotting/`, {
            user_number: localStorage.getItem('user_number'),
            myplant_id: this.myplant_detail.id,
          })

          .then((response) => {
            let msg = '분갈이에 실패하였습니다.';
            if (response.data.message === 'success') {
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

    chatting() {
      axios
        .post(`${SERVER_URL}/myplant/chat/`, {
          user_number: localStorage.getItem('user_number'),
          id: this.myplant_detail.id,
        })

        .then((response) => {
          let msg = '말걸기에 실패하였습니다.';
          if (response.data.message === 'success') {
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

    changenickname(getdata) {
      axios
        .put(`${SERVER_URL}/myplant/mod/nickname/`, {
          user_number: localStorage.getItem('user_number'),
          myplant_id: this.myplant_detail.id,
          plant_nickname: getdata.name,
        })

        .then((response) => {
          let msg = '별명수정에 실패하였습니다.';
          if (response.data.message === 'success') {
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

    getdiarycreate(getdata) {
      axios
        .post(`${SERVER_URL}/diary/add/`, {
          user_number: localStorage.getItem('user_number'),
          myplant_id: this.myplant_detail.id,
          title: getdata.creatediary_title,
          content: getdata.creatediary_contents,
        })

        .then((response) => {
          let msg = '등록에 실패하였습니다.';
          if (response.data.message === 'success') {
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

    deletediary(getdata) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios
          .delete(`${SERVER_URL}/diary/del/`, {
            data: {
              diary_id: getdata,
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
      } else {
        location.reload();
      }
    },

    modifydiary(getdata) {
      if (confirm('정말 수정하시겠습니까?')) {
        axios
          .put(`${SERVER_URL}/diary/mod/`, {
            diary_id: getdata.modifydiary_id,
            title: getdata.modifydiary_title,
            content: getdata.modifydiary_contents,
          })

          .then((response) => {
            let msg = '수정에 실패하였습니다.';
            if (response.data.message === 'success') {
              location.reload();
            } else {
              alert(msg);
              location.reload();
            }
          })
          .catch(() => {
            alert('서버와 통신할 수 없습니다.');
          });
      } else {
        location.reload();
      }
    },
    goBack() {
      history.back();
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
