import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { createPinia } from "pinia";
import vfmPlugin from 'vue-final-modal';
import Toast, { POSITION } from "vue-toastification";
import VueApexCharts from 'vue3-apexcharts';
import urql from '@urql/vue';
import { defaultExchanges, subscriptionExchange } from '@urql/vue';
import { createClient as createWSClient } from 'graphql-ws';

import App from "./App.vue";
import { routes } from "@/router/index";
import { isAuthenticated } from "@/utils/auth-util";

const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (isAuthenticated()) {
      next();
    } else {
      next("/login");
    }
  } else {
    next();
  }
});

const wsClient = createWSClient({
  url: `ws://127.0.0.1:8000/graphql`,
});

app.use(router);
app.use(createPinia());
app.use(Toast, {
  // Setting the global default position
  position: POSITION.BOTTOM_RIGHT,
});
app.use(vfmPlugin);
app.use(VueApexCharts);
app.use(urql, {
  url: '/graphql',
  fetchOptions: () => {
    const token = sessionStorage.getItem("token");
    return token ? { headers: { Authorization: `Bearer ${token}` } } : {};
  },
  exchanges: [
    ...defaultExchanges,
    subscriptionExchange({
      forwardSubscription: (operation) => ({
        subscribe: (sink) => ({
          unsubscribe: wsClient.subscribe(operation, sink),
        }),
      }),
    }),
  ],
});

app.mount("#app");
