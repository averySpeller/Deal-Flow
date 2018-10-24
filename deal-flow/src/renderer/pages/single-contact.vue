<template>
  <div id ="Constact">
    <img src="static/imgs/linux.png">
    <div v-if="errors && users.length">
      <ul v-for="user of users">
          <div class="title"><h1>{{user.name}}</h1></div>
          <p><strong>Comapany: </strong>{{user.company.name}}</p>
          <br><br>
          <li><p><strong>Email: </strong>{{user.email}}</p></li>
          <li><p><strong>Phone: </strong>{{user.phone}}</p></li>
          <li><p><strong>Website: </strong>{{user.website}}</p></li>
          <li><p><strong>Comapany Moto: </strong> "{{user.company.catchPhrase}}"</p></li>
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
  name: 'Single-Contact',
  data(){
    return {
      id: 0,
      users:[],
      errors: [],
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  },
  created() {
    // this.id = this.$route.params.id;
    axios.get("https://jsonplaceholder.typicode.com/users?id=".concat(this.$route.params.id)).then(response => {
      this.users = response.data
      console.log("https://jsonplaceholder.typicode.com/users?id=".concat(this.$route.params.id));
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
