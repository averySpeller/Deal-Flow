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

    <router-link to="AddContact" tag="el-button">Add contact</router-link>
    <!-- <el-button><router-link to="/AddContact">Add Contact</router-link></el-button> -->
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Contacts',
  data(){
    return {
      contacts:[],
      errors: [],
      loading:true
    }
  },
  methods:{

  },
  created() {
    var myRequest = this.$parent.createGetRequest("contacts")

    axios.get(myRequest).then(response => {
      this.contacts = response.data
      console.log(response.data);
      this.loading = false;
    })
    .catch(e => {
      this.errors.push(e)
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
