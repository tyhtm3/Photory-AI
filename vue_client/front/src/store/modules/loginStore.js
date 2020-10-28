// import axios from 'axios'
// // import router from '../../router/index.js'
// // import store from '../index.js'

// const loginStore = {
//     namespaced: true,
//     state: {
//         isUser: false,
//         userInfo: {},
//         isLogin: '',
//     },
//     getters: {
//         isLogin: (state) => { return state.isLogin; },
//         userInfo: (state) => state.userInfo,
//     },
//     mutations: {
//         ADDUSERINFO(state, userInfo) {
//             state.userInfo = userInfo
//         },
//         MUTATEISLOGIN(state, isLogin) {
//             state.isLogin = isLogin
//         },
//         MUTATEUSERINFO(state, userInfo) {
//             state.userInfo = userInfo
//         },
//     },
//     actions: {
//         login(context, signInfo) {
//             context.commit('MUTATEISLOGIN', '');
//             axios.post(`http://127.0.0.1:8000/rest-auth/login/`, signInfo)
//                 .then(res => {
//                     context.commit('MUTATEISLOGIN', '성공')
//                     context.commit('MUTATEUSERINFO', signInfo.email)
//                     alert("로그인 되었습니다.");
//                     console.log(res.data);
//                 })
//                 .catch(err => {
//                     console.log(err);
//                     context.commit('MUTATEISLOGIN', '실패');
//                     alert("아이디 또는 비밀번호 실패입니다.");
//                 })
//         },
//         signup(context, { email, password }) {
//             axios.post(`http://127.0.0.1:8000/rest-auth/signup/?email=${email}&password1=${password}&password2=${password}&username=user2`)
//                 .then(res => {
//                     alert(res.data);
//                     context.commit('SIGNUP');
//                 })
//                 .catch(err => {
//                     console.log(err)
//                 })
//         },

//         // logout(context) {
//         //     context.commit('mutateIsLogin', '')
//         //     context.commit('mutateUserInfo', {})
//         // },


//     }
// }

// export default loginStore