<template>
  <div class="content">
    <div class="head">
      <img :src="Plantitimg" />
      <span id="plus-btn" @click="addMyPlant()">+ 내 식물로 추가하기</span>
    </div>
    <div class="division"></div>
    <PlantInfo v-bind:info="this.plant_detail" />
    <PlantCare v-bind:care="this.plant_detail" />
    <div class="problem-name">혹시 식물이 아파요?</div>
    <div class="problem-division"></div>
    <PlantProblem v-for="(problem, idx) in sos" :key="idx" :problem="problem" />
    <div class="back">
      <div class="back-icon" @click="goBack()"><img :src="Backimg" /></div>
    </div>
    <div style="padding-bottom: 75px"></div>
  </div>
</template>

<script>
import planticon from "@/assets/img/PLANTIT.png";
import backicon from "@/assets/img/arrows/left-arrow.png";
import axios from "axios";
import PlantInfo from "@/components/SearchDetail/PlantInfo.vue";
import PlantCare from "@/components/SearchDetail/PlantCare.vue";
import PlantProblem from "@/components/SearchDetail/PlantProblem.vue";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "SearchDetail",
  data: () => {
    return {
      Plantitimg: planticon,
      Backimg: backicon,
      plant_detail: {},
      sos: [],
    };
  },
  components: {
    PlantInfo,
    PlantCare,
    PlantProblem,
  },
  methods: {
    getDetail() {
      axios
        .get(`${SERVER_URL}/search/detail/${this.$route.params.searchnumber}`)
        .then((response) => {
          this.plant_detail = response.data.result;
          // sos 값 가져와서 undefind 제외하고 리스트에 넣기
          for (var i = 1; i <= 8; i++) {
            var titleName = "sos_" + i;
            var detailName = "sos_solution_" + i;
            var temp = new Object();
            if (this.plant_detail[titleName] == undefined) {
              break;
            } else {
              temp.title = this.plant_detail[titleName];
              temp.detail = this.plant_detail[detailName];
              this.sos.push(temp);
            }
          }
        })
        .catch(() => {
          alert("결과를 가져오는 중에 오류가 발생했습니다");
          this.$router.push({ name: "Home" }).catch((error) => {
            if (error.name === "NavigationDuplicated") {
              location.reload();
            }
          });
        });
    },

    addMyPlant() {
      axios
        .post(`${SERVER_URL}/search/add/`, {
          user_number: localStorage.getItem("user_number"),
          plant_id: this.plant_detail.id,
        })
        .then(() => {
          if (
            confirm(
              "식물이 MYPLANT에 등록되었습니다. 해당 페이지로 이동하시겠습니까?"
            )
          ) {
            this.$router.push({ name: "MyPlant" }).catch((error) => {
              if (error.name === "NavigationDuplicated") {
                location.reload();
              }
            });
          }
        })
        .catch(() => {
          alert("서버와 통신할 수 없습니다.");
        });
    },

    goBack() {
      history.back();
    },
  },

  // created 할 때 jwt가 없다면 home으로 보내기
  created() {
    const token = localStorage.getItem("jwt");
    if (token == null) {
      alert("로그인 하고 이용해주세요.");
      this.$router.push({ name: "Home" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    } else {
      this.getDetail();
    }
  },
};
</script>

<style></style>
