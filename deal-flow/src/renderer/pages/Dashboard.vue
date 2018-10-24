<template>
  <div>
    <h1>Dashboard</h1>
    <div id="slider1">
      <h2>Browsers</h2>
      <carousel :perPageCustom="[[768, 3], [1024, 4]]">
        <slide v-for="company in companies" v-if="company.tagging === 'browser'">
          <div>
            <img v-bind:src="company.logo" height="200" width="200"/>
            <h5>{{company.name}}</h5>
            {{company.valuation}}
          </div>
        </slide>
      </carousel>
    </div>
    <div id="slider2">
      <h2>Jobs</h2>
      <carousel :perPageCustom="[[768, 3], [1024, 4]]">
        <slide v-for="company in companies" v-if="company.tagging === 'jobs'">
          <div>
            <img v-bind:src="company.logo" height="200" width="200"/>
            <h5>{{company.name}}</h5>
            {{company.valuation}}
          </div>
        </slide>
      </carousel>
    </div>
    <div id="slider2">
      <h2>Jobs</h2>
      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="user of users">
          <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: user.id }} ">
            <div class="">
              <img v-bind:src="companies[1].logo" height="200" width="200"/>
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
        users:[],
        errors: [],
        variable: null,
        examplelogo: '../assets/randomLogo1.png',
        companies: [
          { name: 'Gmail', logo: 'static/imgs/randomLogo1.png', tagging: 'browser', valuation:'1.2' },
          { name: 'CHEP', logo: 'static/imgs/randomLogo2.jpg', tagging: 'browser', valuation:'1.2' },
          { name: 'Shopify', logo: 'static/imgs/randomLogo3.png', tagging: 'jobs', valuation:'1.2' },
          { name: 'Internet Explorer', logo: 'static/imgs/randomLogo4.png', tagging: 'browser', valuation:'1.2' },
          { name: 'LinkedIn', logo: 'static/imgs/randomLogo5.png', tagging: 'jobs', valuation:'1.2' },
          { name: 'Chrome', logo: 'static/imgs/randomLogo6.png', tagging: 'browser', valuation:'1.2' },
        ]
      }
    },
    created() {
      axios.get('https://jsonplaceholder.typicode.com/users').then(response => {
        this.users = response.data
        console.log(response.data);
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
