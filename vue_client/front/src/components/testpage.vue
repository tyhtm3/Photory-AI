<template>
<div class="containermain">
    <div class="box">
        <div class="front">
          <img src="@/assets/hill.png" style="max-width: -webkit-fill-available; height:100vh">
        </div>
        <div class="back">
          <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available;">
        </div>
        <div class="effect">
            <img src="@/assets/loading/effect.svg">
        </div>
        <div class="mid">
            <img src="@/assets/loading/logo.svg">
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
div.containermain{
    margin-left: 0;
    margin-right: 0; 
    padding: 0;
    max-width: -webkit-fill-available;
    height: 100vh;
}
.box{
    float: left;
    position: relative;
    max-width: -webkit-fill-available;
    width:-webkit-fill-available;
}
.back{
    position: absolute;
    top: 88vh;
    left: 0;
    width:-webkit-fill-available;
}
.mid{
    position: absolute;
    top: 3vh;
    height: -webkit-fill-available;
    width: -webkit-fill-available;
}
.effect{
    position: absolute;
    top: 0;
    left: 0;
}
</style>
