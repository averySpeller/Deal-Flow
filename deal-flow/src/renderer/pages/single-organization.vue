<template>
  <div id ="Organization" v-loading="loading" :data="organization">
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
          <el-button @click="deleteCompany()" type="danger">Delete</el-button>
          <router-link :to="{ name:'EditOrganization', params: { id: organization.organization_id }}">
            <el-button>Edit</el-button>
          </router-link>
        </div>
      </el-col>
    </el-row>

    <el-row type="flex" class="row-bg" justify="center">
      <el-col >
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
          <el-radio-group v-model="currentView">
            <el-radio-button :label="0">Overview</el-radio-button>
            <el-radio-button v-for="(deal, key) in deals" :label="(key+1)" >Pitch {{key+1}}</el-radio-button>
          </el-radio-group>
          <el-button uk-toggle="target: #offcanvas-addDeal" type="success" plain  size="medium">Add Pitch</el-button>
        </el-row>
      </el-col>
    </el-row>
    <div class="uk-margin">
      <hr class="uk-divider-icon"/>
      <el-row type="flex" class="row-bg" justify="center">
        <router-link tag="div" :to="{ name:'Tag', params: { id: tag }}" v-for="tag in dynamicTags" class="tagContainer">
          <div>
            <el-tag
              :key="tag"
              closable
              :disable-transitions="false"
              @close="handleClose(tag)">
              #{{tag}}
            </el-tag>
          </div>
        </router-link>

        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="mini"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm" >
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
      </el-row>
      <br>
      <CompanyOverview v-if="this.currentView == 0" v-bind:organization="this.organization" v-bind:contacts="this.contacts"></CompanyOverview>
      <DealOverview v-else v-bind:organization="this.organization" v-bind:deal="this.deals[currentView-1]" ></DealOverview>
    </div>

    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>

    <div id="offcanvas-addDeal" uk-offcanvas="mode: slide; overlay: true; flip: true">
      <div class="uk-offcanvas-bar">
        <button class="uk-offcanvas-close" type="button" uk-close></button>
        <div class="title uk-flex uk-flex-center">
            <h1>Add Deal</h1>
        </div>
          <AddEditDeal v-bind:organization="this.organization"></AddEditDeal>
      </div>
    </div>
  </div>
</template>

<script>
import lib from '../lib'
import CompanyOverview from '../components/CompanyOverview';
import DealOverview from '../components/DealOverview';
import AddEditDeal from '../components/AddEditDeal';
export default {
  name: 'Single-Organization',
  components: {
    'CompanyOverview' : CompanyOverview,
    'DealOverview' : DealOverview,
    'AddEditDeal' : AddEditDeal
  },
  data(){
    return {
      organization: {},
      currentDeal: {},
      contacts: [],
      deals: [],
      errors: [],
      contacterrors: [],
      dynamicTags: ['Tag 1', 'Tag 2', 'Tag 3'],
      inputVisible: false,
      isCollapse: false,
      inputValue: '',
      address: "",
      overviewFlag: true,
      currentView: 0,
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    loadIt(arg) {
      this.loadSelect()
      this.form.organization_id=arg
    },

    loadSelect() {
      lib.getRequest('/organizations', response => {
        console.log(response);
        for(let item of response.data){
          this.orgOptions.push({
            'label': item.name,
            'value': item.organization_id
          })
        }
        this.loading = false;
      })
    },
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    goToTag(tag) {
      console.log("myTag");
      console.log(tag);
    }
  },
  created() {

    lib.getRequest("/organizations/".concat(this.$route.params.id), response => {
      this.organization = response.data
      console.log(response.data);

      console.log(this.organization.organization_id);
      lib.getRequest("/deals?organization_id=".concat(this.organization.organization_id), response => {
        console.log("GOT A ");
        this.deals = response.data
        console.log(response.data);
        this.loading = false;
      })
    })


    lib.getRequest("/contacts", response => {
      this.contacts = response.data
      console.log(response.data);
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
      height:250px;
      width:250px;
  }
  .uk-offcanvas-bar{
    width: 50%;
    background: #fff;
    color: black;
  }

  .tagContainer:first-child {
    margin-top: 0 !important;
    margin-left: 0 !important;
  }
  .tagContainer{
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }

</style>
