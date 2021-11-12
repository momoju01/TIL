<template>
  <div>
    <li @click="selectVideo">
      <img :src="videoImg" alt="">
      <span>{{ videoTitle }}</span>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods:{
    selectVideo: function () {
      // console.log('비디오 선택됨')
      this.$store.dispatch('selectVideo', this.video)
    }
  },
  computed: {
    videoTitle: function () {
      return _.unescape(this.video.snippet.title)
    },
    videoImg: function () {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>

</style>