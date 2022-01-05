import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  mutations: {
    // method는 handler 함수 <= 동기적 함수만 들어가야됨
    CREATE_TODO: function (state, todoItem) {  
      // 첫 번째 인자로 항상 state 받음: 왜? mutation의 역할은 state 조작
      // 두 번째 인자는 payload 받은 거
      // 대문자로 쓰는 이유 : mutation이 state를 수정하기 때문에 매우 중요!! mutation임을 바로 알 수 있도록
      // console.log(state)
      console.log(todoItem)
      state.todos.push(todoItem)  // state 변경!
    },
    DELETE_TODO: function (state, todoItem) {
      // 1. todoItem이 첫 번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 index 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo => { 
        if (todo === todoItem) {
          return {
            // title: todoItem.title,
            // date: new Date(),
            ...todo, //js spread syntax
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
    // 구조분해 할당으로 쓰는 것만 가져오기  
    createTodo: function ({ commit }, todoItem) {  
      //actions는 첫 번째 인자로 context
      // context를 통해 mu/ac/get/state 다 접근할 수 있음(변경은 권장x)
      // action : state 변경 이외의 다른 모든 동작
      // console.log(context, todoItem)
      
      // context.commit('뮤테이션 이름', todoItem)    
      // context.commit('CREATE_TODO', todoItem)    
      // 구조 분해 할당시 context. 안 써도 됨 이미 commit으로 가져와서.. 
      commit('CREATE_TODO', todoItem)
      // 굳이 actions를 거쳐서 간다?? NO!  여기서 많은 연산들 함. axios도 여기서 쓰고... 
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({commit}, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    }
  },
  modules: {
  }
})
