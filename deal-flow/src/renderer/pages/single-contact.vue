<template>
  <div id ="Constact">
    <img src="static/imgs/linux.png">
    <div v-if="contact">
      <ul>
          <div class="title">
            <h1>{{contact.first}} {{contact.last}}</h1>
          </div>
          <p><strong>Name: </strong>{{contact.first}}</p>
          <br><br>
          <li><p><strong>Email: </strong>{{contact.email}}</p></li>
          <li><p><strong>Phone: </strong>{{contact.phone1}}</p></li>
          <li><p><strong>Website: </strong>{{contact.website}}</p></li>
      </ul>

    </div>
    <button @click="goBack()" class="uk-button uk-button-secondary uk-button-large uk-margin">GO BACK</button>
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
      contact: {},
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
    var myRequest = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))

    axios.get(myRequest).then(response => {
      this.contact = response.data
      console.log(myRequest);
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
