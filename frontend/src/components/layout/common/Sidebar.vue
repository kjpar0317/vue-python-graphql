<template>
  <div class="h-0 drawer">
    <aside
      id="sidebar"
      aria-label="Sidebar"
      :class="store.sidebar
          ? 'apply_sidebar_aside transition-width drawer-side hidden'
          : 'apply_sidebar_aside transition-width drawer-side flex'"
    >
      <div
        class="relative flex flex-col flex-1 min-h-0 pt-0 border-r border-base-300 bg-base-200 text-base-content"
      >
        <div class="flex flex-col flex-1 pt-5 pb-4 overflow-y-auto">
          <div class="flex-1 px-3 space-y-1 divide-y">
            <ul class="pb-2 space-y-2 menu menu-compact">
              <li>
                <form action="#" method="GET" class="lg:hidden">
                  <label html-for="mobile-search" class="sr-only">
                    Search
                  </label>
                  <div class="relative">
                    <div
                      class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
                    >
                      <svg
                        class="w-5 h-5"
                        fill="currentColor"
                        view-box="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
                        ></path>
                      </svg>
                    </div>
                    <input
                      type="text"
                      name="email"
                      id="mobile-search"
                      class="focus:primary focus:primary-focus block w-full rounded-lg border p-2.5 pl-10 text-sm"
                      placeholder="Search"
                    />
                  </div>
                </form>
              </li>
              <li v-for="(menu, index) in sidebars" :key="index">
                <router-link
                  :to="menu.path"
                  @click.native="handleSidebar"
                  :class="route.path == menu.path ? 'flex items-center p-2 text-base font-normal rounded-lg group active' : 'flex items-center p-2 text-base font-normal rounded-lg group' "
                >
                  <svg
                    class="w-6 h-6 transition duration-75"
                    fill="currentColor"
                    view-box="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                    v-html="menu.svgPath"
                  />
                  <span v-if="!menu.hint" className="flex-1">{{
                    menu.title
                  }}</span>
                  <span v-if="menu.hint" className="flex-1">{{
                    menu.title
                  }}</span>
                  <span
                    v-if="menu.hint"
                    className="flex-none lowercase badge badge-sm"
                  >
                    {{ menu.hint }}
                  </span>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </aside>
    <div
      class="fixed inset-0 z-10 hidden bg-gray-900 opacity-50"
      id="sidebarBackdrop"
    ></div>
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router';

import { layoutStore } from "@/store/layout";

const route = useRoute();
const store = layoutStore();
const sidebars = [
  {
    title: "Dashboard",
    path: "/",
    svgPath:
      '<path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path><path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path>',
    hint: null,
  },
  {
    title: "GraphQL Query",
    path: "/about",
    svgPath:
      '<path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>',
    hint: "Test",
  },
  {
    title: "GraphQL Subscription",
    path: "/subscription",
    svgPath:
      '<path fillRule="evenodd" d="M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z" clipRule="evenodd" />',
    hint: "Test",
  },
];

function handleSidebar() {
  // store.setSidebar(false);
}
</script>

<style scoped>
.apply_sidebar_aside {
  @apply fixed top-0 left-0 z-20 h-full w-64 flex-shrink-0 flex-col pt-16 duration-75 lg:flex;
}
</style>
