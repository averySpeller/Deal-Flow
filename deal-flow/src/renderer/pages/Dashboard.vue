<template>
  <div v-if="companies" v-loading="loading" :data="companies">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="20">
          <div class="uk-flex uk-flex-center uk-inline">
            <img src="static/imgs/logo.jpg">
          </div>
        <h1 class="uk-flex uk-flex-center uk-inline">Deal Flow</h1>
      </el-col>
    </el-row>
    <br>
    <el-row :gutter="70" type="flex" class="row-bg" justify="center">
      <el-col :span="1"></el-col>
      <el-col :span="5">
        <h4>Funded</h4>
        <div class="dash-tile dash-green uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1 class="dash-tile-content">{{this.fundedNum}}%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>In Progress</h4>
        <div class="dash-tile dash-yellow uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1 class="dash-tile-content">{{this.inProgressNum}}%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>Not Funded</h4>
        <div class="dash-tile dash-red uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1 class="dash-tile-content">{{this.notFundedNum}}%</h1>
        </div>
      </el-col>
      <el-col :span="5">
        <h4>Total Deals</h4>
        <div class="dash-tile dash-grey uk-flex uk-flex-center uk-flex-middle uk-flex-column">
            <h1 class="dash-tile-content">{{this.totalDeals}}</h1>
        </div>
      </el-col>
      <el-col :span="1"></el-col>
    </el-row>




    <hr data-v-6b294509="" class="uk-divider-icon">
    <el-row v-if="recentlyAdded" type="flex" class="row-bg" justify="center">
      <el-col :span="24">
        <div id="slider4">
          <br>
          <h2><i class="el-icon-date"></i> Recently Added Pitches</h2>
          <el-carousel :interval="10000" type="card" width="100%" height="200px">
            <el-carousel-item v-for="organization of recentlyAdded">
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






    <hr data-v-6b294509="" class="uk-divider-icon">
    <el-row v-if="ofInterest" type="flex" class="row-bg" justify="center">
      <el-col :span="24">
        <div id="slider2">
          <br>
          <h2><i class="el-icon-star-on"></i> High Interest Pitches</h2>
          <el-carousel :interval="10000" type="card" height="200px">
            <el-carousel-item v-for="organization of ofInterest">
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
    <hr data-v-6b294509="" class="uk-divider-icon">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="24">
        <div id="slider3">
          <h2><i class="el-icon-menu"></i> All Companies</h2>
          <el-carousel id="Jobs" :interval="4000" type="card" height="200px">
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
        <el-col :span="20">
            <br><br>
        </el-col>
    </el-row>

  </div>
</template>

<script>
  import lib from '../lib'
  export default {
    name: 'Dashboard', //this is the name of the component
    data() {
      return {
        organizations:[],
        deals:[],
        ofInterest: [],
        recentlyAdded: [],
        recentlyAddedIds: [],
        errors: [],
        variable: null,
        totalDeals: 0,
        fundedNum:0,
        notFundedNum: 0,
        inProgressNum: 0,
        ofInterestIds: [],
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
        loading:true,
        loading_interest:true,
        loading_recent: true
      }
    },
    mounted() {
      this.$emit('backButton', false);
      lib.getRequest("/deals", response => {
        this.deals = response.data
        console.log(response.data);

        lib.getRequest('/organizations'.concat('?fields=logo'), response => {
          this.organizations = response.data
          console.log(response.data);
          this.setStatistics();

          lib.getRequest('/tagmappings'.concat("?organization_id:gt=0"), response => {
            this.tagmappings = response.data
            console.log(response.data);
            this.loading = false;
            this.parseTags();
          })
        })
      })
    },
    methods: {
      setStatistics(){
        var myDeal;
        this.totalDeals = 0;
        this.inProgressNum = 0;
        this.fundedNum = 0;
        this.notFundedNum = 0;

        for (var i = 0; i < this.deals.length; i++) {
          myDeal = this.deals[i]
          this.totalDeals += 1;

          if (myDeal.interest == "High") {
            if (!this.ofInterestIds.includes(myDeal.organization_id)) {
              this.ofInterestIds.push(myDeal.organization_id);

              var newOfInterest = null
              newOfInterest = this.findOrg(myDeal.organization_id)
              console.log("RETURN SEARCH interest");
              console.log(newOfInterest);
              if (newOfInterest) {
                this.ofInterest.push(newOfInterest)
                console.log("Found High interest");
                console.log(newOfInterest);
              }
            }
          }
          if (myDeal.status === "inProgress") {
            this.inProgressNum += 1;
          }
          else if (myDeal.status === "funded") {
            this.fundedNum += 1;
          }
          else if (myDeal.status === "notFunded") {
            this.notFundedNum += 1;
          }
          else {
            console.log("Error: Deal without a status");
            console.log(myDeal.deal_id);
          }
        }

          for (var i = this.deals.length; i < (this.deals.length - 10); i--) {
            myDeal = this.deals[i]
            this.recentlyAddedIds.push(myDeal.organization_id);
            this.recentlyAdded.push(this.findOrg(myDeal.organization_id));
          }


        this.inProgressNum = Math.round((this.inProgressNum / this.totalDeals) * 100);
        this.fundedNum = Math.round((this.fundedNum / this.totalDeals) * 100);
        this.notFundedNum = Math.round((this.notFundedNum / this.totalDeals) * 100);

      },
      findOrg(orgId){

        for (var i = 0; i < this.organizations.length; i++) {
          if (parseInt(this.organizations[i].organization_id) == parseInt(orgId)){
            console.log("FOUND");
            console.log(this.organizations[i]);
            return(this.organizations[i]);
          }
        }
        return null;
      },
      parseTags(){
        for (var i = 0; i < this.tagmappings.length; i++) {
          this.tagmappings[i].organization_id
        }
      },
      hashValue(){

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
  	position: relative;
    width: 80%
  }
  .dash-tile:before{
  	content: "";
  	display: block;
  	padding-top: 70%; 	/* initial ratio of 1:1*/
  }
  .dash-tile-content{
    position: absolute;
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
