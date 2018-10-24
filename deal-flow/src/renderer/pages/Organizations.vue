<template>
  <div id ="Organizations">
    <h1>Organizations</h1>
    <div v-if="errors && users.length">
      <ul v-for="user of users">
          <router-link :to="{ name: 'Single-Organization', params: { id: user.id } }">{{user.company.name}}</router-link>
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
      users:[],
      errors: [],
    }
  },
  methods:{

  },
  created() {
    axios.get('https://jsonplaceholder.typicode.com/users').then(response => {
      this.users = response.data
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
