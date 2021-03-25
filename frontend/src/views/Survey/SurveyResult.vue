<template>
  <div class="content">
    <div v-if="delay_time">
      <Loading />
    </div>
    <div v-else>
      <Result v-bind:result="this.result_detail" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Loading from '@/components/Survey/Loading.vue';
import Result from '@/components/Survey/Result.vue';

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'SurveyResult',
  data: () => {
    return {
      delay_time: true,
      result_detail: {},
    };
  },
  components: {
    Loading,
    Result,
  },
  methods: {
    getResult() {
      axios
        .post(`${SERVER_URL}/detail/`, {
          user_number: localStorage.getItem('user_number'),
        })
        .then((response) => {
          this.result_detail = response.data;
        })
        .catch(() => {
          alert('결과를 가져오는 중에 오류가 발생했습니다');
          this.$router.push({ name: 'Home' }).catch((error) => {
            if (error.name === 'NavigationDuplicated') {
              location.reload();
            }
          });
        });
    },
  },

  // created 할 때 jwt가 없다면 home으로 보내기
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
      this.getResult();
      setTimeout(() => {
        this.delay_time = false;
      }, 3000);
    }
  },
};
</script>
