<template>
  <div id="plantcategory">
    <div
      v-if="isleaf"
      class="plantcategoryfilter-active"
      id="leaf"
      @click="selectleaf()"
    >
      잎이 있는 식물
    </div>
    <div v-else class="plantcategoryfilter" id="leaf" @click="selectleaf()">
      잎이 있는 식물
    </div>
    <div
      v-if="issky"
      class="plantcategoryfilter-active"
      id="sky"
      @click="selectsky()"
    >
      공중식물
    </div>
    <div v-else class="plantcategoryfilter" id="sky" @click="selectsky()">
      공중식물
    </div>
    <div
      v-if="isdungul"
      class="plantcategoryfilter-active"
      id="dungul"
      @click="selectdungul()"
    >
      덩굴식물
    </div>
    <div v-else class="plantcategoryfilter" id="dungul" @click="selectdungul()">
      덩굴식물
    </div>
    <div
      v-if="iscactus"
      class="plantcategoryfilter-active"
      id="cactus"
      @click="selectcactus()"
    >
      선인장/다육식물
    </div>
    <div v-else class="plantcategoryfilter" id="cactus" @click="selectcactus()">
      선인장/다육식물
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'PlantCategory',

  data: () => {
    return {
      selectleafbutton: false,
      isleaf: false,
      issky: false,
      isdungul: false,
      iscactus: false,
    };
  },
  components: {},
  methods: {
    selectleaf() {
      this.$emit('callLeaf');
      this.isleaf = !this.isleaf;
      this.issky = false;
      this.isdungul = false;
      this.iscactus = false;
    },

    selectsky() {
      this.$emit('callSky');
      this.issky = !this.issky;
      this.isleaf = false;
      this.isdungul = false;
      this.iscactus = false;
    },

    selectdungul() {
      this.$emit('callDungul');
      this.isdungul = !this.isdungul;
      this.isleaf = false;
      this.issky = false;
      this.iscactus = false;
    },

    selectcactus() {
      this.$emit('callCactus');
      this.iscactus = !this.iscactus;
      this.isleaf = false;
      this.issky = false;
      this.isdungul = false;
    },
  },
  created() {
    this.isleaf = false;
    this.issky = false;
    this.isdungul = false;
    this.iscactus = false;
  },
};
</script>
<style></style>
