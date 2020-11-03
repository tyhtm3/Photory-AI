<template>
  <div id="Mystory">
    <div id="storyList">
      <img id="shelve" src="@/assets/my_story.png" alt="" />
      <div id="listIndex">123</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Mystory",
  data() {
    return {
      a: 1,
    };
  },
};
</script>

<style lang="scss">
#Mystory {
  height: 100%;
  overflow-x: hidden;
  width: 100vw;
  #storyList{
    display: flex;
    justify-content: space-around;
    flex-flow: column nowrap;
    width: 100vw;
    height: 100%;
    min-height: 95vw;
    #shelve{
      width: 100vw;
    }
    #listIndex{
    }
  }
}
</style>