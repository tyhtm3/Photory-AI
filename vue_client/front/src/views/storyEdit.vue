<template>
  <div class="storyEdit" :style="{ flexDirection: mainDir }">
    <ul id="tools" :style="{ flexDirection: toolDir }">
      <li @click="toolSelect(0)" class="select">이동 및 크기 조절</li>
      <li @click="toolSelect(1)">글 수정</li>
      <li @click="toolSelect(2)">글 상자 추가</li>
      <li @click="toolSelect(3)">스티커</li>
      <li @click="toolSelect(4)">페이지</li>
      <li @click="toolSelect(5)">그림 스타일 바꾸기</li>
      <li @click="toolSelect(6)">저장 후 나가기</li>
      <!-- <li @click="toolSelect(4)">색상 변경</li> -->
    </ul>
    <div id="playground"></div>
    <vue-editor
      id="ed0"
      v-model="editor.con"
      v-show="editText"
      style="position: fixed; z-index: 101"
      :style="{
        left: editor.left,
        top: editor.top,
        width: editor.wid,
        height: editor.hei,
      }"
      :editor-toolbar="cutomTb"
    ></vue-editor>
    <div v-if="!(active === '' || active === 'playground')" id="resizer">
      <div id="dotLT"></div>
      <div id="dotRT"></div>
      <div id="dotLB"></div>
      <div id="dotRB"></div>
    </div>
    <img
      id="remover"
      v-if="
        !(
          active === '' ||
          active === 'playground' ||
          active === 'con1' ||
          active === 'mainImg'
        )
      "
      src="@/assets/remove.png"
    />
    <div id="sPanel" v-if="sPanelOn">
      <h3>스티커 추가하기</h3>
      <img src="@/assets/stickers/s0.png" alt="" />
      <img src="@/assets/stickers/s1.png" alt="" />
      <img src="@/assets/stickers/s2.png" alt="" />
      <img src="@/assets/stickers/s3.png" alt="" />
      <img src="@/assets/stickers/s4.png" alt="" />
      <img src="@/assets/stickers/s5.png" alt="" />
      <img src="@/assets/stickers/s6.png" alt="" />
      <img src="@/assets/stickers/s7.png" alt="" />
      <img src="@/assets/stickers/s8.png" alt="" />
      <img src="@/assets/stickers/s9.png" alt="" />
      <img src="@/assets/stickers/s10.png" alt="" />
      <img src="@/assets/stickers/s11.png" alt="" />
      <img src="@/assets/stickers/s12.png" alt="" />
      <img src="@/assets/stickers/s13.png" alt="" />
      <img src="@/assets/stickers/s14.png" alt="" />
    </div>
    <div id="pagePanel" v-if="pagePanelOn">
      <h3>page 선택</h3>
      <div
        v-for="(page, index) in pageData"
        :key="index"
        v-html="page"
        :data-idx="index"
      ></div>
    </div>
    <div id="savePanel" v-if="savePanelOn">
      <h3>저장 후 나가기</h3>
      <span>
        제목 :
        <input type="text" v-model="title" />
      </span>
      <span>
        지은이 :
        <input type="text" v-model="writer" />
      </span>
      <button @click="saveAll()">저장</button>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import { VueEditor } from "vue2-editor";
const url = "http://127.0.0.1:8000/";
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
        [{ indent: "-1" }, { indent: "+1" }],
        [{ color: [] }, { background: [] }],
      ],
      hei: 0,
      screenHorizontal: 0,
      mainDir: "row",
      toolDir: "column",
      pageData: ["", "", "", "", ""],
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
      sPanelOn: false,
      pagePanelOn: false,
      savePanelOn: false,
      pageCurrent: -1,
      storyNum: 1,
      title: "",
      writer: "",
    };
  },
  created() {
    window.addEventListener("resize", this.reposition);
  },
  mounted() {
    this.reposition();
    this.$nextTick(() => this.reposition());

    this.storyNum = this.$route.params.storyNum;
    Axios.get(`${url}storys/${this.storyNum}/`).then((res) => {
      this.pageData = res.data.content;
      this.title = res.data.title;
      this.writer = res.data.writer;
      this.pageSelect(0);
    });
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
        this.sPanelOn = false;
        this.pagePanelOn = false;
        this.savePanelOn = false;
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
          pg.onmousedown = (e) => this.act(e);
          pg.childNodes.forEach((item) => {
            item.onmousedown = (e) => {
              this.dragXY = [
                +(e.screenX - item.offsetLeft),
                e.screenY - item.offsetTop,
              ];
              document.onmousemove = (e) => this.moveObj(e, pg, item);
              document.onmouseup = () => {
                document.onmousemove = null;
              };
            };
          });
        } else if (tool === 1) {
          // 글 수정
          pg.childNodes.forEach((item) => {
            if (item.classList[0] === "contentt") {
              item.onmousedown = () => {
                this.onEditText(item);
              };
            }
          });
        } else if (tool === 2) {
          // 글상자 추가
          if (document.querySelectorAll(".contentt").length < 5) {
            this.addContent(document.querySelectorAll(".contentt").length + 1);
          } else {
            alert("더이상 글 상자를 늘릴 수 없습니다.");
          }
        } else if (tool === 3) {
          // 스티커 추가
          this.sPanelOn = true;
          pg.onclick = () => {
            this.toolSelect(0);
            pg.onclick = null;
          };
          this.$nextTick(() => {
            document.querySelectorAll("#sPanel img").forEach((item) => {
              item.onclick = () => {
                let stkrCnt = Array.from(pg.childNodes).filter(
                  (item) => item.classList[0] === "sticker"
                ).length;
                if (stkrCnt >= 20) {
                  alert("스티커는 20개 까지만 생성 가능합니다.");
                } else {
                  let newImg = item.cloneNode();
                  pg.appendChild(newImg);
                  newImg.draggable = false;
                  newImg.classList.add("sticker");
                  newImg.id = `stkr${stkrCnt}`;
                  newImg.style.cssText =
                    "position:absolute;left:0px;top:0px;width:30%;height:30%;";
                  this.toolSelect(0);
                }
              };
            });
          });
        } else if (tool === 4) {
          // 페이지 선택
          this.pagePanelOn = true;
          this.pageData[this.pageCurrent] = pg.innerHTML;
          this.$nextTick(() => {
            let pp = document.querySelector("#pagePanel");
            pp.childNodes.forEach((item) => {
              if (item.nodeName === "DIV") {
                item.childNodes.forEach((item2) => {
                  // console.log(item2.nodeName);
                  if (item2.nodeName !== "IMG") {
                    item2.remove();
                  }
                });
                item.onclick = () => {
                  this.pageSelect(item.dataset.idx * 1);
                };
              }
            });
          });
        } else if (tool === 5) {
          let mI = document.querySelector("#mainImg");
          if (Array.from(mI.classList).includes("normImg")) {
            mI.src = "123";
            mI.className = "img0";
          } else if (Array.from(mI.classList).includes("img0")) {
            mI.src = "123";
            mI.className = "img1";
          } else if (Array.from(mI.classList).includes("img1")) {
            mI.src = "123";
            mI.className = "img2";
          } else if (Array.from(mI.classList).includes("img2")) {
            Axios.get(
              `${url}storys/images/${this.storyNum}/${this.pageCurrent}`
            ).then((res) => {
              mI.src = res.data.img;
              mI.className = "normImg";
            });
          }
          this.toolSelect(0);
        } else if (tool === 6) {
          this.savePanelOn = true;
        }
      }
    },
    pageSelect(idx) {
      let pg = document.querySelector("#playground");
      if (idx !== this.pageCurrent) {
        this.pageCurrent = idx;
        pg.innerHTML = this.pageData[idx];
      }
      this.toolSelect(0);
    },
    removerMove(item) {
      let remover = document.querySelector("#remover");
      let pg = document.querySelector("#playground");
      remover.onclick = () => {
        this.act({ target: pg });
        item.parentNode.removeChild(item);
      };
      remover.style.left = `${
        item.offsetLeft + pg.offsetLeft + item.clientWidth + 10
      }px`;
      remover.style.top = `${
        item.offsetTop + pg.offsetTop + item.clientHeight + 10
      }px`;
    },
    addContent(n) {
      //class 가 콘텐트인게 한개라면 div 추가
      let cont = document.createElement("div");
      cont.id = `con${n}`;
      cont.className = "contentt";
      cont.classList.add("ql-editor");
      cont.draggable = false;
      cont.style.cssText =
        "position:absolute;left:0px;top:0px;width:30%;height:30%;z-index:100";
      document.querySelector("#playground").appendChild(cont);
      this.onEditText(cont);
    },
    reposition() {
      // 화면 비율을 감지, 가로와 세로를 비교했을 때 가장
      let pg = document.querySelector("#playground");
      let tls = document.querySelector("#tools");
      let el = document.querySelector(".storyEdit");
      let ratio = (el.clientHeight - 50) / el.clientWidth;
      let defaultXY = [];
      el.style.height = `${window.innerHeight - 50}px`;
      defaultXY[0] = el.clientWidth;
      defaultXY[1] = el.clientHeight;
      if (ratio <= 1.333) {
        this.screenHorizontal = true;
        tls.style.height = `${defaultXY[1]}px`;
        tls.style.width = "200px";
        defaultXY[0] -= 200;
      } else {
        this.screenHorizontal = false;
        tls.style.width = `${defaultXY[0]}px`;
        tls.style.height = "200px";
        defaultXY[1] -= 200;
      }
      /////////////////////////////////
      if (defaultXY[1] * 3 > defaultXY[0] * 4) {
        pg.style.width = `${defaultXY[0]}px`;
        pg.style.height = `${(defaultXY[0] * 4) / 3}px`;
        pg.style.marginLeft = "0px";
        if (ratio <= 1.333) {
          pg.style.marginTop = `${defaultXY[1] / 2 - pg.clientHeight / 2}px`;
          pg.style.marginBottom = 0;
        } else {
          pg.style.marginTop = 0;
          pg.style.marginBottom = `${defaultXY[1] / 2 - pg.clientHeight / 2}px`;
        }
      } else {
        pg.style.height = `${defaultXY[1]}px`;
        pg.style.width = `${(defaultXY[1] * 3) / 4}px`;
        pg.style.marginTop = "0px";
        pg.style.marginBottom = "0px";
        pg.style.marginLeft = `${defaultXY[0] / 2 - pg.clientWidth / 2}px`;
      }
    },
    moveObj(e, pg, target) {
      target.style.left = `${Math.max(
        0,
        Math.min(
          100 - (target.clientWidth / pg.clientWidth) * 100,
          ((e.screenX - this.dragXY[0]) / pg.clientWidth) * 100
        )
      )}%`;
      target.style.top = `${Math.max(
        0,
        Math.min(
          100 - (target.clientHeight / pg.clientHeight) * 100,
          ((e.screenY - this.dragXY[1]) / pg.clientHeight) * 100
        )
      )}%`;
      this.act({ target });
      this.resizerFunc(target);
      if (!(this.active === "con1" || this.active === "mainImg")) {
        this.removerMove(target);
      }
    },
    act(e) {
      // 타겟 찾기
      let tar;
      if (e.target.classList[0] !== "sticker" && e.target.id === "") {
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
        if (!(this.active === "" || this.active === "playground")) {
          this.resizerFunc(tar);
          if (!(this.active === "con1" || this.active === "mainImg")) {
            this.$nextTick(() => this.removerMove(tar));
          }
        }
        tar.classList.add("active");
      }
    },
    resizerFunc(item) {
      this.$nextTick(() => {
        let resizer = [
          document.querySelector("#dotLT"),
          document.querySelector("#dotRT"),
          document.querySelector("#dotRB"),
          document.querySelector("#dotLB"),
        ];
        this.resizerMove(resizer, item);
        let pg = document.querySelector("#playground");
        const pgWH = [pg.clientWidth / 100, pg.clientHeight / 100];
        // LT
        resizer[0].onmousedown = (e) => {
          const resizeXY = [e.screenX, e.screenY];
          const originWH = [item.clientWidth, item.clientHeight];
          const originLT = [item.offsetLeft, item.offsetTop];
          document.onmousemove = (e) => {
            const move = [e.screenX - resizeXY[0], e.screenY - resizeXY[1]];
            item.style.width = `${(0, (originWH[0] - move[0]) / pgWH[0])}%`;
            item.style.left = `${(originLT[0] + move[0]) / pgWH[0]}%`;
            item.style.top = `${(originLT[1] + move[1]) / pgWH[1]}%`;
            item.style.height = `${(originWH[1] - move[1]) / pgWH[1]}%`;
            this.resizerMove(resizer, item);
          };
          document.onmouseup = () => {
            document.onmousemove = null;
          };
        };
        // RT
        resizer[1].onmousedown = (e) => {
          const resizeXY = [e.screenX, e.screenY];
          const originWH = [item.clientWidth, item.clientHeight];
          const originLT = [item.offsetLeft, item.offsetTop];
          document.onmousemove = (e) => {
            const move = [e.screenX - resizeXY[0], e.screenY - resizeXY[1]];
            item.style.width = `${(originWH[0] + move[0]) / pgWH[0]}%`;
            item.style.top = `${(originLT[1] + move[1]) / pgWH[1]}%`;
            item.style.height = `${(originWH[1] - move[1]) / pgWH[1]}%`;
            this.resizerMove(resizer, item);
          };
          document.onmouseup = () => {
            document.onmousemove = null;
          };
        };
        // RB
        resizer[2].onmousedown = (e) => {
          const resizeXY = [e.screenX, e.screenY];
          const originWH = [item.clientWidth, item.clientHeight];
          document.onmousemove = (e) => {
            const move = [e.screenX - resizeXY[0], e.screenY - resizeXY[1]];
            item.style.width = `${(originWH[0] + move[0]) / pgWH[0]}%`;
            item.style.height = `${(originWH[1] + move[1]) / pgWH[1]}%`;
            this.resizerMove(resizer, item);
            if (!(this.active === "con1" || this.active === "mainImg")) {
              this.removerMove(item);
            }
          };
          document.onmouseup = () => {
            document.onmousemove = null;
          };
        };
        // LB
        resizer[3].onmousedown = (e) => {
          const resizeXY = [e.screenX, e.screenY];
          const originWH = [item.clientWidth, item.clientHeight];
          const originLT = [item.offsetLeft, item.offsetTop];
          document.onmousemove = (e) => {
            const move = [e.screenX - resizeXY[0], e.screenY - resizeXY[1]];
            item.style.width = `${(originWH[0] - move[0]) / pgWH[0]}%`;
            item.style.left = `${(originLT[0] + move[0]) / pgWH[0]}%`;
            item.style.height = `${(originWH[1] + move[1]) / pgWH[1]}%`;
            this.resizerMove(resizer, item);
          };
          document.onmouseup = () => {
            document.onmousemove = null;
          };
        };
      });
    },
    resizerMove(resizer, item) {
      let pg = document.querySelector("#playground");
      resizer[0].style.left = `${pg.offsetLeft + item.offsetLeft - 2}px`;
      resizer[0].style.top = `${item.offsetTop + pg.offsetTop - 2}px`;
      resizer[1].style.left = `${
        pg.offsetLeft + item.offsetLeft + item.clientWidth - 2
      }px`;
      resizer[1].style.top = `${item.offsetTop + pg.offsetTop - 2}px`;
      resizer[2].style.left = `${
        pg.offsetLeft + item.offsetLeft + item.clientWidth - 2
      }px`;
      resizer[2].style.top = `${
        item.offsetTop + pg.offsetTop + item.clientHeight - 2
      }px`;
      resizer[3].style.left = `${pg.offsetLeft + item.offsetLeft - 2}px`;
      resizer[3].style.top = `${
        item.offsetTop + pg.offsetTop + item.clientHeight - 2
      }px`;
    },
    onEditText(item) {
      if (this.editText !== item.id) {
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
          if (e.target.classList[0] !== "contentt") {
            this.saveEditor(this.editText);
          }
        };
      }
    },
    saveEditor(id) {
      document.querySelector("#" + id).innerHTML = this.editor.con;
      this.editText = "";
      document.querySelector("#playground").onclick = null;
    },
    saveAll() {
      let data = {
        id:this.storyNum,
        title:this.title,
        writer: this.writer,
        content0:this.pageData[0],
        content1:this.pageData[1],
        content2:this.pageData[2],
        content3:this.pageData[3],
        content4:this.pageData[4],
      }
      Axios.put(`${url}storys/edit/`,data).then(()=>{
        this.$router.push('/MyStory')
      })
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.storyEdit {
  margin: 0;
  margin-top: 50px;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
  width: 100vw;
  display: flex;
  align-content: center;
  justify-content: flex-start;
  overflow: hidden;
  background-color: #777;
  #tools {
    padding: 0;
    margin: 0;
    list-style: none;
    display: flex;
    justify-content: space-between;
    background-color: white;
    border-right: 2px black solid;
    border-top: 2px black solid;
    li {
      padding: 5px;
      border: 1px solid gray;
      flex-grow: 1;
      border-radius: 10px;
      &:hover {
        cursor: pointer;
      }
      &.select {
        border: red 2px solid;
      }
    }
  }
  #sPanel {
    background-color: ivory;
    border: #555 2px solid;
    border-radius: 15px;
    box-shadow: black 2px 2px 5px;
    width: 90vw;
    height: 80vh;
    position: fixed;
    top: 16vh;
    left: 5vw;
    padding: 30px;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 102;
    h3 {
      width: 100%;
    }
    img {
      margin: 10px;
      height: 150px;
      &:hover {
        cursor: pointer;
        border: 1px black solid;
        background-color: #ccc;
      }
    }
  }
  #pagePanel {
    background-color: ivory;
    border: #555 2px solid;
    border-radius: 15px;
    box-shadow: black 2px 2px 5px;
    width: 90vw;
    height: 80vh;
    position: fixed;
    top: 16vh;
    left: 5vw;
    padding: 30px;
    overflow-y: auto;
    overflow-x: hidden;
    display: flex;
    flex-flow: row wrap;
    align-content: flex-start;
    z-index: 102;
    h3 {
      width: 100%;
    }
    div {
      margin: 10px;
      height: 32vmin;
      width: 24vmin;
      min-height: 160px;
      min-width: 120px;
      background-color: white;
      position: relative;
      &:hover {
        cursor: pointer;
        border: 1px black solid;
        background-color: #ccc;
      }
    }
  }
  #savePanel {
    background-color: ivory;
    border: #555 2px solid;
    border-radius: 15px;
    box-shadow: black 2px 2px 5px;
    width: 90vw;
    position: fixed;
    top: 16vh;
    left: 5vw;
    padding: 30px;
    overflow-y: auto;
    overflow-x: hidden;
    display: flex;
    flex-flow: row wrap;
    align-content: flex-start;
    z-index: 102;
    h3 {
      width: 100%;
    }
    span {
      width: 100%;
      display: flex;
    }
    input {
      flex-grow: 1;
      border: #555 1px solid;
      margin: 6px;
      padding: 3px;
      border-radius: 5px;
      background-color: white;
    }
    button {
      border: #555 1px solid;
      margin: 6px;
      padding: 3px;
      border-radius: 5px;
      background-color: #ffffaa;
    }
  }
  #playground {
    position: relative;
    background-color: white;
    .active:hover {
      cursor: move;
    }
    .active {
      border: 1px solid black;
    }
    .contentt {
      overflow: visible;
    }
  }
  #remover {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    position: fixed;
    z-index: 105;
    &:hover {
      cursor: pointer;
    }
  }
  #resizer {
    div {
      width: 7px;
      height: 7px;
      background-color: white;
      border: 1px solid black;
      // border-radius: 50%;
      position: fixed;
      z-index: 105;
    }
    #dotLT,
    #dotRB:hover {
      cursor: se-resize;
    }
    #dotRT,
    #dotLB:hover {
      cursor: sw-resize;
    }
  }
}
</style>
