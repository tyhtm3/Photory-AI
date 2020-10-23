// restAPI 설계후 수정하기
// import axios from 'axios'
// import router from '../../router/index.js'
// import store from '../index.js'

const loginStore = {
    namespaced: true,
    state: {
        isUser: false,
        userInfo: {},
        isLogin: false,
    },
    getters: {
        userInfo: (state) => state.userInfo,
    },
    mutations: {
        ADDUSERINFO(state, userInfo) {
            state.userInfo = userInfo
        },
        MUTATEISLOGIN(state, isLogin) {
            state.isLogin = isLogin
        },
        MUTATEUSERINFO(state, userInfo) {
            state.userInfo = userInfo
        },
    },
    actions: {
        // login(context, { id, pw }) {
        //     axios.post('우리 서버 주소넣기')
        //         .then(res => {
        //             context.commit('mutateIsLogin', true)
        //             context.commit('mutateUserInfo', res)

        //             router.go(0);
        //             alert("로그인 성공");
        //         })
        //         .catch(err => {
        //             alert("아이디 또는 비밀번호 실패입니다.");
        //             router.push("/errorPage");
        //         })
        // },
        // logout(context) {
        //     context.commit('mutateIsLogin', false)
        //     context.commit('mutateUserInfo', {})
        // },


    }
}

export default loginStore