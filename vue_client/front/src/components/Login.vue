<template>
  <v-row justify="center">
    <v-dialog
      v-model="logindialog"
      max-width="1000px"
      persistent
    >
       <v-card
        class="mx-auto"
        >
        <v-container>
          <v-row dense>
            <v-col
            class = "d-none d-md-block"
            cols="6"
            >
            <img src="@/assets/loginbackground.png" style="max-width: -webkit-fill-available;" >
            </v-col>
            <v-col
              cols="6"
              class = "d-none d-md-block"
            >
              <v-card
              flat
              >
                <v-system-bar
                color="#FFFFFF">
                  <v-spacer></v-spacer>
                  <v-icon @click="closeLogin">mdi-close</v-icon>
                </v-system-bar>
                <v-card-title>
                 <v-row>
                  <v-col cols="12">
                    <span class="text-h3" style="font-family: 'UhBeeSeulvely';">Sign in Now!</span>
                  </v-col>
                </v-row>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row
                    style="justify-content: center;">
                      <v-col 
                      cols="10"
                      id = "signin"
                      >
                        <v-text-field
                          v-model="email"
                          prepend-inner-icon="mdi-email"
                          label="Email"
                          required
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="10"
                      id = "signin">
                        <v-text-field
                          v-model="password"
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                       <v-col cols="10" id = "signupbtn">
                        <v-btn
                          color="#87c7c6"
                          dark
                          rounded
                          @click="onLogin"
                        >
                          Sign in  
                          <v-icon>
                           mdi-arrow-right-thick
                          </v-icon>
                       </v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                  <small>아이디가 없으세요? </small>
                  <v-btn
                    color="#ff4747"
                    text
                    rounded
                    @click="openSignup"
                  >
                    Sign Up  
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-col>
            <!-- 모바일버전 -->
             <v-col
              cols="12"
              class ="d-md-none"
            >
              <v-card
              flat
              >
                <v-system-bar
                color="#FFFFFF">
                  <v-spacer></v-spacer>
                  <v-icon @click="closeLogin">mdi-close</v-icon>
                </v-system-bar>
                <v-card-title>
                 <v-row>
                  <v-col cols="12">
                    <span class="text-h4">Sign in Now!</span>
                  </v-col>
                </v-row>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row
                    style="justify-content: center;">
                      <v-col 
                      cols="10"
                      id = "signin"
                      >
                        <v-text-field
                          v-model="email"
                          prepend-inner-icon="mdi-email"
                          label="Email"
                          required
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="10"
                      id = "signin">
                        <v-text-field
                          v-model="password"
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                       <v-col cols="10" id = "signupbtn">
                        <v-btn
                          color="#87c7c6"
                          dark
                          rounded
                          @click="onLogin"
                        >
                          Sign in  
                          <v-icon>
                           mdi-arrow-right-thick
                          </v-icon>
                       </v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                  <small>아이디가 없으세요? </small>
                  <v-btn
                    color="#ff4747"
                    text
                    rounded
                    @click="openSignup"
                  >
                    Sign Up  
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>
    <!-- 회원가입 -->
    <Signup v-bind:signupdialog="signupdialog" v-on:close-signup="closeSignup" v-on:open-login="openLogin"/>
  </v-row>
</template>
<script>
import Signup from '../components/Signup.vue'
import store  from '../store/index'
  export default {
   components:{
      Signup
    },
    props:['logindialog'],
    data: () => ({
       signupdialog : false,
       password: '',
       email:'',
    }),

    methods : {
    closeLogin (){
        this.$emit('close-login');
      },
      openLogin(){
        this.$emit('open-login');
      },
      openSignup(){
        this.signupdialog = true;
        this.$emit('close-login');
      },
      closeSignup(){
        this.signupdialog = false;
      },
      onLogin(){
        const signinInfo = {
          'username': 'user',
          'password': this.password,
          'email': this.email
        }
        store.dispatch('login', signinInfo);
      },
    },
  }
</script>

<style>
#signin{
  padding-bottom: 0px;
}
#signupbtn{
  padding-top: 20px;
}

</style>

