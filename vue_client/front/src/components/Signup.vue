<template>
  <v-row justify="center">
    <v-dialog
      v-model="signupdialog"
      max-width="1000px"
      persistent
    >
       <v-card
        class="mx-auto"
        >
        <v-container>
          <v-row dense>
            <v-col
            cols="6"
            class = "d-none d-md-block"
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
                  <v-icon @click="closeSignup">mdi-close</v-icon>
                </v-system-bar>
                <v-card-title>
                 <v-row>
                 
                  <v-col cols="12">
                    <span class="text-h3">Sign Up Now!</span>
                  </v-col>
                </v-row>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row
                    style="justify-content: center;">
                      <v-col 
                      cols="10"
                      id = "signup"
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
                      id = "signup">
                        <v-text-field
                          v-model="password"
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="10"
                       id = "signup">
                        <v-text-field
                          v-model="nickname"
                          prepend-inner-icon="mdi-baby-face-outline"
                          label="Nickname"
                          required
                        ></v-text-field>
                      </v-col>
                        <v-col cols="10"
                        id = "signup">
                        <v-btn
                            color="#87c7c6"
                            dark
                            rounded
                            @click="onSignup"
                        >
                            Sign Up  
                            <v-icon>
                            mdi-arrow-right-thick
                            </v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                  </v-container>
                  <small>이미 아이디가 있으신가요? </small>
                  <v-btn
                    color="#ff4747"
                    text
                    rounded
                    @click="openLogin"
                  >
                    Sing in 
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-col>
            <!-- 모바일 버전 -->
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
                  <v-icon @click="closeSignup">mdi-close</v-icon>
                </v-system-bar>
                <v-card-title>
                 <v-row>
                 
                  <v-col cols="12">
                    <span class="text-h4">Sign Up Now!</span>
                  </v-col>
                </v-row>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row
                    style="justify-content: center;">
                      <v-col 
                      cols="10"
                      id = "signup"
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
                      id = "signup">
                        <v-text-field
                          v-model="password"
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="10"
                       id = "signup">
                        <v-text-field
                          v-model="nickname"
                          prepend-inner-icon="mdi-baby-face-outline"
                          label="Nickname"
                          required
                        ></v-text-field>
                      </v-col>
                        <v-col cols="10"
                        id = "signup">
                        <v-btn
                            color="#87c7c6"
                            dark
                            rounded
                            @click="onSignup"
                        >
                            Sign Up  
                            <v-icon>
                            mdi-arrow-right-thick
                            </v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                  </v-container>
                  <small>이미 아이디가 있으신가요? </small>
                  <v-btn
                    color="#ff4747"
                    text
                    rounded
                    @click="openLogin"
                  >
                    Sing in 
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import store  from '../store/index'
  export default {
    props:['signupdialog'],
    data: () => ({
       password: '',
       email:'',
       nickname:'',
    }),
    methods : {
      closeSignup (){
        this.$emit('close-signup');
      },
      openLogin(){
        this.$emit('open-login');
        this.$emit('close-signup');
      },
      onSignup(){
        const signupInfo = {
          'username': this.nickname,
          'email': this.email,
          'password1': this.password,
          'password2' : this.password,
        }
        store.dispatch('signup', signupInfo);
      }
    },
  }
</script>

<style>
#signup{
   padding-top: 0px;
   padding-bottom: 0px;
}
</style>
