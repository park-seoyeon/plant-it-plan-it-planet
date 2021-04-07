<template>
  <div id="leafcategory">
    <div class="dashedline"></div>
    <div
      v-if="isleafType"
      class="leafcategoryfilter-active"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-else
      class="leafcategoryfilter"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-if="isair"
      class="leafcategoryfilter-active"
      id="air"
      @click="selectair()"
    >
      공기정화
    </div>
    <div v-else class="leafcategoryfilter" id="air" @click="selectair()">
      공기정화
    </div>
    <div
      v-if="issmell"
      class="leafcategoryfilter-active"
      id="smell"
      @click="selectsmell()"
    >
      향기나는
    </div>
    <div v-else class="leafcategoryfilter" id="smell" @click="selectsmell()">
      향기나는
    </div>
    <div
      v-if="isanimal"
      class="leafcategoryfilter-active"
      id="animal"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div v-else class="leafcategoryfilter" id="animal" @click="selectanimal()">
      반려동물 안전한
    </div>
    <div
      v-if="islight"
      class="leafcategoryfilter-active"
      id="light"
      @click="selectlight()"
    >
      빛이 적어도 되는
    </div>
    <div v-else class="leafcategoryfilter" id="light" @click="selectlight()">
      빛이 적어도 되는
    </div>
    <div
      v-if="isfruit"
      class="leafcategoryfilter-active"
      id="fruit"
      @click="selectfruit()"
    >
      열매 맺는
    </div>
    <div v-else class="leafcategoryfilter" id="fruit" @click="selectfruit()">
      열매 맺는
    </div>
    <div
      v-if="isstick"
      class="leafcategoryfilter-active"
      id="stick"
      @click="selectstick()"
    >
      목대 있는
    </div>
    <div v-else class="leafcategoryfilter" id="stick" @click="selectstick()">
      목대 있는
    </div>
    <div
      v-if="isbottom"
      class="leafcategoryfilter-active"
      id="bottom"
      @click="selectbottom()"
    >
      밑이 통통한
    </div>
    <div v-else class="leafcategoryfilter" id="bottom" @click="selectbottom()">
      밑이 통통한
    </div>
    <div
      v-if="isflower"
      class="leafcategoryfilter-active"
      id="flower"
      @click="selectflower()"
    >
      꽃이 피는
    </div>
    <div v-else class="leafcategoryfilter" id="flower" @click="selectflower()">
      꽃이 피는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'LeafCategory',

  data: () => {
    return {
      isleafType: false,
      isair: false,
      issmell: false,
      isflower: false,
      islight: false,
      isanimal: false,
      isfruit: false,
      isstick: false,
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

    selectsmell() {
      this.$emit('callSmell');
      this.issmell = !this.issmell;
    },

    selectanimal() {
      this.$emit('callAnimal');
      this.isanimal = !this.isanimal;
    },

    selectlight() {
      this.$emit('callLight');
      this.islight = !this.islight;
    },

    selectfruit() {
      this.$emit('callFruit');
      this.isfruit = !this.isfruit;
    },

    selectstick() {
      this.$emit('callStick');
      this.isstick = !this.isstick;
    },

    selectbottom() {
      this.$emit('callBottom');
      this.isbottom = !this.isbottom;
    },

    selectflower() {
      this.$emit('callFlower');
      this.isflower = !this.isflower;
    },
  },
  created() {
    this.isleafType = false;
    this.isair = false;
    this.issmell = false;
    this.isflower = false;
    this.islight = false;
    this.isanimal = false;
    this.isfruit = false;
    this.isstick = false;
    this.isbottom = false;
  },
};
</script>
<style></style>
