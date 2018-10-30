<template>
  <div id ="Contact" v-loading="loading" :data="contact">
    <el-row type="flex" class="row-bg" justify="center">
      <el-col :span="8">
        <div class="uk-flex uk-flex-center uk-inline" style="border-radius: 50%">
          <img src="static/imgs/linux.png">
        </div>
        <div class="title uk-flex uk-flex-center">
          <h1>{{contact.first}} {{contact.last}}</h1>
        </div>
      </el-col>
    </el-row>
    <div class="">
      <ul>

          <p><strong>Name: </strong>{{contact.first}}</p>
          <br><br>
          <li><p><strong>Email: </strong>{{contact.email}}</p></li>
          <li><p><strong>Phone: </strong>{{contact.phone1}}</p></li>
          <li><p><strong>Website: </strong>{{contact.website}}</p></li>
      </ul>
      <el-row>
        <el-col :span="12">
            Notes: <el-input
                      v-model="contact.notes"
                      type="textarea"
                      :autosize="{ minRows: 4, maxRows: 8}"
                      placeholder="Additional Notes" >
                    </el-input>
        </el-col>
      </el-row>


      <el-button @click="deleteContact()">delete</el-button>

      <router-link :to="{ name:'EditContact', params: { id: this.id }}">Edit</router-link>
    </div>
    <br>
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
      contact_id: 0,
      contact: {},
      errors: [],
      loading:true
    }
  },
  methods:{
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    deleteContact(){
      var myRequest = this.$parent.createGetRequest("contacts/".concat(this.contact.contact_id))

      axios.delete(myRequest).then(response => {
        console.log(myRequest);
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')

      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  created() {
    var myRequest = this.$parent.createGetRequest("contacts/".concat(this.$route.params.id))
    this.id = this.$route.params.id;

    axios.get(myRequest).then(response => {
      this.contact = response.data
      console.log(myRequest);
      this.loading = false;
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
