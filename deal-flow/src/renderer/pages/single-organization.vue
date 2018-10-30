<template>
  <div id ="Organization" v-loading="loading" :data="organization">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline">
          <img src="static/imgs/UoG.png">
        </div>
        <div class="title uk-flex uk-flex-center">
          <h1>{{organization.name}}</h1>
        </div>
        <div class="title uk-flex uk-flex-center">
          <h5><strong>{{organization.vision}}</strong></h5>
        </div>

        <div class="title uk-flex uk-flex-center">
          DEALS:
        </div>
        <el-row type="flex" class="row-bg" justify="center">

            <router-link :to="{ name: 'Single-Deal', params: { id: organization.organization_id} }">
              <el-button type="primary" plain round size="small">Deal #1</el-button>
            </router-link>
        </el-row>

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
            <li><p><strong>Website: </strong>{{organization.website}}</p></li>
            <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->
          </ul>

          <p><strong>Contacts: </strong></p>
          <ol>
            <li v-for="contact in contacts">
              <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id} }">
                {{contact.first}}
              </router-link>
            </li>
          </ol>
        </el-col>
        <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <div class="uk-flex uk-flex-center uk-inline">
            <img src="static/imgs/sampleRadarChart.png" height="100" uk-img>
          </div>
          <br><br>
          <div class="uk-flex uk-flex-center uk-inline">
            <p>NOTES GO HERE</p>
          </div>

        </el-col>
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
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
  name: 'Single-Organization',
  data(){
    return {
      organization: {},
      contacts: [],
      errors: [],
      contacterrors: [],
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
    var myRequest = this.$parent.createGetRequest("organizations/".concat(this.$route.params.id))

    axios.get(myRequest).then(response => {
      this.organization = response.data
      console.log(myRequest);
      this.loading = false;
    })
    .catch(e => {
      this.errors.push(e)
      console.log('failed');
    })

    myRequest = this.$parent.createGetRequest("contacts")

    axios.get(myRequest).then(response => {
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
  .grid-content {
    min-height: 36px;
  }

</style>
