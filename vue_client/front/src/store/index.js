import Vue from 'vue'
import Vuex from 'vuex'
import router from "../router"

// import loginStore from './modules/loginStore'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        user: null,
        isLogin: false,
    },
    getters: {
        user: (state) => { return state.user; }
    },
    mutations: {
        SETUSER(state, user) { state.user = user; },
        MUTATEISLOGIN(state, isLogin) {
            state.isLogin = isLogin
        },
        MUTATEUSERINFO(state, user) {
            state.user = user
        },
    },
    actions: {
        login(context, signInfo) {
            axios.post(`http://127.0.0.1:8000/rest-auth/login/`, signInfo, { "Content-Type": "application-json" })
                .then(res => {
                    if (res.data.key) {
                        context.commit('MUTATEISLOGIN', true)
                        context.commit('MUTATEUSERINFO', res.data)
                        alert("로그인 되었습니다.");
                        router.go(0);
                    } else {
                        alert(res.data)
                    }
                })
                .catch(err => {
                    console.log(err);
                    alert("아이디 또는 비밀번호 실패입니다.");
                })
        },
        logout(context) {
            context.commit('MUTATEISLOGIN', false)
            context.commit('MUTATEUSERINFO', {})
            router.go(0);
        },

        signup(context,signupInfo) {
            axios.post(`http://127.0.0.1:8000/rest-auth/signup/`, signupInfo, { "Content-Type": "application-json" })
                .then(res => {
                    context.commit('SignUP');
                    alert("회원가입되었습니다.");
                    console.log(res.data);
                    router.go(0);
                })
                .catch(err => {
                    alert("회원가입에 실패하셨습니다.");
                    console.log(err);
                })
        },
    },
    plugins: [
        createPersistedState({
            storage: window.sessionStorage,
            paths: ["isLogin", "user"]
        })
    ],
    modules: {
        // loginStore
    },
})

export default store