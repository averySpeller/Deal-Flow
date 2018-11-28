<template>
  <div id ="Contacts">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="22">
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="12">
            <h1>Contacts</h1>
          </el-col>
          <el-col :span="12">
            <div class="uk-align-right uk-margin-right">
              <router-link :to="{ name: 'AddContactPage', params: { id: null } }" type="primary"><el-button type="primary">Add Contact</el-button></router-link>
            </div>
          </el-col>
        </el-row>
        <div v-loading="loading" :data="contacts">
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
                  <router-link :to="{ name: 'AddContactPage', params: { id: scope.row.contact_id } }">
                    <el-button type="text" size="small">Edit</el-button>
                  </router-link>
                  <el-button v-on:click="deleteContact(scope.row.contact_id)" type="text" size="small">Delete</el-button>

              </template>
            </el-table-column>
           </el-table>
        </div>
      </el-col>
    </el-row>
    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>

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
      loading:true
    }
  },
  methods:{
    deleteContact(id){
      for (var i = 0; i < this.contacts.length; i++) {
        if(this.contacts[i].contact_id === id){
           lib.deleteRequest("/contacts/".concat(id), response => {
             console.log("Request Completed: Delete Contact #".concat(id));
             console.log(response.data);
             this.contacts.splice(i, 1);
           })
        }
      }
    }
  },
  created() {
    this.$emit('backButton', false);

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
