<template>
  <div id="cactuscategory">
    <div class="dashedline"></div>
    <div
      v-if="isleafType"
      class="cactuscategoryfilter-active"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-else
      class="cactuscategoryfilter"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-if="isair"
      class="cactuscategoryfilter-active"
      id="air4"
      @click="selectair()"
    >
      공기정화
    </div>
    <div v-else class="cactuscategoryfilter" id="air4" @click="selectair()">
      공기정화
    </div>
    <div
      v-if="isflower"
      class="cactuscategoryfilter-active"
      id="flower4"
      @click="selectflower()"
    >
      꽃 피는
    </div>
    <div
      v-else
      class="cactuscategoryfilter"
      id="flower4"
      @click="selectflower()"
    >
      꽃 피는
    </div>
    <div
      v-if="islight"
      class="cactuscategoryfilter-active"
      id="light4"
      @click="selectlight()"
    >
      빛이 적어도 되는
    </div>
    <div v-else class="cactuscategoryfilter" id="light4" @click="selectlight()">
      빛이 적어도 되는
    </div>
    <div
      v-if="isanimal"
      class="cactuscategoryfilter-active"
      id="animal4"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div
      v-else
      class="cactuscategoryfilter"
      id="animal4"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div
      v-if="isfruit"
      class="cactuscategoryfilter-active"
      id="fruit4"
      @click="selectfruit()"
    >
      열매 맺는
    </div>
    <div v-else class="cactuscategoryfilter" id="fruit4" @click="selectfruit()">
      열매 맺는
    </div>
    <div
      v-if="isstick"
      class="cactuscategoryfilter-active"
      id="stick4"
      @click="selectstick()"
    >
      목대 있는
    </div>
    <div v-else class="cactuscategoryfilter" id="stick4" @click="selectstick()">
      목대 있는
    </div>
    <div
      v-if="isniddle"
      class="cactuscategoryfilter-active"
      id="niddle4"
      @click="selectniddle()"
    >
      가시가 없는
    </div>
    <div
      v-else
      class="cactuscategoryfilter"
      id="niddle4"
      @click="selectniddle()"
    >
      가시가 없는
    </div>
    <div
      v-if="isbottom"
      class="cactuscategoryfilter-active"
      id="bottom4"
      @click="selectbottom()"
    >
      밑이 통통한
    </div>
    <div
      v-else
      class="cactuscategoryfilter"
      id="bottom4"
      @click="selectbottom()"
    >
      밑이 통통한
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'CactusCategory',

  data: () => {
    return {
      isleafType: false,
      isair: false,
      isflower: false,
      islight: false,
      isanimal: false,
      isfruit: false,
      isstick: false,
      isniddle: false,
      isbottom: false,
    };
  },
  components: {},
  methods: {
    selectleaftype() {
      this.$emit('callLeaftype');
      this.isleafType = !this.isleafType;
    },

    selectair() {
      this.$emit('callAir');
      this.isair = !this.isair;
    },

    selectflower() {
      this.$emit('callFlower');
      this.isflower = !this.isflower;
    },

    selectlight() {
      this.$emit('callLight');
      this.islight = !this.islight;
    },

    selectanimal() {
      this.$emit('callAnimal');
      this.isanimal = !this.isanimal;
    },

    selectfruit() {
      this.$emit('callFruit');
      this.isfruit = !this.isfruit;
    },

    selectstick() {
      this.$emit('callStick');
      this.isstick = !this.isstick;
    },
    selectniddle() {
      this.$emit('callNiddle');
      this.isniddle = !this.isniddle;
    },

    selectbottom() {
      this.$emit('callBottom');
      this.isbottom = !this.isbottom;
    },
  },
  created() {
    this.isleafType = false;
    this.isair = false;
    this.isflower = false;
    this.islight = false;
    this.isanimal = false;
    this.isfruit = false;
    this.isstick = false;
    this.isniddle = false;
    this.isbottom = false;
  },
};
</script>
<style></style>
