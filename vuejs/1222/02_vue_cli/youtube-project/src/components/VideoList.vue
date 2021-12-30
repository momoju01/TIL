<template>
  <ul>
    <video-list-item
      v-for="video in videos" 
      :key="video.id.videoId"
      :video="video"
      @select-video="onSelectVideo"
    >
    <!-- :video="video" : video를 videoListItem으로 내려줌  -->
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'


export default {
  name: 'VideoList',
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  components: {
    VideoListItem,
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>
