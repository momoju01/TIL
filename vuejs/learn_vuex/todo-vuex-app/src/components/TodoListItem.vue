<template>
  <div>
    {{ todo.title }}
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  }
}
</script>

<style>

</style>