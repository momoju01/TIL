<template>
  <div v-if="isSelected">
    <iframe :src="videoUrl" frameborder="0"></iframe>
    <h2>{{ videoTitle }}</h2>
    <h2>{{ videoDesc }}</h2>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name: 'VideoDetail',
  computed: {
    ... mapGetters([
      'isSelected',
      'videoUrl',
      'videoTitle',
      'videoDesc',
    ])



    // isSelected: function () {
      // 가공하고싶을 때는 이걸로 가공해서 쓰기
    //   return this.$store.getters.isSelected
    // },
    // videoUrl: function () {
    //   return this.$store.getters.videoUrl
    // },
    // videoTitle: function () {
    //   return this.$store.getters.videoTitle
    // },
    // videoDesc: function () {
    //   return this.$store.getters.videoDesc
    // }
  }
}
</script>

<style>

</style>