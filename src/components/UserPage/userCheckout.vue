<template>
  <div class="checkout">
    <div class="data">
      <div v-if="user.platform == 'Vk'">
        <div v-for="item in vk" :key="item">
          <div v-if="item.id == user.id">
            <div v-if="item.predicted_platform">
              Файл: {{ item.original_file }},
              Платформа по мнению нейросети: {{ item.predicted_platform }},
              Метрика: {{ item.metrics[0].name }}, Значение: {{ item.metrics[0].value }}
            </div>
            <div v-else>
              Файл: {{ item.original_file }} не распознан
            </div>
          </div>
        </div>
      </div>
      <div v-if="user.platform == 'Tg'">
        <div v-for="item in tg" :key="item">
          <div v-if="item.id == user.id">
            <div v-if="item.predicted_platform">
              Файл: {{ item.original_file }},
              Платформа по мнению нейросети: {{ item.predicted_platform }},
              Метрика: {{ item.metrics[0].name }}, Значение: {{ item.metrics[0].value }}
            </div>
            <div v-else>
              Файл: {{ item.original_file }} не распознан
            </div>
          </div>
        </div>
      </div>
      <div v-if="user.platform == 'Yt'">
        <div v-for="item in yt" :key="item">
          <div v-if="item.id == user.id">
            <div v-if="item.predicted_platform">
              Файл: {{ item.original_file }},
              Платформа по мнению нейросети: {{ item.predicted_platform }},
              Метрика: {{ item.metrics[0].name }}, Значение: {{ item.metrics[0].value }}
            </div>
            <div v-else>
              Файл: {{ item.original_file }} не распознан
            </div>
          </div>
        </div>
      </div>
      <div v-if="user.platform == 'Zn'">
        <div v-for="item in zn" :key="item">
          <div v-if="item.id == user.id">
            <div v-if="item.predicted_platform">
              Файл: {{ item.original_file }},
              Платформа по мнению нейросети: {{ item.predicted_platform }},
              Метрика: {{ item.metrics[0].name }}, Значение: {{ item.metrics[0].value }}
            </div>
            <div v-else>
              Файл: {{ item.original_file }} не распознан
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

let userMetrics = []

export default {
  name: "userCheckout.vue",
  data() {
    return {
      tg: tg,
      vk: vk,
      yt: yt,
      zn: zn,
      userMetrics: userMetrics,
      userMetricsValue: []
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
  mounted() {
  },
  computed: {}
}

</script>

<style scoped>
.checkout {
  border-radius: 40px;
  display: flex;
  justify-content: space-between;
  background: #EBE8FF;
  padding: 20px 10px 20px 10px;
}

.buttons {
  display: flex;
  gap: 30px;

}

.data {
  display: flex;
  gap: 10px;
  justify-content: space-between;
  min-width: 1200px;
}
</style>
