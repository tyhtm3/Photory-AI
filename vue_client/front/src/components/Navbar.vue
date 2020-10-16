<template>
  <div>
    <v-app-bar
      color="#FFFFFF" dense flat fixed
    >
      <v-toolbar-title style="cursor: pointer;padding-top: 10px;" @click="()=>$router.push('/')">
        <img src="@/assets/logo_name.png" alt="logo" style="height: 50px" >
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text @click="()=>$router.push('ShareStory')">
        <v-col style="color: black" >ShareStory</v-col>
      </v-btn>

      <v-btn text @click="()=>$router.push('CreateStory')">
        <v-col style="color: black">CreateStory</v-col>
      </v-btn>
      
      <v-btn text @click="()=>$router.push('MyStory')">
        <v-col style="color: black">MyStory</v-col>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style>

</style>
