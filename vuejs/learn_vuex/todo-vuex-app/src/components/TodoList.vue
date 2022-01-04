<template>
  <div>
    <!-- {{ $store.state.todos }} -->
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
      >
      <!-- 원래는 kebab-case로 prop data 해줘야됨 !  -->
    </todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // data: function (params) {
  //   여전히 로컬 데이터 쓸 수 있음!1
  // }
  computed: {
    todos: function () {
      return this.$store.state.todos  //store에 this를 통해 접근 가능
    }
  }
}
</script>

<style>

</style>