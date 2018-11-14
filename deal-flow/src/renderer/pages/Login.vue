<template>
  <div class="uk-position-center uk-inline">
    <img src="static/imgs/logo.jpg">
    <div id="loginForm" class="uk-align-center uk-text-center">
      <!-- <el-form ref="form" :model="form">
        <el-form-item label="Username">
          <el-input v-model="form.name" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input type="password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Create</el-button>
        </el-form-item>
      </el-form> -->
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
              <input v-if="passwordError" v-model="password" class="uk-input uk-form-width-medium uk-form-danger" type="text" >
              <input v-else v-model="password" class="uk-input uk-form-width-medium"  type="password" placeholder="password">
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
  import lib from '../lib'
  import axios from 'axios';
  export default {
    name: 'Login',
    props: ['authenticated'],
    data() {
      return {
        username: "",
        password: "",
        errors: null,
        errorArray: [],
        jwtAuth:"",
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
        console.log(lib.baseUrl.concat('/auth'));
        lib.postRequest('/auth', { "username": this.username, "password": this.password }, response => {
          console.log('here');
          if (response.data) {
            console.log(response.data);
            this.jwtAuth = response.data.token
            if (typeof(Storage) !== "undefined") {
              // Store
              localStorage.setItem("jwtAuth", this.jwtAuth);
            }
            else {
              document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
            }
            this.$emit("authenticated", true);
            this.$router.replace({ name: "Dashboard" });
            this.loading = false;
            lib.checkForToken();
            this.authenticated = true;
          }
          else {
            this.usernameError = true;
            this.passwordError = true;
            this.errors = "Bad Credentials\n";
          }
        }, function() {console.log('failed');})
      },
      validateLoginCredentials() {
        this.loading= true;
        this.usernameError= false;
        this.passwordError= false;
        this.errors= "";

        if (this.username == "") {
          this.usernameError = true;
          this.errors = this.errors + "username is empty\n";
        }
        if (this.password == "") {
          this.passwordError = true;
          this.errors = this.errors + "password is empty\n";
        }

        if (!(this.usernameError && this.passwordError)) {
          this.finishLogging()
        }

      },
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>
<style>
</style>
