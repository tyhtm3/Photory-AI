<template>
  <v-container style="text-align: -webkit-center;">
    <v-row style="height:10vh" >
      <v-col>
        <div class="back">
          <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
        </div>
      </v-col>
    </v-row>
    <v-row justify="center" id="write" >
      <v-col cols="6" id="data">
        <v-text-field
            v-model="boardData.title"
            counter="25"
          ></v-text-field>
      </v-col>
      <v-col cols="10" id="editor">
        <v-textarea
          clearable
          clear-icon="mdi-close-circle"
          v-model="boardData.content"
          no-resize
          solo
          flat
        ></v-textarea>
      </v-col>
      <v-col cols="12"
      >
        <v-row
        justify="center">
          <v-col cols="2">
            <v-btn
              color="#87c7c6"
              dark
              rounded
              @click="update"
            >
              수정하기 
              <v-icon>
                mdi-arrow-right-thick
              </v-icon>
            </v-btn>
          </v-col>
          <v-col cols="2">
            <v-btn
              color="#f48a8e"
              dark
              rounded
              @click="()=>$router.push('/sharestorylist').catch(()=>{})"
            >
              취소하기 
              <v-icon>
                mdi-arrow-right-thick
              </v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="4">
        <v-btn
              color="#bbe454"
              dark
              rounded
              @click="bringStory"
            >
              내 스토리 가져오기 
              <v-icon>
                mdi-arrow-right-thick
              </v-icon>
            </v-btn>
      </v-col>
      <v-col cols="6" style="padding-top: 0px;">
        <v-text-field
            v-model="storytitle"
            disabled
        ></v-text-field>
      </v-col>
    </v-row>
     <v-dialog
      v-model="dialogSelect"
      scrollable
      max-width="300px"
    >
      <v-card>
        <v-card-title>Select Story</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 100px;">
          <v-select v-model="selectedstoryid" :items="bookList" item-value="id" item-text="title" >
            <template v-slot:item="{ item }">
            <span>{{ item.title }}</span>
            </template>
          </v-select>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
            @click="dialogSelect = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="saveselectstory"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
 
  </v-container>
</template>
<script>
import axios from 'axios'
import router from '../router'
export default {
  data: () => ({
    boardNum:'',
    boardData:[],
    description:"내용을 입력해주세요",
    title:"제목",
    storytitle:"내 스토리 제목",
    dialogSelect:false,
    bookList: [{'id':1, title :'story',writer:'방냥이'},{'id':2, title :'story2',writer:'방냥이'},{'id':3, title :'story3',writer:'방냥이'}],
    Stories: ['story1', 'story2', 'story3', 'story4'],
    selectedstory:'',
    selectedstoryid:'',
    storycover:'',
  }),
  methods :{
    update(){
      const TOKEN = this.$store.state.token
      const config = {
          headers: { 'Authorization': 'jwt ' + TOKEN }
      }
      const updateinfo = {
        'title' : this.boardData.title,
        'writer' : this.$store.state.user.nickname,
        'content' : this.boardData.content,
        'category' :1,
        'nickname' : this.$store.state.user.id,
        'story' : this.selectedstoryid,
        'bookcover': null,
      }
      axios.put(`http://127.0.0.1:8000/board/${this.boardNum}/ `, updateinfo, config, { "Content-Type": "application-json" })
          .then(res => {
              console.log(res.data);
              router.push('/sharestorylist').catch(()=>{})
          })
          .catch((error) => {
              console.log(error.response);
          })
    },
    saveselectstory(){
      axios.get(`http://127.0.0.1:8000/storys/books/${this.selectedstoryid}/`)
      .then((res) => {
        this.storytitle = res.data.title;
        this.storycover = res.data.content0;
      });
      this.dialogSelect = false
    },
    bringStory(){
      if(this.Stories===undefined || this.Stories ===null){
        alert("가져올 스토리가 없습니다.")
      }else{
        this.dialogSelect = true
      }
      // this.dialogSelect =true;
    }
  },
  created(){
    const TOKEN = this.$store.state.token
    const config = {
        headers: { 'Authorization': 'jwt ' + TOKEN }
    }
    axios.get(`http://127.0.0.1:8000/storys/books/`, config)
      .then((res) => {
        this.bookList = res.data;
        this.Stories = res.data.title;
        console.log(this.Stories)
      });

    this.boardNum = this.$route.params.boardNum;
    axios.get(`http://127.0.0.1:8000/board/${this.boardNum}/detail/ `, { "Content-Type": "application-json" })
      .then(res => {
          this.boardData = res.data
      })
      .catch((error) => {
          console.log(error.response.data);
      })
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
}

 
</style>