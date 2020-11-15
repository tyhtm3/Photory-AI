<template>
    <v-row justify="center">
    <v-dialog
      v-model="mypagedialog"
      max-width="650px"
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
                <v-img v-if="this.$store.state.isLogin" :src="imgs[userInfo.profile].image" />
                <v-icon @click="dialogimg = true"> mdi-comment-edit-outline</v-icon>
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
                      v-if="this.$store.state.isLogin"
                      solo
                      flat
                      v-model="userInfo.nickname"
                      style="font-size : x-large;"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" id="height50">
                <v-row>
                  <v-col cols="4"
                  class="d-none d-sm-block">
                    E-mail
                  </v-col>
                  <v-col cols="6"
                  class="d-none d-sm-block">
                    <v-text-field
                      label="Email"
                      v-if="this.$store.state.isLogin"
                      v-model="userInfo.email"
                      style="font-size : x-large;"
                      required
                      solo
                      flat
                      disabled
                    ></v-text-field>
                  </v-col>
                  <v-col cols="8"
                  class="d-sm-none">
                    <v-text-field
                      label="Email"
                      v-if="this.$store.state.isLogin"
                      v-model="userInfo.email"
                      style="font-size : small;"
                      required
                      solo
                      flat
                      disabled
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                  </v-col>
                </v-row>
                
              </v-col>
              <v-col cols="12"  id="height50">
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
                      style="font-size : x-large;"
                      value="password"
                      required
                      solo
                      flat
                      disabled
                    >
                  </v-text-field>
                  </v-col>
                  <v-col cols="2">
                    <v-icon @click="dialogpwd=true">
                    mdi-comment-edit-outline
                    </v-icon>
                  </v-col>
                  <v-col cols="8"
                   class="d-sm-none">
                    <v-text-field
                      label="Password"
                      type="password"
                      value="password"
                      style="font-size : small;"
                      required
                      solo
                      flat
                    ></v-text-field>
                  </v-col>
                </v-row>
               
              </v-col>
              <v-col cols="4">
                 <v-btn
                  color="#87c7c6"
                  dark
                  rounded
                  @click="onupdate"
                >
                  수정하기 
                  <v-icon>
                    mdi-comment-edit-outline
                  </v-icon>
                </v-btn>
              </v-col>
              <v-col cols="4">
                 <v-btn
                  color="#bbe454"
                  dark
                  rounded
                  @click="deletemember"
                >
                  탈퇴하기 
                  <v-icon>
                    mdi-arrow-right-thick
                  </v-icon>
                </v-btn>
              </v-col>
              <v-col cols="4">
                 <v-btn
                  color="#f48a8e"
                  dark
                  rounded
                  @click="closeMypage"
                >
                  닫기 
                  <v-icon>
                    mdi-arrow-right-thick
                  </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog
        v-model="dialogimg"
        max-width="500px"
      >
        <v-card>
          <v-card-title>
            프로필 이미지 선택하기
          </v-card-title>
          <v-card-text>
            <v-select v-model="imgs.value" :items="imgs" item-value="value" item-text="name" >
               <template v-slot:item="{ item }">
                <img :src="item.image" style="height: 50px;" >
                <span>{{ item.name }}</span>
              </template>
            </v-select>
          </v-card-text>
          <v-card-actions style="justify-content: flex-end;">
            <v-btn
              color="#87c7c6"
              dark
              rounded
              @click="changeimg"
            >
              저장하기
            </v-btn>
           <v-btn
              color="#f48a8e"
              dark
              rounded
                @click="dialogimg = false"
            >
              닫기
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialogpwd"
        max-width="500px"
      >
        <v-card>
          <v-card-title>
            비밀번호 변경하기
          </v-card-title>
          <v-card-text>
             <v-text-field
                v-model="userPwd.password1"
                label="Password"
                style="min-height: 96px"
                type="password"
              ></v-text-field>
              <v-text-field
                v-model="userPwd.password2"
                label="Password 확인"
                style="min-height: 96px"
                type="password"
              ></v-text-field>
          </v-card-text>
          <v-card-actions style="justify-content: flex-end;">
            <v-btn
              color="#87c7c6"
              dark
              rounded
              @click="changepwd"
            >
              저장하기
            </v-btn>
           <v-btn
              color="#f48a8e"
              dark
              rounded
                @click="dialogpwd = false"
            >
              닫기
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex'
import store  from '../store/index'
export default {
    name: 'Mypage',
    data: () => ({
      dialogimg: false,
      dialogpwd: false,
      imgs: [
      { name: '곰', image:  require('@/assets/user_bear.png'), value:0},
      { name: '사슴', image: require('@/assets/user_deer.png'), value:1},
      { name: '고슴도치', image: require('@/assets/user_hedgehog.png'), value:2},
      { name: '부엉이', image: require('@/assets/user_owl.png'), value:3},
      { name: '토끼', image: require('@/assets/user_rabbit.png'), value:4},
      { name: '너구리', image: require('@/assets/user_raccoon.png'),value:5}],
      userPwd : {password1:'',password2:''},
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
        let nickname = this.userInfo.nickname
        let profile = this.userInfo.profile
        const userInfo = {
          'nickname': nickname,
          'profile' : profile
        }
        store.dispatch('updateuser', userInfo);
      },
      deletemember(){
        store.dispatch('deleteuser');
      },
      changeimg(){
        let profile = this.imgs.value
        let nickname = this.$store.state.user.nickname
        const userInfo = {
          'nickname': nickname,
          'profile' : profile
        }
        store.dispatch('changeimg', userInfo);
        this.dialogimg =false
      },
      changepwd(){
        let new_password1 = this.userPwd.password1
        let new_password2 = this.userPwd.password2
        const password = {
          'new_password1': new_password1,
          'new_password2': new_password2,
        }
        store.dispatch('changepwd', password);
        this.dialogpwd =false
      },
    },
    computed:{
      ...mapGetters({
          userInfo : 'user',
      }),
    },
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
#anifoot{
  border-style: none;
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
  }
  #height50{
    height: 50px;
  }
  #imgexample{
    height: 20px;
  }
}
</style>
