<template>
  <div id="skycategory">
    <div class="dashedline"></div>
    <div
      v-if="isleafType"
      class="skycategoryfilter-active"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-else
      class="skycategoryfilter"
      id="leaftype"
      @click="selectleaftype()"
    >
      잎 모양
    </div>
    <div
      v-if="isair"
      class="skycategoryfilter-active"
      id="air2"
      @click="selectair()"
    >
      공기정화
    </div>
    <div v-else class="skycategoryfilter" id="air2" @click="selectair()">
      공기정화
    </div>
    <div
      v-if="isflower"
      class="skycategoryfilter-active"
      id="flower2"
      @click="selectflower()"
    >
      꽃 피는
    </div>
    <div v-else class="skycategoryfilter" id="flower2" @click="selectflower()">
      꽃 피는
    </div>
    <div
      v-if="islight"
      class="skycategoryfilter-active"
      id="light2"
      @click="selectlight()"
    >
      빛이 적어도 되는
    </div>
    <div v-else class="skycategoryfilter" id="light2" @click="selectlight()">
      빛이 적어도 되는
    </div>
    <div
      v-if="isanimal"
      class="skycategoryfilter-active"
      id="animal2"
      @click="selectanimal()"
    >
      반려동물 안전한
    </div>
    <div v-else class="skycategoryfilter" id="animal2" @click="selectanimal()">
      반려동물 안전한
    </div>
    <div
      v-if="isfruit"
      class="skycategoryfilter-active"
      id="fruit2"
      @click="selectfruit()"
    >
      열매 맺는
    </div>
    <div v-else class="skycategoryfilter" id="fruit2" @click="selectfruit()">
      열매 맺는
    </div>
    <div
      v-if="issoil"
      class="skycategoryfilter-active"
      id="soil2"
      @click="selectsoil()"
    >
      흙이 필요 없는
    </div>
    <div v-else class="skycategoryfilter" id="soil2" @click="selectsoil()">
      흙이 필요 없는
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'SkyCategory',

  data: () => {
    return {
      isleafType: false,
      isair: false,
      isflower: false,
      islight: false,
      isanimal: false,
      isfruit: false,
      issoil: false,
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

    selectsoil() {
      this.$emit('callSoil');
      this.issoil = !this.issoil;
    },
  },
  created() {
    this.isleafType = false;
    this.isair = false;
    this.isflower = false;
    this.islight = false;
    this.isanimal = false;
    this.isfruit = false;
    this.issoil = false;
  },
};
</script>
<style></style>
