<template>
    <div class="content">
        <div id="icons">
            <img :src='planticon'>
            <img :src='planicon'>
            <img :src='planeticon' style="margin-right: 0;">  
        </div>

        <div style="color: white;">
          {{ this.answer_list }}
        </div>

        <!-- 상태바 찾아서 넣기 -->
        <!-- 임시로 css로 흰색 얇은 박스 하나 넣어놈 -->
        <div id="progressbar">
            
        </div>

        <div v-if="isStatusOn" @click="swap">
          <div id="ask">
            {{ this.question_list.question }}
          </div>

          <div class="buttons" id="select1" @click="select1()">
              {{ this.question_list.answer_01 }}
          </div>
          <div class="buttons" id="select2" @click="select2()">
              {{ this.question_list.answer_02 }}
          </div>
          <div class="buttons" id="select3" @click="select3()">
              {{ this.question_list.answer_03 }}
          </div>
          <div class="buttons" id="select4" @click="select4()">
              {{ this.question_list.answer_04 }}
          </div>
        </div>
        <div v-else>
           <div id="ask">
            {{ this.question_list.question }}
          </div>

          <div class="buttons" id="select1" @click="select1()">
              {{ this.question_list.answer_01 }}
          </div>
          <div class="buttons" id="select2" @click="select2()">
              {{ this.question_list.answer_02 }}
          </div>
          <div class="buttons" id="select3" @click="select3()">
              {{ this.question_list.answer_03 }}
          </div>
          <div class="buttons" id="select4" @click="select4()">
              {{ this.question_list.answer_04 }}
          </div>
        </div>
                      
        
    </div>
</template>
<script>
import axios from "axios";

import planticon from '@/assets/img/plantit_icon.png'
import planicon from '@/assets/img/planit_icon.png'
import planeticon from '@/assets/img/planet_icon.png'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "SurveyProgress",
  data: () => {
    return {
        planticon : planticon,
        planicon : planicon,
        planeticon : planeticon,

        // 질문의 index값 -> 시작은 0 -> 첫 번째 질문... -> selectAnswer() 함수를 통해서 값을 증가시켜 다음 질문 받아오기
        where : 0,

        // select1 ~ select4 함수를 통해서 내가 선택한 답안이 몇 번째 답안인지 알아내기 위한 변수
        now : 0,

        // this.where 즉, 현재 index값의 계속 유지하면서 다음 질문을 받아오기 위해서 v-if를 통해 두 가지 div를 만들고
        // 번갈아서 보여주는 방식을 이용
        isStatusOn : false,

        question_list: {
          question_number : 0,
          question : '',
          answer_01 : '',
          answer_02 : '',
          answer_03 : '',
          answer_04 : '',
        },

        answer_list: [],
    }
  },
  methods : {

    startSurvey(){
      axios
        .get(`${SERVER_URL}/servey/list/`)
        
        .then((response)=>{
            this.question_list.question_number = response.data.question_list[this.where]['question_number'];
            this.question_list.question = response.data.question_list[this.where]['question'];
            this.question_list.answer_01 = response.data.question_list[this.where]['answer_01'];
            this.question_list.answer_02 = response.data.question_list[this.where]['answer_02'];
            this.question_list.answer_03 = response.data.question_list[this.where]['answer_03'];
            this.question_list.answer_04 = response.data.question_list[this.where]['answer_04'];
        })
    },

    endSurvey(){
      axios
        .post(`${SERVER_URL}/servey/`, { answer_list : this.answer_list })
        
        .then(()=>{
            
        })

      alert(this.answer_list);
      this.$router.push({ name: 'SurveyResult' });
    },

    select1: function(){
      this.now = 1;
      this.selectAnswer(this.now);
      if(this.where == 12){
        this.endSurvey();
      }
    },
    select2: function(){
      this.now = 2;
      this.selectAnswer(this.now);
      if(this.where == 12){
        this.endSurvey();
      }
    },
    select3: function(){
      this.now = 3;
      this.selectAnswer(this.now);
      if(this.where == 12){
        this.endSurvey();
      }
    },
    select4: function(){
      this.now = 4;
      this.selectAnswer(this.now);
      if(this.where == 12){
        this.endSurvey();
      }
    },

    // answer_list 배열에 선택한 답안이 몇 번째 인지 넣어주고 다음 index로 넘어가기
    selectAnswer(now){

      this.answer_list[this.where] = now;

      this.where = this.where + 1;

      axios
        .get(`${SERVER_URL}/servey/list/`)
        
        .then((response)=>{
            this.question_list.question_number = response.data.question_list[this.where]['question_number'];
            this.question_list.question = response.data.question_list[this.where]['question'];
            this.question_list.answer_01 = response.data.question_list[this.where]['answer_01'];
            this.question_list.answer_02 = response.data.question_list[this.where]['answer_02'];
            this.question_list.answer_03 = response.data.question_list[this.where]['answer_03'];
            this.question_list.answer_04 = response.data.question_list[this.where]['answer_04'];
        })
    },

    swap: function(){
      if(this.isStatusOn){
        this.isStatusOn = false;
        this.selectAnswer();
      }
      else{
        this.isStatusOn = true;
        this.selectAnswer();
      }
    },

  },

  // 설문조사의 첫 시작, 첫 번째 질문이 나오게 하자.
  beforeMount(){
    this.startSurvey()
  },

};
</script>
<style>
  .content {
      /* background-color: black; */
      background: rgb(36, 36, 36) no-repeat center center fixed; 
      -webkit-background-size: cover;
      -moz-background-size: cover;
      -o-background-size: cover;
      background-size: cover;
      text-align: center;
      background-size: 100%;
      min-height: 800px;
    }

    .content #icons {
        padding: 20% 0 0 0;
    }

    .content #icons img {
        width: 15%;
        height: 15%;
        margin: 0 5% 0 0;
    }

    .content #progressbar {
        height: 5px;
        background: white;
        width: 80%;
        margin: 5% auto 0 auto;
    }

    .content #ask {
      color: white;
      margin: 10% 0 20% 0;
      font-size: 15px;
    }

    .content .buttons {
      border: 2px solid white;
      border-radius: 10px;
      width: 80%;
      height: 60px;
      margin: 10% auto 0 auto;
      color: white;
      font-size: 12px;
      vertical-align: middle;
      line-height: 60px;
    }
</style>