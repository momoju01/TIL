<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      // console.log('Todo Create!!')
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        data: new Date().getTime(),
      }
      // this.$store.commit('CREATE_TODO', todoItem)
      // this.$store.commit('호출mutation', payload)
      // mutation 호출하는 method는 commit : 원래 action에서 호출해야됨
      // 두 번째 인자로는 payload(전송되는 data)

      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem) // action 호출
      }
      this.todoTitle = null //초기화
    }
  }
}
</script>

<style>

</style>