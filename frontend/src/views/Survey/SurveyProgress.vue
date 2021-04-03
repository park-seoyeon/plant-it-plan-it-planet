<template>
  <div class="content">
    <div id="icons">
      <img :src="planticon" />
      <img :src="planicon" />
      <img :src="planeticon" style="margin-right: 0" />
    </div>

    <!-- 상태바 표시 -->
    <div id="progressbar">
      <div id="mybar"></div>
    </div>

    <div v-if="this.question_list[this.where] !== undefined">
      <div id="numbering">&lt; {{ where + 1 }} &gt;</div>
      <div
        id="ask"
        v-html="handleNewLine(this.question_list[this.where].question)"
      ></div>

      <div class="survey-buttons" @click="select(1)">
        {{ this.question_list[this.where].answer_01 }}
      </div>
      <div class="survey-buttons" @click="select(2)">
        {{ this.question_list[this.where].answer_02 }}
      </div>
      <div class="survey-buttons" @click="select(3)">
        {{ this.question_list[this.where].answer_03 }}
      </div>
      <div class="survey-buttons" @click="select(4)">
        {{ this.question_list[this.where].answer_04 }}
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

import planticon from '@/assets/img/plantit_icon.png';
import planicon from '@/assets/img/planit_icon.png';
import planeticon from '@/assets/img/planet_icon.png';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'SurveyProgress',
  data: () => {
    return {
      planticon: planticon,
      planicon: planicon,
      planeticon: planeticon,

      // 질문의 index값 -> 시작은 0 -> 첫 번째 질문... -> selectAnswer() 함수를 통해서 값을 증가시켜 다음 질문 받아오기
      where: 0,

      // 들어오는 전체 리스트
      question_list: [],
      // 사용자가 고른 답변 리스트
      answer_list: [],

      // progress 수치
      width: 0,
    };
  },

  methods: {
    startSurvey() {
      axios
        .get(`${SERVER_URL}/survey/list/`)
        .then((response) => {
          this.question_list = response.data.question_list;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },

    // 설문이 끝나면 post로 값을 보내줌
    endSurvey() {
      axios
        .post(`${SERVER_URL}/survey/result/`, { answer_list: this.answer_list })
        .then(({ data }) => {
          let msg = '설문에 실패하였습니다.';
          if (data.message === 'success') {
            this.$router.push({ name: 'SurveyResult' }).catch((error) => {
              if (error.name === 'NavigationDuplicated') {
                location.reload();
              }
            });
          } else {
            alert(msg);
            location.reload();
          }
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });
    },

    //선택한 문항의 번호가 저장
    select(now) {
      this.answer_list[this.where] = now;
      this.where += 1;
      if (this.where == 12) {
        this.answer_list[12] = localStorage.getItem('user_number');
        this.endSurvey();
      }
      this.width += 100 / 12;
      document.getElementById('mybar').style.width = this.width + '%';
    },

    handleNewLine(str) {
      return String(str).replace(/(?:\r\n|\r|\n)/g, '</br>');
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
      this.startSurvey();
    }
  },
};
</script>
<style></style>
