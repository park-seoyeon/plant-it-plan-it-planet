<template>
  <div id="searchname">
    <form v-on:submit.prevent="searchplant">
      <img :src="Searchname" />
      <input
        id="plantname"
        type="text"
        ref="plantname"
        placeholder="검색어를 입력해주세요"
      />
      <button class="submitbutton" type="submit">검색</button>
    </form>
  </div>
</template>

<script>
// import axios from "axios";
import Searchname from '@/assets/img/searchinput.png';

export default {
  name: 'SearchName',

  props: ['filter_list'],

  data: () => {
    return {
      Searchname: Searchname,
    };
  },
  components: {},
  methods: {
    searchplant() {
      this.$emit('callParent', this.$refs.plantname.value);
      document.getElementById('plantname').value = '';
    },

    resetfilters() {},
  },
  created() {},
};
</script>
<style></style>
