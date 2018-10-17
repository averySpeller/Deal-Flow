<template>
  <div class="uk-position-center uk-inline">
    <img src="static/imgs/logo.jpg">
    <div id="loginForm" class="uk-align-center uk-text-center">
      <form v-on:submit.prevent="validateLoginCredentials()">
        <div v-if="!loading" id="textInputs">
          <div class="uk-margin">
            <div class="uk-inline">
              <span class="uk-form-icon" uk-icon="icon: user"></span>
              <input v-if="usernameError" v-model="username" class="uk-input uk-form-width-medium uk-form-danger" type="text" >
              <input v-else v-model="username" class="uk-input uk-form-width-medium"  type="text" placeholder="username">
            </div>
          </div>
          <div class="uk-margin">
            <div class="uk-inline">
              <span class="uk-form-icon" uk-icon="icon: lock"></span>
              <input v-model="password" class="uk-input uk-form-width-medium" type="password" placeholder="password">
            </div>
          </div>
        </div>

        <span v-else uk-spinner="ratio: 4.5"></span>
        <br>
        <input type="submit" value="Log In" class="uk-button uk-button-primary uk-button-large uk-margin" >
        <!-- <button @click="validateLoginCredentials()" class="uk-button uk-button-primary uk-button-large uk-margin">Log In</button> -->
      </form>
      <br>
      <button @click="somefunc()"class="uk-button uk-button-secondary uk-button-small uk-margin-small" >Forgot Password</button>
      <h3 style="color:red"v-if="errors">{{errors}}</h3>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Login',
    data() {
      return {
          username: null,
          password: null,
          errors: null,
          usernameErrors: false,
          loading: false,
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      finishLogging(){
        var re = /^\w+$/;
        if (!re.test(this.username)) {
          this.usernameError = true;
          this.errors = "*username is using special characters";
        }
        this.loading= false;
      },
      validateLoginCredentials() {
        this.loading= true;
        this.errors= null;
        this.usernameError= false;
        setTimeout(()=>{
           this.finishLogging()
        },3000);



      }
    }
  }
</script>
<style>
</style>
