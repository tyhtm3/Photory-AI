<template>
  <div class="Createstory" :style="{ height: `${hei}px` }">
    <div id="filmForm">
      <svg :height="Math.max(0,hei-100)" :width="wid">
        <path
          :d="`M 0 ${hei / 5} q ${wid / 2} ${hei / 5} ${wid} 0`"
          stroke="#000"
          stroke-width="3"
          fill="none"
        />
      </svg>
      <div id="films" v-for="pic in pics" :key="pic.id">
        <div
          class="film"
          :style="{ top: `${pic.y + 50}px`, left: `${pic.x}px` }"
        >
          <img src="@/assets/film.png" />
          <label :for="`file${pic.id}`">사진 올리기</label>
          <input type="file" :id="`file${pic.id}`" />
        </div>
      </div>
    </div>
    <router-link to="/CreateStory/edit">다음</router-link>
  </div>
</template>

<script>
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
    };
  },
  created() {
    console.log(window.innerHeight);
    window.addEventListener("resize", this.reCalc);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.reCalc);
  },
  mounted() {
    this.reCalc();
  },
  methods: {
    reCalc() {
      this.wid = window.innerWidth;
      this.hei = Math.max(0,window.innerHeight - 100);
      let card = this.hei * 0.3 * 0.4;
      this.pics.forEach((item, index) => {
        item.x = -card + (this.wid / 6) * (index + 1);
        item.y = this.hei / 4 - (index - 2) * (index - 2) * 13;
      });
    },
    debug() {
      this.editMode = !this.editMode;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
.Createstory {
  margin: 0;
  padding: 0;
  padding-top: 50px;
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
      top: 100px;
      left: 0;
      display: flex;
      flex-flow: column;
      align-items: center;
      img {
        height: 30vh;
        width: auto;
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
        top: -5vh;
        border: 1px solid green;
        background-color: greenyellow;
        border-radius: 7px;
        padding: 2px;
      }
    }
  }
}
</style>
