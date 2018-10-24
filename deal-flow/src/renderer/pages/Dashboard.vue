<template>
  <div>
    <h1>Dashboard</h1>
    <div id="slider2">
      <h2>Jobs</h2>
      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="organization of organizations">
          <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.organization_id }} ">
            <div class="">
              <img v-bind:src="companies[1].logo" height="200" width="200"/>

            </div>
          </router-link>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div id="slider2">
      <h2>Jobs</h2>
      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="organization of organizations">
          <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.id }} ">
            <div class="">
              <img v-bind:src="companies[2].logo" height="200" width="200"/>
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
          { logo: 'static/imgs/randomLogo1.png' },
          { logo: 'static/imgs/randomLogo2.jpg' },
          { logo: 'static/imgs/randomLogo3.png' },
          { logo: 'static/imgs/randomLogo4.png' },
          { logo: 'static/imgs/randomLogo5.png' },
          { logo: 'static/imgs/randomLogo6.png' },
        ]
      }
    },
    created() {
      var myRequest = this.$parent.createGetRequest("organizations")
      axios.get(myRequest).then(response => {
        this.organizations = response.data
        console.log('log it up');
        console.log(response.data);
        for (var i = 0; i < organizations.length; i++) {
          console.log(companies[i].logo);
          organizations[i].logo = companies[i].logo
        }
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
