<template>
  <div v-if="companies"  :data="companies">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="22">
        <h1 class="uk-margin">Dashboard</h1>
      </el-col>
    </el-row>
    <br>
    <el-row :gutter="70" type="flex" class="row-bg" justify="center">
      <el-col :span="5">
        <h4>Funded</h4>
        <div class="dash-tile dash-green uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1>25%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>In Progress</h4>
        <div class="dash-tile dash-yellow uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1>55%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>Not Funded</h4>
        <div class="dash-tile dash-red uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1>45%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>Total Organizations</h4>
        <div class="dash-tile dash-grey uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1>120</h1>
        </div>
      </el-col>
    </el-row>
    <br>
    <br>
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="22">
        <div id="slider2">
          <h2>Of Interest <i class="el-icon-star-on"></i></h2>
          <el-carousel :interval="10000" type="card" height="200px">
            <el-carousel-item v-for="organization of organizations">
              <div class="uk-flex uk-flex-center uk-flex-middle uk-flex-column">
                <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.organization_id }} ">
                  <img v-if="organization.logo"v-bind:src="organization.logo"/>
                  <img v-else v-bind:src="examplelogo"/>
                </router-link>
                {{organization.name}}
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
      </el-col>
    </el-row>
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="22">
        <div id="slider3">
          <h2>Jobs</h2>
          <el-carousel id="Jobs" class="uk-margin" :interval="4000" type="card" height="200px">
            <el-carousel-item class="uk-margin" v-for="organization of organizations">
              <div class="uk-flex uk-flex-center uk-flex-middle uk-flex-column">
                <router-link tag="div" :to="{ name: 'Single-Organization', params: { id: organization.organization_id }} ">
                  <img v-if="organization.logo"v-bind:src="organization.logo"/>
                  <img v-else v-bind:src="examplelogo"/>
                </router-link>
                {{organization.name}}
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
      </el-col>
    </el-row>

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
        totalCompanies: 0,
        fundedNum:0,
        nonFundedNum: 0,
        inProgressNum: 0,
        examplelogo: 'static/imgs/404.png',
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
      console.log(requestFields.myRequest);

      axios.get(requestFields.myRequest, requestFields.auth).then(response => {
        this.organizations = response.data
        this.setStatistics();
        this.loading = false
      })
      .catch(e => {
        this.errors.push(e)
      })

      requestFields = this.$parent.createGetRequest("deals")
      console.log(requestFields.myRequest);
      axios.get(requestFields.myRequest, requestFields.auth).then(response => {
        this.deals = response.data
        this.setStatistics();
        this.loading = false
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    methods: {
      setStatistics(){
        for (var i = 0; i < this.deals.length; i++) {
          console.log(this.deals[i]);

        }

      }
    }
  }
</script>
<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item {
    /* background-color: #909399; */
    background-color: rgba(0,0,0,0);

  }

  img {
    margin: 0 auto;
      border-radius: 15%;
      height: 180px;
      width: 180px;
  }

  .dash-tile{
    border-radius: 10%;
    min-height: 150px;
  }
  .dash-green{
    background-color: #67C23A;
    color: black;
  }
  .dash-red{
    background-color: #F56C6C;
    color: white;
  }
  .dash-blue{
    background-color: #409EFF;
    color: white;
  }
  .dash-yellow{
    background-color: #E6A23C;
    color: white;
  }
  .dash-grey{
    background-color: #909399;
    color: white;
  }

</style>
