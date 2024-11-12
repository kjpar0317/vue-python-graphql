<template>
  <router-view></router-view>
  <ModalsContainer />
</template>

<script setup lang="ts">
import { ModalsContainer } from "vue-final-modal";

import "windi.css";
// import "ag-grid-community/dist/styles/ag-grid.css";
// import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import "vue-toastification/dist/index.css";
import "vue-final-modal/style.css";

// import 'virtual:windi.css'
// import 'virtual:windi-devtools'
import "./index.css";
import "@/assets/css/aggrid.css";
</script>
