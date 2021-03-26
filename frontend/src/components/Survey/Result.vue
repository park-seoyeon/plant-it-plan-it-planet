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
      <div id="division-bar"></div>
      <div id="recommend">
        <div id="title">당신에게 어울리는 식물</div>
        <div id="desc">
          <img src="@/assets/img/plant/1_1.jpg" />
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
        <div id="desc">
          <img src="@/assets/img/plant/2_1.jpg" />
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
        <div id="desc">
          <img src="@/assets/img/plant/3_1.jpg" />
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
      <div id="start-tool"><span id="start">플랜잇 시작하기</span></div>
    </div>
  </div>
</template>

<script>
import planticon from '@/assets/img/plantit_icon.png';
import planicon from '@/assets/img/planit_icon.png';
import planeticon from '@/assets/img/planet_icon.png';

export default {
  name: 'Result',
  data: () => {
    return {
      planticon: planticon,
      planicon: planicon,
      planeticon: planeticon,
    };
  },

  props: {
    result: Object,
  },

  methods: {
    getMbtiImgPath() {
      return require(`@/assets/img/mbti/${this.result.mbti_name}.png`);
    },
    getBestImgPath() {
      return require(`@/assets/img/mbti/${this.result.best_partner}.png`);
    },
    getWorstImgPath() {
      return require(`@/assets/img/mbti/${this.result.worst_partner}.png`);
    },
  },
};
</script>

<style></style>
