import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import Vue2Editor from "vue2-editor";
//session 등록
import VueSession from 'vue-session'



Vue.use(Vue2Editor);
Vue.use(Vuetify);

Vue.config.productionTip = false

var sessionOptions = {
    persist: true
};

new Vue({
    router,
    store,
    vuetify: new Vuetify(),
    render: h => h(App)
}).$mount('#app')

Vue.use(VueSession, sessionOptions);