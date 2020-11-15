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
      <v-col cols="6" id="title">
        <v-text-field
            v-model="title"
            counter="25"
          ></v-text-field>
      </v-col>
      <v-col cols="10" id="editor">
      <!-- <EditorTipTap :description="description" :menubar="menubar" :readOnly="readOnly"/> -->
        <v-textarea
          clearable
          clear-icon="mdi-close-circle"
          v-model="description"
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
              @click="write"
            >
              등록하기 
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
              @click="dialogSelect = true"
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
           <v-select
          :items="Stories"
          label="Story"
          v-model="selectedstroy"
        ></v-select>
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
// import EditorTipTap from '@/components/EditorTipTap.vue'
export default {
  components:{
    // EditorTipTap,
  },
  data: () => ({
    description:"내용을 입력해주세요",
    menubar:true,
    readOnly:false,
    title:"제목",
    storytitle:"내 스토리 제목",
    dialogSelect:false,
    Stories: ['story1', 'story2', 'story3', 'story4'],
    selectedstroy:'',
  }),
  methods :{
    write(){
      const TOKEN = this.$store.state.token
      const config = {
          headers: { 'Authorization': 'jwt ' + TOKEN }
      }
      const writeinfo = {
        'title' : this.title
      }
      axios.post(`http://127.0.0.1:8000/board/create/ `, config, writeinfo, { "Content-Type": "application-json" })
          .then(res => {
              console.log(res.data);
          })
          .catch((error) => {
              console.log(error.response);
          })
    },
    selectmystory(){

    },
    saveselectstory(){
      this.dialogSelect = false
      this.storytitle = this.selectedstroy
    }
  }
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