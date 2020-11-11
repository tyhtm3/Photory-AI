<template>
  <div id="Mystory">
    <img id="bg" src="@/assets/hill.png" alt="">
    <img src="@/assets/loading/wave.png" style="width: 100vw;position:fixed;bottom:0;left:0;height:10%">
    <div id="storyList">
      <img
        v-for="book in list"
        :key="book.id"
        class="bookCover"
        :class="{ editable: !book.editable }"
        :src="`${url}media/${book.images[0]}`"
        style=""
        alt=""
        @click="editStory(book.id)"
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
    // if (this.state.)
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
  methods:{
    editStory(id){
      this.$router.push('EditStory/'+id)
    },
  },
};
</script>
<style lang="scss">
#Mystory {
  height: 100%;
  overflow: hidden;
  width: 100vw;
  #bg{
    position: fixed;
    left: 0;
    top: 50px;
    width: 100vw;
    height: 100vh;
  }
  #storyList {
    padding: 15px;
    width: 100vw;
    height: 100vh;
    transform: translateY(50px);
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
    align-content: flex-start;
    .bookCover {
      height: 20vmin;
      width: 15vmin;
      min-height: 140px;
      min-width: 105px;
      margin: 0 10px 20px 10px;
      &:hover{
        cursor: pointer;
        
      }
    }
  }
}
</style>