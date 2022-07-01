<template>
  <div v-if="result.error">
    Oh no... {{result.error}}
  </div>
  <div v-else>
    <ul v-if="result.data">
      <li v-for="msg in result.data">{{ msg.from }}: "{{ msg.text }}"</li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { gql, useSubscription } from '@urql/vue';

function handleSubscription(messages: any = [] , response: any) {
  console.log(response);
  return [response.newMessages, ...messages];
};

const result: any = useSubscription({
  query: gql`
    subscription {
      count(target: 5)
    }
  `
}, handleSubscription);
</script>