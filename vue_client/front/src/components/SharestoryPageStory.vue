<template>
<v-container fluid >
  <div class="back">
    <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
  </div>
  <flipbook class="flipbook" :pages="pages"></flipbook>  
  <div class="d-none d-md-block ani3">
      <img @click="()=>$router.push(`/sharestorypageboard/${this.boardNum}`).catch(()=>{})" src="@/assets/asset/bearbtnback.png" style="max-width:300px; width:30vw; position: absolute; bottom: 0;left: 0;">
  </div>
  <div class="d-none d-md-block ani4">
      <img @click="()=>$router.push('/sharestorylist').catch(()=>{})" src="@/assets/asset/raccoongolist.png" style="max-width:350px; width:30vw;">
  </div>
  {{}}
</v-container>
  
</template>
<script>
import Flipbook from 'flipbook-vue';
import axios from 'axios';
export default {
  components: { Flipbook },
  data :()=>({
    boardNum:'',
    storyId:'',
    storydata:'',
    pages: [
      "/img/logo_name.334d3675.png",
      "/img/logo_name.334d3675.png",
      "/img/logo_name.334d3675.png",
      "/img/logo_name.334d3675.png",
    ],
 }),
  methods:{
    
  },
  created(){
    this.boardNum = this.$route.params.boardNum;
    this.storyId = this.$route.params.storyId;
    axios
      .get(`http://k3a205.p.ssafy.io:8000/storys/books/${this.storyId}/`)
      .then((res) => {
        this.storydata = res.data;
        this.pages[0] =
          "http://k3a205.p.ssafy.io:8000/media" +
          res.data.content[0].split("media")[1];
        this.pages[1] =
          "http://k3a205.p.ssafy.io:8000/media" +
          res.data.content[1].split("media")[1];
        this.pages[2] =
          "http://k3a205.p.ssafy.io:8000/media" +
          res.data.content[2].split("media")[1];
        this.pages[3] =
          "http://k3a205.p.ssafy.io:8000/media" +
          res.data.content[3].split("media")[1];
        this.pages[4] =
          "http://k3a205.p.ssafy.io:8000/media" +
          res.data.content[4].split("media")[1];
      });
  }
}
</script>
<style>
.flipbook {
  width: 90vw;
  height: 90vh;
}
.editimg{
    position: absolute;
    bottom: 0;
    left: 3%;
}
.ani3{
    position: absolute;
    bottom: 0;
    left: 3%;
}
.ani4 img{
    position: fixed;
    bottom: 0;
    right: 3%;
}

#leftbtn{
  position: absolute;
  top: 40%;
}
#rightbtn{
  position: absolute;
  top: 40%;
}
img.page.fixed{
  border: 20px solid rgb(220, 247, 158);
  border-radius: 80px / 40px;
}
</style> 
