<template>
  <div class="">
    <br><br>
    <el-row type="flex" class="" justify="center">
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>

      <el-col>

        <el-row type="flex" class="" justify="center">
          <form v-on:submit.prevent="submitSearch()" class="uk-navbar-container uk-search uk-search-large">
            <span uk-search-icon></span>
            <input ref="searchBar" v-model="searchParam" class="uk-search-input" type="search" placeholder="Search..."/>
          </form>
        </el-row>

        <div v-if="firstsearch">
          <el-row type="flex" class="" justify="center">
            <el-col :xs="0" :sm="0" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>
            <el-col :xs="24" :sm="24" :md="10" :lg="9" :xl="8" v-loading="loadingOrganizations" :data="organizations">
              <h1>Organizations</h1>
              <ul>
                <li v-for="organization in organizations">
                  <router-link  :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">{{organization.name}}</router-link>
                </li>
              </ul>
            </el-col>
            <el-col :xs="24" :sm="24" :md="10" :lg="9" :xl="8" v-loading="loadingContacts" :data="contacts">
              <h1>Contacts</h1>
              <ul>
                <li v-for="contact in contacts">
                  <router-link :to="{ name: 'Single-Contact', params: { id: contact.contact_id } }">{{contact.first}} {{contact.last}}</router-link>
                </li>
              </ul>
            </el-col>
            <el-col :xs="0" :sm="0" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>
          </el-row>

          <el-row type="flex" class="" justify="center">
            <el-col :xs="0" :sm="0" :md="4" :lg="5" :xl="6"><div class="grid-content bg-purple"></div></el-col>
            <el-col :xs="24" :sm="24" :md="16" :lg="14" :xl="12" v-loading="loadingTags" :data="tags">
              <h1>Tags</h1>
              <ul>
                <li v-for="tag in tags">
                  <router-link :to="{ name: 'Tag', params: { id: tag.tag_id } }">{{tag.tag_name}}</router-link>
                </li>
              </ul>
            </el-col>
            <el-col :xs="0" :sm="0" :md="4" :lg="5" :xl="6"><div class="grid-content bg-purple"></div></el-col>
          </el-row>
        </div>
      </el-col>

      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>
  </el-row>
  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Search',
  data(){
    return{
      firstsearch: false,
      loadingContacts: false,
      loadingOrganizations: false,
      loadingTags: false,
      loading: false,
      searchParam: "",
      contacts: [],
      organizations: [],
      tags: [],
    }
  },
  methods: {
    submitSearch(){
      console.log("SUBMTED");
      this.loadingContacts = true;
      this.loadingOrganizations = true;
      this.loadingTags = true;
      this.loading = true;
      this.$refs.searchBar.blur();
      this.firstsearch = true;
      this.retrieveData();
    },

    retrieveData(){
      lib.getRequest("/contacts?first:like=".concat(this.searchParam).concat('&last:like=').concat(this.searchParam), response => {
        this.contacts = response.data
        console.log("Request Completed: Contacts");
        console.log(response.data);
        this.loadingContacts = false;
      })
      lib.getRequest("/organizations?name:like=".concat(this.searchParam), response => {
        this.organizations = response.data
        console.log("Request Completed: Organizations");
        console.log(response.data);
        this.loadingOrganizations = false;
      })
      lib.getRequest("/tags?tag_name:like=".concat(this.searchParam), response => {
        this.tags = response.data
        console.log("Request Completed: Tags");
        console.log(response.data);
        this.loadingTags = false;
      })
    }
  },
  mounted(){
    this.$refs.searchBar.focus();
  }
}
</script>

<style>
</style>
