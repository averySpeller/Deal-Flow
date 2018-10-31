<template>
  <div v-if="companies"  :data="companies">
    <h1>Dashboard</h1>
    <div id="slider2">
      <h2>Jobs</h2>
      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="organization of organizations">
          <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.organization_id }} ">
            <div class="">
              <img v-bind:src="organization.logo" height="200" width="200"/>
              {{organization.name}}
            </div>
          </router-link>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div id="slider3">
      <h2>Jobs</h2>
      <el-carousel id="Jobs" class="uk-margin" :interval="4000" type="card" height="200px">
        <el-carousel-item class="uk-margin" v-for="organization of organizations">
          <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.organization_id  }} ">
            <div class="">
              <img v-bind:src="organization.logo" height="100%" width="100%"/>
              {{organization.name}}
            </div>
          </router-link>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Dashboard', //this is the name of the component
    data() {
      return {
        organizations:[],
        errors: [],
        variable: null,
        examplelogo: '../assets/randomLogo1.png',
        companies: [
          { logo: 'static/imgs/randomLogo1.jpg' },
          { logo: 'static/imgs/randomLogo8.jpg' },
          { logo: 'static/imgs/randomLogo2.jpg' },
          { logo: 'static/imgs/randomLogo3.png' },
          { logo: 'static/imgs/randomLogo4.png' },
          { logo: 'static/imgs/randomLogo5.png' },
          { logo: 'static/imgs/randomLogo6.png' },
          { logo: 'static/imgs/randomLogo7.png' },
        ],
        loading:false
      }
    },
    mounted() {
      var requestFields = this.$parent.createGetRequest("organizations")
      console.log(requestFields.auth);
      // axios({
      //   method: 'get',
      //   url: requestFields.myRequest,
      //   headers: { "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQwOTEzNzc0fQ.RSLJOy0aRg09WeYWBFHCZD7xrAmOGydNP-NZTN6DYRI" }
      // }).then(response => {
      //   console.log(response);
      // }).catch(e => {
      //   console.log(e);
      // })

      axios.get(requestFields.myRequest, requestFields.auth).then(response => {
        this.organizations = response.data
        for (var i = 0; i < this.organizations.length; i++) {
          this.organizations[i].logo = this.companies[i].logo;
        }
        this.loading = false
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
</script>
<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
