<template>
  <div class="myplants_card">
    <div v-if="!ismodifyon" class="plantscard">
      <div class="title">
        <div class="titlename">
          {{ myplants.title }}
        </div>
        <div class="delete" @click="diarydelete">삭제</div>
        <div class="modify" @click="changemodify">수정</div>
      </div>
      <div class="date">
        {{ this.today_date }}
      </div>
      <div class="contents">
        {{ myplants.content }}
      </div>
    </div>

    <div v-if="ismodifyon" class="plantscard">
      <form @submit.prevent="modifydiarys">
        <div class="title2">
          <input
            class="titlename2"
            type="text"
            v-model="modifydiary.modifydiary_title"
            placeholder="수정 할 제목을 입력하세요."
          />
          <button class="modifyconfirm" type="submit">수정완료</button>
          <div class="delete" @click="changemodify">취소</div>
        </div>
        <input
          class="contents2"
          type="text"
          v-model="modifydiary.modifydiary_contents"
          placeholder="수정 할 일지 내용을 입력하세요."
          style="white-space: pre-line"
        />
      </form>
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
      gettitle: '',
      getcontents: '',
      ismodifyon: false,
      modifydiary: {
        modifydiary_id: '',
        modifydiary_title: '',
        modifydiary_contents: '',
      },
    };
  },

  computed: {},

  components: {},
  methods: {
    diarydelete() {
      this.$emit('calldelete', this.getid);
    },

    changemodify() {
      if (this.ismodifyon) {
        this.ismodifyon = false;
      } else {
        this.modifydiary.modifydiary_title = this.gettitle;
        this.modifydiary.modifydiary_contents = this.getcontents;
        this.ismodifyon = true;
      }
    },

    modifydiarys() {
      this.modifydiary.modifydiary_id = this.getid;
      this.$emit('callmodify', this.modifydiary);
    },
  },
  created() {
    this.today_date = this.myplants.add_date.slice(0, 10).replace(/-/g, '.');
    this.getid = this.myplants.id;
    this.gettitle = this.myplants.title;
    this.getcontents = this.myplants.content;
  },
};
</script>
<style></style>
