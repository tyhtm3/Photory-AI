import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Createstory from '../views/Createstory'
import Mystory from '../views/Mystory'
import SharestoryList from '../views/SharestoryList'
import SharestoryPageBoard from '../views/SharestoryPageBoard'
import SharestoryPageWrite from '../views/SharestoryPageWrite'
import SharestoryPageUpdate from '../views/SharestoryPageUpdate'
import SharestoryPageStory from '../views/SharestoryPageStory'
import storyEdit from '../views/storyEdit'


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
        path: '/sharestorylist',
        name: 'SharestoryList',
        component: SharestoryList
    }, {
        path: '/sharestorypageboard/:boardNum',
        name: 'SharestoryPageBoard',
        component: SharestoryPageBoard
    }, {
        path: '/sharestorywrite',
        name: 'SharestoryPageWrite',
        component: SharestoryPageWrite
    }, {
        path: '/sharestoryupdate/:boardNum',
        name: 'SharestoryPageUpdate',
        component: SharestoryPageUpdate
    }, {
        path: '/sharestorypagestory',
        name: 'SharestoryPageStory',
        component: SharestoryPageStory
    }, {
        path: '/EditStory/:storyNum',
        name: 'storyEdit',
        component: storyEdit
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router