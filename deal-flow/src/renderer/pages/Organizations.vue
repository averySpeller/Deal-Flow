<template>
  <div id ="Organizations">
    <h1>Organizations</h1>
    <div  v-loading="loading" :data="organizations">
      <ul v-for="organization in organizations">
          <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">{{organization.name}}</router-link>
      </ul>
    </div>
    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
    <router-link to="AddOrganizationPage" tag="el-button">Add Company</router-link>

  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Organizations',
  data(){
    return {
      organizations:[],
      errors: [],
      loading: false
    }
  },
  methods:{

  },
  created() {
    lib.getRequest('/organizations', response => {
      this.organizations = response.data
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
