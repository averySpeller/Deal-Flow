import Vue from 'vue'
import Router from 'vue-router'
import  Contacts from '@/pages/Contacts'
import  ContactCatalogue from '@/pages/ContactCatalogue'
import  Login from '@/pages/Login'
import  Organizations from '@/pages/Organizations'
import  Settings from '@/pages/Settings'
import  Dashboard from '@/pages/Dashboard'
import  Deals from '@/pages/Deals'
Vue.use(Router)

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
