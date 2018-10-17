//libraries
import Vue from 'vue'
import Router from 'vue-router'
// @import url("//unpkg.com/element-ui@2.4.8/lib/theme-chalk/index.css");

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
//Pages
import  Contacts from '@/pages/Contacts'
import  ContactCatalogue from '@/pages/ContactCatalogue'
import  Login from '@/pages/Login'
import  Organizations from '@/pages/Organizations'
import  Settings from '@/pages/Settings'
import  Dashboard from '@/pages/Dashboard'
import  Deals from '@/pages/Deals'

Vue.use(Router)
Vue.use(ElementUI);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/pages/Dashboard').default
    },
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/Contacts',
      name: 'Contacts',
      component: Contacts
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Organizations',
      name: 'Organizations',
      component: Organizations
    },
    {
      path: '/Settings',
      name: 'Settings',
      component: Settings
    },
    {
      path: '/Deals',
      name: 'Deals',
      component: Deals
    },
    {
      path: '/Dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/ContactCatalogue',
      name: 'ContactCatalogue',
      component: ContactCatalogue
    }
  ]
})
