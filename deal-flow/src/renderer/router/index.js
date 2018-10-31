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
import  SingleOrganization from '@/pages/single-organization'
import  CompanyOverview from '@/components/CompanyOverview'
import  DealOverview from '@/components/DealOverview'
import  AddContact from '@/pages/AddContact' //NOT PAGE ----------- MOVE TO COMPONENT DIR
import  AddOrganization from '@/pages/AddOrganization' //NOT PAGE ----------- MOVE TO COMPONENT DIR
import  EditContact from '@/pages/EditContact'
import  AddOrganizationPage from '@/pages/AddOrganizationPage'
import  AddContactPage from '@/pages/AddContactPage'
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
      path: '/AddContact',
      name: 'AddContact',
      component: AddContact
    },
    {
      path: '/AddOrganization',
      name: 'AddOrganization',
      component: AddOrganization
    },
    {
      path: '/AddOrganizationPage',
      name: 'AddOrganizationPage',
      component: AddOrganizationPage
    },
    {
      path: '/AddContactPage',
      name: 'AddContactPage',
      component: AddContactPage
    },
    {
      path: '/EditContact/:id',
      name: 'EditContact',
      component: EditContact
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
    },
    {
      path: '../components/CompanyOverview',
      name: 'CompanyOverview',
      component: CompanyOverview
    }
  ]
})
