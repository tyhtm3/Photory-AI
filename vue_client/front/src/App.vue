<template>
  <v-app id="app">
    <div id="nav">
      <Navbar/>
    </div>
    <!-- 스크롤 없이 윗 공간 주기 위한 div -->
    <!-- <div id="padding">
    </div> -->
    <router-view/>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  components:{
   Navbar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f8f8f0;
}

#nav {
   font-family: UhBeeSeulvely ,Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-bottom: 0px;
}


#padding{
  height: 50px;
}
</style>
