<template>
  <header>
    <div class="buttons">
      <div class="logo"><img src="../assets/blog.png" height="55" width="155" alt="">
      </div>
      <div class="navigation">
        <img src="../assets/img.png" height="75" width="75" alt="">
      </div>
    </div>
    <div>
      <div class="userProfile"></div>
    </div>
  </header>
  <div class="body">
    <div class="leftPillar">
      <div class="reviewButton">
        <button>ОтчётИИк</button>
      </div>
      <div class="filter">
        <div>
          Выбор платформы:
          <div>
            <select v-model="platform">
              <option>Vk</option>
              <option>Tg</option>
              <option>Yt</option>
              <option>Zn</option>
            </select>
          </div>
        </div>
        <div class="uploadButton">
        </div>
      </div>
      <div class="checkButton">
          <button  v-if="platform != ''" @click="this.$router.push({name:'checkData', params: {platform: this.platform}})">Проверить все скиншоты</button>
      </div>
    </div>
    <div class="contentBody">
      <user-preview v-for="item in users" :key="item" :user="item" :id="item.id"></user-preview>
    </div>
  </div>
</template>

<script>
import UserPreview from "@/components/userReview/userPreview";
import users from "../users.json"
export default {

  name: "userReviewView.vue",
  components: {UserPreview},
  data() {
    return {
      users,
      platform: '',
    }
  },
  methods:{
    toCheckData() {
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

.userProfile {
  gap: 5px;
  display: flex;
  align-content: baseline;
}

.userProfile p {
  text-overflow: clip;
}

.body {
  display: flex;

}

.leftPillar {
  display: flex;
  flex-direction: column;
  border-right: #545454 solid 1px;
  width: 195px;
  justify-content: space-between;
  height: calc(100vh - 75px);
  padding: 5px 5px 5px 5px;
}

.contentBody {
  display: flex;
  padding: 10px;
  gap: 10px;
  flex-wrap: wrap;
}

.filter {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
  text-align: left;
  flex-wrap: nowrap;
}

.filter input {
  border-radius: 24px;
  border: #3461FF solid 1px;
  height: 37px;
}

.filter button {
  border-radius: 20px;
  border: none;
  background: #3461FF;
  color: white;
  width: 155px;
  height: 49px;
  font-size: 16px;
}

.reviewButton {
  border-bottom: #545454 solid 1px;
  padding-bottom: 10px;
  padding-top: 10px;
}

.checkButton {
  padding: 10px 0 10px 0;
  border-top: #545454 solid 1px;
  border-bottom: #545454 solid 1px;
}

.checkButton button {
  border-radius: 20px;
  border: none;
  background: #3461FF;
  color: white;
  width: 155px;
  height: 49px;
  font-size: 16px;
  cursor: pointer;
}

.reviewButton button {
  border-radius: 30px;
  border: none;
  background: #4FF07C;
  color: black;
  font-weight: normal;
  width: 155px;
  height: 49px;
  font-size: 16px;
}

</style>