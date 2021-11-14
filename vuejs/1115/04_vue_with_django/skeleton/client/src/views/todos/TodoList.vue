<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span @click="updateTodoStatus(todo)" :class="{ 'is-completed': todo.is_completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    getTodos: function () {
      axios({
        method: 'get', 
        url: 'http://127.0.0.1:8000/todos/'
      })
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`
      })
        .then(res => {
          console.log(res)
          this.getTodos()  //삭제 후 업데이트된 todoList get 요청
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        ...todo,  //기존 todo 객체 복사
        is_completed: !todo.is_completed  // 수정할 부분만 수정
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
      })
        .then(res => {
          console.log(res)
          todo.is_completed = !todo.is_completed  // 화면 업데이트하기
        })
      },
    },
  created: function () {
    this.getTodos()
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
