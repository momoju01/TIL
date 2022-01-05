<template>
  <div>
    <span 
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
    {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo) //삭제된 todo 객체 actions로 보내기 
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }
}
</script>

<style>
  .is-completed { 
    text-decoration: line-through;
  }
</style>