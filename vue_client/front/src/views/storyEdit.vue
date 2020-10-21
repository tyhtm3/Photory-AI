<template>
  <div
    class="storyEdit"
    :style="{ height: `${hei}px`, flexDirection: mainDir }"
  >
    <ul id="tools" :style="{ flexDirection: toolDir }">
      <li @click="toolSelect(0)" class="select">이동 및 크기 조절</li>
      <li @click="toolSelect(1)">글 수정</li>
      <li @click="toolSelect(2)">글 상자 추가</li>
      <li @click="toolSelect(3)">스티커</li>
      <!-- <li @click="toolSelect(4)">색상 변경</li> -->
    </ul>
    <div id="playground" v-html="pageData"></div>
    <vue-editor
      id="ed0"
      v-model="editor.con"
      v-show="editText"
      style="position: fixed"
      :style="{
        left: editor.left,
        top: editor.top,
        width: editor.wid,
        height: editor.hei,
      }"
      :editor-toolbar="cutomTb"
    ></vue-editor>
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
      cutomTb: [
        [{ header: [false, 1, 2, 3, 4, 5, 6] }],
        [
          { align: "" },
          { align: "center" },
          { align: "right" },
          { align: "justify" },
        ],
        [{ indent: "-1" }, { indent: "+1" }], // outdent/indent
        [{ color: [] }, { background: [] }], // dropdown with defaults from theme
      ],
      hei: 0,
      screenHorizontal: 0,
      mainDir: "row",
      toolDir: "column",
      pageData:
        '<img id="mainImg" draggable="false" src="/img/logo_name.334d3675.png" style="position:absolute;left:0px;top:0px;width:100px;height:100px;"/><div id="con1" class="content ql-editor" draggable="false" style="position:absolute;left:0px;top:0px;width:400px;height:400px"><h1><span style="color: rgb(0, 102, 204);">로렌 </span></h1><p class="ql-align-right"><span style="color: rgb(255, 255, 255); background-color: rgb(255, 153, 0);">입슘 달러 싯 </span></p><p class="ql-align-center"><span style="background-color: rgb(187, 187, 187); color: rgb(68, 68, 68);">기타 등등</span></p><p><br></p></div>',
      dragXY: [0, 0],
      active: "",
      editText: false,
      editor: {
        left: 0,
        top: 0,
        con: "",
        hei: "500px",
        wid: "500px",
      },
      toolStatus: 1,
    };
  },
  created() {
    window.addEventListener("resize", this.reposition);
    this.hei = window.innerHeight - 50;
  },
  mounted() {
    this.reposition();
    this.toolSelect(0);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.reposition);
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
    toolSelect(tool) {
      if (tool !== this.toolStatus) {
        document
          .querySelector(`#tools li:nth-child(${this.toolStatus + 1})`)
          .classList.remove("select");
        document
          .querySelector(`#tools li:nth-child(${tool + 1})`)
          .classList.add("select");
        this.toolStatus = tool;
        if (this.editText) {
          this.saveEditor(this.editText);
        }
        let pg = document.querySelector("#playground");
        pg.childNodes.forEach((item) => {
          item.onmousedown = null;
        });
        pg.onmousedown = null;
        this.act({ target: pg });
        this.editText = false;
        if (tool === 0) {
          let el = document.querySelector(".storyEdit");
          pg.onmousedown = (e) => this.act(e);
          pg.childNodes.forEach((item) => {
            item.onmousedown = (e) => {
              this.dragXY = [
                el.offsetLeft + e.clientX - item.offsetLeft,
                el.offsetTop + e.clientY - item.offsetTop - 50,
              ];
              document.onmousemove = (e) => this.moveObj(e, el, item);
            };
          });
        } else if (tool === 99) {
          // 크기
        } else if (tool === 1) {
          // 글 수정
          pg.childNodes.forEach((item) => {
            if (item.classList[0] === "content") {
              item.onmousedown = () => {
                // console.log(e);
                this.onEditText(item);
              };
            }
          });
        } else if (tool === 2) {
          // 글상자 추가
        } else if (tool === 3) {
          // 아이콘 추가
        }
      }
    },
    reposition() {
      this.hei = window.innerHeight - 50;
      let el = document.querySelector(".storyEdit");
      if (el.clientWidth >= el.clientHeight) {
        this.screenHorizontal = true;
      } else {
        this.screenHorizontal = false;
      }
    },
    moveObj(e, el, target) {
      target.style.left = `${Math.max(
        0,
        Math.min(90, ((e.clientX - this.dragXY[0]) / el.clientWidth) * 100)
      )}%`;
      target.style.top = `${Math.max(
        0,
        Math.min(90, ((e.clientY - this.dragXY[1]) / el.clientHeight) * 100)
      )}%`;
      this.act({ target });
      document.onmouseup = () => {
        document.onmousemove = null;
      };
    },
    act(e) {
      // 타겟 찾기
      let tar;
      if (e.target.id === "") {
        tar = e.target.parentNode;
        if (e.target.id === "") {
          tar = tar.parentNode;
        }
      } else {
        tar = e.target;
      }
      // 만약 타겟이 달라졌다면
      if (this.active !== tar.id) {
        // 이전 타겟을 지워줌
        if (this.active !== "") {
          document.querySelector(`#${this.active}`).classList.remove("active");
        }
        this.active = tar.id;

        tar.classList.add("active");
      }
    },
    addResize(item){
      // dotLT
      // dotRT
      // dotLB
      // dotRB
      console.log(item);
    },
    onEditText(item) {
      this.editor.con = item.innerHTML;
      item.innerHTML = "";
      this.editor.left = `${
        item.offsetLeft + document.querySelector("#playground").offsetLeft
      }px`;
      this.editor.top = `${Math.max(
        document.querySelector("#playground").offsetTop,
        item.offsetTop
      )}px`;
      this.editor.wid = `${item.clientWidth}px`;
      this.editor.hei = `${item.clientHeight}px`;
      this.editText = item.id;
      document.querySelector("#playground").onclick = (e) => {
        if (e.target.classList[0] !== "content") {
          this.saveEditor(this.editText);
        }
      };
    },
    saveEditor(id) {
      document.querySelector("#" + id).innerHTML = this.editor.con;
      this.editText = "";
      document.querySelector("#playground").onclick = null;
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
    justify-content: space-between;
    background-color: aquamarine;
    li {
      padding: 5px;
      border: 2px solid black;
      flex-grow: 1;
      border-radius: 10px;
      background-color: #ddd;
      &:hover {
        cursor: pointer;
      }
      &.select {
        border: red 2px solid;
      }
    }
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
    .content {
      min-height: 200px;
    }
  }
}
</style>
