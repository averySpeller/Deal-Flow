<template>
  <div id ="Organization" v-loading="loading" :data="organization">
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
          <el-button @click="deleteCompany()" type="danger">Delete</el-button>
          <router-link :to="{ name:'EditOrganization', params: { id: this.organization_id }}">
            <el-button>Edit</el-button>
          </router-link>
        </div>
      </el-col>
    </el-row>

    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline">
          <img  class="avatar" v-bind:src ="organization.logo">
        </div>
        <div class="title uk-flex uk-flex-center">
          <h1>{{organization.name}}</h1>
        </div>
        <div class="title uk-flex uk-flex-center">
          <h5><strong>{{organization.vision}}</strong></h5>
        </div>

        <div class="title uk-flex uk-flex-center">
        </div>
        <el-row type="flex" class="row-bg" justify="center">
            <el-button v-on:click="overviewFlag=true; currentView='Overview'" type="info" :plain="currentView === currentView" round size="small">Overview</el-button>


            <el-button v-for="deal in deals" v-on:click="overviewFlag==='false';" type="primary" :plain="currentView === 'Overview'" round size="small">Deal #1</el-button>

            <el-button uk-toggle="target: #offcanvas-addDeal" type="success" plain round size="small">Add Deal</el-button>
        </el-row>
      </el-col>
    </el-row>
    <div class="uk-margin">
      <hr class="uk-divider-icon"/>
      <CompanyOverview v-if="overviewFlag" v-bind:organization="this.organization" v-bind:contacts="this.contacts"></CompanyOverview>
      <DealOverview v-else v-bind:organization="this.organization" ></DealOverview>
    </div>

    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>

    <div id="offcanvas-addDeal" uk-offcanvas="mode: slide; overlay: true; flip: true">
      <div class="uk-offcanvas-bar">
        <button class="uk-offcanvas-close" type="button" uk-close></button>
        <div class="title uk-flex uk-flex-center">
            <h1>Add Deal</h1>
        </div>
          <AddEditDeal v-bind:organization="this.organization"></AddEditDeal>
      </div>
    </div>
  </div>
</template>

<script>
import lib from '../lib'
import CompanyOverview from '../components/CompanyOverview';
import DealOverview from '../components/DealOverview';
import AddEditDeal from '../components/AddEditDeal';
export default {
  name: 'Single-Organization',
  components: {
    'CompanyOverview' : CompanyOverview,
    'DealOverview' : DealOverview,
    'AddEditDeal' : AddEditDeal
  },
  data(){
    return {
      organization: {},
      contacts: [],
      deals: [],
      errors: [],
      contacterrors: [],
      address: "",
      overviewFlag: true,
      currentView: "Overview",
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    loadIt(arg) {
      this.loadSelect()
      this.form.organization_id=arg
    },

    loadSelect() {
      lib.getRequest('/organizations', response => {
        console.log(response);
        for(let item of response.data){
          this.orgOptions.push({
            'label': item.name,
            'value': item.organization_id
          })
        }
        this.loading = false;
      })
    }
  },
  created() {

    lib.getRequest("/organizations/".concat(this.$route.params.id), response => {
      this.organization = response.data
      console.log(response.data);
      this.loading = false;
    })


    lib.getRequest("/contacts", response => {
      this.contacts = response.data
      console.log(response.data);
    })

    lib.getRequest("/deals?organization_id=".concat(organization.organization_id), response => {
      console.log("GOT A ");
      this.deals = response.data
      console.log(response.data);
    })

  }
}
</script>
<style scoped>

  #title{
    text-align: center;
    margin: 0 auto;
  }
  img {
    margin: 0 auto;
      border-radius: 15%;
      height:250px;
      width:250px;
  }
  .uk-offcanvas-bar{
    width: 50%;
    background: #fff;
    color: black;
  }

</style>
