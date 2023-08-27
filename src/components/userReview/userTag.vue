<template>
  <div class="user-tag__body">
    {{text}}
  </div>
</template>

<script>
export default {
  name: "userTag",
  props: {
    text: String
  }
}
</script>

<style scoped>
.user-tag__body {
  min-width: 47px;
  min-height: 32px;
  background: #4D64E0;
  color: white;
  border-radius: 20px;
  display: flex;
  max-width: 100px;
  text-align: center;
  align-items: center;
  justify-content: center;
  padding: 3px;
}
</style>