//libraries
import Vue from 'vue'
import Router from 'vue-router'
// @import url("//unpkg.com/element-ui@2.4.8/lib/theme-chalk/index.css");

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
import VueCarousel from 'vue-carousel';
import VueCharts from 'vue-chartjs'
import "chart.js";
import "hchs-vue-charts";
Vue.use(window.VueCharts);

//Pages
import  Contacts from '@/pages/Contacts'
import  ContactCatalogue from '@/pages/ContactCatalogue'
import  Login from '@/pages/Login'
import  Organizations from '@/pages/Organizations'
import  Settings from '@/pages/Settings'
import  Dashboard from '@/pages/Dashboard'
import  Deals from '@/pages/Deals'
import  SingleContact from '@/pages/single-contact'
import SingleOrganization from '@/pages/single-organization'
//Components
// import SkillChart from @/components/SkillChart

Vue.use(Router)
Vue.use(ElementUI);
Vue.use(VueCarousel);

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
      path: '/single-contact/:id',
      name: 'Single-Contact',
      component: SingleContact
    },
    {
      path: '/single-organization/:id',
      name: 'Single-Organization',
      component: SingleOrganization
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
