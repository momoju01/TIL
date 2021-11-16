<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
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
      todos: [],
    }
  },
  methods: {
    getTodos: function () {
      axios.get('http://127.0.0.1:8000/todos/')
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios.delete(`http://127.0.0.1:8000/todos/${todo.id}/`)
        .then((res) => {
          console.log(res)
          // const targetTodoIdx = this.todos.findIndex((todo) => {
          //   return todo.id === res.data.id
          // })
          // this.todos.splice(targetTodoIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }

      axios.put(`http://127.0.0.1:8000/todos/${todo.id}/`, todoItem)
        .then((res) => {
          console.log(res)
          // todo.completed = !todo.completed
        })
      },
    },
  // created: function () {
  //   this.getTodos()
  // }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>