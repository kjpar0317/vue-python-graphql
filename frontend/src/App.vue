<template>
  <router-view></router-view>
</template>

<script setup lang="ts">
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css"; // 테마에 맞게 수정
import "vue-toastification/dist/index.css";

import "./index.css";
import "@/assets/css/aggrid.css";
</script>
