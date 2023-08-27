<template>
  <header>
    <div class="buttons">
      <div class="logo"> <img src="../assets/blog.png" height="55" width="155" alt="">
      </div>
      <div class="navigation">
        <img src="../assets/img.png" height="75" width="75" alt="">
      </div>
    </div>
    <div>
      <div class="userProfile"></div>
    </div>
  </header>
  <div class="content">
    <div class="content__body">
      <div class="left-side">
        <div v-for="item in workData" :key="item">
          <div v-if="item.processed_file != null">
            <div v-if="platform == 'Vk'"  @click="chooseData(item)">
              {{item.processed_file}}
              <img :src="require('../vk/processed_images/' + item.processed_file)" width="300" height="200">
            </div>
            <div v-if="platform == 'Tg'"  @click="chooseData(item)">
              {{item.processed_file}}
              <img :src="require('../tg/processed_images/' + item.processed_file)" width="300" height="200">
            </div>
            <div v-if="platform == 'Yt'"  @click="chooseData(item)">
              {{item.processed_file}}
              <img :src="require('../yt/processed_images/' + item.processed_file)" width="300" height="200">
            </div>
            <div v-if="platform == 'Zn'"  @click="chooseData(item)">
              {{item.processed_file}}
              <img :src="require('../zn/processed_images/' + item.processed_file)" width="300" height="200">
            </div>

            <div @click="chooseData(item)">

            </div>
          </div>
        </div>
      </div>
      <div class="right-side">
        <div class="right-side__content">
          <div v-if="workItem.processed_file != null" style="max-width: 500px; max-height: 300px">
            Метрика: {{ workItem.metrics[0].name }}, Значение: {{ workItem.metrics[0].value }},
            Платформа по мнению нейросети: {{ workItem.predicted_platform }}
            <div v-if="platform == 'Vk'">
              <img :src="require('../vk/processed_images/' + workItem.processed_file)" width="500" height="600">
            </div>
            <div v-if="platform == 'Tg'">
              <img :src="require('../tg/processed_images/' + workItem.processed_file)" width="500" height="600">
            </div>
            <div v-if="platform == 'Yt'">
              <img :src="require('../yt/processed_images/' + workItem.processed_file)" width="500" height="600">
            </div>
            <div v-if="platform == 'Zn'">
              <img :src="require('../zn/processed_images/' + workItem.processed_file)" width="500" height="600">
            </div>
          </div>
        </div>
        <div class="right-side__panel">
          <div class="panel">
            <div class="panel__text"> asd</div>
            <div class="panel__buttons">
              <button class="panel__buttons--red"> Назад </button>
              <button class="panel__buttons--green"> Потвердить </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import tg from "@/tg.json"
import vk from "@/vk.json"
import yt from "@/yt.json"
import zn from "@/zn.json"
export default {
  name: "loadDataResultView.vue",
  data() {
    return {
      tg: tg,
      vk: vk,
      yt: yt,
      zn: zn,
      workData: '',
      workItem: '',
      platform: this.$route.params.platform
    }
  },
  computed: {
    getImgUrl(url) {
      console.log(url)
      return ('../' + url)
    }
  },
  mounted() {
    console.log(tg[0].original_file)
    console.log(this.platform)
    if (this.platform == 'Vk') {
      this.workData = this.vk
    } else if (this.platform == 'Tg') {
      this.workData = this.tg
    } else if (this.platform == 'Yt') {
      this.workData = this.yt
    } else if (this.platform == 'Zn') {
      this.workData = this.zn
    }
  },
  methods: {
    chooseData(item) {
      this.workItem = item
    }
  }
}
</script>

<style scoped>
header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 75px;
  box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
  padding: 0 20px 0 20px;
  min-width: 366px;
}

.buttons {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  text-align: center;
  align-items: center;
}
.content {
  background: #F9F9F9;
  height: 100vh;
}
.content__body {
  padding: 30px 54px 31px 54px;
  display: flex;
  gap: 58px

}
.left-side {
  width: 385px;
  height: calc(100vh - 75px);
  background: #82D9FF;
  border-radius: 20px;
}
.right-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  gap:10px
}
.right-side__content {
  background: white;
  border-radius: 20px;
  height: 100%;
}
.right-side__panel {
  height: 91px;
  background: #82D9FF;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.panel {
  display: flex;
  gap: 20px;
  padding: 5px;
  align-items: baseline;
  width: 100%;
  justify-content: space-between;
}
.panel__text {
  background: white;
  border-radius: 40px;
  padding: 10px 20px;
  width: 100%;
  text-align: left;
}
.panel__buttons {
  display: flex;
  gap:10px;
}
.panel__buttons button{
  border-radius: 35px;
  border: none;
  cursor: pointer;
  color: white;
  padding: 10px;
  height: 100%;
}
.panel__buttons--red {
  background: #FF4F4F;
}
.panel__buttons--green {
  background: #4FF07C;
}
</style>