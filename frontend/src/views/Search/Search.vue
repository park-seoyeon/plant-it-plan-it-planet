<template>
  <div class="content">
    <div class="plantitlogo" style="text-align: left;">
        <img :src="Plantitimg" />
    </div>

    <div class="startline"></div>

    <div class="searchtitle">
        어떤 종류의<br>
        식물을 찾고 있나요?
    </div>

    <div class="searchicons">
        <!-- <button @click="reset">
            리셋
        </button> -->
        <img :src="Reseticon" @click="reset" />
        <!-- <button @click="usename">
            검색하기
        </button> -->
        <img :src="Searchicon" @click="usename" style="margin-left: 3%;" />
        <!-- <button @click="usefilter">
            필터
        </button> -->
        <img :src="Filtericon" @click="usefilter" style="margin-left: 3%;" />
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
        style="float: left;"
      />
    </div>
    <div v-else>
      <SearchName 
        @callParent="getplantname"
        ref="resetfilter"
        style="float: left;"
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

        Plantitimg : Plantitimg,
        Reseticon : Reseticon,
        Searchicon : Searchicon,
        Filtericon : Filtericon,

        isStatusOn : true,

        selected_list : [],
        last_selected : 0,
        filter_list : [],
        plant_list : '',

        idx : 0,

        getlist : [],
    };
  },
  components: {
    SearchName,
    SearchFilter,
    SearchList,
  },

  methods: {
    reset(){
        this.selected_list = [];

        this.$refs.resetfilter.resetfilters();

        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    usename(){
        this.isStatusOn = false;
        this.selected_list = [];

        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    usefilter(){
        this.isStatusOn = true;
        this.selected_list = [];
        
        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    startsearch() {
      axios
        .post(`${SERVER_URL}/search/`, { selected_list : []  })

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

    getfilterlist(getdata){

        this.addfiltertolist(getdata);

        // alert(this.selected_list);

        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    getfilterlistdelete(getdata){

        this.addfiltertolistdelete(getdata);

        // alert(this.selected_list);

        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    getfilterlistdeleteleaftype(getdata){

        this.addfiltertolistdeleteleaftype(getdata);

        // alert(this.selected_list);

        axios
            .post(`${SERVER_URL}/search/`, { selected_list : this.selected_list })

            .then((response) => {
                this.plant_list = response.data;
            })
            .catch(() => {
                alert('서버와 통신할 수 없습니다.');
            });
    },

    addfiltertolist(getdata){
      if(this.selected_list.includes(getdata)){
        // alert("dete");
        const where =  this.selected_list.indexOf(getdata);
        this.selected_list.splice(where, 1);
        this.idx = this.idx - 1;
      }
      else{
        // alert("add");
        this.selected_list[this.idx] = getdata;
        this.idx = this.idx + 1;
      }
      
    },

    addfiltertolistdelete(getdata){
    //   alert("초기화");

      this.selected_list = [];
      this.idx = 0;
      this.selected_list[this.idx] = getdata;
      this.idx = this.idx + 1;
    },

    addfiltertolistdeleteleaftype(getdata){
    //   alert("잎 모양만 초기화");

      const where =  this.selected_list.indexOf(getdata);
      this.selected_list.splice(where, 1);
      this.idx = this.idx - 1;

      for(var i=14; i<29; i++){
        if(this.selected_list.includes(i)){
            const where =  this.selected_list.indexOf();
            this.selected_list.splice(where, 1);
            this.idx = this.idx - 1;
        }
      }
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
    .searchicons {
        text-align: left;
        margin: 0 0 0 5%;
    }

    .searchicons img {
        width: 10%;
        height: 10%;
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
