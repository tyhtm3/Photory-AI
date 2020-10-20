<template>
  <div>
    <!-- nav bar sm 보다 클 때 -->
    <v-app-bar 
      color="#FFFFFF" dense flat fixed
      class="d-none d-sm-block"
    >
      <v-toolbar-title style="cursor: pointer;padding-top: 10px;" @click="()=>$router.push('/')">
        <img src="@/assets/logo_name.png" alt="logo" style="height: 50px" >
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text @click="()=>$router.push('ShareStory')">
        <v-col style="color: black" >Share Story</v-col>
      </v-btn>

      <v-btn text @click="()=>$router.push('CreateStory')">
        <v-col style="color: black">Create Story</v-col>
      </v-btn>
      
      <v-btn text @click="()=>$router.push('MyStory')">
        <v-col style="color: black">My Story</v-col>
      </v-btn>
      
      <!-- 로그인 하기전 -->
      <v-btn icon>
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>
      <!-- 로그인 한 후 -->
      <!-- 사용자 정보 받아와서 유저 아이콘 해놓기 -->
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
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data: () => ({
      drawer: false,
      group: null,
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
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
