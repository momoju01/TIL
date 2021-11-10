import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {  // todoForm에서 완성된 todo를 payload로 전달받기
      // console.log(state)
      // console.log(todoItem)
      state.todos.push(todoItem)  // state 변경은 mutations에서~~
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map( todo => {
        if (todo === todoItem) {
          return{
            // title: todoItem.title, 
            // date: new Date(),
            ...todo,  // JS spread syntax
            isCompleted: !todo.isCompleted
          }
        } else {
          return todo
        }
      })
    }
  },
  actions: {
    // createTodo: function (context, todoItem) {
    //   // console.log(context)
    //   // console.log(todoItem)
    //   context.commit('CREATE_TODO', todoItem)
    // }

    // 구조 분해 할당하는 경우
    createTodo: function ({ commit }, todoItem) { 
      // console.log(state)  -> { commit, state }
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)   // 'DELETE_TODO': mutation 이름 어떤 todoItem 지워지는지 알아야해서 같이 호출
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },



  modules: {
  }
})
