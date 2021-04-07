<template>
  <div class="content">
    <div class="magazine-logo">
      <img :src="MagazineImg" />
    </div>
    <div class="division"></div>
    <div class="mag-cont">
      <div>
        <strong>물주기,<br />내가 뭘 잘못한거지?</strong>
      </div>
      <div class="division"></div>
      <div class="mag-desc">
        <img src="@/assets/img/magazine/magazine_01.jpg" />
        <div class="mag-text">
          <strong style="font-size: 14px">내가 알고 있던 물 주기 상식</strong>
          <br />
          <br />
          1. 배고프지, 물 좀 줄까?
          <br />
          2. 시들시들하네, 물 좀 줄까?
          <br />
          3. 왜 안 자라지, 물 좀 줄까?
          <br />
          4. 덥지? 물 좀 먹어.
        </div>
        <img src="@/assets/img/magazine/magazine_02.jpg" />
        <div class="mag-text">
          모든 이유를 막론하고 물을 준다. <br />
          (내가 할 수 있는 것은 그것뿐)
          <br />
          <br />
          물이 부족하면 시들고, 너무 많이 줘도 시들고 <br />
          얼마만큼이 적당한 걸까?
        </div>
        <img src="@/assets/img/magazine/magazine_03.jpg" />
        <div class="mag-text">
          <strong style="font-size: 14px">실내 식물에게 물 주기란 </strong>
          <br />
          <strong style="font-size: 14px">빨래 말리기와 닮았다 </strong>
          <br />
          <br />
          눅눅하게 마른 빨래를 좋아하는 사람은 없다. <br />
          식물의 뿌리도 계속 눅눅한 상태는<br />
          싫어한다는 사실!
          <br />
          <br />
          햇빛 잘 드는 곳에 두면 몇 시간 만에 <br />
          보송보송하게 마르지만, <br />
          실내에 널어둔 빨래는 좀 더 걸리는 것과 <br />
          같은 원리다. 시들었던 대부분의 식물들은 <br />
          흙 속 수분이 잘 마르지 않아서 <br />
          뿌리가 썩은 경우가 많았다.
          <br />
          <br />
          환기가 잘 안되거나, <br />
          <span style="color: #00b564"
            >햇빛이 잘 안 드니까 빨래가 눅눅해지는 것처럼!</span
          >
          <br />
        </div>
        <img src="@/assets/img/magazine/magazine_04.jpg" />
        <div class="mag-text">
          물을 줬으면, <br />
          흙이 보송보송하게 <br />
          마르게 하는 것까지가 <br />
          물 주기의 마무리!
        </div>
        <div class="mag-copy">
          <span style="color: #00b564">copy</span>. 김파카 |
          <span style="color: #00b564">date</span>. 2020.12.04
        </div>
      </div>
      <div class="back">
        <div class="back-icon" @click="goBack()"><img :src="Backimg" /></div>
      </div>
    </div>
    <div style="padding-bottom: 75px"></div>
  </div>
</template>

<script>
import magazinelogo from '@/assets/img/MAGAZINE.png';
import backicon from '@/assets/img/arrows/left-arrow.png';

export default {
  name: 'Magazine',
  data: () => {
    return {
      MagazineImg: magazinelogo,
      Backimg: backicon,
    };
  },
  methods: {
    goBack() {
      history.back();
    },
  },
};
</script>

<style></style>
