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
      <div  class="userProfile"> Кирилл Резников <img src="../assets/quitIco.png" height="20" width="20" alt=""></div>
    </div>
  </header>
  <div class="load-data__body">
    <div>
      Выбор платформы:
      <select v-model="platform">
        <option>Telegram</option>
        <option>Vk</option>
        <option>YouTube</option>
        <option>Ok</option>
      </select>
    </div>

    <div class="load-window-container">
      <div class="load-window-container__body" @dragover.prevent="onDragOver" @dragleave.prevent="onDragLeave" @drop.prevent="onDrop">
        <div v-if="!isDragging" class="load-window-container__body__text">
          Перетащите одини или несколько файлов в данную область
          <br/>
          Или
          <br/>
          <input name="file" type="file" class="file" ref="fileInput" multiple @change="onFileSelect"/>
        </div>
        <div v-else
             class="load-window-container__body__text"> Сбросьте картинки вот сюда

        </div>
        <div class="load-window-container__body__images">
          <div class="load-window-container__body_images_image" v-for="(image, index) in images" :key="index">
            <span class="load-window-container__body_images_image--delete" @click="deleteImage(index)">
            &times;
            </span>
            <img :src="image.url" alt="" />
          </div>
        </div>
      </div>
    </div>
    <div class="button">
      <button v-if="((images.length > 0) && platform !=='')"> Продолжить </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "loadDataView.vue",
  data() {
    return {
      platform: "",
      images: [],
      isDragging: false
    }
  },
  methods: {
    selectFiles(){
      this.$refs.fileInput.click();
    },
    onDragOver(event){
      event.preventDefault();
      this.isDragging = true;
      event.dataTransfer.dropEffect = "copy"
    },
    onDragLeave(event){
      event.preventDefault();
      this.isDragging = false;
    },
    onDrop(event){
      event.preventDefault();
      this.isDragging = false;
      const files = event.dataTransfer.files;
      for (let i = 0; i < files.length; i++){
        if(files[i].type.split('/')[0] !== 'image') continue;
        if(!this.images.some((e) => e.name ===files[i].name)) {
          this.images.push({name: files[i].name, url:URL.createObjectURL(files[i])})
        }
      }
    },
    deleteImage(index){
      this.images.splice(index,1)
    },
    onFileSelect(event){
      const files = event.target.files;
      for (let i = 0; i < files.length; i++){
        if(files[i].type.split('/')[0] !== 'image') continue;
        if(!this.images.some((e) => e.name ===files[i].name)) {
          this.images.push({name: files[i].name, url:URL.createObjectURL(files[i])})
        }
      }
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

.load-data__body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: calc(100vh - 75px);
}

.load-window-container{
  display: flex;
  justify-content: center;
}
.load-window-container__body {
  border: #00C2FF solid 1px;
  justify-content: center;
  height: 595px;
  width: 920px;
  display: flex;
  flex-direction: column;
  border-radius: 40px;
  color: #767676;
}

.load-window-container__body__text {
  white-space: pre-line;
}
.load-window-container__body__text button {
  border: #767676 solid 1px;
  background: none;
}
.load-window-container__body__images {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  border-radius: 20px;
  padding: 5px;
}
.load-window-container__body_images_image {
}
.load-window-container__body_images_image img{
  max-height: 100px;
  max-width: 200px;
  border-radius: 20px;
}
.load-window-container__body_images_image span{
  position: absolute;
  font-size: 20px;
  cursor: pointer;
}
.load-window-container__body_images_image--delete {
  z-index: 10;
}
.load-data__body .button{
  padding: 5px;
}
.load-data__body .button button {
  height: 100px;
  width: 300px;
  border-radius: 20px;
  border: none;
  background: #00C2FF;
}
</style>