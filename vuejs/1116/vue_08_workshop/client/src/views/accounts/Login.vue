<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model="credentials.password"
      @keypress.enter="login(credentials)">
    </div>
    <button @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function (credentials) {
      console.log(credentials)
      //axios
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        // console.log(res)
        localStorage.setItem('jwt', res.data.token)
        // App 컴포넌트는 login data 변경 사실 알 수 없으므로 emit login 이벤트 호출
        this.$emit('login') 
        this.$router.push({ name: 'TodoList' })

      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
