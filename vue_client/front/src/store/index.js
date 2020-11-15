import Vue from 'vue'
import Vuex from 'vuex'
import router from "../router"

// import loginStore from './modules/loginStore'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';
import storyStore from './modules/storyStore'

Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        user: null,
        isLogin: false,
        msg: null,
        token: null,
    },
    getters: {
        user: (state) => { return state.user; },
        msg: (state) => { return state.msg; },
        token: (state) => { return state.token; },
    },
    mutations: {
        SETUSER(state, user) { state.user = user; },
        MUTATEISLOGIN(state, isLogin) {
            state.isLogin = isLogin
        },
        MUTATEUSERINFO(state, user) {
            state.user = user
        },
        MUTATEUSERTOKEN(state, token) {
            state.token = token
        },
        MUTATEUSMSG(state, msg) {
            state.msg = msg
        }
    },
    actions: {
        login(context, signInfo) {
            axios.post(`http://127.0.0.1:8000/rest-auth/login/`, signInfo, { "Content-Type": "application-json" })
                .then(res => {
                    context.commit('MUTATEISLOGIN', true)
                    context.commit('MUTATEUSERINFO', res.data.user)
                    context.commit('MUTATEUSERTOKEN', res.data.token)
                        // context.commit('MUTATEUSMSG',res.data.user.nickname+"님 환영합니다.")
                    alert(res.data.user.nickname + "님 환영합니다.");
                    router.go(0);
                })
                .catch(err => {
                    console.log(err.response.data);
                    if (err.response.data.non_field_errors) {
                        alert(err.response.data.non_field_errors);
                    } else if (err.response.data.email) {
                        alert(err.response.data.email);
                    }
                })
        },
        logout(store) {
            alert(store.state.user.nickname + "님 안녕히 가세요")
            store.commit('MUTATEISLOGIN', false)
            store.commit('MUTATEUSERINFO', {})
            router.go(0);
        },

        signup(context, signupInfo) {
            axios.post(`http://127.0.0.1:8000/rest-auth/signup/`, signupInfo, { "Content-Type": "application-json" })
                .then(res => {
                    context.commit('SignUP');
                    alert("회원가입되었습니다.");
                    console.log(res.data);
                    router.go(0);
                })
                .catch((error) => {
                    console.log(error.response.data);
                    if (error.response.data.email) {
                        alert(error.response.data.email);
                    } else if (error.response.data.password1) {
                        alert(error.response.data.password1)
                    } else {
                        alert("회원가입에 실패하셨습니다.");
                    }
                })
        },

        deleteuser(context) {
            const TOKEN = store.state.token
            const config = {
                headers: { 'Authorization': 'jwt ' + TOKEN }
            }
            axios.delete(`http://127.0.0.1:8000/accounts/userinfo/ `, config)
                .then(res => {
                    alert(store.state.user.nickname + "님 탈퇴처리 되었습니다.")
                    console.log(res.data);
                    store.commit('MUTATEISLOGIN', false)
                    context.commit('MUTATEUSERINFO', {});
                    router.go(0);
                })
                .catch((error) => {
                    console.log(error.response);
                })
        },

        updateuser(context, userInfo) {
            const TOKEN = store.state.token
            const config = {
                headers: { 'Authorization': 'jwt ' + TOKEN }
            }
            axios.put(`http://127.0.0.1:8000/accounts/userinfo/ `, userInfo, config, { "Content-Type": "application-json" })
                .then(res => {
                    alert("회원 정보가 수정되었습니다.");
                    console.log(res.data);
                    context.commit('MUTATEUSERINFO', res.data)
                    router.go(0);
                })
                .catch((error) => {
                    console.log(error.response.data);
                })
        }
    },
    plugins: [
        createPersistedState({
            storage: window.sessionStorage,
            paths: ["isLogin", "user", "token"]
        })
    ],
    modules: {
        // loginStore
        storyStore
    },
})

export default store