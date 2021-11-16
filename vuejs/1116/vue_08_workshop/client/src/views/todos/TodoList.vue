<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ completed: todo.completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt")

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      }

      return config
    },
    getTodos: function () {
      const config = this.setToken()

      axios({
        method: 'get',
        url: `${SERVER_URL}/todos/`,
        headers: config
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
      const config = this.setToken()
      axios({
        method: 'delete',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        headers: config
      })
        .then(res => {
          console.log(res)
          this.getTodos()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const config = this.setToken()
      const todoItem = {
        ...todo,
        completed: !todo.completed,
      }
      axios({
        method: 'put',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        data: todoItem,
        headers: config
      })
        .then(res => {
          console.log(res)
          todo.completed = !todo.completed
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getTodos()
    } else {
      this.$router.push( {name: 'Login' })
    }
  }
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
