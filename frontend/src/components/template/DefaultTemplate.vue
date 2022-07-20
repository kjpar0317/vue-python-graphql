<template>
  <div :data-theme="store.theme">
    <Header />
    <Sidebar />
    <main>
      <div
        id="main-content"
        data-theme="store.theme"
        class="relative h-full w-full overflow-y-auto border-base-300 bg-base-200 pt-20 text-base-content lg:ml-64 lg:w-[calc(100%-16rem)]"
      >
        <RouterView name="default" v-slot="{ Component, route }">
          <transition :name="route.meta.transition" :key="route.path">
            <Suspense>
              <template #default>
                <component :is="Component" :key="route.path" />
              </template>
              <template #fallback>
                <div><Loading /></div>
              </template>
            </Suspense>
          </transition>
        </RouterView>
      </div>
      <Footer class="lg:pl-64" />
    </main>
  </div>
</template>

<script lang="ts" setup>
import { layoutStore } from "@/store/layout";

import Header from "@/components/layout/common/Header.vue";
import Sidebar from "@/components/layout/common/Sidebar.vue";
import Footer from "@/components/layout/common/Footer.vue";
import Loading from "@/components/layout/common/Loading.vue";

const store = layoutStore();
</script>

<style>
.ag-theme-alpine .ag-header {
  --tw-bg-opacity: 1;
  background-color: hsl(var(--b2, var(--b1)/var(--tw-bg-opacity)));
  border-bottom: solid 1px;
  border-bottom-color: hsl(var(--b3, var(--b2)/var(--tw-bg-opacity)));
}
.ag-theme-alpine .ag-row {
  --tw-bg-opacity: 1;
  background-color: hsl(var(--b1)/var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: hsl(var(--bc)/var(--tw-text-opacity));
  border-width: 1px;
  border-color: hsl(var(--b3, var(--b1)/var(--tw-bg-opacity)));
  border-bottom-style: solid;
}
.ag-theme-alpine .ag-row-odd {
  --tw-bg-opacity: 1;
  background-color: hsl(var(--b2)/var(--tw-bg-opacity));
}
.ag-theme-alpine .ag-row-hover {
  --tw-bg-opacity: 1;
  background-color: hsl(var(--p)/var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: hsl(var(--pc)/var(--tw-text-opacity));
}
.ag-header-group-cell-label, .ag-header-cell-label {
  display: flex;
  flex: 1 1 auto;
  overflow: hidden;
  align-items: center;
  text-overflow: ellipsis;
  align-self: stretch;
  --tw-text-opacity: 1;
  color: hsl(var(--bc)/var(--tw-text-opacity));
}
.ag-center-col-viewport {
  width: 100%;
  overflow-x: auto;
  background-color: hsl(var(--b1)/var(--tw-bg-opacity));
}
.ag-theme-alpine .ag-paging-panel {
  background-color: hsl(var(--b2, var(--b1)/var(--tw-bg-opacity)));
  border-top: 1px solid;
  border-top-color: hsl(var(--b2, var(--b1)/var(--tw-bg-opacity)));
  --tw-text-opacity: 1;
  color: hsl(var(--bc)/var(--tw-text-opacity));
}
</style>