<template>
  <div>
    <div>
    <span @click="updateTodoStatus">{{ todo.title }}</span>
    </div>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object
    }
  },
  methods: {
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)  // 'deleteTodo': action methods 이름
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }
}
</script>

<style>

</style>