<template>
  <div id="searchfilter">
    <!-- 1. 잎이 있는 식물, 공중식물, 덩굴식물,  선인장/다육식물  컴포넌트  -> PlantCategory.vue -->
    <PlantCategory
      @callLeaf="getleafcategory"
      @callSky="getskycategory"
      @callDungul="getdungulcategory"
      @callCactus="getcactuscategory"
      style="margin: 10px 0 0 0"
    />

    <!-- 2. 잎이 있는 식물 선택했을 때 나오는 하위 필터 컴포넌트 -> LeafCategory.vue -->
    <LeafCategory
      class="filters"
      v-if="isLeafcategoryOn"
      @callLeaftype="getleaftype"
      @callAir="getair"
      @callSmell="getsmell"
      @callAnimal="getanimal"
      @callLight="getlight"
      @callFruit="getfruit"
      @callStick="getstick"
      @callBottom="getbottom"
      @callFlower="getflower"
      style="margin: 10px 0 0 0"
    />

    <!-- 3. 공중식물 선택했을 때 나오는 하위 필터 컴포넌트 -> SkyCategory.vue -->
    <SkyCategory
      v-if="isSkycategoryOn"
      @callLeaftype="getleaftype"
      @callAir="getair"
      @callFlower="getflower"
      @callLight="getlight"
      @callAnimal="getanimal"
      @callFruit="getfruit"
      @callSoil="getsoil"
      style="margin: 10px 0 0 0"
    />

    <!-- 4. 덩굴식물 선택했을 때 나오는 하위 필터 컴포넌트 -> DungulCategory.vue -->
    <DungulCategory
      v-if="isDungulcategoryOn"
      @callLeaftype="getleaftype"
      @callAir="getair"
      @callFlower="getflower"
      @callLight="getlight"
      @callAnimal="getanimal"
      @callFruit="getfruit"
      style="margin: 10px 0 0 0"
    />

    <!-- 5. 선인장/다육식물 선택했을 때 나오는 하위 필터 컴포넌트 -> CactusCategory.vue -->
    <CactusCategory
      v-if="isCactuscategoryOn"
      @callLeaftype="getleaftype"
      @callAir="getair"
      @callFlower="getflower"
      @callLight="getlight"
      @callAnimal="getanimal"
      @callFruit="getfruit"
      @callStick="getstick"
      @callNiddle="getniddle"
      @callBottom="getbottom"
      style="margin: 10px 0 0 0"
    />

    <!-- 6. 잎 모양 선택했을 때 나오는 하위 필터 컴포넌트 -> LeafType.vue -->
    <LeafType
      v-if="isLeaftypeOn"
      @call1="getcall1"
      @call2="getcall2"
      @call3="getcall3"
      @call4="getcall4"
      @call5="getcall5"
      @call6="getcall6"
      @call7="getcall7"
      @call8="getcall8"
      @call9="getcall9"
      @call10="getcall10"
      @call11="getcall11"
      @call12="getcall12"
      @call13="getcall13"
      @call14="getcall14"
      @call15="getcall15"
      style="margin: 10px 0 0 0"
    />
  </div>
</template>

<script>
// import axios from "axios";

// import FilterButton from '@/components/Search/FilterButton.vue';

import PlantCategory from '@/components/Search/PlantCategory.vue';

import LeafCategory from '@/components/Search/PlantCategory/LeafCategory.vue';
import SkyCategory from '@/components/Search/PlantCategory/SkyCategory.vue';
import DungulCategory from '@/components/Search/PlantCategory/DungulCategory.vue';
import CactusCategory from '@/components/Search/PlantCategory/CactusCategory.vue';

import LeafType from '@/components/Search/PlantCategory/LeafType/LeafType.vue';

export default {
  name: 'SearchFilter',

  props: ['resetOn'],

  data: () => {
    return {
      idx: 0,
      selectedfilter: 0,
      last_selected: 0,
      result: [],

      isLeafcategoryOn: false,
      isSkycategoryOn: false,
      isDungulcategoryOn: false,
      isCactuscategoryOn: false,
      isLeaftypeOn: false,
    };
  },
  components: {
    // FilterButton,

    PlantCategory,
    LeafCategory,
    SkyCategory,
    DungulCategory,
    CactusCategory,
    LeafType,
  },
  methods: {
    resetfilters() {
      if (this.isLeafcategoryOn) {
        this.isLeafcategoryOn = false;
      }
      if (this.isSkycategoryOn) {
        this.isSkycategoryOn = false;
      }
      if (this.isDungulcategoryOn) {
        this.isDungulcategoryOn = false;
      }
      if (this.isCactuscategoryOn) {
        this.isCactuscategoryOn = false;
      }
      if (this.isLeaftypeOn) {
        this.isLeaftypeOn = false;
      }
    },

    getleafcategory() {
      this.selectedfilter = 1;

      if (this.isLeafcategoryOn) {
        this.isLeafcategoryOn = false;

        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
          this.$emit('sendCategorydelete', this.selectedfilter);
        } else {
          this.$emit('sendCategory', this.selectedfilter);
        }
      } else {
        if (this.isSkycategoryOn) {
          this.isSkycategoryOn = false;
        }
        if (this.isDungulcategoryOn) {
          this.isDungulcategoryOn = false;
        }
        if (this.isCactuscategoryOn) {
          this.isCactuscategoryOn = false;
        }
        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
        }

        this.isLeafcategoryOn = true;
        this.$emit('sendCategorydelete', this.selectedfilter);
      }
    },

    getskycategory() {
      this.selectedfilter = 2;

      if (this.isSkycategoryOn) {
        this.isSkycategoryOn = false;

        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
          this.$emit('sendCategorydelete', this.selectedfilter);
        } else {
          this.$emit('sendCategory', this.selectedfilter);
        }
      } else {
        if (this.isLeafcategoryOn) {
          this.isLeafcategoryOn = false;
        }
        if (this.isDungulcategoryOn) {
          this.isDungulcategoryOn = false;
        }
        if (this.isCactuscategoryOn) {
          this.isCactuscategoryOn = false;
        }
        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
        }
        this.isSkycategoryOn = true;
        this.$emit('sendCategorydelete', this.selectedfilter);
      }
    },

    getdungulcategory() {
      this.selectedfilter = 3;

      if (this.isDungulcategoryOn) {
        this.isDungulcategoryOn = false;

        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
          this.$emit('sendCategorydelete', this.selectedfilter);
        } else {
          this.$emit('sendCategory', this.selectedfilter);
        }
      } else {
        if (this.isSkycategoryOn) {
          this.isSkycategoryOn = false;
        }
        if (this.isLeafcategoryOn) {
          this.isLeafcategoryOn = false;
        }
        if (this.isCactuscategoryOn) {
          this.isCactuscategoryOn = false;
        }
        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
        }
        this.isDungulcategoryOn = true;
        this.$emit('sendCategorydelete', this.selectedfilter);
      }
    },

    getcactuscategory() {
      this.selectedfilter = 4;

      if (this.isCactuscategoryOn) {
        this.isCactuscategoryOn = false;

        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
          this.$emit('sendCategorydelete', this.selectedfilter);
        } else {
          this.$emit('sendCategory', this.selectedfilter);
        }
      } else {
        if (this.isSkycategoryOn) {
          this.isSkycategoryOn = false;
        }
        if (this.isDungulcategoryOn) {
          this.isDungulcategoryOn = false;
        }
        if (this.isLeafcategoryOn) {
          this.isLeafcategoryOn = false;
        }
        if (this.isLeaftypeOn) {
          this.isLeaftypeOn = false;
        }
        this.isCactuscategoryOn = true;
        this.$emit('sendCategorydelete', this.selectedfilter);
      }
    },

    getleaftype() {
      this.selectedfilter = 5;

      if (this.isLeaftypeOn) {
        this.isLeaftypeOn = false;
        this.$emit('sendLeaftypedelete', this.selectedfilter);
      } else {
        this.isLeaftypeOn = true;
        this.$emit('sendLeaftype', this.selectedfilter);
      }
    },

    getair() {
      this.selectedfilter = 6;
      this.$emit('sendAir', this.selectedfilter);
    },

    getsmell() {
      this.selectedfilter = 7;
      this.$emit('sendSmell', this.selectedfilter);
    },

    getanimal() {
      this.selectedfilter = 8;
      this.$emit('sendAnimal', this.selectedfilter);
    },

    getlight() {
      this.selectedfilter = 9;
      this.$emit('sendLight', this.selectedfilter);
    },

    getfruit() {
      this.selectedfilter = 10;
      this.$emit('sendFruit', this.selectedfilter);
    },

    getstick() {
      this.selectedfilter = 11;
      this.$emit('sendAir', this.selectedfilter);
    },

    getbottom() {
      this.selectedfilter = 12;
      this.$emit('sendBottom', this.selectedfilter);
    },

    getflower() {
      this.selectedfilter = 13;
      this.$emit('sendFlower', this.selectedfilter);
    },

    getsoil() {
      this.selectedfilter = 29;
      this.$emit('sendSoil', this.selectedfilter);
    },

    getniddle() {
      this.selectedfilter = 30;
      this.$emit('sendNiddle', this.selectedfilter);
    },

    getcall1() {
      this.selectedfilter = 14;
      this.$emit('send1', this.selectedfilter);
    },

    getcall2() {
      this.selectedfilter = 15;
      this.$emit('send2', this.selectedfilter);
    },

    getcall3() {
      this.selectedfilter = 16;
      this.$emit('send3', this.selectedfilter);
    },

    getcall4() {
      this.selectedfilter = 17;
      this.$emit('send4', this.selectedfilter);
    },

    getcall5() {
      this.selectedfilter = 18;
      this.$emit('send5', this.selectedfilter);
    },

    getcall6() {
      this.selectedfilter = 19;
      this.$emit('send6', this.selectedfilter);
    },

    getcall7() {
      this.selectedfilter = 20;
      this.$emit('send7', this.selectedfilter);
    },

    getcall8() {
      this.selectedfilter = 21;
      this.$emit('send8', this.selectedfilter);
    },

    getcall9() {
      this.selectedfilter = 22;
      this.$emit('send9', this.selectedfilter);
    },

    getcall10() {
      this.selectedfilter = 23;
      this.$emit('send10', this.selectedfilter);
    },

    getcall11() {
      this.selectedfilter = 24;
      this.$emit('send11', this.selectedfilter);
    },

    getcall12() {
      this.selectedfilter = 25;
      this.$emit('send12', this.selectedfilter);
    },

    getcall13() {
      this.selectedfilter = 26;
      this.$emit('send13', this.selectedfilter);
    },

    getcall14() {
      this.selectedfilter = 27;
      this.$emit('send14', this.selectedfilter);
    },

    getcall15() {
      this.selectedfilter = 28;
      this.$emit('send15', this.selectedfilter);
    },
  },

  created() {},
};
</script>
<style></style>
