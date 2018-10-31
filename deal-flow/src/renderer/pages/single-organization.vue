<template>
  <div id ="Organization" v-loading="loading" :data="organization">
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
          <!-- <el-col :span="8"> -->
            <el-button v-on:click="overviewFlag=true;" type="info" plain round size="small">Overview</el-button>
          <!-- </el-col> -->
          <!-- <el-col :span="8"> -->
            <el-button v-on:click="overviewFlag=false;" type="primary" plain round size="small">Deal #1</el-button>
          <!-- </el-col> -->
          <!-- <el-col :span="8"> -->
            <el-button v-on:click="overviewFlag=false;" type="primary" plain round size="small">Deal #1</el-button>
          <!-- </el-col> -->
        </el-row>
      </el-col>
    </el-row>
    <div class="uk-margin">
      <hr class="uk-divider-icon"/>
      <CompanyOverview v-if="overviewFlag" v-bind:organization="this.organization" v-bind:contacts="this.contacts"></CompanyOverview>
    </div>

    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>

  </div>
</template>

<script>
import axios from 'axios';
import CompanyOverview from '../components/CompanyOverview';
export default {
  name: 'Single-Organization',
  components: {
    'CompanyOverview' : CompanyOverview
  },
  data(){
    return {
      organization: {},
      contacts: [],
      errors: [],
      contacterrors: [],
      address: "",
      overviewFlag: true,
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  },
  created() {
    var requestFields = this.$parent.createGetRequest("organizations/".concat(this.$route.params.id))

    axios.get(requestFields.myRequest, requestFields.auth).then(response => {
      this.organization = response.data
      console.log(requestFields.myRequest);
      this.loading = false;
    })
    .catch(e => {
      this.errors.push(e)
      console.log('failed');
    })

    requestFields = this.$parent.createGetRequest("contacts")

    axios.get(requestFields.myRequest, requestFields.auth).then(response => {
      this.contacts = response.data
      console.log(response.data);
    })
    .catch(e => {
      this.contacterrors.push(e)
      console.log('faileds');
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
  }


</style>
