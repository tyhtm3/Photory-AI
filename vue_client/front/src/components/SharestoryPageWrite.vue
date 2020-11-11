<template>
  <v-container>
    <v-row style="height:10vh">
      <v-col>
        <div class="back">
          <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
        </div>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="8" id="title">
        <v-text-field
            v-model="title"
            :rules="rules"
            counter="25"
            label="Outlined"
            outlined
            rounded
          ></v-text-field>
      </v-col>
      <v-col cols="8" id="editor">
      <EditorTipTap :description="description" :menubar="menubar" :readOnly="readOnly"/>
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
    description:"글을 적어주세요",
    menubar:true,
    readOnly:false,
  }),
}
</script>
<style>
#title{

}
 #editor{
  background-color: white;
  border: 10px solid rgb(220, 247, 158);
  border-radius: 80px / 40px;
 }
</style>