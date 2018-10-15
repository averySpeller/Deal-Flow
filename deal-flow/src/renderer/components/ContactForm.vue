<template>
  <div>
    <h1>ContactForm</h1>
    <div id="loginForm">
      <h3 v-if="contactName">{{contactName}}</h3>
      <h3 v-else>&lt Contact Name Goes here &gt</h3>
      <h3 v-if="password">{{password}}</h3>
      <input v-model="contactName" type="text">
      <br>
      <input v-model="password" type="password">
      <br>
      <button @click="validateLoginCredentials()">Log In!</button>
      <br>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Login',
    data() {
      return {
          usernaame: null,
          password: null
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      validateLoginCredentials() {

        var re = /^\w+$/;
        if (!re.test(this.contactName.trim())) {
          alert('Using special characters');
        }
      	// this.variable.split(' ')
      	// this.bigdata.push({ first: splitty[0], last: splitty[1]})
      	// this.variable = ''
      }
    }
  }
</script>
<style>
</style>
