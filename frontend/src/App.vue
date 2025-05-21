<script setup>
import { useWebApp } from 'vue-tg'
import { Alert } from 'vue-tg'
import { useFetch } from "@vueuse/core";

const { initData, initDataUnsafe, sendData, ready, close } = useWebApp();
const user = initDataUnsafe.user || {};

const { data, error } = useFetch('/api/user', {
  mode: 'cors',
  method: 'GET',
  headers:{'Content-Type': 'application/json', 'initData': initData},
  credentials: 'include'
});


if (error.value) {
  close();
} else {
  ready();
  sendData('test');
}


</script>

<template>
  <div>
    <h1>Telegram Mini App</h1>
    <p v-if="user">User ID: {{ user?.id }}</p>
    <p v-if="error">Error: {{ error }}</p>
    <button class="tg-button" @click="sendData('test button')">Close</button>
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
