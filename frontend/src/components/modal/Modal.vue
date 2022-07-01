<template>
  <vue-final-modal
    v-model="open"
    :click-to-close="false"
    classes="flex justify-center items-center"
    content-class="relative flex flex-col max-h-full p-4 mx-4 bg-primary-content border rounded border-neutral"
  >
    <span v-if="title" class="mr-8 text-xl font-bold">{{ title }}</span>
    <div class="flex-grow overflow-y-auto">
      <slot :params="params" />
    </div>
    <!-- <div class="flex-grow overflow-y-auto"><slot /></div> -->
    <div class="flex items-center justify-center flex-shrink-0 pt-4 space-x-1">
      <button v-if="$attrs.onOk" class="btn btn-outline btn-primary btn-sm" @click="$emit('ok')">
        ok
      </button>
      <button v-if="$attrs.onClose" class="btn btn-outline btn-accent btn-sm" @click="$emit('close')">
        cancel
      </button>
    </div>
    <button class="absolute top-0 right-0 mt-2 mr-2" @click="$emit('close')">
      <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-7 h-7"
          viewBox="0 0 20 20"
          fill="currentColor"
      >
        <path
            fill-rule="evenodd"
            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
            clip-rule="evenodd"
        />
      </svg>
    </button>
  </vue-final-modal>
</template>

<script lang="ts" setup>
defineProps(["open", "title", "params"])
</script>
