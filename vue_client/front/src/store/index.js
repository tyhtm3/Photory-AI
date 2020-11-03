import Vue from 'vue'
import Vuex from 'vuex'

import loginStore from './modules/loginStore'
import storyStore from './modules/storyStore'

Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        loginStore,
        storyStore
    },
})

export default store