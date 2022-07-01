/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  // eslint-disable-next-line @typescript-eslint/no-explicit-any, @typescript-eslint/ban-types
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module 'vue3-grid-layout' {
  import Vue from 'vue';

  export class GridLayout extends Vue {}

  export class GridItem extends Vue {}

  export interface GridItemData {
    x: number;
    y: number;
    w: number;
    h: number;
    minW: number;
    minH: number;
    title: string;
    module: string;
    static: boolean;
    i: string;
  }
}