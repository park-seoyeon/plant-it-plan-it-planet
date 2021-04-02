<template>
  <div>
    <div class="profile-card">
      <div id="sky-head"></div>
      <div class="head">
        <img id="mypage-profile-image" v-if="myprofile.profile_image" :src="myprofile.profile_image" />
        <img id="mypage-profile-image" v-else :src="getDefaultProfileImg()" />
        <div id="title">{{ myprofile.level.title }}</div>
      </div>
      <div class="bottom">
        <div class="bottom-name">
          <div id="name">{{ myprofile.name }}</div>
          <img id="level-thumbnail-image" :src="getLevelThumbnail()" />
        </div>
        <div class="level">
          <div class="level-text" v-if="myprofile.level.level < 5">
            <div id="next">다음등급까지</div>
            <div id="number">{{ myprofile.level.reward_cnt }} / {{ myprofile.level.max_reward_cnt }} 개</div>
          </div>
          <div class="level-text" v-else>
            <div id="next">Max Level</div>
            <div id="number">{{ myprofile.level.reward_cnt }} / {{ myprofile.level.max_reward_cnt }} 개</div>
          </div>
          <div id="level-bar">
            <div id="level-progress" v-bind:style="{ width: myprofile.level.level_pc + '%' }"></div>
          </div>
        </div>
      </div>
    </div>
    <div id="bottom-profile-card"></div>
  </div>
</template>

<script>
export default {
  name: 'ProfileCard',
  props: {
    myprofile: Object,
  },
  data: () => {
    return {};
  },
  methods: {
    getDefaultProfileImg() {
      return require(`@/assets/img/profile/basic_profile_img.png`);
    },
    getLevelThumbnail() {
      var level = this.myprofile.level.level;
      if (level == 0) {
        return require(`@/assets/img/profile/level_0.png`);
      } else if (level == 1) {
        return require(`@/assets/img/profile/level_1.png`);
      } else if (level == 2) {
        return require(`@/assets/img/profile/level_2.png`);
      } else if (level == 3) {
        return require(`@/assets/img/profile/level_3.png`);
      } else if (level == 4) {
        return require(`@/assets/img/profile/level_4.png`);
      } else {
        return require(`@/assets/img/profile/level_5.png`);
      }
    },
  },
};
</script>
