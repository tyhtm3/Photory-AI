<template>
  <div id="Main">
    <div id="hill"  class="d-none d-sm-block">
      <img src="@/assets/hill.png" style="max-width: -webkit-fill-available;">
    </div>
    <div id="hill" class="d-sm-none">
      <img src="@/assets/hill_mini.png" style="max-width: -webkit-fill-available;">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mainpage',
}
</script>

<style>
#hill{
  height: 30vh;
  
}

</style>
