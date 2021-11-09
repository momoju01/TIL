<template>
<div>
  <h1>This is parent</h1>
  <p>ParentData: {{ parentData }}</p>
  <input v-model="parentData" type="text" @input="inputParentData">
  <p>appData: {{ appData }}</p>
  <p>ChildData: {{ childData }}</p>
  <Child :appData="appData" :parentData="parentData"
  @child-input="inputChildData"/>  
  <!-- child-input 시그널 들으면 inputChildData 실행 -->
</div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  data: function() {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputChildData: function(data) {    // payload 안에 있는 데이타 data에 담김.
      this.childData = data
      this.$emit('child-input', this.childData)  // 한번 더 위로(app으로) 보냄. 순서 주의
      // console.log('!!!! text from child')
    },
    inputParentData: function() {
      this.$emit('parent-input', this.parentData)
    },
  },
  props:{
    appData: String,
  },
  components: {
    Child,
  }
}
</script>

<style>

</style>