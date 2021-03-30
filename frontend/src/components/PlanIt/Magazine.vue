<template>
  <div class="main_component_magazine">
      <div class="main_component_magazine_title">
        MAGAZINE
      </div>
      <div class="main_component_magazine_sub">
        식물 관련 tip
      </div>
      <div class="main_component_magazine_content">
        <img :src="Magazinebox" />
        <div class="main_component_magazine_content_story">
            <div class="main_component_magazine_content_story_title">
                <div class="main_component_magazine_content_story_title_text">
                    물주기, 내가 뭘 잘못한거지?
                </div>
                <div class="main_component_magazine_content_story_title_back">
                    <img :src="Magazineback" /> 
                </div>
            </div>
            <div class="main_component_magazine_content_story_content">
                <div class="main_component_magazine_content_story_content_img">
                   <img :src="Magazineexample" /> 
                </div>
                <div class="main_component_magazine_content_story_content_text">
                    사실 처음에는 화분을 받으며,<br>
                    약간은 난감함이 교차했다.<br>
                    집에 들여놓는 식물은<br>
                    들이는 족족 죽이는..
                </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
import Magazinebox from '@/assets/img/magazinebox.png';
import Magazineexample from '@/assets/img/magazineexample.png';
import Magazineback from '@/assets/img/magazineback.png';

export default {
  name: "MainMagazine",
  data: () => {
    return {
        Magazinebox: Magazinebox,
        Magazineexample: Magazineexample,
        Magazineback: Magazineback,
    }
  },
  components: {
    
  },
  methods: {
    
  },

  // Mount 이전에, localStorage값이 1인 경우 ( 로그인 안해서 storage에 정보가 들어가지 않은 경우 ) Intro로 돌아가라.
  created() {
    const token = localStorage.getItem('jwt');
    if (token == null) {
      alert('로그인 하고 이용해주세요.');
      this.$router.push({ name: 'Home' }).catch((error) => {
        if (error.name === 'NavigationDuplicated') {
          location.reload();
        }
      });
    }
  },
};
</script>
