<template>
  <div>
    <div v-if="this.$route.path == '/'"></div>
    <div v-else-if="this.$route.path == '/survey/start'"></div>
    <div v-else-if="this.$route.path == '/survey/progress'"></div>
    <div v-else-if="this.$route.path == '/survey/result'"></div>
    <div v-else class="nav">
      <img v-if="this.$route.path == '/main'" :src="indoorActiveIcon" />
      <img
        v-else-if="this.$route.path == '/magazine'"
        :src="indoorActiveIcon"
      />
      <img v-else :src="indoorIcon" />
      <img v-if="this.$route.path == '/search'" :src="searchActiveIcon" />
      <img
        v-else-if="this.$route.path == '/search/detail/search:searchnumber'"
        :src="searchActiveIcon"
      />
      <img v-else :src="searchIcon" />
      <img :src="ecologyIcon" />
      <img :src="planetIcon" />
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
};
</script>

<style></style>
