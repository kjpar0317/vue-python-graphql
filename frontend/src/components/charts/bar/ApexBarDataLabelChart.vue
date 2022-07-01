<template>
  <apexchart
  ref="chartRef"
    :options="chartObj.options"
    :series="chartObj.series"
    width="100%"
    height="100%"
  ></apexchart>
</template>

<script lang="ts" setup>
import { reactive, ref, watch } from "vue";
import chroma from "chroma-js";

import { getTextColorByTheme } from '@/utils/comm-util';
import { layoutStore } from "@/store/layout";

defineProps(["index", "title"])

const store = layoutStore();
const chartRef = ref<any>({});
const chartObj = reactive({
  series: [
    {
      data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
    },
  ],
  options: {
    chart: {
      type: "bar",
      foreColor: getTextColorByTheme(store.theme)
    },
    plotOptions: {
      bar: {
        barHeight: "100%",
        distributed: true,
        horizontal: true,
        dataLabels: {
          position: "bottom",
        },
      },
    },
    // colors: [
    //   "#33b2df",
    //   "#546E7A",
    //   "#d4526e",
    //   "#13d8aa",
    //   "#A5978B",
    //   "#2b908f",
    //   "#f9a3a4",
    //   "#90ee7e",
    //   "#f48024",
    //   "#69d2e7",
    // ],
    colors: chroma.scale(["#fafa6e", "#2A4858"]).mode("lch").colors(10),
    dataLabels: {
      enabled: true,
      textAnchor: "start",
      style: {
        colors: ["#fff"],
      },
      formatter: function (val: string, opt: any) {
        return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
      },
      offsetX: 0,
      dropShadow: {
        enabled: true,
      },
    },
    stroke: {
      width: 1,
      colors: ["#fff"],
    },
    xaxis: {
      categories: [
        "South Korea",
        "Canada",
        "United Kingdom",
        "Netherlands",
        "Italy",
        "France",
        "Japan",
        "United States",
        "China",
        "India",
      ],
    },
    yaxis: {
      labels: {
        show: false,
      },
    },
    // title: {
    //   text: "Custom DataLabels",
    //   align: "center",
    //   floating: true,
    // },
    subtitle: {
      text: "Category Names as DataLabels inside bars",
      align: "center",
    },
    tooltip: {
      theme: "dark",
      x: {
        show: false,
      },
      y: {
        title: {
          formatter: function () {
            return "";
          },
        },
      },
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          legend: {
            show: false,
          },
        },
      },
    ],
  },
});

watch(() => store.theme, () => {
  chartRef.value.updateOptions({
    chart: {
      foreColor: getTextColorByTheme(store.theme)
    },
  })
});

</script>
