import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      
    ]
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)  // 데이터 조작
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem) //todoItem의 인덱스값 찾기
      state.todos.splice(index, 1)  // index에서 하나 지우고 새로운 배열 생성
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo=> {  // todos의 배열
        if (todo === todoItem) {              // 새로 들어온 todoItem이 mapping되는 게 있다면
          return {                            // 상태 변경해주기
            // title: todoItem.title,
            // date: new Date().getTime,
            ...todo,  //js spread syntax
            isCompleted: !todo.isCompleted    // 변경되는 것만
          }
        } else {  // 일치하지 않으면 배열 그대로 리턴
          return todo
        }
      })
    }
  },
  actions: {
    // createTodo: function (context, todoItem) {
    //   context.commit('CREATE_TODO', todoItem)
    // }
    createTodo: function ({commit}, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({commit}, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({commit}, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  modules: {
  }
})
