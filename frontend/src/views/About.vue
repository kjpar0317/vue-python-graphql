<template>
  <div class="px-4 pt-1 min-w-96 w-full h-full">
      <ag-grid-vue
      class="w-full h-full ag-theme-alpine"
      :columnDefs="columnDefs"
      :rowData="data.codes"
      detilRowAutoHeight="true"
      pagination="true"
      paginationAutoPageSize="true"
      @grid-ready="handleGridReady"
    />
  </div>
</template>

<script lang="ts" setup>
import { reactive, onMounted } from "vue";
import { gql, useQuery } from '@urql/vue';
import { AgGridVue } from "ag-grid-vue3";
import { GridReadyEvent } from "ag-grid-community";

const gridObj = reactive<any>({ gridApi: null, gridColumnApi: null });
const { data, error } = await useQuery({
  query: gql`
    {
      codes {
        CDescription
        CEngName
        CId
        CName
        CParentId
      }
    }
  `
});
const columnDefs = [
  { headerName: "코드", field: "CId" },
  { headerName: "코드명", field: "CName" },
  { headerName: "설명", field: "CDescription" },
];

onMounted(() => {
  onSizeColumnToFit();
});

function handleGridReady(params: GridReadyEvent) {
  gridObj.gridApi = params.api;
  gridObj.gridColumnApi = params.columnApi;

  onSizeColumnToFit();
}
function onSizeColumnToFit() {
  if (gridObj && gridObj.gridApi) {
    gridObj.gridApi.sizeColumnsToFit();
  }
}   
</script>
