<template>
    <div class="language">
        <div class="name">{{ lang }}</div>
        <div class="image">
            <img src="@/assets/russian.jpeg" alt="flag" width="20" height="20">
        </div>   
    </div>
    
</template>

<script>
export default {
    name: 'languageSetup',
    data() {
        return {
            lang: "Ru"
        }
    },
}
</script>

<style scoped>
    img {
        border-radius: 5px;
    }
    .language{
        display: flex;
        flex-direction: row;
        align-items: center;
        border-radius: 10px;
        background-color: #F1F1F1;
        padding: 5px;
        gap: 3px;
        cursor: pointer;
    }

</style>