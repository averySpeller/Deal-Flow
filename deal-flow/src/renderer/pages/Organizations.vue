<template>
  <div id ="Organizations">
    <h1>Organizations</h1>
    <div v-if="errors && organizations.length">
      <ul v-for="organization in organizations">
          <router-link :to="{ name: 'Single-Organization', params: { id: organization.organization_id } }">{{organization.name}}</router-link>
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
import axios from 'axios';
export default {
  name: 'Organizations',
  data(){
    return {
      organizations:[],
      errors: [],
    }
  },
  methods:{

  },
  created() {
    var myRequest = this.$parent.createGetRequest("organizations")
    axios.get(myRequest).then(response => {
      this.organizations = response.data
      console.log('log it up');
      console.log(response.data);
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
