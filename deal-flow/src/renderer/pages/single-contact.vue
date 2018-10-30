<template>
  <div id ="Contact" v-loading="loading" :data="contact">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline" style="border-radius: 50%">
          <img src="static/imgs/linux.png">
        </div>

        <div class="title uk-flex uk-flex-center">
          <h1>{{contact.first}} {{contact.last}}</h1>
        </div>
        <div class="title uk-flex uk-flex-center">
          <h4>From *Company*</h4>
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
            <p><strong>Name: </strong>{{contact.first}}</p>
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
          <div class="uk-flex uk-flex-center uk-inline">
            <p>NOTES GO HERE</p>
          </div>

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
      var myRequest = this.$parent.createGetRequest("contacts/".concat(this.contact.contact_id))

      axios.delete(myRequest).then(response => {
        console.log(myRequest);
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
    var myRequest = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))
    this.id = this.$route.params.id;

    axios.get(myRequest).then(response => {
      this.contact = response.data
      console.log(myRequest);
      this.loading = false;
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
  img {
    margin: 0 auto;
      border-radius: 50%;
  }
  .grid-content {
    min-height: 36px;
  }

</style>
