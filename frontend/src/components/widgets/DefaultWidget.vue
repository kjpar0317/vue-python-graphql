<template>
  <div
    class="flex flex-col w-full h-full p-4 shadow-lg card rounded-xl bg-base-100"
  >
    <WidgetTitle
      :title="title"
      :module="module"
      :hidden="false"
      @open-modal="$emit('open-modal')"
      @remove="$emit('remove', index)"
    />
    <div v-if="module == 'barDataLabel'" class="h-full mt-2">
      <ApexBarDataLabelChart />
    </div>
    <div v-else-if="module == 'candle'" class="h-full mt-2">
      <ApexCandleStickChart />
    </div>
    <div v-else-if="module == 'radial'" class="h-full mt-2">
      <ApexRadialChart />
    </div>
    <div v-else-if="module == 'treemap'" class="h-full mt-2">
      <ApexTreemapChart />
    </div>
    <div v-else-if="module == 'board'" class="h-full mt-2">
      <GridSample ref="gridRef" />
    </div>
    <div v-else class="mt-2"># TODO</div>
  </div>
</template>

<script lang="ts" setup>
// import { ref } from "vue";

import WidgetTitle from "@/components/layout/widget/WidgetTitle.vue";
import ApexBarDataLabelChart from "@/components/charts/bar/ApexBarDataLabelChart.vue";
import ApexCandleStickChart from "@/components/charts/candlestick/ApexCandleStickChart.vue";
import ApexTreemapChart from "@/components/charts/treemap/ApexTreemapChart.vue";
import ApexRadialChart from "@/components/charts/radial/ApexRadialChart.vue";
import GridSample from "@/components/grid/GridSample.vue";

defineProps(["index", "title", "module"])

// const gridRef = ref<any>({});

// function callGridItemResized() {
//   gridRef &&
//     gridRef.value.onSizeColumnToFit &&
//     gridRef.value.onSizeColumnToFit();
// }
</script>
