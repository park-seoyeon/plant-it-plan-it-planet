<template>
  <div id="leaftype">
    <div class="dashedline2"></div>
    <div
      v-if="is_1"
      class="leaftypefilter-active"
      id="select1"
      @click="select1()"
    >
      구멍
    </div>
    <div v-else class="leaftypefilter" id="select1" @click="select1()">
      구멍
    </div>

    <div
      v-if="is_2"
      class="leaftypefilter-active"
      id="select2"
      @click="select2()"
    >
      넓은
    </div>
    <div v-else class="leaftypefilter" id="select2" @click="select2()">
      넓은
    </div>

    <div
      v-if="is_3"
      class="leaftypefilter-active"
      id="select3"
      @click="select3()"
    >
      둥근
    </div>
    <div v-else class="leaftypefilter" id="select3" @click="select3()">
      둥근
    </div>

    <div
      v-if="is_4"
      class="leaftypefilter-active"
      id="select4"
      @click="select4()"
    >
      뾰족한
    </div>
    <div v-else class="leaftypefilter" id="select4" @click="select4()">
      뾰족한
    </div>

    <div
      v-if="is_5"
      class="leaftypefilter-active"
      id="select5"
      @click="select5()"
    >
      길쭉한
    </div>
    <div v-else class="leaftypefilter" id="select5" @click="select5()">
      길쭉한
    </div>

    <div
      v-if="is_6"
      class="leaftypefilter-active"
      id="select6"
      @click="select6()"
    >
      갈라진
    </div>
    <div v-else class="leaftypefilter" id="select6" @click="select6()">
      갈라진
    </div>

    <div
      v-if="is_7"
      class="leaftypefilter-active"
      id="select7"
      @click="select7()"
    >
      하트모양
    </div>
    <div v-else class="leaftypefilter" id="select7" @click="select7()">
      하트모양
    </div>

    <div
      v-if="is_8"
      class="leaftypefilter-active"
      id="select8"
      @click="select8()"
    >
      별모양
    </div>
    <div v-else class="leaftypefilter" id="select8" @click="select8()">
      별모양
    </div>

    <div
      v-if="is_9"
      class="leaftypefilter-active"
      id="select9"
      @click="select9()"
    >
      작은
    </div>
    <div v-else class="leaftypefilter" id="select9" @click="select9()">
      작은
    </div>

    <div
      v-if="is_10"
      class="leaftypefilter-active"
      id="select10"
      @click="select10()"
    >
      두꺼운
    </div>
    <div v-else class="leaftypefilter" id="select10" @click="select10()">
      두꺼운
    </div>

    <div
      v-if="is_11"
      class="leaftypefilter-active"
      id="select11"
      @click="select11()"
    >
      무늬
    </div>
    <div v-else class="leaftypefilter" id="select11" @click="select11()">
      무늬
    </div>

    <div
      v-if="is_12"
      class="leaftypefilter-active"
      id="select12"
      @click="select12()"
    >
      꽃 모양
    </div>
    <div v-else class="leaftypefilter" id="select12" @click="select12()">
      꽃 모양
    </div>

    <div
      v-if="is_13"
      class="leaftypefilter-active"
      id="select13"
      @click="select13()"
    >
      통통한
    </div>
    <div v-else class="leaftypefilter" id="select13" @click="select13()">
      통통한
    </div>

    <div
      v-if="is_14"
      class="leaftypefilter-active"
      id="select14"
      @click="select14()"
    >
      납작한
    </div>
    <div v-else class="leaftypefilter" id="select14" @click="select14()">
      납작한
    </div>

    <div
      v-if="is_15"
      class="leaftypefilter-active"
      id="select15"
      @click="select15()"
    >
      잎이 없음
    </div>
    <div v-else class="leaftypefilter" id="select15" @click="select15()">
      잎이 없음
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'LeafType',

  data: () => {
    return {
      is_1: false,
      is_2: false,
      is_3: false,
      is_4: false,
      is_5: false,
      is_6: false,
      is_7: false,
      is_8: false,
      is_9: false,
      is_10: false,
      is_11: false,
      is_12: false,
      is_13: false,
      is_14: false,
      is_15: false,
    };
  },
  components: {},
  methods: {
    select1() {
      this.$emit('call1');
      this.is_1 = !this.is_1;
    },
    select2() {
      this.$emit('call2');
      this.is_2 = !this.is_2;
    },
    select3() {
      this.$emit('call3');
      this.is_3 = !this.is_3;
    },
    select4() {
      this.$emit('call4');
      this.is_4 = !this.is_4;
    },
    select5() {
      this.$emit('call5');
      this.is_5 = !this.is_5;
    },
    select6() {
      this.$emit('call6');
      this.is_6 = !this.is_6;
    },
    select7() {
      this.$emit('call7');
      this.is_7 = !this.is_7;
    },
    select8() {
      this.$emit('call8');
      this.is_8 = !this.is_8;
    },
    select9() {
      this.$emit('call9');
      this.is_9 = !this.is_9;
    },
    select10() {
      this.$emit('call10');
      this.is_10 = !this.is_10;
    },
    select11() {
      this.$emit('call11');
      this.is_11 = !this.is_11;
    },
    select12() {
      this.$emit('call12');
      this.is_12 = !this.is_12;
    },
    select13() {
      this.$emit('call13');
      this.is_13 = !this.is_13;
    },
    select14() {
      this.$emit('call14');
      this.is_14 = !this.is_14;
    },
    select15() {
      this.$emit('call15');
      this.is_15 = !this.is_15;
    },
  },
  created() {
    this.is_1 = false;
    this.is_2 = false;
    this.is_3 = false;
    this.is_4 = false;
    this.is_5 = false;
    this.is_6 = false;
    this.is_7 = false;
    this.is_8 = false;
    this.is_9 = false;
    this.is_10 = false;
    this.is_11 = false;
    this.is_12 = false;
    this.is_13 = false;
    this.is_14 = false;
    this.is_15 = false;
  },
};
</script>
<style></style>
