<template>
  <div class="content">
    <div class="head">
      <img :src="Plantitimg" />
    </div>
    <div class="division"></div>
    <div class="plantit-title">
      <div id="myplant">MY PLANT</div>
      <div id="care">식물들을 관리해주세요</div>
    </div>
    <PlantCard
      v-for="(myplant, idx) in myplant_list"
      :key="idx"
      :myplant="myplant"
    />
    <div style="padding-bottom: 75px"></div>
  </div>
</template>

<script>
import axios from "axios";
import Plantitimg from "@/assets/img/PLANTIT.png";
import PlantCard from "@/components/MyPlant/PlantCard.vue";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;
export default {
  name: "MyPlant",
  data: () => {
    return {
      Plantitimg: Plantitimg,
      myplant_list: [],
    };
  },
  components: {
    PlantCard,
  },
  methods: {
    getPlant() {
      axios
        .post(`${SERVER_URL}/myplant/`, {
          user_number: localStorage.getItem("user_number"),
        })
        .then((response) => {
          this.myplant_list = response.data.myplant_list;
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
  },
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
      this.getPlant();
    }
  },
};
</script>

<style></style>
