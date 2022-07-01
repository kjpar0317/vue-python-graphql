<template>
  <div class="w-full h-full px-4 pt-1 min-w-96 min-h-96">
    <div>
      <button class="btn btn-xs" @click="addItem()">추가</button>
    </div>
    <div class="w-full">
      <grid-layout
        :layout.sync="layoutObj.layout"
        :col-num="layoutObj.colNum"
        :row-height="30"
        :is-draggable="layoutObj.draggable"
        :is-resizable="layoutObj.resizable"
        :responsive="layoutObj.responsive"
        :vertical-compact="true"
        :use-css-transforms="true"
        @breakpoint-changed="handleBreakpointChanged"
        @layout-updated="handleLayoutChanged"
      >
        <grid-item
          v-for="(item, index) in layoutObj.layout"
          :static="item.static"
          :x="item.x"
          :y="item.y"
          :w="item.w"
          :h="item.h"
          :i="item.i"
          :minW="item.minW"
          :minH="item.minH"
          :key="index"
          @resized="handleGridItemResized"
        >
          <DefaultWidget
            ref="childWidgetRef"
            :index="item.i"
            :title="item.title"
            :module="item.module"
            @remove="removeItem"
            @open-modal="() => handleModal(item.title)"
          />
        </grid-item>
      </grid-layout>
    </div>
    <Modal :open="modalObj.open" :title="modalObj.title" @close="handleModal"
      >TEST입니다.</Modal
    >
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import { GridLayout, GridItem, GridItemData } from 'vue3-grid-layout';

import DefaultWidget from "@/components/widgets/DefaultWidget.vue";
import Modal from "@/components/modal/Modal.vue";

const layoutObj = reactive<any>({
  layout: [
    {
      x: 0,
      y: 0,
      w: 3,
      h: 6,
      minW: 3,
      minH: 6,
      i: "0",
      static: false,
      title: "Candle 차트",
      module: "candle",
    },
    {
      x: 3,
      y: 0,
      w: 3,
      h: 6,
      minW: 3,
      minH: 6,
      i: "1",
      static: false,
      title: "Treemap 차트",
      module: "treemap",
    },
    {
      x: 6,
      y: 0,
      w: 3,
      h: 6,
      minW: 3,
      minH: 6,
      i: "2",
      static: false,
      title: "Radial 차트",
      module: "radial",
    },
    {
      x: 9,
      y: 0,
      w: 3,
      h: 6,
      minW: 3,
      minH: 6,
      i: "3",
      static: false,
      title: "DataLabel 차트",
      module: "barDataLabel",
    },
    {
      x: 0,
      y: 6,
      w: 3,
      h: 6,
      minW: 3,
      minH: 6,
      i: "4",
      static: false,
      title: "Sample Grid",
      module: "board",
    },
  ],
  draggable: true,
  resizable: true,
  responsive: true,
  index: 4,
  colNum: 12,
});
const modalObj = reactive({ open: false, title: "" });
const childWidgetRef = ref<any>({});

function addItem() {
  // Add a new item. It must have a unique key!
  layoutObj.layout.push({
    x: (layoutObj.layout.length * 3) % (layoutObj.colNum || 9),
    y: layoutObj.layout.length + (layoutObj.colNum || 9), // puts it at the bottom
    w: 3,
    h: 6,
    i: layoutObj.index.toString(),
  });
  // Increment the counter to ensure key is always unique.
  layoutObj.index++;
}
function removeItem(val: GridItemData) {
  const index = layoutObj.layout.map((item: any) => item.i).indexOf(val);
  layoutObj.layout.splice(index, 1);
  layoutObj.index--;
}
function handleModal(title: string) {
  modalObj.open = !modalObj.open;
  modalObj.title = title;
}
function handleBreakpointChanged(breakpoint: string, layout: GridItemData) {
  layoutObj.layout = layout;
}
function handleLayoutChanged(layouts: Array<GridItemData>) {
  // layoutObj.layout = layouts;
}
function handleGridItemResized() {
  childWidgetRef.value.callGridItemResized &&
    childWidgetRef.value.callGridItemResized();
}
</script>
