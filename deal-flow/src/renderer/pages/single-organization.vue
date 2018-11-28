<template>
  <div id ="Organization" v-loading="loading" :data="organization">
    <el-row>
      <el-col>
        <div class="uk-align-right uk-margin-right">
            <router-link :to="{ name:'EditOrganization', params: { id: organization.organization_id }}">
              <el-button>Edit</el-button>
            </router-link>
            <el-popover
                placement="bottom"
                width="160"
                v-model="popoverVisible">
                <p>Are you sure to delete the company and all pitches included?</p>
                <div style="text-align: right; margin: 0">
                    <el-button size="mini" type="text" @click="popoverVisible = false">cancel</el-button>
                    <el-button type="primary" size="mini" @click="popoverVisible = false; deleteCompany()">confirm</el-button>
                </div>
                <el-button slot="reference" type="danger">Delete</el-button>
            </el-popover>
        </div>
      </el-col>
    </el-row>

    <el-row type="flex" class="row-bg" justify="center">
      <el-col >
        <div class="uk-flex uk-flex-center uk-inline">
          <img class="avatar" v-bind:src ="organization.logo">
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
          <el-radio-group v-model="currentDeal">
            <el-radio-button  :label="emptyDeal">Overview</el-radio-button>
            <el-radio-button v-for="(deal, key) in deals" v-on:click.native="setFileList()" :label="deal" >Pitch {{key+1}}</el-radio-button>
          </el-radio-group>
          <el-button @click="emptyCurrentDeal()" uk-toggle="target: #offcanvas-addDeal" type="success" plain  size="medium">Add Pitch</el-button>
        </el-row>
      </el-col>
    </el-row>
    <div class="uk-margin">
      <hr class="uk-divider-icon"/>
      <div v-if="this.currentDeal === emptyDeal" id="CompanyOverview Container">
        <el-row id="tagContainer" type="flex" class="row-bg" justify="center">
          <router-link tag="div" :to="{ name:'Tag', params: { id: tag.tag_id }}" v-for="tag in tags" class="tagContainer">
            <div>
              <el-tag
                :key="tag.tag_name"
                closable
                :disable-transitions="false"
                @close="deleteTagMapping(tag)">
                #{{tag.tag_name}}
              </el-tag>
            </div>
          </router-link>



          <el-autocomplete
            class="inline-input input-new-tag"
            v-model="inputTag"
            v-if="inputVisible"
            size="small"
            ref="saveTagInput"
            :fetch-suggestions="searchTags"
            placeholder="Please Input"
            :trigger-on-focus="false"
            @select="handleTagConfirm"
            @keyup.enter.native="handleTagConfirm">
            <i
              uk-icon="icon: hashtag"
              class="el-input__icon"
              slot="prefix">
            </i>
            <template slot-scope="{ item }">
              <div>#{{ item.value }}</div>
            </template>
          </el-autocomplete>

          <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
        </el-row>
        <br>
        <CompanyOverview v-bind:organization="this.organization" v-bind:contacts="this.contacts"></CompanyOverview>
      </div>
      <DealOverview v-else v-bind:organization="this.organization" v-bind:deal="this.currentDeal" ></DealOverview>
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
          <AddEditDeal v-bind:organization="this.organization" v-bind:editDeal="this.editDeal" v-bind:deal="this.currentDeal" v-bind:fileList="this.fileList"></AddEditDeal>
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
      tags: [],
      fileList: [],
      tagSuggestions: [],
      popoverVisible: false,
      inputVisible: false,
      inputTag: '',
      emptyDeal: {
        organization_id: null,
        interest: null,
        status: null,
        valuation: null,
        raise: null,
        revenue: null,
        revenue_model: null,
        round: null,
        slide_deck: null,
        notes: null
      },
      loading:true,
      editDeal:false
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },

    emptyCurrentDeal() {
      this.emptyDeal.organization_id = this.organization.organization_id;
      this.emptyDeal.interest = null;
      this.emptyDeal.status = null;
      this.emptyDeal.valuation = null;
      this.emptyDeal.raise = null;
      this.emptyDeal.revenue = null;
      this.emptyDeal.revenue_model = null;
      this.emptyDeal.round = null;
      this.emptyDeal.slide_deck = null;
      this.emptyDeal.notes = null;

      this.currentDeal = this.emptyDeal
      this.fileList = []
    },

    setFileList(){
      console.log("SETTING FILE list");
      this.fileList = [{name: 'savedPdf.pdf', url: 'static/imgs/pdfDefault.png'}]
    },

    //Dynamic tag control methods.
    deleteTagMapping(tag) {
      lib.deleteRequest("/tagmappings/".concat(tag.tagmapping_id), response => {
        console.log(response.data);
        this.tags.splice(this.tags.indexOf(tag), 1);
      })
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    //tag submit
    handleTagConfirm(item) {

      if (item instanceof KeyboardEvent){
        //NEED to create New Tag
        let inputTag = this.inputTag;
        if (inputTag) {
          var newTag = {"tag_name": inputTag, "tag_color": "blue"}
          lib.postRequest("/tags", newTag, response => {
            console.log("Request Completed: Post New Tag");
            console.log(response.data);

            this.tagSuggestions.push({"value": response.data.tag_name, "tag_id": response.data.tag_id, "tag_color": response.data.tag_color,})

            var newTagMapping = {"tag_id": response.data.tag_id, "organization_id": this.organization.organization_id}

            lib.postRequest("/tagmappings", newTagMapping, response => {
              console.log(response.data);
              this.tags.push({"tag_id": newTagMapping.tag_id, "tag_name": newTag.tag_name, "tag_color": newTag.tag_color, "tagmapping_id": response.data.tagmapping_id});
            })
          })
        }

        //get tag id back from tag
        //add Tag Mapping for tag
      }
      else {

        var newTagMapping = {"tag_id": item.tag_id, "organization_id": this.organization.organization_id}

        lib.postRequest("/tagmappings", newTagMapping, response => {
          console.log(response.data);
          this.tags.push({"tag_id": item.tag_id, "tag_name": item.value, "tag_color": item.tag_color, "tagmapping_id": response.data.tagmapping_id});
        })
      }
      //
      // let inputTag = this.inputTag;
      // if (inputTag) {
      //   this.tags.push(inputTag);
      // }
      this.inputVisible = false;
      this.inputTag = '';
    },

    // AutoComplete methods
    searchTags(queryString, cb) {
      var tagSuggestions = this.tagSuggestions;
      var results = queryString ? tagSuggestions.filter(this.createFilter(queryString)) : tagSuggestions;
      // call callback function to return suggestions
      cb(results);
    },
    createFilter(queryString) {
      return (tagSuggestion) => {
        return (tagSuggestion.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
    deleteCompany(){
      //delete all pitches
      for (var i = 0; i < this.deals.length; i++) {
        lib.deleteRequest("/deals/".concat(this.deals[i].deal_id), response => {
          console.log("Request Completed: Delete Deal #".concat(this.deals[i].deal_id));
          console.log(response.data);
        })
      }
      //update all contact bindings
      var payload = {organization_id: null}

      for (var i = 0; i < this.contacts.length; i++) {
        lib.putRequest("/contacts/".concat(this.contacts[i].contact_id), payload, response => {
          console.log("Request Completed: Updated organization in Contact #".concat(this.contacts[i].contact_id));
          console.log(response.data);
        })
      }

      //delete all tagmappings
      for (var i = 0; i < this.tags.length; i++) {
        this.deleteTagMapping(this.tags[i]);
      }


      lib.deleteRequest("/organizations/".concat(this.organization.organization_id), response => {
        console.log("Request Completed: Delete Organization #".concat(this.organization.organization_id));
        console.log(response.data);
        this.goBack();
      })

    }
  },
  created() {

    lib.getRequest("/organizations/".concat(this.$route.params.id).concat('?fields=logo'), response => {
      this.organization = response.data;
      console.log("Request Completed: Organization");
      console.log(response.data);

      this.emptyDeal.organization_id = this.organization.organization_id;
      this.emptyCurrentDeal();

      this.currentDeal = this.emptyDeal

      lib.getRequest("/deals?organization_id=".concat(this.organization.organization_id).concat('&fields=slide_deck'), response => {
        this.deals = response.data
        console.log("Request Completed: Deals");
        console.log(response.data);
        this.loading = false;
      })

      lib.getRequest('/tagmappings?organization_id='.concat(this.organization.organization_id), response => {
        var tagIds = "";
        var tm = {};

        for (var i = 0; i < response.data.length; i++) {
          if (tagIds !== "") {
            tagIds = tagIds.concat(",");
          }
          tagIds = tagIds.concat(response.data[i].tag_id);
          tm[response.data[i].tag_id] = response.data[i].tagmapping_id;
        }

        if (tagIds !== "") {
          lib.getRequest('/tags?tag_id='.concat(tagIds), response => {


            for (var i = 0; i < response.data.length; i++) {
              response.data[i].tagmapping_id = tm[response.data[i].tag_id]
            }
            console.log("Request Completed: Tags");
            console.log(response.data);
            this.tags = response.data;
          })
        }
      })


      lib.getRequest("/contacts?organization_id=".concat(this.organization.organization_id), response => {
        this.contacts = response.data
        console.log("Request Completed: Contacts");
        console.log(response.data);
      })
    })


    lib.getRequest('/tags', response => {

      console.log("Request Completed: TagSuggestions");
      console.log(response.data);

      var myTagSuggestions = []
      for (var i = 0; i < response.data.length; i++) {
        myTagSuggestions.push({"value": response.data[i].tag_name, "tag_id": response.data[i].tag_id, "tag_color": response.data[i].tag_color,})
      }

      this.tagSuggestions = myTagSuggestions;

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
    height:175px;
    width:175px;
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
    width: 150px;
    margin-left: 10px;
  }

</style>
