<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
const count_miss = ref(0)
const count_heavy = ref(0)
const count_model = ref(0)

</script>

<template>
  <div class="card">
    <!-- <div >
      <p>测试:{{ count_model }}</p>
      <button type="button"      :click="count_model++">+</button>
      <button :click="count_model--">-</button>

    </div>
   -->
    
    <button type="button" @click="count++">错 {{ count }}</button>
    <button type="button" @click="count_miss++">漏 {{ count_miss }}</button>
    <button type="button" @click="count_heavy++">多 {{ count_heavy }}</button>
  </div>
    
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
