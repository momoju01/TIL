<template>
  <div>
    <h1>About</h1>
    <h2>{{ myMessage }}</h2>
    <h2>{{ parentData }}</h2>
    <input 
      type="text"
      @keyup.enter="childInputChange"
      v-model="childInputData"
    >
  </div>
</template>

<script>
export default {
  name: 'About',
  props: {
    myMessage: String,
    parentData: String,
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childInputChange: function () {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>