import Vue from 'vue'
import Router from 'vue-router'
import login from '@/home/login'
import mainpage from '@/home/mainpage'
import deal from '@/view/deal'
import heart from '@/view/heart'
import info from '@/view/info'
import nav from '@/view/nav'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/mainpage',
      name: 'mainpage',
      component: mainpage,
      children:[
        {path: '/mainpage/deal', name: 'deal', component: deal},
        {path: '/mainpage/heart', name: 'heart', component: heart},
        {path: '/mainpage/info', name: 'info', component: info},
        {path: '/mainpage/nav', name: 'nav', component: nav},
      ]
    }
  ],
  mode:'history'
})
