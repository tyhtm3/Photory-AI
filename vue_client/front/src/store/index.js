import Vue from 'vue'
import Vuex from 'vuex'

import loginStore from './modules/loginStore'

Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        loginStore,
    },
})

export default store