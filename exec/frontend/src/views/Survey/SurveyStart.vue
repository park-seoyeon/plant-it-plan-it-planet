<template>
  <div class="content">
    <div id="logo">
      <img :src="Logo" />
    </div>
    <div id="ask_start">
      설문 조사를 통해<br />나에게 맞는 식물을 알아볼까요?
    </div>
    <div id="ask_ok_button" @click="goSurvey()">네, 그렇게 할게요</div>
    <div id="ask_no_button" @click="goSearch()">아니요, 괜찮아요</div>
  </div>
</template>
<script>
import Logo from "@/assets/img/Logo.png";

export default {
  name: "SurveyStart",
  data: () => {
    return {
      Logo: Logo,
    };
  },
  methods: {
    goSurvey() {
      this.$router.push({ name: "SurveyProgress" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
    goSearch() {
      this.$router.push({ name: "Search" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    },
  },

  // created 할 때 jwt가 없다면 home으로 보내기
  created() {
    const token = localStorage.getItem("jwt");
    if (token == null) {
      this.$swal.fire({
        icon: "error",
        title: "로그인 하고 이용해주세요.",
      });
      this.$router.push({ name: "Home" }).catch((error) => {
        if (error.name === "NavigationDuplicated") {
          location.reload();
        }
      });
    }
  },
};
</script>
<style></style>
