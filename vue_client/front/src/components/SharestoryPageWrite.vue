<template>
  <div>
    <h1>lakfjsdljksfldkjsalfjsdl</h1>
    <EditorTipTap :description="description" :menubar="menubar" :readOnly="readOnly"/>
  </div>
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
  
</style>