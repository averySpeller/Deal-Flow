<template>
  <div id ="Organization">
    <img src="static/imgs/UoG.png">
    <div v-if="organization">
      <ul>
          <div class="title"><h1>{{organization.name}}</h1></div>
          <p><strong>Comapany Vision: </strong> "{{organization.vision}}"</p>
          <br><br>
          <li><p><strong>Website: </strong>{{organization.website}}</p></li>
          <!-- <li><p><strong>Address: </strong>{{organization.address.street}} "Street, "{{organization.address.suite}}", "{{organization.address.city}}", "{{organization.address.zipcode}}</p></li> -->

          <ol>
            <li v-for="contact in contacts">
              <router-link :to="{ name: 'Single-Contact', params: { contact_id: contact.contact_id} }">
                {{contact.first}}
              </router-link>
            </li>
          </ol>
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
  name: 'Single-Organization',
  data(){
    return {
      organization: {},
      contacts: [],
      errors: [],
      contacterrors: [],
      address: ""
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
    var myRequest = this.$parent.createGetRequest("organizations/".concat(this.$route.params.id))

    axios.get(myRequest).then(response => {
      this.organization = response.data
      console.log(myRequest);
    })
    .catch(e => {
      this.errors.push(e)
      console.log('failed');
    })

    myRequest = this.$parent.createGetRequest("contacts")

    axios.get(myRequest).then(response => {
      this.contacts = response.data
      console.log(response.data);
    })
    .catch(e => {
      this.contacterrors.push(e)
      console.log('faileds');
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
    border-radius: 20%;
}

</style>
