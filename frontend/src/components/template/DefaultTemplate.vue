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
          <transition :name?="route.meta.transition" :key="route.path">
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
