<template>
  <div id ="Tag" v-loading="loading" :data="tags">
    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>

    <el-row type="flex" class="row-bg" justify="center">
      <h1>{{this.$route.params.id}}</h1>
    </el-row>
    <el-row type="flex" class="row-bg" justify="center">
      <h1>Companies</h1>
    </el-row>
    <div v-if="errors && organizations.length">
      <ul v-for="organization of organizations">
          {{organization.name}}
          <!-- <router-link :to="{ name: 'Single-Contact', params: { id: tag.tag } }">
            {{contact.first}} {{contact.last}}
          </router-link> -->
      </ul>
    </div>
    <el-row type="flex" class="row-bg" justify="center">
      <h1>Contacts</h1>
    </el-row>

    <div v-if="errors && contacts.length">
      <ul v-for="contact of contacts">
          {{contact.contact_id}}
          <!-- <router-link :to="{ name: 'Single-Contact', params: { id: tag.tag } }">
            {{contact.first}} {{contact.last}}
          </router-link> -->
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
      tags:[],
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

      for (var i = 0; i < this.tags.length; i++) {
        if (this.tags[i].organization_id) {
          if (orgIds !== "") {
            orgIds = orgIds.concat(",");
          }
          console.log("Adding orgID");
          console.log(this.tags[i].organization_id);
          orgIds = orgIds.concat(this.tags[i].organization_id);
        }
        else if (this.tags[i].contact_id) {
          if (contactIds !== "") {
            contactIds = contactIds.concat(",");
          }
          console.log("Adding contactID");
          console.log(this.tags[i].contact_id);
          contactIds = contactIds.concat(this.tags[i].contact_id);
        }
      }
      console.log("Organization Ids");
      console.log(orgIds);
      console.log("Contact Ids");
      console.log(contactIds);

      if (orgIds !== "") {
        var requestString = "/organizations?organization_id=" + orgIds;
        lib.getRequest(requestString, response => {
          this.organizations = response.data
          console.log(response.data);
          this.loading = false;
        })
      }
      if (contactIds !== "") {
        var requestString = "/contacts?contact_id=" + contactIds;
        lib.getRequest(requestString, response => {
          this.contacts = response.data
          console.log(response.data);
          this.loading = false;
        })
      }

    }
  },
  created() {

    lib.getRequest('/tagmappings', response => {
      this.tags = response.data
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
