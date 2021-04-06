<template>
  <div id="dungulcategory">
    <div class="dashedline"></div>
    <div
      v-if="isleafType"
      class="dungulcategoryfilter-active"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-else
      class="dungulcategoryfilter"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-if="isair"
      class="dungulcategoryfilter-active"
      id="air3"
      @click="selectair()"
    >
      공기정화
    </div>
    <div v-else class="dungulcategoryfilter" id="air3" @click="selectair()">
      공기정화
    </div>
    <div
      v-if="isflower"
      class="dungulcategoryfilter-active"
      id="flower3"
      @click="selectflower()"
    >
      꽃 피는
    </div>
    <div
      v-else
      class="dungulcategoryfilter"
      id="flower3"
      @click="selectflower()"
    >
      꽃 피는
    </div>
    <div
      v-if="islight"
      class="dungulcategoryfilter-active"
      id="light3"
      @click="selectlight()"
    >
      빛이 적어도 되는
    </div>
    <div v-else class="dungulcategoryfilter" id="light3" @click="selectlight()">
      빛이 적어도 되는
    </div>
    <div
      v-if="isanimal"
      class="dungulcategoryfilter-active"
      id="animal3"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div
      v-else
      class="dungulcategoryfilter"
      id="animal3"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div
      v-if="isfruit"
      class="dungulcategoryfilter-active"
      id="fruit3"
      @click="selectfruit()"
    >
      열매 맺는
    </div>
    <div v-else class="dungulcategoryfilter" id="fruit3" @click="selectfruit()">
      열매 맺는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'DungulCategory',

  data: () => {
    return {
      isleafType: false,
      isair: false,
      isflower: false,
      islight: false,
      isanimal: false,
      isfruit: false,
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
  },
  created() {
    this.isleafType = false;
    this.isair = false;
    this.isflower = false;
    this.islight = false;
    this.isanimal = false;
    this.isfruit = false;
  },
};
</script>
<style></style>
