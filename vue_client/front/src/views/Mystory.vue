<template>
  <div id="Mystory">
    <div id="storyList">
      <img
        v-for="book in list"
        :key="book.id"
        class="bookCover"
        :class="{ editable: !book.editable }"
        :src="`${url}media/${book.images[0]}`"
        style=""
        alt=""
      />
      <div id="listIndex">{{ list }}</div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
const url = "http://127.0.0.1:8000/";

export default {
  // 사진이름 url/stpk_photonum_styleNum.jpg
  // story_pk/
  name: "Mystory",
  data() {
    return {
      list: [],
      update: 0,
      url: url,
    };
  },
  created() {
    let config = {
      headers: {
        Authorization: `JWT ${this.$store.state.token}`,
      },
    };

    axios.get(url + "storys/", config).then((res) => {
      this.list = res.data;
      this.list.forEach((item) => {
        item.images.sort();
      });
    });
    // this.update = setInterval(() => {
    //   axios.get(url + "storys/",config).then((res) => {
    //     this.list = res.data;
    //     this.list.forEach((item) => {
    //       item.images.sort();
    //     });
    //   });
    // }, 5000);
  },
};
</script>
<style lang="scss">
#Mystory {
  height: 100%;
  overflow: hidden;
  width: 100vw;
  #storyList {
    padding: 15px;
    width: 100vw;
    height: 100vh;
    transform: translateY(50px);
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
    align-content: flex-start;
    background-color: rgba($color: #999, $alpha: 0.6);
    .bookCover {
      height: 20vmin;
      width: 15vmin;
      min-height: 140px;
      min-width: 105px;
      margin: 0 10px 20px 10px;
    }
  }
}
</style>