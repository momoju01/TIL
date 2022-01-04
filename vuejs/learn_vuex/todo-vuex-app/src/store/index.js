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
    }
  },
  actions: {
    createTodo: function (context, todoItem) {  //actions는 첫 번째 인자로 context
      // context를 통해 mu/ac/get/state 다 접근할 수 있음(변경은 권장x)
      // action : state 변경 이외의 다른 모든 동작
      // console.log(context, todoItem)
      context.commit('CREATE_TODO', todoItem)
      // 굳이 actions를 거쳐서 간다?? NO!  여기서 많은 연산들 함. axios도 여기서 쓰고... 

    }
  },
  modules: {
  }
})
