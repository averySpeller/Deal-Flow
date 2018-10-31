<template>
  <div id ="Constacts" v-loading="loading" :data="contacts">
    <h1>Contacts</h1>
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

    <router-link to="AddContactPage" tag="el-button">Add contact</router-link>
    <!-- <el-button><router-link to="/AddContact">Add Contact</router-link></el-button> -->
  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Contacts',
  data(){
    return {
      contacts:[],
      errors: [],
      loading:false
    }
  },
  methods:{

  },
  created() {
    var requestFields = this.$parent.createGetRequest("contacts")

    lib.getRequest('/contacts', response => {
      this.contacts = response.data
      console.log(response.data);
      this.loading = false;
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
    border-radius: 50%;
}

</style>
