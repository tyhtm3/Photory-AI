<template>
  <div>
    <!-- nav bar sm 보다 클 때 -->
    <v-app-bar 
      color="#FFFFFF" dense flat fixed
      class="d-none d-sm-block"
    >
      <v-toolbar-title style="cursor: pointer;padding-top: 10px;" @click="()=>$router.push('/')">
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

      <v-btn text @click="()=>$router.push('/ShareStory')">
        <v-col style="color: black" >Share Story</v-col>
      </v-btn>

      <v-btn text @click="()=>$router.push('/CreateStory')">
        <v-col style="color: black">Create Story</v-col>
      </v-btn>
      
      <v-btn text @click="()=>$router.push('/MyStory')">
        <v-col style="color: black">My Story</v-col>
      </v-btn>
      
      <!-- 로그인 한 후 -->
      <!-- 사용자 정보 받아와서 유저 아이콘 해놓기 -->
      <v-tooltip bottom v-if="isLogin=='성공'">
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            v-bind="attrs"
            v-on="on"
            @click="logout"
          >
            mdi-account-circle
          </v-icon>
        </template>
        <span>Logout</span>
      </v-tooltip>
      
      <!-- 로그인 하기전 -->
      <v-tooltip bottom v-else>
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
      <v-btn icon>
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>
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
          <v-list-item @click="()=>$router.push('ShareStory')">
            <v-list-item-title>SHARESTORY</v-list-item-title>
          </v-list-item>
                  <v-list-item @click="()=>$router.push('CreateStory')">
            <v-list-item-title>CREATESTORY</v-list-item-title>
          </v-list-item>
        <v-list-item @click="()=>$router.push('MyStory')">
            <v-list-item-title>MYSTORY</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <!-- 로그인 Popup -->
    <Login v-bind:logindialog="logindialog" v-on:close-login="closeLogin" v-on:open-login="openLogin"/>
  </div>
</template>

<script>
import Login from '../components/Login.vue'
import { mapActions, mapGetters } from 'vuex'
const loginStore = 'loginStore'
export default {
  name: 'Navbar',
  components:{
    Login
  },
  data: () => ({
      drawer: false,
      group: null,
      logindialog : false,
    }),
  // 로그인 확인하기
  computed:{
      ...mapGetters(loginStore, [
      'isLogin',
      'userInfo'
      ]),
  },
  watch: {
    group () {
      this.drawer = false
    },
  },
  
  methods : {
    ...mapActions(loginStore, [
      'logout'
    ]),
    openLogin(){
      this.logindialog = true
    },
    closeLogin(){
      this.logindialog = false
    },
    logout(){
      this.logout()
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
</style>
