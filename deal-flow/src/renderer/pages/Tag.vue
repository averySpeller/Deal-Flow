<template>
  <div id ="Tag" v-loading="loading" :data="tagMappings">

    <el-row type="flex" class="row-bg" justify="center">
      <h1>#{{this.tag.tag_name}}</h1>
    </el-row>
    <div>
      <hr class="uk-divider-icon"/>
      <el-row :gutter="40">
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
        <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <h3>Companies</h3>
          <ul v-for="organization of organizations">
              <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">
                {{organization.name}}
              </router-link>
          </ul>
        </el-col>
        <el-col :xs="12" :sm="11" :md="10" :lg="9" :xl="9">
          <h3>Contacts</h3>
          <ul v-for="contact of contacts">
              <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id } }">
                {{contact.first}} {{contact.last}}
              </router-link>
          </ul>
          <ul v-if="contacts.length < 1">
            No Contacts with this tag
          </ul>

        </el-col>
        <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="3"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
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
      loading: true
    }
  },
  methods:{
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
    this.$emit('backButton', true);

    this.tagId = this.$route.params.id
    lib.getRequest('/tags/'.concat(this.tagId), response => {
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
