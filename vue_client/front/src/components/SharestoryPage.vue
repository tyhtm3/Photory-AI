<template>
<div>
  <div class="back">
    <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
  </div>
  <flipbook class="flipbook" :pages="pages"></flipbook>  
  <div class="ani3">
      <img src="@/assets/asset/bearbtn.png" style="max-width:300px; width:30vw; position: absolute; bottom: 0;left: 0;">
  </div>
  <div class="ani4">
      <img @click="()=>$router.push('/sharestory').catch(()=>{})" src="@/assets/asset/raccoongolist.png" style="max-width:350px; width:30vw;">
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
</div>
  
</template>
<script>
import Flipbook from 'flipbook-vue'
export default {
  components: { Flipbook },
  data :()=>({
    pages:["https://img.ridicdn.net/cover/1227000018/xxlarge","https://image.aladin.co.kr/product/1520/39/cover500/8981404135_1.jpg","https://i.pinimg.com/564x/05/1f/f3/051ff3fb781ff83c9b0f8a32f9922fa6.jpg","/img/logo_name.334d3675.png",]
  }),
  methods:{
  }
}
</script>
<style>
.flipbook {
  width: 90vw;
  height: 90vh;
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
