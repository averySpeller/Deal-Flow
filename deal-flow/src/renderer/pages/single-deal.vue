<template>
  <div id ="Organization" v-loading="loading" :data="deal">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline">
          <img  class="avatar" v-bind:src ="organization.logo">
        </div>
        <div class="title uk-flex uk-flex-center">
          <h1>ORG</h1>
        </div>
      </el-col>
    </el-row>
    <div class="uk-divider-vertical uk-margin">
      <hr class="uk-divider-icon"/>
      <el-row :gutter="50">
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <ul>
            <p><strong>Comapany Vision: </strong> "{{organization.vision}}"</p>
            <br><br>
            <p><strong>Website: </strong>{{organization.website}}</p>
            <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->
          </ul>
        </el-col>
        <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <p><strong>Valuation: </strong> fill...</p>
          <br>
          <p><strong>Current Raise: </strong>fill...</p>
          <br>
          <p><strong>Symbol: </strong>fill...</p>
          <br>
          <p><strong>Stock Price: </strong>fill...</p>

        </el-col>
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      </el-row>

      <div class="uk-flex uk-flex-center uk-inline">
        <p>NOTES GO HERE</p>
      </div>
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
export default {
  name: 'Single-Deal',
  data(){
    return {
      deal: {},
      errors: [],
      address: "",
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
  .grid-content {
    min-height: 36px;
  }

</style>
