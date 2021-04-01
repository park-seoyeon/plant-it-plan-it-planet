<template>
  <div class="myplants_card">
    <div class="plantscard">
      <div class="title">
        <div class="titlename">
          {{ myplants.title }}
        </div>
        <div class="modify">
          수정
        </div>
        <div class="delete" @click="diarydelete">
          삭제
        </div>
      </div>
      <div class="date">
        {{ this.today_date }}
      </div>
      <div class="contents">
        {{ myplants.content }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MyPlantsCard',

  props: ['myplants'],

  data: () => {
    return {
      today_date: '',
      getid: '',
    };
  },

  computed: {
    
  },

  components: {},
  methods: {
    diarydelete(){
      this.$emit('calldelete' , this.getid);
    },
  },
  created() {
    this.today_date = this.myplants.add_date.slice(0, 10).replace(/-/g, '.')
    this.getid = this.myplants.id
  },
};
</script>
<style></style>
