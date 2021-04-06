<template>
  <div>
    <div v-if="this.$route.name == 'Home'"></div>
    <div v-else-if="this.$route.name == 'SurveyStart'"></div>
    <div v-else-if="this.$route.name == 'SurveyProgress'"></div>
    <div v-else-if="this.$route.name == 'SurveyResult'"></div>
    <div v-else class="nav">
      <!-- main -->
      <img
        @click="goMain()"
        v-if="this.$route.name == 'Main'"
        :src="indoorActiveIcon"
      />
      <img
        @click="goMain()"
        v-else-if="this.$route.name == 'Magazine'"
        :src="indoorActiveIcon"
      />
      <img @click="goMain()" v-else :src="indoorIcon" />
      <!-- search -->
      <img
        @click="goSearch()"
        v-if="this.$route.name == 'Search'"
        :src="searchActiveIcon"
      />
      <img
        @click="goSearch()"
        v-else-if="this.$route.name == 'SearchDetail'"
        :src="searchActiveIcon"
      />
      <img @click="goSearch()" v-else :src="searchIcon" />
      <!-- myplant -->
      <img
        @click="goMyPlant()"
        v-if="this.$route.name == 'MyPlant'"
        :src="ecologyActiveIcon"
      />
      <img
        @click="goMyPlant()"
        v-else-if="this.$route.name == 'MyplantDetail'"
        :src="ecologyActiveIcon"
      />
      <img @click="goMyPlant()" v-else :src="ecologyIcon" />
      <!-- mypage -->
      <img
        @click="goMyPage()"
        v-if="this.$route.name == 'MyPage'"
        :src="planetActiveIcon"
      />
      <img @click="goMyPage()" v-else :src="planetIcon" />
    </div>
  </div>
</template>

<script>
import indoorIcon from '@/assets/img/nav_icon/indoor-plants.png';
import searchIcon from '@/assets/img/nav_icon/search.png';
import ecologyIcon from '@/assets/img/nav_icon/ecology.png';
import planetIcon from '@/assets/img/nav_icon/planet-earth.png';
import indoorActiveIcon from '@/assets/img/nav_icon/indoor-plants-active.png';
import searchActiveIcon from '@/assets/img/nav_icon/search-active.png';
import ecologyActiveIcon from '@/assets/img/nav_icon/ecology-active.png';
import planetActiveIcon from '@/assets/img/nav_icon/planet-earth-active.png';
export default {
  name: 'Navbar',
  data: () => {
    return {
      indoorIcon: indoorIcon,
      searchIcon: searchIcon,
      ecologyIcon: ecologyIcon,
      planetIcon: planetIcon,
      indoorActiveIcon: indoorActiveIcon,
      searchActiveIcon: searchActiveIcon,
      ecologyActiveIcon: ecologyActiveIcon,
      planetActiveIcon: planetActiveIcon,
    };
  },
  methods: {
    goMain() {
      document.documentElement.scrollTop = 0;
      this.$router.push({ name: 'Main' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
    goSearch() {
      document.documentElement.scrollTop = 0;
      this.$router.push({ name: 'Search' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
    goMyPlant() {
      document.documentElement.scrollTop = 0;
      this.$router.push({ name: 'MyPlant' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
    goMyPage() {
      document.documentElement.scrollTop = 0;
      this.$router.push({ name: 'MyPage' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    },
  },
};
</script>

<style></style>
