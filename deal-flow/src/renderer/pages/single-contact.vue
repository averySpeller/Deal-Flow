<template v-loading="loading" :data="contact">
  <div id ="Contact">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline" style="border-radius: 50%">
          <img  class="avatar"v-bind:src ="contact.avatar">
        </div>

        <div class="title uk-flex uk-flex-center">
          <h1>{{contact.first}} {{contact.last}}</h1>
        </div>
        <div class="title uk-flex uk-flex-center">
          <h4>{{organization.name}}</h4>
          <!-- <router-link tag="h4" :to="{ name: 'Single-Organization', params: { id: contact.company }} ">
            {{contact.company}}
          </router-link> -->
        </div>
        <div class="title uk-flex uk-flex-center">
          <h4>{{this.myTest}}</h4>
        </div>

      </el-col>
    </el-row>
    <div class="uk-divider-vertical uk-margin">
      <hr class="uk-divider-icon"/>
      <el-row :gutter="50">
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <ul>
            <br><br>
            <li><p><strong>Email: </strong>{{contact.email}}</p></li>
            <li><p><strong>Phone: </strong>{{contact.phone1}}</p></li>
            <li><p><strong>Website: </strong>{{contact.website}}</p></li>
          </ul>
        </el-col>
        <el-col  :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <div class="uk-flex uk-flex-center uk-inline" >
            <img src="static/imgs/sampleRadarChart.png" height="100" uk-img>
          </div>
          <br><br>
      </ul>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="20">
          Notes:
          <el-input
                      v-model="contact.notes"
                      type="textarea"
                      :autosize="{ minRows: 4, maxRows: 8}"
                      placeholder="Additional Notes" >
                    </el-input>
        </el-col>
      </el-row>


        </el-col>
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </div>
      <el-button @click="deleteContact()">delete</el-button>
      <router-link :to="{ name:'EditContact', params: { id: this.id }}">Edit</router-link>
    <br>
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
  name: 'Single-Contact',
  data(){
    return {
      id: 0,
      myTest:"WRONG",
      contact: {},
      errors: [],
      organization: {},
      orgID: 0,
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    deleteContact(){
      var requestFields = this.$parent.createGetRequest("contacts/".concat(this.contact.contact_id))

      axios.delete(requestFields.myRequest, requestFields.auth).then(response => {
        console.log(requestFields.myRequest);
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')

      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  created() {
    var requestFields = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))
    this.id = this.$route.params.id;

    axios.get(requestFields.myRequest, requestFields.auth).then(response => {
      this.contact = response.data
      this.orgID = this.contact.organization_id;
      console.log("orgID ISSSS: ",this.orgID);
      console.log(requestFields.myRequest);
      this.loading = false;

      requestFields = this.$parent.createGetRequest("organizations/".concat(this.orgID))
      console.log("orgID IS: ",this.orgID);
      axios.get(requestFields.myRequest, requestFields.auth).then(response => {
        this.organization = response.data
        console.log(requestFields.myRequest);
        this.loading = false;
      })
      .catch(e => {
        this.errors.push(e)
        console.log('failed');
      })


    })
    .catch(e => {
      this.errors.push(e)
    })

    if (typeof(Storage) !== "undefined") {
      // Store
      // Retrieve
      this.myTest = localStorage.getItem("testMe");
    } else {
      this.myTest = "Sorry, your browser does not support Web Storage...";
    }











  }
}
</script>
<style scoped>

  #title{
    text-align: center;
    margin: 0 auto;
  }
  img .class{
    margin: 0 auto;
      border-radius: 50%;
      width: 250px;
      height: 250px;
  }
  .grid-content {
    min-height: 36px;
  }

</style>
