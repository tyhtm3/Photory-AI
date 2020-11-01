<template>
  <div>
    <StoryshareList/>
  </div>
</template>
<script>
import StoryshareList from '@/components/StoryshareList.vue'
export default {
  components:{
   StoryshareList,
  }
}
</script>
<style>
  #storysharelist{
    background-image:url("../assets/hill.png");
		background-size : cover;
  }
</style>