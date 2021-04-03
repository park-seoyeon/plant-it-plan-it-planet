<template>
  <div class="reward">
    <div id="badge">
      <img id="badge-get" v-if="myreward" src="@/assets/img/badge/badge.png" />
      <img id="badge-nonget" v-else src="@/assets/img/badge/default2.png" />
    </div>
    <div id="reward-title">{{ this.reward_title[index] }}</div>
  </div>
</template>

<script>
export default {
  name: "MyReward",
  props: {
    myreward: Number,
    index: Number,
  },
  data: () => {
    return {
      reward_title: [
        "이제 나도 식물 집사!",
        "첫 대화 그리고 설렘",
        "너의 이름은...",
        "아이~ 맛있어..!",
        "새 집 마련",
        "너와의 추억",
        "권태기",
        "하바드 식물학과 졸업",
        "식목 대신 플랜잇",
        "플랜잇과 365일",
        "나사 빠진 식물",
        "식물아일체",
      ],
    };
  },
};
</script>