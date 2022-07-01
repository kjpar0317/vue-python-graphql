<template>
  <div
    class="relative flex items-center min-h-screen p-5 overflow-hidden bg-blue-100 min-w-screen lg:p-20"
  >
    <div
      class="relative items-center flex-1 min-w-full min-h-full p-10 text-center text-gray-800 bg-white shadow-xl rounded-3xl md:flex md:text-left lg:p-20"
    >
      <div class="w-full md:w-1/2">
        <div class="mb-10 lg:mb-20">
          <img src="https://flipstore.withun.link/identity/Group%201.svg" />
        </div>
        <div class="mb-10 font-light text-gray-600 md:mb-20">
          <h1
            class="mb-10 text-3xl font-black text-indigo-700 uppercase lg:text-5xl"
          >
            입력하신 페이지는
            <br />
            존재하지 않습니다.
          </h1>
          <p>찾고 계시는 페이지가 접속이 안되는 경우에는</p>
          <p>관리자에게 연락하여 주세요.</p>
        </div>
        <div class="mb-20 md:mb-0">
          <button
            class="text-lg font-light text-blue-500 transition-all transform outline-none hover:scale-110 hover:text-blue-600 focus:outline-none"
            @click="handleClick"
          >
            홈으로 돌아가기
          </button>
        </div>
      </div>
      <div class="w-full text-center md:w-1/2">
        <img
          src="https://flipstore.withun.link/images/404.png"
          class="w-64 h-64"
        />
      </div>
    </div>
    <div
      class="absolute w-64 transform -rotate-45 bg-blue-200 rounded-full pointer-events-none -top-64 right-20 h-96 bg-opacity-30 md:-top-96 md:right-32 md:h-full md:w-96"
    ></div>
    <div
      class="absolute h-full transform -rotate-45 bg-indigo-200 rounded-full pointer-events-none -bottom-96 right-64 w-96 bg-opacity-20"
    ></div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from "vue-router";

const router = useRouter();

function handleClick() {
  router.push("/");
}
    
</script>
