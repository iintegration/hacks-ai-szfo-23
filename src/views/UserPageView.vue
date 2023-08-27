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
      <div  class="userProfile"></div>
    </div>
  </header>
  <div class="contentBody">
    <div class="userInfoTable">
      <div>
        <img :src="user.avatar" width="770" height="351" alt="userChanelImage"  class="userImage">
      </div>
      <div class="userNameAndDesk">
        <div class="userName">
          {{ user.name }}
        </div>
        <div class="userDesc">
          {{ user.description }}
        </div>
      </div>
      <div>
        <div>
            <div class="userStats">
              {{user.platform}}
            </div>
        </div>
        <div>
          <button class="checkButton">
            Отчёт
          </button>
          <button class="uploadButton">
            Загрузить
          </button>
        </div>
      </div>
    </div>
    <div class="checkout">
      <UserCheckout :user="user">
      </UserCheckout>
    </div>



  </div>
</template>

<script>
import UserCheckout from '../components/UserPage/userCheckout'
import users from '../users.json'
export default {
  name: "UserPage",
  components: {UserCheckout},
  props: {

  },
  data(){
    return{
      user: users[this.$route.params.id]
    }
  },
  computed: {
    getUser() {
      return users[this.$route.params.id]
    }
  },
  mounted() {
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

.contentBody {
  margin: 16px 32px 0 32px;

}

.userInfoTable {
  max-height: 351px;
  padding: 31px 72px;
  display: flex;
  background: #EBE8FF;
  border-radius: 30px;
  box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2);
  justify-content: space-evenly;
}
.userName {
  background: white;
  height: 97px;
  width: 543px;
  border-radius: 10px;
  margin-left: 42px;
  font-size: 42px;
  text-align: left;
}

.userImage {
  border-radius: 20px;
}
.userDesc {
  background: white;
  height: 237px;
  width: 543px;
  border-radius: 10px;
  margin-left: 42px;
  margin-top: 17px;
  font-size: 32px;
  text-align: left;
}
.userStats {
  background: white;
  width: 330px;
  margin-left: 24px;
  height: 271px;
  border-radius: 18px;
}
.checkButton {
  border-radius: 20px;
  margin-left: 20px;
  width: 149px;
  height: 60px;
  margin-top: 20px;
  border: none;
  background: #4FF07C;
}
.uploadButton {
  border-radius: 20px;
  margin-left: 10px;
  width: 149px;
  height: 60px;
  margin-top: 20px;
  border: none;
  background: #82D9FF;
}
.checkout {
  margin-top: 10px;
}
</style>