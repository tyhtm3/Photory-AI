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
      <img @click="()=>$router.push('/sharestorylist').catch(()=>{})" src="@/assets/asset/raccoongolist.png" style="max-width:350px; width:30vw;">
  </div>
  <div class = "d-none d-md-block">
    <v-btn
        class="mx-2"
        id="leftbtn"
        fab
        color="#57bcc4"
        small
        depressed
        height="100"
        width="100"
        style="left: 50px;"
    >
        <v-icon
            color="#c4e86b"
            size=80
        >
            mdi-arrow-left
        </v-icon>
    </v-btn>
    <v-btn
        class="mx-2"
        id="rightbtn"
        fab
        color="#57bcc4"
        small
        depressed
        height="100"
        width="100"
        style="right: 50px;"
    >
        <v-icon
            color="#c4e86b"
            size =80
        >
            mdi-arrow-right
        </v-icon>
    </v-btn>
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
      <EditorTipTap :description="description" :menubar="menubar" :readOnly="readOnly"/>
      </v-col>
      <v-col cols="4">
        <v-btn
              color="#bbe454"
              dark
              rounded
              @click="()=>$router.push('/sharestorypagestory').catch(()=>{})"
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
import EditorTipTap from '@/components/EditorTipTap.vue'
export default {
  components:{
    EditorTipTap,
  },
  data: () => ({
    description:"내용1.",
    menubar:false,
    readOnly:true,
    title:"제목1",
    storytitle:"글 스토리 제목"
  }),
  methods :{
    updateboard(){
      alert("수정하기")
    },
    deleteboard(){
     alert("삭제하기")
    },
   
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