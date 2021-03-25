<template>
  <div class="content">
    <div class="plantitlogo">
        <img :src="Plantitimg" />
    </div>

    <div class="startline"></div>

    <div class="searchtitle">
        어떤 종류의<br>
        식물을 찾고 있나요?
    </div>

    <button @click="usename">
        검색하기
    </button>
    <button @click="usefilter">
        필터
    </button>

    <div v-if="isStatusOn">
      <SearchFilter
        :filter_list="plant_list['filter_list']"
        @callParent="getfilterlist"
      />
    </div>
    <div v-else>
      <SearchName 
        @callParent="getplantname"
      />
    </div>
    
    <SearchList 
        :plant_list="plant_list['plant_list']"
    />
  </div>
</template>
<script>
import axios from 'axios';

import Plantitimg from '@/assets/img/PLANTIT.png';

import SearchName from '@/components/Search/SearchName.vue';
import SearchFilter from '@/components/Search/SearchFilter.vue';
import SearchList from '@/components/Search/SearchList.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Search',
  data: () => {
    return {

        Plantitimg : Plantitimg,

        isStatusOn : true,

        selected_list : [],
        last_selected : 0,
        filter_list : [],
        plant_list : '',
    };
  },
  components: {
    SearchName,
    SearchFilter,
    SearchList,
  },

  methods: {
    usename(){
        this.isStatusOn = false;
    },

    usefilter(){
        this.isStatusOn = true;
    },

    startsearch() {
      axios
        .post(`${SERVER_URL}/search/`, { selected_list : [], last_selected : 0 })

        .then((response) => {
            this.plant_list = response.data;
        })
        .catch(() => {
            alert('서버와 통신할 수 없습니다.');
        });
    },

    getplantname(getdata){
        axios
        .get(`${SERVER_URL}/search/${getdata}`)

        .then((response) => {
            this.plant_list = response.data;
        })
        .catch(() => {
            alert('서버와 통신할 수 없습니다.');
        });
    },

    // getdata에는 selectedlist-> 선택된 필터들 , last_selected -> 마지막 선택된 필터 가 들어있다.
    // getdata[0] -> selectedlist
    // getdata[1] -> last_selected
    getfilterlist(getdata){
        axios
        .post(`${SERVER_URL}/search/`, { selected_list : getdata[0], last_selected : getdata[1] })

        .then((response) => {
            this.plant_list = response.data;
        })
        .catch(() => {
            alert('서버와 통신할 수 없습니다.');
        });
    },
  },

  created() {
      this.startsearch();
  },

  beforeMount(){
    if(localStorage.length == 1){
      alert("로그인 하고 이용해주세요.")
      this.$router.push({ name: 'Home' });
    }
  },
};
</script>
<style>
    .content {
        text-align: left;
    }

    .plantitlogo img {
        width: 154px;
        height: 51px;
        margin: 5% 0 2% 5%;
    }

    .startline {
        width: 90%;
        height: 0px;
        border: 1px solid #FFFFFF;
        margin: 0 auto 5% auto;
    }
    .searchtitle {
        font-style: normal;
        font-weight: normal;
        font-size: 22px;
        line-height: 28px;
        color: white;
        text-align: left;
        margin: 0 0 5% 5%;
    }
</style>
