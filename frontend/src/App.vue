<script setup>
import { ref } from 'vue';
import { useMiniApp, usePopup } from 'vue-tg';
import { useFetch } from "@vueuse/core";

const miniApp = useMiniApp();
// { initData, initDataUnsafe, sendData, ready, close }
const popup = usePopup();
const user = miniApp.initDataUnsafe.user || {};

const { data, error } = useFetch('/api/user', {
  mode: 'cors',
  method: 'GET',
  headers:{'Content-Type': 'application/json', 'initData': miniApp.initData},
  credentials: 'include'
});


if (error.value) {
  miniApp.close();
} else {
  miniApp.ready();
}

const test = ref('');

async function buttonTest() {
  await popup.showAlert('test')
  test.value = 'Value';
}

</script>

<template>
  <div>
    <h1>Telegram Mini App</h1>
    <p v-if="user">User ID: {{ user?.id }}</p>
    <p v-if="error">Error: {{ error }}</p>
    <p v-if="test">Test: {{ test }}</p>
    <button class="tg-button" @click="buttonTest">Test</button>
    <!-- <Alert message="Test!" @close="Test" /> -->
  </div>
</template>

<style scoped>
/* :root {
  --tg-theme-bg-color: var(--tg-theme-bg-color, #ffffff);
  --tg-theme-text-color: var(--tg-theme-text-color, #000000);
  --tg-theme-hint-color: var(--tg-theme-hint-color, #707579);
  --tg-theme-link-color: var(--tg-theme-link-color, #3390ec);
  --tg-theme-button-color: var(--tg-theme-button-color, #3390ec);
  --tg-theme-button-text-color: var(--tg-theme-button-text-color, #ffffff);
  --tg-theme-secondary-bg-color: var(--tg-theme-secondary-bg-color, #f4f4f5);
} */

body div {
  background-color: var(--tg-theme-bg-color);
  color: var(--tg-theme-text-color);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.tg-button {
  background-color: var(--tg-theme-button-color);
  color: var(--tg-theme-button-text-color);
  border: none;
  border-radius: 10px;
  padding: 10px 16px;
  font-size: 16px;
  cursor: pointer;
}

.tg-button:active {
  opacity: 0.8;
}
</style>
