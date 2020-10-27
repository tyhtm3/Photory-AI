<template>
  <v-row justify="center">
    <v-dialog
      content-class = "d-none d-md-block"
      v-model="signupdialog"
      persistent
      max-width="1000px"
    >
       <v-card
        class="mx-auto"
        >
        <v-container>
          <v-row dense>
            <v-col
            cols="6"
            >
              <img src="@/assets/loginbackground.png" style="max-width: -webkit-fill-available;" >
            </v-col>
            <v-col
              cols="6"
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
                          prepend-inner-icon="mdi-email"
                          label="Email"
                          required
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="10" 
                      id = "signup">
                        <v-text-field
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="10"
                       id = "signup">
                        <v-text-field
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
                            @click="closeSignup"
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
    <!-- 모바일 버전 -->
    <v-dialog
      content-class ="d-md-none"
      v-model="signupdialogM"
      persistent
      max-width="1000px"
    >
       <v-card
        class="mx-auto"
        >
        <v-container>
          <v-row dense>
            <v-col
              cols="12"
            >
              <v-card
              flat
              >
                <v-system-bar
                color="#FFFFFF">
                  <v-spacer></v-spacer>
                  <v-icon @click="closeSignupM">mdi-close</v-icon>
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
                          prepend-inner-icon="mdi-email"
                          label="Email"
                          required
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="10" 
                      id = "signup">
                        <v-text-field
                          prepend-inner-icon="mdi-shield-lock-outline"
                          label="Password"
                          type="password"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="10"
                       id = "signup">
                        <v-text-field
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
                            @click="closeSignupM"
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
                    @click="openLoginM"
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
  export default {
    props:['signupdialog','signupdialogM'],
    data: () => ({
       
    }),
    methods : {
      closeSignup (){
        this.$emit('close-signup');
      },
      openLogin(){
        this.$emit('open-login');
        this.$emit('close-signup');
      },
      closeSignupM (){
        this.$emit('close-signup-m');
      },
      openLoginM(){
        this.$emit('open-login-m');
        this.$emit('close-signup-m');
      },
    },
  }
</script>

<style>
#signup{
   padding-top: 0px;
   padding-bottom: 0px;
}
</style>
