<template>
    <v-row >
        <v-col>
            <div class="back">
                <img src="@/assets/loading/wave.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
            </div>
            <div class="book">
                <img src="@/assets/asset/book2.png" style="max-width: -webkit-fill-available; position: absolute; bottom: 0;left: 0;">
            </div>
            
            <!-- <div class="word">
              <p style="font-family: 'UhBeeSeulvely'; font-size:60px; color:#3ba0a8;">ShareStory</p>
            </div> -->
        </v-col>
    </v-row>
</template>

<script>
export default {
  data: () => ({
  }),
}
</script>

<style>

.book{
    position: absolute;
    bottom: 0;
    left: 50vh;
    width:-webkit-fill-available;
}
.word{
    position: absolute;
    top: 10vh;
    left: 0;
    width:-webkit-fill-available;
}

</style>
