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
        <div v-loading="loading" :data="currentContacts">
          <el-table
           :data="currentContacts"
           style="width: 100%"
           @cell-click="contactRowClick">
             <el-table-column
               prop="contact_name"
               label="Name">
             </el-table-column>
             <el-table-column
               prop="org_name"
               label="Company">
             </el-table-column>
             <el-table-column
               prop=""
               label="">
             </el-table-column>
             <el-table-column
              fixed="right"
              label="Operations"
              width="120">
              <template slot-scope="scope">
                  <router-link :to="{ name: 'AddContactPage', params: { id: scope.row.contact_id } }">
                    <el-button type="primary" icon="el-icon-edit" circle></el-button>
                  </router-link>
                  <el-button v-on:click="deleteContact(scope.row.contact_id)" type="danger" icon="el-icon-delete" circle></el-button>
              </template>
            </el-table-column>
           </el-table>
        </div>
        <br>
        <el-row type="flex" class="row-bg" justify="center">
          <el-pagination
            :page-size="maxContactsPerPage"
            :pager-count="11"
            layout="prev, pager, next"
            :total="maxContacts"
            @current-change="changePage">
          </el-pagination>
        </el-row>
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
      currentContacts:[],
      organizations:[],
      orgDict: {},
      maxContacts: 1,
      maxContactsPerPage: 7,
      errors: [],
      loading:true
    }
  },
  methods:{
    deleteContact(id){
      console.log("DELETING");
      var i;
      for (i = 0; i < this.currentContacts.length; i++) {
        console.log(i);
        if(this.currentContacts[i].contact_id === id){
           break;
        }
      }
      lib.deleteRequest("/contacts/".concat(id), response => {
        console.log("Request Completed: Delete Contact #".concat(id));
        console.log(response.data);
        console.log("splicing #".concat(i));
        this.currentContacts.splice(i, 1);
        console.log(this.currentContacts);
      })
    },
    contactRowClick(row, col, cell, e){
      console.log(row);
      console.log(col);
      if (col.label == "Operations") {
        // dont do anything
      }
      else {
        this.$router.push({ name: 'Single-Contact', params: { id: row.contact_id }})
      }
    },
    changePage(page){
      this.currentContacts = this.contacts[page-1]
    }
  },
  created() {
    this.$emit('backButton', false);

    lib.getRequest('/organizations', response => {
      this.organizations = response.data
      console.log("Request Completed: Organizations");
      console.log(response.data);
      for (var i = 0; i < this.organizations.length; i++) {
        this.orgDict[this.organizations[i].organization_id] = this.organizations[i].name
      }
      console.log(this.orgDict);

      lib.getRequest('/contacts', response => {
        console.log(response.data);

        console.log(response.data.length)
        this.maxContacts = response.data.length
        console.log(this.maxContacts);

        var myIndex = 1;
        var newList = [];
        var newNumber = 1;

        for (var i = 0; i < response.data.length; i++) {
          response.data[i].org_name = this.orgDict[response.data[i].organization_id]
          response.data[i].contact_name = response.data[i].first.concat(" ").concat(response.data[i].last)

          newNumber = Math.ceil((i+1)/this.maxContactsPerPage)

          if (myIndex < newNumber) {
            this.contacts.push(newList)
            newList = [];
            myIndex = newNumber;
          }

          newList.push(response.data[i])

        }
        if (newList.length > 0) {
          this.contacts.push(newList)
          newList = [];
        }

        console.log(this.contacts);
        this.currentContacts = this.contacts[0]

        console.log("Current Contacts");
        console.log(this.currentContacts);

        this.loading = false;
      })
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
