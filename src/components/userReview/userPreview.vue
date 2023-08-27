<template>
  <div class="user-preview" @click="toUserPage()">
    <div class="user-preview__title">
      {{ user.name }}
    </div>
    <div class="user-preview__body">
      <img :src="user.avatar" alt="" width="350" height="235">
    </div>
    <div class="user-preview__tags">
      <user-tag :text="user.platform"></user-tag>
    </div>
  </div>
</template>

<script>
import UserTag from "@/components/userReview/userTag";
import router from "@/router";

export default {
  name: "userPreview",
  components: {UserTag},
  data() {
    return {
      bgColor: ''
    }
  },
  props: {
    user: {
      id: Number,
      name: String,
      avatar: String,
      platform: String,
    }
  },
  methods: {
    toUserPage() {
      router.push({name: "user", params: {id: this.user.id}})
    },
  },
  mounted() {
    if (this.user.platform == "Vk")
    {
      this.bgColor = '#5181B8'
    } else if (this.user.platform == "Tg") {
      this.bgColor = '#229ED9'
    } else if (this.user.platform == "Yt") {
      this.bgColor = '#DA271E'
    } else if (this.user.platform == "Zn") {
      this.bgColor = '#0D1522'
    }
  }
}
</script>

<style scoped>
  .user-preview{
    display: flex;
    flex-direction: column;
    height: 325px;
    width: 350px;
    background: v-bind(bgColor);
    border-radius: 20px;

  }
  .user-previewTg{
    display: flex;
    flex-direction: column;
    height: 325px;
    width: 350px;
    background: #229ED9;
    border-radius: 20px;

  }
  .user-previewZn{
    display: flex;
    flex-direction: column;
    height: 325px;
    width: 350px;
    background: #0D1522;
    border-radius: 20px;

  }
  .user-previewYt{
    display: flex;
    flex-direction: column;
    height: 325px;
    width: 350px;
    background: #DA271E;
    border-radius: 20px;

  }
  .user-preview__title {
    height: 40px;
    color: white;
    display: flex;
    justify-content: center;
    margin-top: 5px;
    font-size: 24px;
  }
  .user-preview__body {
    height: 235px;
    width: 348px;
    cursor: pointer;
  }
  .user-preview__tags {
    padding: 5px 5px;
    display: flex;
    justify-content: flex-end;
  }
</style>