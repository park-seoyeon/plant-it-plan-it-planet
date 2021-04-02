<template>
  <div class="content">
    <div class="head">
      <img :src="Plantitimg" />
    </div>

    <div class="division"></div>

    <div class="searchtitle">
      어떤 종류의<br />
      식물을 찾고 있나요?
    </div>

    <div class="searchicons">
      <div class="top-btn" @click="reset"><img :src="Reseticon" /></div>
      <div class="top-btn" @click="usename"><img :src="Searchicon" /></div>
      <div class="top-btn" @click="usefilter"><img :src="Filtericon" /></div>
    </div>

    <div v-if="isStatusOn">
      <SearchFilter
        @sendCategory="getfilterlist"
        @sendCategorydelete="getfilterlistdelete"
        @sendLeaftype="getfilterlist"
        @sendLeaftypedelete="getfilterlistdeleteleaftype"
        @sendAir="getfilterlist"
        @sendSmell="getfilterlist"
        @sendAnimal="getfilterlist"
        @sendLight="getfilterlist"
        @sendFruit="getfilterlist"
        @sendStick="getfilterlist"
        @sendBottom="getfilterlist"
        @sendFlower="getfilterlist"
        @sendSoil="getfilterlist"
        @sendNiddle="getfilterlist"
        @send1="getfilterlist"
        @send2="getfilterlist"
        @send3="getfilterlist"
        @send4="getfilterlist"
        @send5="getfilterlist"
        @send6="getfilterlist"
        @send7="getfilterlist"
        @send8="getfilterlist"
        @send9="getfilterlist"
        @send10="getfilterlist"
        @send11="getfilterlist"
        @send12="getfilterlist"
        @send13="getfilterlist"
        @send14="getfilterlist"
        @send15="getfilterlist"
        ref="resetfilter"
      />
    </div>
    <div v-else>
      <SearchName
        @callParent="getplantname"
        ref="resetfilter"
        style="float: left"
      />
    </div>

    <SearchList :plant_list="plant_list['plant_list']" 
      ref="resetlist"
    />
  </div>
</template>
<script>
import axios from 'axios';

import Plantitimg from '@/assets/img/PLANTIT.png';
import Reseticon from '@/assets/img/reseticon.png';
import Searchicon from '@/assets/img/searchicon.png';
import Filtericon from '@/assets/img/filtericon.png';

import SearchName from '@/components/Search/SearchName.vue';
import SearchFilter from '@/components/Search/SearchFilter.vue';
import SearchList from '@/components/Search/SearchList.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Search',
  data: () => {
    return {
      Plantitimg: Plantitimg,
      Reseticon: Reseticon,
      Searchicon: Searchicon,
      Filtericon: Filtericon,

      isStatusOn: true,

      selected_list: [],
      last_selected: 0,
      filter_list: [],
      plant_list: '',

      idx: 0,

      getlist: [],
    };
  },
  components: {
    SearchName,
    SearchFilter,
    SearchList,
  },

  methods: {
    reset() {
      this.selected_list = [];

      this.$refs.resetfilter.resetfilters();
      this.isStatusOn = false;
      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
          this.isStatusOn = true;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    usename() {
      this.isStatusOn = false;
      this.selected_list = [];

      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    usefilter() {
      this.selected_list = [];
      this.$refs.resetfilter.resetfilters();
      this.isStatusOn = false;

      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
          this.isStatusOn = true;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    startsearch() {
      axios
        .post(`${SERVER_URL}/search/`, { selected_list: [] })

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    getplantname(getdata) {
      axios
        .get(`${SERVER_URL}/search/${getdata}`)

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    getfilterlist(getdata) {
      this.addfiltertolist(getdata);

      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    getfilterlistdelete(getdata) {
      this.addfiltertolistdelete(getdata);

      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    getfilterlistdeleteleaftype(getdata) {
      this.addfiltertolistdeleteleaftype(getdata);

      axios
        .post(`${SERVER_URL}/search/`, { selected_list: this.selected_list })

        .then((response) => {
          this.plant_list = response.data;
        })
        .catch(() => {
          alert('서버와 통신할 수 없습니다.');
        });

      this.$refs.resetlist.resetlists();
    },

    addfiltertolist(getdata) {
      if (this.selected_list.includes(getdata)) {
        const where = this.selected_list.indexOf(getdata);
        this.selected_list.splice(where, 1);
        this.idx = this.idx - 1;
      } else {
        this.selected_list[this.idx] = getdata;
        this.idx = this.idx + 1;
      }
    },

    addfiltertolistdelete(getdata) {

      this.selected_list = [];
      this.idx = 0;
      this.selected_list[this.idx] = getdata;
      this.idx = this.idx + 1;
    },

    addfiltertolistdeleteleaftype(getdata) {

      const where = this.selected_list.indexOf(getdata);
      this.selected_list.splice(where, 1);
      this.idx = this.idx - 1;

      for (var i = 14; i < 29; i++) {
        if (this.selected_list.includes(i)) {
          const where = this.selected_list.indexOf();
          this.selected_list.splice(where, 1);
          this.idx = this.idx - 1;
        }
      }
    },
  },

  created() {
    const token = localStorage.getItem('jwt');
    if (token == null) {
      alert('로그인 하고 이용해주세요.');
      this.$router.push({ name: 'Home' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    } else {
      this.startsearch();
    }
  },
};
</script>
<style></style>
