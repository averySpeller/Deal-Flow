<template>
  <div id ="Contacts" v-loading="loading" :data="contacts">
    <h1>Contacts</h1>
    <div v-if="errors && contacts.length">
        <el-table
         :data="contacts"
         style="width: 100%">
         <el-table-column
           prop="organization_id"
           label="Company"
           width="180">
         </el-table-column>
         <el-table-column
           prop="first"
           label="First Name"
           width="180">
         </el-table-column>
         <el-table-column
           prop="last"
           label="Last Name">
         </el-table-column>
         <el-table-column
          fixed="right"
          label="Operations"
          width="120">
          <template slot-scope="scope">
              <router-link :to="{ name: 'Single-Contact', params: { id: scope.row.contact_id } }">
                <el-button type="text" size="small">Detail</el-button>
              </router-link>
            <el-button type="text" size="small">Edit</el-button>
          </template>
        </el-table-column>
       </el-table>

      <!-- <ul v-for="contact of contacts">
          <router-link :to="{ name: 'Single-Contact', params: { id: scope.row.contact_id } }">
            <el-button @click="handleClick" type="text" size="small">Detail</el-button>
          </router-link>
      </ul> -->
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
