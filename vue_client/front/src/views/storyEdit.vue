<template>
  <div
    class="storyEdit"
    :style="{ height: `${hei}px`, flexDirection: mainDir }"
  >
    <ul id="tools" :style="{ flexDirection: toolDir }">
      <li>툴1</li>
      <li>툴2</li>
      <li>툴3</li>
      <li>툴4</li>
      <li>툴5</li>
      <li>툴6</li>
    </ul>
    <div id="playground" v-html="pageData"></div>
    <vue-editor id="ed0" v-model="con1" v-if="false"></vue-editor>
  </div>
</template>

<script>
import { VueEditor } from "vue2-editor";

export default {
  name: "storyEdit",
  components: {
    VueEditor,
  },
  data() {
    return {
      hei: 0,
      screenHorizontal: 0,
      con1: "",
      mainDir: "row",
      toolDir: "column",
      pageData:
        '<img id="mainImg" src="/img/logo_name.334d3675.png" style="position:absolute;left:0px;top:0px;width:100px;height:100px;"/><div id="con1" style="position:absolute;left:0px;top:0px;"><p>로렌 입슘 달러 싯 기타 등등</p></div>',
      dragXY: [0, 0],
      active: "",
    };
  },
  created() {
    window.addEventListener("resize", this.reposition);
    this.hei = window.innerHeight - 50;
  },
  mounted() {
    let el = document.querySelector(".storyEdit");
    let pg = document.querySelector("#playground");
    pg.addEventListener("click", (e) => this.act(e));
    pg.childNodes.forEach((item) => {
      item.addEventListener("dragstart", (e) => {
        this.dragXY = [
          el.offsetLeft + e.clientX - item.offsetLeft,
          el.offsetTop + e.clientY - item.offsetTop - 50,
        ];
      });
      item.addEventListener("dragend", (e) => this.moveObj(e, el, item));
    });

    this.reposition();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.reposition);
    document.querySelector("#playground").removeEventListener("click");
    document.querySelector("#mainImg").removeEventListener("dragstart");
    document.querySelector("#mainImg").removeEventListener("dragend");
  },
  watch: {
    screenHorizontal(boo) {
      if (boo) {
        this.mainDir = "row";
        this.toolDir = "column";
      } else {
        this.mainDir = "column-reverse";
        this.toolDir = "row";
      }
    },
  },
  methods: {
    reposition() {
      this.hei = window.innerHeight - 50;
      let el = document.querySelector(".storyEdit");
      if (el.clientWidth >= el.clientHeight) {
        this.screenHorizontal = true;
      } else {
        this.screenHorizontal = false;
      }
    },
    onEditor() {
      document.querySelector("#con1").innerHTML = this.con1;
    },
    moveObj(e, el, target) {
      console.log(target);
      target.style.left = `${Math.max(
        0,
        Math.min(95, ((e.clientX - this.dragXY[0]) / el.clientWidth) * 100)
      )}%`;
      target.style.top = `${Math.max(
        0,
        Math.min(95, ((e.clientY - this.dragXY[1]) / el.clientHeight) * 100)
      )}%`;
      this.act({ target });
    },
    act(e) {
      let tar;
      if (e.target.id === "") {
        tar = e.target.parentNode;
      } else {
        tar = e.target;
      }
      if (this.active !== tar.id) {
        if (this.active !== "") {
          document.querySelector(`#${this.active}`).classList.remove("active");
        }
        this.active = tar.id;
        tar.classList.add("active");
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
  height: 100%;
  display: flex;
  overflow: hidden;
  #tools {
    padding: 0;
    margin: 0;
    list-style: none;
    display: flex;
    background-color: aquamarine;
  }
  #playground {
    display: flex;
    position: relative;
    background-color: rosybrown;
    flex-grow: 1;
    #mainImg.active:hover {
      cursor: move;
    }
    .active {
      border: 1px solid black;
    }
  }
}
</style>
