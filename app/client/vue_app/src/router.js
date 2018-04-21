import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'

import PageOne from './views/PageOne'
import PageTwo from './views/PageTwo'
import Login from './views/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      components: {
        main: Login
      }
    },
    {
      path: '/one',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: PageOne
      }
    },
    {
      path: '/two',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: PageTwo
      }
    }
  ]
})
