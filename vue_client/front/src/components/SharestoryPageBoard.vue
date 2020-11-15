<template>
  <v-container style="text-align: -webkit-center;">
    <v-row style="height:10vh" >
      <v-col>
        <div class="back">
          <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
        </div>
      </v-col>
    </v-row>
    <div class="d-none d-md-block editimg">
    <img @click="updateboard" src="@/assets/asset/edit.png" style="max-width:150px; width:13vw; position: absolute; bottom: 23vh;left: 10vh;">
  </div>
  <div class="d-none d-md-block ani3">
      <img @click="deleteboard" src="@/assets/asset/bearbtn.png" style="max-width:300px; width:30vw; position: absolute; bottom: 0;left: 0;">
  </div>
  <div class="d-none d-md-block ani4">
      <img  @click="()=>$router.push('/sharestorylist').catch(()=>{})" src="@/assets/asset/raccoongolist.png" style="max-width:350px; width:30vw;">
  </div>
    <v-row justify="center" id="write" >
      <v-col cols="6" id="title">
        <v-text-field
            v-model="title"
            counter="25"
            disabled
        ></v-text-field>
      </v-col>
      <v-col cols="10" id="editor">
      <!-- <EditorTipTap :description="description" :menubar="menubar" :readOnly="readOnly" /> -->
      <v-textarea
          clearable
          clear-icon="mdi-close-circle"
          v-model="description"
          no-resize
          solo
          flat
          disabled
        ></v-textarea>
      </v-col>
      <v-col cols="4">
        <v-btn
          color="#bbe454"
          dark
          rounded
          @click="goStory"
        >
          스토리 보러가기 
          <v-icon>
            mdi-arrow-right-thick
          </v-icon>
        </v-btn>
      </v-col>
      <v-col cols="6" style="padding-top: 0px;" class="d-none d-md-block">
        <v-text-field
            v-model="storytitle"
            disabled
        ></v-text-field>
      </v-col>
    </v-row>

  </v-container>
</template>
<script>
// import EditorTipTap from '@/components/EditorTipTap.vue'
import router from "../router"
import axios from 'axios';
export default {
  components:{
    // EditorTipTap,
  },
  data: () => ({
    description:"내용1",
    menubar:false,
    readOnly:true,
    title:"제목1",
    storytitle:"글 스토리 제목",
    boardNum :1,
    boardData:[],
    storydata:[],
    isStroy:false
  }),
  methods :{
    updateboard(){
      if(this.$store.state.isLogin && (this.$store.state.user.id == this.boardData.nickname)){
        router.push(`/sharestoryupdate/${this.boardNum}`).catch(()=>{})
      }else{
        alert("권한이 없습니다.")
      }
    },
    deleteboard(){
      if(this.$store.state.isLogin && (this.$store.state.user.id == this.boardData.nickname)){
        const TOKEN = this.$store.state.token
        const config = {
            headers: { 'Authorization': 'jwt ' + TOKEN }
        }
      axios.delete(`http://127.0.0.1:8000/board/${this.boardNum}/`,config, { "Content-Type": "application-json" })
        .then(res => {
            alert('삭제되었습니다.')
            console.log(res.data)
            router.push('/sharestorylist').catch(()=>{})
        })
        .catch((error) => {
            console.log(error.response.data);
        })
      }else{
        alert("권한이 없습니다.")
      }
      
    },
    goStory(){
      if(this.isStroy){
        let data ={'storyid':this.storydata.id, 'boardid':this.boardNum}
        router.push(`/sharestorypagestory/${data.boardid}/${data.storyid}`).catch(()=>{})
      }else{
        alert("등록된 스토리가 없습니다.")
      }
    },
  },
  created(){
    this.boardNum = this.$route.params.boardNum;
    axios.get(`http://127.0.0.1:8000/board/${this.boardNum}/detail/ `, { "Content-Type": "application-json" })
      .then(res => {
          this.boardData = res.data
          console.log(res.data)
          this.title = this.boardData.title
          this.description = this.boardData.content
      })
      .catch((error) => {
          console.log(error.response.data);
      })
    if(this.boardData.story !== undefined ){
      axios.get(`http://127.0.0.1:8000/storys/books/${this.boardData.story}/ `, { "Content-Type": "application-json" })
     .then(res => {
         this.storydata = res.data
         console.log(res.data)
         this.storytitle = this.storydata.title
         this.isStroy = true;
     })
     .catch((error) => {
         console.log(error.response.data);
     })
    }else{
      this.storytitle = '등록된 스토리가 없습니다.'
    }
  },
}
</script>
<style>
#write{
  background-color: white;
  border: 10px solid rgb(220, 247, 158);
  border-radius: 80px / 40px;
  max-height: 75vh;
  max-width: 1000px;
  height: 1000px;
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
 
</style>