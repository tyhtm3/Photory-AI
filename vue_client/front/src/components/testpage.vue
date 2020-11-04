<template>
<div class="container">
    <div class="box">
        <div class="front">
          <img src="@/assets/hill.png" style="max-width: -webkit-fill-available; height:100vh">
        </div>
        <div class="back">
          <img src="@/assets/loading/wave.svg" style="max-width: -webkit-fill-available;">
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'testpage',
}
</script>

<style>
div.container{
    margin-left: 0;
    margin-right: 0; 
    padding: 0;
    max-width: -webkit-fill-available;
}
.box{
    float: left;
    position: relative;
    max-width: -webkit-fill-available;
}
.back{
    position: absolute;
    top: 0;
    left: 0;
    max-width: -webkit-fill-available;
}
</style>
