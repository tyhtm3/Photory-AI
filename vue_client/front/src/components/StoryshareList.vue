<template>
<div id="storysharelist">
  <div id="gallery_layout">
    <div class="gallery_content" v-for="index in num"  v-bind:key="index">
      <div id ="imgbox" style="float: left; position: relative;">
        <div class="front"><img src="@/assets/book.png" alt="travel_img"></div>
        <div id="back" style="position: absolute;  left: 58px;  top: 33px;  width: 55%; height: 63%;"><img src="@/assets/book_cover.png" alt="travel_img"></div>
      </div>
      <div class="content">
            <h1>book {{index}}</h1>
            <p>{{index}}</p>
      </div>
      <div class="overlay darkBlue"></div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data: () => ({
    num : 10,
  }),
}
</script>

<style>

@import url(https://cdn.rawgit.com/openhiun/hangul/14c0f6faa2941116bb53001d6a7dcd5e82300c3f/nanumbarungothic.css); 

* {
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
      margin: 0;
      padding: 0;
  }

  body {
      font-family: "Nanum Barun Gothic", "Ubuntu Condensed", "Noto Sans Korean";;
  }

  .gallery_content:hover .overlay.right {
      top: 0;
  }
   #storysharelist{
    background-image:url("../assets/hill.png");
		background-size : cover;
  }
  #gallery_layout {
      width: 1200px;
      margin: 0 auto;
  }

  #gallery_layout:after {
      content: "";
      display: block;
      clear: both;
  }

  .gallery_content {
      position: relative;
      float: left;
      width: 20%;
      overflow: hidden;
  }

  .gallery_content img {
      width: 80%;
      height: 80%;
      display: block;
      margin: 0 auto;
      transition: all 1s ease-in-out;
  }

  .content {
      z-index: 1;
      display: none;
      color: #fff;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
  }

  .content h1 {
      font-size: 1.2em;
      text-transform: uppercase;
      text-align: center;
  }
  .content p {
      padding: 2px 0;
      font-size: 0.8em;
      text-align: center;
  }        
  .gallery_content:hover .content {
      display: block;
      transition: all 1s ease-in-out;
  }

  .gallery_content:hover img {
      transform: scale(1.2);
      transition: all 1s ease-in-out;
  }

  .overlay {
      display: none;
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      transition: top 0.3s, right 0.3s, bottom 0.3s, left 0.3s;
  }

  /* overlay color */
  .overlay.darkBlue {
      background-color:rgba(31, 50, 99, 0.6);
  }
  .overlay.gold {
      background-color:rgba(216, 177, 126, 0.5);
  }  
  .overlay.pink {
      background-color:rgba(255, 113, 181, 0.7);
  }  
  .overlay.black {
      background-color: rgba(0, 0, 0, 0.5);
  }  
  .overlay.yellow {
      background-color: rgba(103, 58, 183, 0.5);
  }
  .overlay.red {
      background-color: rgba(244, 67, 54, 0.5);
  }      

  .gallery_content:hover .overlay {
      display: block;
      transition: all 0.5s ease-in-out;
  }

  @media all and (min-width: 1200px) {
      #gallery_layout {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
      }  
  }

  @media all and (max-width: 1200px) {
  #gallery_layout {
      width: 100%;
  }
  .gallery_content {
      width: 50%;
  }

  }
  @media all and (max-width: 499px) {
  #gallery_layout {
      width: 100%;
  }
  .gallery_content {
      width: 100%;
  }
  /* #imgbox {
    float: left;
    position: relative;
  }
  #back {
    position: absolute;
    top:10%;
    left: 0;
  } */

}
</style>
