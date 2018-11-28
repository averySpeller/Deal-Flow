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
            <div v-loading="loading" :data="organizations">
              <ul v-for="organization in organizations">
                  <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">{{organization.name}}</router-link>
              </ul>
            </div>
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
      errors: [],
      loading: true
    }
  },
  methods:{

  },
  created() {

    this.$emit('backButton', false);
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
