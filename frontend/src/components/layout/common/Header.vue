<template>
  <nav class="fixed z-30 w-full border-b bg-neutral text-neutral-content">
    <div class="px-3 py-3 lg:px-5 lg:pl-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center justify-start">
          <label class="btn swap btn-circle swap-rotate lg:hidden">
            <!-- this hidden checkbox controls the state -->
            <input type="checkbox" @click="handleClick" class="hidden" />

            <!-- hamburger icon -->
            <svg
              class="fill-current swap-off"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 512 512"
            >
              <path
                d="M64,384H448V341.33H64Zm0-106.67H448V234.67H64ZM64,128v42.67H448V128Z"
              />
            </svg>

            <!-- close icon -->
            <svg
              class="fill-current swap-on"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 512 512"
            >
              <polygon
                points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49"
              />
            </svg>
          </label>
          <a
            href="/"
            class="flex items-center text-base font-bold md:text-xl lg:ml-2.5"
          >
            <img
              src="https://demo.themesberg.com/windster/images/logo.svg"
              class="h-6 mr-2"
              alt="Windster Logo"
            />
            <span class="self-center whitespace-nowrap">Test Page</span>
          </a>
          <form action="#" method="GET" class="hidden lg:block lg:pl-32">
            <label htmlFor="topbar-search" class="sr-only"> Search </label>
            <div class="relative mt-1 lg:w-64">
              <div
                class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
              >
                <svg
                  class="w-5 h-5 text-gray-500"
                  fill="currentColor"
                  view-box="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
              </div>
              <input
                type="text"
                name="email"
                id="topbar-search"
                :class="store.sidebar
                    ? 'block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 pl-10 text-gray-900 focus:border-cyan-600 focus:ring-cyan-600 sm:text-sm'
                    : 'hidden'"
                placeholder="Search"
              />
            </div>
          </form>
        </div>
        <div class="flex items-center">
          <button
            id="toggleSidebarMobileSearch"
            type="button"
            class="p-2 text-gray-500 rounded-lg hover:bg-gray-100 hover:text-gray-900 lg:hidden"
          >
            <span class="sr-only">Search</span>
            <svg
              class="w-6 h-6"
              fill="currentColor"
              view-box="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </button>
          <div class="items-center hidden lg:flex">
            <div title="Change Theme" class="dropdown dropdown-end">
              <div tabindex="0" class="gap-1 normal-case btn btn-ghost">
                <svg
                  width="20"
                  height="20"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="inline-block w-5 h-5 stroke-current md:h-6 md:w-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
                  ></path>
                </svg>
                <span class="hidden md:inline">Theme</span>
                <svg
                  width="12px"
                  height="12px"
                  class="hidden w-3 h-3 ml-1 fill-current opacity-60 sm:inline-block"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 2048 2048"
                >
                  <path
                    d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"
                  ></path>
                </svg>
              </div>
              <div
                class="dropdown-content rounded-t-box rounded-b-box top-px mt-16 h-[70vh] max-h-96 w-52 overflow-y-auto shadow-2xl"
              >
                <div
                  v-if="themes.length"
                  class="grid grid-cols-1 gap-3 p-3"
                  tabindex="0"
                >
                  <div v-for="(theme, index) in themes" :key="index">
                    <div
                      class="overflow-hidden rounded-lg outline outline-2 outline-offset-2 outline-base-content"
                      :data-set-theme="theme"
                      data-act-className="outline"
                      @click="handleThemeClick(theme)"
                    >
                      <div
                        :data-theme="theme"
                        class="w-full font-sans cursor-pointer bg-base-100 text-base-content"
                      >
                        <div class="grid grid-cols-5 grid-rows-3">
                          <div
                            class="flex col-span-5 row-span-3 row-start-1 gap-1 px-4 py-3"
                          >
                            <div class="flex-grow text-sm font-bold">
                              {{ theme }}
                            </div>
                            <div class="flex flex-wrap flex-shrink-0 gap-1">
                              <div class="w-2 rounded bg-primary"></div>
                              <div class="w-2 rounded bg-secondary"></div>
                              <div class="w-2 rounded bg-accent"></div>
                              <div class="w-2 rounded bg-neutral"></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="-mb-1 btn btn-ghost">
              <div
                className="tooltip tooltip-bottom"
                data-tip="Log out"
                @click="handleLogOut"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  view-box="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { useRouter } from "vue-router";

import { layoutStore } from "@/store/layout";

const router = useRouter();
const store = layoutStore();
const themes = [
  "light",
  "dark",
  "cupcake",
  "bumblebee",
  "emerald",
  "corporate",
  "synthwave",
  "retro",
  "cyberpunk",
  "valentine",
  "halloween",
  "garden",
  "forest",
  "aqua",
  "lofi",
  "pastel",
  "fantasy",
  "wireframe",
  "black",
  "luxury",
  "dracula",
  "cmyk",
  "autumn",
  "business",
  "acid",
  "lemonade",
  "night",
  "coffee",
  "winter",
];

function handleClick() {
  store.setSidebar(!store.sidebar);
}
function handleThemeClick(theme: string) {
  store.setTheme(theme);
}
function handleLogOut() {
  sessionStorage.removeItem("token");
  sessionStorage.removeItem("email");

  router.push("/login");
}
</script>
