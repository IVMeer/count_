<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
const count_miss = ref(0)
const count_heavy = ref(0)
const test = ref(0)


</script>

<template>
  <div class="type3">
      <div class="button-row">
        <button type="button" @click="count++">+</button>
        <button type="button" @click="count_miss++">+</button>
        <button type="button" @click="count_heavy++">+</button>
      </div>
      <div class="button-row">
        <button type="button" @click="count++">错 {{ count }}</button>
        <button type="button" @click="count_miss++">漏 {{ count_miss}}</button>
        <button type="button" @click="count_heavy++">多 {{ count_heavy }}</button>
      </div>
      <div class="button-row">
        <button type="button" @click="count--">-</button>
        <button type="button" @click="count_miss--">-</button>
        <button type="button" @click="count_heavy--">-</button>
        <!-- <button type="button" @click="count = 0;count_miss = 0; count_heavy = 0">重置</button> -->
      </div>
      <div class="right-align">
        <!-- 重置按钮 -->
         <button type="button" @click="count = 0;count_miss = 0; count_heavy = 0">RESET</button>
      </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
.type3{
  display: flex;               /* 展示方式flex */
  flex-direction: column;      /* 垂直排列每一行 */
  gap: 1px                     /* 每一行之间的间距 */
}
.button-row {
  display: flex;                /* 展示方式flex */
  justify-content: flex-start;  /* 按钮紧密排列 */
  margin: 0;                    /* 移除默认的外边距 */
}

.button-row button{
  /* flex-grow: 0.5;           */
  min-width: 100px; 
  text-align: center;     /* 按钮文本居中 */
  /* margin: 0;               */
}
.right-align {
  text-align: right;
}
</style>
