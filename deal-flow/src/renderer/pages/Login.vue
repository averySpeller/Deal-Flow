<template>
  <div class="uk-position-center uk-inline">
    <img src="static/imgs/logo.jpg">
    <div id="loginForm" class="uk-align-center uk-text-center">
      <el-form ref="form" :model="form">
        <el-form-item label="Username">
          <el-input v-model="form.name" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input type="password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Create</el-button>
        </el-form-item>
      </el-form>
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

        username: "",
        password: "",
        errors: null,
        usernameError: false,
        passwordError: false,
        loading: false,
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      finishLogging(){
        if (this.username == "") {
          this.usernameError = true;
          this.errors = this.errors + "username is empty\n";
        }
        else if (this.password == "") {
          this.passwordError = true;
          this.errors = this.errors + "password is empty\n";
        }
        else {
          if(this.username == this.$parent.mockAccount.username && this.password == this.$parent.mockAccount.password){
            this.$emit("authenticated", true);
            this.$router.replace({ name: "Dashboard" });
          }
          else {
            this.usernameError = true;
            this.passwordError = true;
            this.errors = "Bad Credentials\n";
          }
        }
        this.loading= false;
      },
      validateLoginCredentials() {
        this.loading= true;
        this.usernameError= false;
        this.passwordError= false;
        this.errors= "";
        setTimeout(()=>{
           this.finishLogging()
        },2000);

      },
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>
<style>
</style>
