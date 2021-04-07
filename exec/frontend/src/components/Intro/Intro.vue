<template>
  <div class="content">
    <div id="Introimg">
      <img :src="Introimg" />
    </div>
    <div id="clicktostart">click to start</div>
  </div>
</template>

<script>
import Introimg from '@/assets/img/Introimg.gif';

export default {
  name: 'Intro',
  data() {
    return {
      Introimg: Introimg,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style></style>
