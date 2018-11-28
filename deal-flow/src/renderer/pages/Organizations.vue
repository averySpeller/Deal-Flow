<template>
  <div id ="Organizations">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="22">
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="12">
            <h1>Organizations</h1>
          </el-col>
          <el-col :span="12">
            <div class="uk-align-right uk-margin-right">
              <router-link to="AddOrganizationPage"><el-button type="primary">Add Organization</el-button></router-link>
            </div>
          </el-col>
        </el-row>
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="22">
            <div v-loading="loading" :data="currentOrganizations">
              <el-table
               :data="currentOrganizations"
               style="width: 100%"
               @cell-click="organizationRowClick">
                 <el-table-column
                   prop="name"
                   label="Name">
                 </el-table-column>
                 <el-table-column
                   prop="valuation"
                   label="Valuation">
                 </el-table-column>
                 <el-table-column
                   prop="website"
                   label="Website">
                 </el-table-column>
                 <el-table-column
                  fixed="right"
                  label="Operations"
                  width="120">
                  <template slot-scope="scope">
                      <router-link :to="{ name: 'EditOrganization', params: { id: scope.row.organization_id } }">
                        <el-button type="primary" icon="el-icon-edit" circle></el-button>
                      </router-link>
                  </template>
                </el-table-column>
               </el-table>
              <ul v-for="organization in organizations">
                  <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">{{organization.name}}</router-link>
              </ul>
            </div>
            <br>
            <el-row type="flex" class="row-bg" justify="center">
              <el-pagination
                :page-size="maxOrganizationsPerPage"
                :pager-count="11"
                layout="prev, pager, next"
                :total="maxOrganizations"
                @current-change="changePage">
              </el-pagination>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
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
  name: 'Organizations',
  data(){
    return {
      organizations:[],
      currentOrganizations:[],
      errors: [],
      maxOrganizations: 1,
      maxOrganizationsPerPage: 7,
      loading: true
    }
  },
  methods:{
    deleteOrganization(id){
      var i;
      for (i = 0; i < this.currentOrganizations.length; i++) {
        console.log(i);
        if(this.currentOrganizations[i].organization_id === id){
           break;
        }
      }
      lib.deleteRequest("/organizations/".concat(id), response => {
        console.log("Request Completed: Delete organization #".concat(id));
        console.log(response.data);
        console.log("splicing #".concat(i));
        this.currentOrganizations.splice(i, 1);
        console.log(this.currentOrganizations);
      })
    },
    organizationRowClick(row, col, cell, e){
      console.log(row);
      console.log(col);
      if (col.label == "Operations") {
        // dont do anything
      }
      else {
        this.$router.push({ name: 'Single-Organization', params: { id: row.organization_id }})
      }
    },
    changePage(page){
      this.currentOrganizations = this.organizations[page-1]
    }
  },
  created() {

    this.$emit('backButton', false);
    lib.getRequest('/organizations', response => {

      console.log(response.data.length)
      this.maxOrganizations = response.data.length

      var myIndex = 1;
      var newList = [];
      var newNumber = 1;

      for (var i = 0; i < response.data.length; i++) {
        newNumber = Math.ceil((i+1)/this.maxOrganizationsPerPage)

        if (myIndex < newNumber) {
          this.organizations.push(newList)
          newList = [];
          myIndex = newNumber;
        }

        newList.push(response.data[i])

      }
      if (newList.length > 0) {
        console.log(this.organizations);
        if (this.organizations.length = 0) {
          console.log("THIS IS AN EMPTY LIST");
          this.organizations = [this.newList]
        }
        this.organizations.push(newList)
        newList = [];
      }

      console.log(this.organizations);
      this.currentOrganizations = this.organizations[0]

      console.log("Current Contacts");
      console.log(this.currentOrganizations);

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
