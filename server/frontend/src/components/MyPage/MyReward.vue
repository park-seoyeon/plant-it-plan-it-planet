<template>
  <div class="reward">
    <div id="badge">
      <img id="badge-get" v-if="myreward" :src="getBadgeActPath()" @click="badgeAlert()"/>
      <img id="badge-nonget" v-else :src="getBadgePath()" @click="badgeAlertNot()"/>
    </div>
    <div id="reward-title">{{ this.reward_title[index] }}</div>
  </div>
</template>

<script>
export default {
  name: 'MyReward',
  props: {
    myreward: Number,
    index: Number,
  },
  data: () => {
    return {
      reward_title: [
        '이제 나도 식물 집사!',
        '첫 대화 그리고 설렘',
        '너의 이름은...',
        '아이~ 맛있어..!',
        '새 집 마련',
        '너와의 추억',
        '권태기',
        '하바드 식물학과 졸업',
        '식목 대신 플랜잇',
        '플랜잇과 365일',
        '나사 빠진 식물',
        '식물아일체',
      ],
      alerts: [
        '플랜잇 가입 후 첫 식물 심기',
        '처음 식물에게 말걸기',
        '식물 이름 지어주기',
        '물주기 50회',
        '분갈이 1회',
        '식물 일지 5번 쓰기',
        '"이제 그만 말걸어" 듣기',
        '한 식물 LV5 달성',
        '식목일에 식물사기',
        '가입 1주년',
        '말걸기 기능을 통해서 NASA 연구관련 5개 물질 다 듣기',
        '"엘프" 등급 달성',
      ],
    };
  },
  methods: {
    getBadgeActPath() {
      return require(`@/assets/img/badgeAct/badge-act_${this.index}.png`);
    },
    getBadgePath() {
      return require(`@/assets/img/badge/badge_${this.index}.png`);
    },
    badgeAlert(){
      this.$swal.fire({
          icon: 'info',
          title: '획득 조건',
          text: this.alerts[this.index],
      })
    },
    badgeAlertNot(){
      this.$swal.fire({
          icon: 'question',
          title: '어떻게 얻을까요?',
          text: '뱃지 획득시 획득 조건 공개',
      })
    },
  },
};
</script>
