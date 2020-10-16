<template>
  <div class="storyEdit" :style="{ height: `${hei}px`, flexDirection: mainDir }">
    <ul id="tools" :style="{flexDirection: toolDir }">
      <li>툴1</li>
      <li>툴2</li>
      <li>툴3</li>
      <li>툴4</li>
      <li>툴5</li>
      <li>툴6</li>
    </ul>
    <div id="playground">가로모드 : {{ screenHorizontal }}</div>
  </div>
</template>

<script>
export default {
  name: "storyEdit",
  data() {
    return {
      hei: 0,
      screenHorizontal: false,
      mainDir:'row',
      toolDir:'column',
    };
  },
  created() {
    this.hei = window.innerHeight - 60;
    window.addEventListener("resize", this.reposition);
  },
  mounted(){
    this.reposition()
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.reposition);
  },
  watch:{
    screenHorizontal(boo){
      if (boo){
        this.mainDir = 'row'
        this.toolDir = 'column'
      }else{
        this.mainDir = 'column-reverse'
        this.toolDir = 'row'
      }
    },
  },
  methods: {
    reposition() {
      this.hei = window.innerHeight - 60;
      let el = document.querySelector(".storyEdit");
      if (el.clientWidth >= el.clientHeight - 50) {
        this.screenHorizontal = true;
      } else {
        this.screenHorizontal = false;
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.storyEdit {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: gray;
  height: 100%;
  display: flex;
  #tools {
    padding: 0;
    margin: 0;
    list-style: none;
    display: flex;
    background-color: aquamarine;
  }
  #playground {
    display: flex;
    background-color: rosybrown;
    flex-grow: 1;
  }
}
</style>
