import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Createstory from '../views/Createstory'
import Mystory from '../views/Mystory'
import Sharestory from '../views/Sharestory'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/createstory',
        name: 'Createstory',
        component: Createstory
    }, {
        path: '/mystory',
        name: 'Mystory',
        component: Mystory
    }, {
        path: '/sharestory',
        name: 'Sharestory',
        component: Sharestory
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router