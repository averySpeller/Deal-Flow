<template>
  <div id ="Tag" v-loading="loading" :data="tagMappings">
    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <el-row type="flex" class="row-bg" justify="center">
      <h1>{{this.tag}}</h1>
    </el-row>
    <el-row type="flex" class="row-bg" justify="center">
      <h1>Companies</h1>
    </el-row>
    <div v-if="errors && organizations.length">
      <ul v-for="organization of organizations">
          <!-- {{organization.name}} -->
          <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">
            {{organization.name}}
          </router-link>
      </ul>
    </div>
    <el-row type="flex" class="row-bg" justify="center">
      <h1>Contacts</h1>
    </el-row>

    <div v-if="errors && contacts.length">
      <ul v-for="contact of contacts">
          <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id } }">
            {{contact.first}} {{contact.last}}
          </router-link>
      </ul>
    </div>
    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>

  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Tag',
  data(){
    return {
      tagId: null,
      tag: {},
      tagMappings:[],
      organizations:[],
      contacts:[],
      errors: [],
      loading:false
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    loadData(){
      var orgIds = "";
      var contactIds = "";

      //Loop through the tag mappings to find the organization and contact ids for the query
      for (var i = 0; i < this.tagMappings.length; i++) {
        if (this.tagMappings[i].organization_id) {
          if (orgIds !== "") {
            orgIds = orgIds.concat(",");
          }
          orgIds = orgIds.concat(this.tagMappings[i].organization_id); //concatenating the ids to the string to later use in query
        }
        else if (this.tagMappings[i].contact_id) {
          if (contactIds !== "") {
            contactIds = contactIds.concat(",");
          }
          contactIds = contactIds.concat(this.tagMappings[i].contact_id);
        }
      }

      if (orgIds !== "") {
        var requestString = "/organizations?organization_id=" + orgIds; //attach ids to the request to get specific set of organizations
        lib.getRequest(requestString, response => {
          this.organizations = response.data
          console.log("Request Completed: Organizations");
          console.log(response.data);
          this.loading = false;
        })
      }
      if (contactIds !== "") {
        var requestString = "/contacts?contact_id=" + contactIds;
        lib.getRequest(requestString, response => {
          this.contacts = response.data
          console.log("Request Completed: Contacts");
          console.log(response.data);
          this.loading = false;
        })
      }

    }
  },
  created() {
    this.tagId = this.$route.params.id
    lib.getRequest('/tag/'.concat(this.tagId), response => {
      this.tag = response.data
      console.log("Request Completed: Tag");
      console.log(response.data);
    })

    // lib.getRequest('/tagmappings?id=&page=2', response => {
    lib.getRequest('/tagmappings/?tag_id='.concat(this.tagId), response => {
      this.tagMappings = response.data
      console.log("Request Completed: TagMappings");
      console.log(response.data);
      this.loadData();
    })
  }
}
</script>
<style scoped>

  #title{
    text-align: center;
    margin: 0 auto;
  }

</style>
