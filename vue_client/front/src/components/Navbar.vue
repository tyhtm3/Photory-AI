<template>
  <div>
    <!-- nav bar sm 보다 클 때 -->
    <v-app-bar 
      color="#FFFFFF" dense flat fixed
      class="d-none d-sm-block"
    >
      <v-toolbar-title style="cursor: pointer;padding-top: 10px;" @click="()=>$router.push('/').catch(()=>{})">
         <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <span
              v-bind="attrs"
              v-on="on"
            >
            <img src="@/assets/logo_name.png" alt="logo" style="height: 50px" >
            </span>
          </template>
          <span>Home</span>
        </v-tooltip>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text @click="()=>$router.push('/sharestorylist').catch(()=>{})">
        <v-col style="color: black" >Share Story</v-col>
      </v-btn>

      <v-btn text @click="()=>$router.push('/CreateStory').catch(()=>{})">
        <v-col style="color: black">Create Story</v-col>
      </v-btn>
      
      <v-btn text @click="()=>$router.push('/MyStory').catch(()=>{})">
        <v-col style="color: black">My Story</v-col>
      </v-btn>
  
      <!-- 로그인 한 후 -->
      <!-- 사용자 정보 받아와서 유저 아이콘 해놓기 -->
      <v-menu
        left
        bottom
        offset-y
        v-if="this.$store.state.isLogin"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <img id = "userimg" :src="imgs[0].image" alt=""> 
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            @click="logout"
          >
            <v-list-item-title style="font-family: 'UhBeeSeulvely';">LOGOUT</v-list-item-title>
          </v-list-item>
          <v-list-item
            @click="openMypage"
          >
            <v-list-item-title style="font-family: 'UhBeeSeulvely';">MYPAGE</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
     <!-- 로그인 하기전 -->
      <v-tooltip bottom  v-if="!this.$store.state.isLogin">
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            v-bind="attrs"
            v-on="on"
            @click="openLogin"
          >
           mdi-account-circle
          </v-icon>
        </template>
        <span>Sign In</span>
      </v-tooltip>
     </v-app-bar>

    <!-- nav bar sm 보다 작을 때 -->
     <v-app-bar
      color="#FFFFFF" dense flat fixed
      class="d-sm-none"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <!-- 로그인 한 후 -->
      <!-- 사용자 정보 받아와서 유저 아이콘 해놓기 -->
      <v-menu
        left
        bottom
        offset-y
        v-if="this.$store.state.isLogin"
        >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <img  id = "userimg" src="@/assets/user_bear.png" alt="">
            <!-- <img id = "userimg" :src="imgs[this.$store.state.user.profile].image" >  -->
          </v-btn>
        </template>

         <v-list>
          <v-list-item
            @click="logout"
          >
            <v-list-item-title style="font-family: 'UhBeeSeulvely';">LOGOUT</v-list-item-title>
          </v-list-item>
          <v-list-item
            @click="openMypage"
          >
            <v-list-item-title style="font-family: 'UhBeeSeulvely';">MYPAGE</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
     
     <!-- 로그인 하기전 -->
        <v-tooltip bottom  v-if="!this.$store.state.isLogin">
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            v-bind="attrs"
            v-on="on"
            @click="openLogin"
          >
           mdi-account-circle
          </v-icon>
        </template>
        <span>Sign In</span>
      </v-tooltip>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      left
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item @click="()=>$router.push('/').catch(()=>{})">
            <v-list-item-title>HOME</v-list-item-title>
          </v-list-item>
          <v-list-item @click="()=>$router.push('/sharestorylist').catch(()=>{})">
            <v-list-item-title>SHARESTORY</v-list-item-title>
          </v-list-item>
          <v-list-item @click="()=>$router.push('/CreateStory').catch(()=>{})">
            <v-list-item-title>CREATESTORY</v-list-item-title>
          </v-list-item>
        <v-list-item @click="()=>$router.push('/MyStory').catch(()=>{})">
            <v-list-item-title>MYSTORY</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <!-- 로그인 Popup -->
    <Login v-bind:logindialog="logindialog" v-on:close-login="closeLogin" v-on:open-login="openLogin"/>
    <Mypage v-bind:mypagedialog="mypagedialog" v-on:close-mypage="closeMypage" v-on:open-mypage="openMypage"/>
  </div>
</template>
<script>
import Login from '../components/Login.vue'
import Mypage from '../components/Mypage.vue'
import store  from '../store/index'
export default {
  name: 'Navbar',
  components:{
    Login,
    Mypage
  },
  data: () => ({
      drawer: false,
      drawer2: false,
      group: null,
      logindialog : false,
      mypagedialog : false,
      imgs: [
      { name: '곰', image:  require('@/assets/user_bear.png'), value:0},
      { name: '사슴', image: require('@/assets/user_deer.png'), value:1},
      { name: '고슴도치', image: require('@/assets/user_hedgehog.png'), value:2},
      { name: '부엉이', image: require('@/assets/user_owl.png'), value:3},
      { name: '토끼', image: require('@/assets/user_rabbit.png'), value:4},
      { name: '너구리', image: require('@/assets/user_raccoon.png'),value:5}],      
    }),
  watch: {
    group () {
      this.drawer = false
    },
  },
  
  methods : {
    openLogin(){
      this.logindialog = true
    },
    closeLogin(){
      this.logindialog = false
    },
    logout(){
      store.dispatch('logout');
    },
    openMypage(){
      this.mypagedialog = true
    },
    closeMypage(){
      this.mypagedialog = false
    },
  }
}
</script>

<style>
@media screen and (max-width: 500px) {
  .v-app-bar {
    float: none;
    display: block;
  }
}
#userimg{
  height: 30px;
  widows: 30px;
}
</style>
