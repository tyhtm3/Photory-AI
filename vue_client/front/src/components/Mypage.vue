<template>
    <v-row justify="center">
    <v-dialog
      v-model="mypagedialog"
      max-width="600px"
      content-class="rounded-xl"
      persistent
    >
      <v-card
      >
        <v-system-bar
          color="#FFFFFF">
          <v-spacer></v-spacer>
          <v-icon @click="closeMypage">mdi-close</v-icon>
        </v-system-bar>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="4"
                md="4"
              >
                <v-img :src="require('@/assets/user_bear.png')" />
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="8"
              >
                <v-row>
                  <v-col cols="12"
                  class="d-none d-sm-block">
                  </v-col>
                  <v-col cols="12"
                  class="d-none d-sm-block">
                  </v-col>
                  <v-col cols="10">
                    <v-text-field
                      solo
                      flat
                      value="보통뭐할까"
                      style="font-size : x-large;"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                  
                  <v-icon
                      @click="onupdate"
                    >
                      mdi-comment-edit-outline
                    </v-icon>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12">
                <v-row>
                  <v-col cols="4"
                  class="d-none d-sm-block">
                    E-mail
                  </v-col>
                  <v-col cols="6"
                  class="d-none d-sm-block">
                    <v-text-field
                      label="Email"
                      value="user@user.com"
                      style="font-size : x-large;"
                      required
                      solo
                      flat
                    ></v-text-field>
                  </v-col>
                  <v-col cols="8"
                  class="d-sm-none">
                    <v-text-field
                      label="Email"
                      value="user@user.com"
                      style="font-size : small;"
                      required
                      solo
                      flat
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                    <v-icon
                      @click="onupdate"
                    >
                      mdi-comment-edit-outline
                    </v-icon>
                  </v-col>
                </v-row>
                
              </v-col>
              <v-col cols="12"
              class="d-none d-sm-block">
              <v-row>
                  <v-col cols="5">
                   <v-banner></v-banner>
                  </v-col>
                  <v-col cols="2">
                    <v-img :src="require('@/assets/animal_foot.png')" />
                  </v-col>
                
                  <v-col cols="5">
                  
              <v-banner></v-banner>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12">
                 <v-row>
                  <v-col cols="4"
                   class="d-none d-sm-block">
                  Password
                  </v-col>
                  <v-col cols="6"
                   class="d-none d-sm-block">
                    <v-text-field
                      label="Password"
                      type="password"
                      value="asdfqwer1234"
                      style="font-size : x-large;"
                      required
                      solo
                      flat
                    ></v-text-field>
                  </v-col>
                  <v-col cols="8"
                   class="d-sm-none">
                    <v-text-field
                      label="Password"
                      type="password"
                      value="asdfqwer1234"
                      style="font-size : small;"
                      required
                      solo
                      flat
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                  <v-icon
                      @click="onupdate"
                    >
                      mdi-comment-edit-outline
                    </v-icon>
                  </v-col>
                </v-row>
               
              </v-col>
              
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
    name: 'Mypage',
    data: () => ({
    }),
    props:['mypagedialog'],
    methods:{
      closeMypage (){
        this.$emit('close-mypage');
      },
      openMypage(){
        this.$emit('open-mypage');
      },
      onupdate(){
        alert("변경되었습니다")
      }
    }
  }
</script>

<style>

.v-dialog{
  font-family: 'UhBeeSeulvely';
}
.v-text-field{
  font-size: x-large;
}
div.v-dialog.rounded-xl.v-dialog--active.v-dialog--persistent{
  border: 5px solid #9bd3d0;
}
div.v-card.v-sheet.theme--light{
  overflow: hidden;
}
div.v-image__image.v-image__image--cover{
  border-radius: 50%;
  border: 5px solid #9bd3d0;
}

@media screen and (max-width: 500px) {
  div.col-sm-6.col-md-8.col-12{
    padding-top: 0px;
    padding-bottom: 0px;
    height: 50px;
  }
  div.col.col-12{
    padding-top: 0px;
    padding-bottom: 0px;
    height: 50px;
  }
}
</style>
