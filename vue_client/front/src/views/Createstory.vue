<template>
  <div class="Createstory" :style="{ height: `${hei}px` }">
    <div id="filmForm">
      <svg :height="Math.max(0, hei - 100)" :width="wid">
        <path
          :d="`M 0 ${hei / 5} q ${wid / 2} ${hei / 5} ${wid} 0`"
          stroke="#000"
          stroke-width="3"
          fill="none"
        />
      </svg>
      <ul v-show="wid < hei" id="filmSelector">
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
      </ul>
      <div id="films" v-for="pic in pics" :key="pic.id">
        <div
          class="film"
          :id="`pic${pic.id}`"
          :style="{ top: `${pic.y + 50}px`, left: `${pic.x}px` }"
        >
          <img class="fil" src="@/assets/film.png" />
          <img
            :id="`file${pic.id}Preview`"
            class="preview"
            src="data:image/bmp;base64,Qk1CAAAAAAAAAD4AAAAoAAAAAQAAAAEAAAABAAEAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wAAAAAA"
            alt=""
          />
          <label :for="`file${pic.id}`">사진 올리기</label>
          <input
            type="file"
            :id="`file${pic.id}`"
            accept=".jpg, .jpeg, .png, .bmp"
          />
        </div>
      </div>
    </div>
    <div id="screen"></div>
    <button id="next" @click="story_init">다음</button>
  </div>
</template>

<script>
import axios from "axios";
const url = "http://127.0.0.1:8000/";

export default {
  name: "Createstory",
  data() {
    return {
      wid: 0,
      hei: 0,
      pics: [
        {
          id: 0,
          x: 0,
          y: 0,
          src: "",
        },
        {
          id: 1,
          x: 30,
          y: 0,
          src: "",
        },
        {
          id: 2,
          x: 50,
          y: 0,
          src: "",
        },
        {
          id: 3,
          x: 70,
          y: 0,
          src: "",
        },
        {
          id: 4,
          x: 90,
          y: 0,
          src: "",
        },
      ],
      picIdx: 0,
      fileList: {
        file0Preview: 0,
        file1Preview: 0,
        file2Preview: 0,
        file3Preview: 0,
        file4Preview: 0,
      },
    };
  },
  created() {
    window.addEventListener("resize", this.reCalc);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.reCalc);
  },
  mounted() {
    this.reCalc();
    [0, 1, 2, 3, 4].forEach((item) => {
      document
        .querySelector(`#file${item}`)
        .addEventListener("change", this.upImg);
    });
  },
  methods: {
    upImg(e) {
      let file = e.target.files[0];
      if (file) {
        let preview = document.querySelector(`#${e.target.id}Preview`);
        let reader = new FileReader();
        reader.onload = () => {
          preview.src = reader.result;
        };
        reader.readAsDataURL(file);
        this.fileList[`${e.target.id}Preview`] = file;
      }
    },
    reCalc() {
      this.wid = window.innerWidth;
      this.hei = Math.max(0, window.innerHeight - 100);
      let card = this.hei * 0.3 * 0.4;
      this.pics.forEach((item, index) => {
        item.x = -card + (this.wid / 6) * (index + 1);
        item.y = this.hei / 5 - (index - 2) * (index - 2) * 8;
        // const fForm = document.querySelector("#filmForm");
        const itemDiv = document.querySelector(`#pic${item.id}`);
        itemDiv.childNodes.forEach((i) => {
          i.onmouseenter = () => {
            itemDiv.querySelector("img").style.height = "40vh";
            itemDiv.querySelector(".preview").style.top = "8vh";
            itemDiv.querySelector(".preview").style.left = "5.6vh";
            itemDiv.querySelector(".preview").style.height = "23.4vh";
            itemDiv.querySelector(".preview").style.width = "26.7vh";
            itemDiv.style.zIndex = "9";
            if (window.innerWidth < itemDiv.clientWidth + itemDiv.offsetLeft) {
              itemDiv.style.left = `${
                window.innerWidth - itemDiv.clientWidth
              }px`;
            }
          };
          i.onmouseout = () => {
            itemDiv.querySelector("img").style.height = "30vh";
            itemDiv.querySelector(".preview").style.top = "6.1vh";
            itemDiv.querySelector(".preview").style.left = "4.2vh";
            itemDiv.querySelector(".preview").style.height = "17.5vh";
            itemDiv.querySelector(".preview").style.width = "20vh";
            itemDiv.style.zIndex = `${item.id}`;
            itemDiv.style.left = `${-card + (this.wid / 6) * (index + 1)}px`;
          };
        });
      });
      if (this.wid < this.hei) {
        document.querySelectorAll("#filmSelector li").forEach((item, index) => {
          item.onclick = () => {
            for (let i = 0; i < 5; i++) {
              let itemDiv = document.querySelector(`#pic${i}`);
              if (index === i) {
                itemDiv.querySelector("img").style.height = "40vh";
                itemDiv.querySelector(".preview").style.top = "8vh";
                itemDiv.querySelector(".preview").style.left = "5.6vh";
                itemDiv.querySelector(".preview").style.height = "23.4vh";
                itemDiv.querySelector(".preview").style.width = "26.7vh";
                itemDiv.style.zIndex = "9";
                if (
                  window.innerWidth <
                  itemDiv.clientWidth + itemDiv.offsetLeft
                ) {
                  itemDiv.style.left = `${
                    window.innerWidth - itemDiv.clientWidth
                  }px`;
                }
              } else {
                itemDiv.querySelector("img").style.height = "30vh";
                itemDiv.querySelector(".preview").style.top = "6.1vh";
                itemDiv.querySelector(".preview").style.left = "4.2vh";
                itemDiv.querySelector(".preview").style.height = "17.5vh";
                itemDiv.querySelector(".preview").style.width = "20vh";
                itemDiv.style.zIndex = `${i}`;
                itemDiv.style.left = `${-card + (this.wid / 6) * (i + 1)}px`;
              }
            }
          };
        });
      }
    },
    story_init() {
      let config = {
        headers: {
          Authorization: `JWT ${this.$store.state.token}`,
        },
      };
      if (Object.values(this.fileList).includes(0)) {
        alert("사진을 모두 넣어 주세요");
      } else {
        axios.post(url + "storys/init/", {},config).then((res) => {
          //res.data.pk
          if (res.data.status) {
            let idx = 0;
            // console.log(this.fileList.values());
            for (let key in this.fileList) {
              let formData = new FormData();
              formData.append("file", this.fileList[key]);
              formData.append("fileName", `file${idx}`);
              idx++;
              axios
                .post(url + "storys/images/" + res.data.pk + "/", formData, {
                  headers: {
                    accept: "application/json",
                    "Content-Type": "multipart/form-data",
                    Authorization: `JWT ${this.$store.state.token}`,
                  },
                })
                .then((res) => {
                  console.log(res.data);
                  if (res.data.last) {
                    this.$router.push("/MyStory");
                  }
                });
            }
          }
        });
      }
    },
    debug() {
      axios.post(url + "storys/init/").then((res) => {
        document.querySelector("#debugForm").innerHTML = res.data;
        console.log(res.data);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.Createstory {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  svg {
    box-sizing: border-box;
    padding: 0;
  }
  #films {
    .film {
      position: absolute;
      display: flex;
      flex-flow: column;
      align-items: center;
      height: 30vh;
      .fil {
        height: 30vh;
        width: auto;
      }
      .preview {
        position: absolute;
        top: 6.1vh;
        left: 4.2vh;
        height: 17.5vh;
        width: 20vh;
      }
      input {
        position: relative;
        top: -5vh;
        text-align: center;
        overflow: hidden;
        width: 1px;
        height: 1px;
      }
      label {
        position: relative;
        top: -6vh;
        font-size: 2vh;
        line-height: 2vh;
        border: 1px solid green;
        background-color: greenyellow;
        border-radius: 7px;
        padding: 3px;
      }
    }
  }
  #filmSelector {
    position: fixed;
    bottom: 20vh;
    left: 0;
    width: 100vw;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    list-style: none;
    li {
      border: 2px solid blue;
      border-radius: 50%;
      width: 44px;
      height: 44px;
      font-size: 20px;
      line-height: 20px;
      text-align: center;
      padding: 10px;
      &:hover {
        cursor: pointer;
      }
    }
  }
  #next {
    position: fixed;
    bottom: 10vh;
    left: 0;
    width: 100vw;
  }
}
</style>
