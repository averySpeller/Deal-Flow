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
              <input v-else v-model="password" class="uk-input uk-form-width-medium"  type="text" placeholder="password">
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

        // axios.post(base_url + '/auth', { "username": this.username, "password": this.password });

        axios.post(base_url + '/auth', { "username": this.username, "password": this.password }).then(response => {
          if (response.data) {
            this.jwtAuth = response.data
            if (typeof(Storage) !== "undefined") {
              // Store
              localStorage.setItem("jwtAuth", this.jwtAuth);
              // Retrieve
              // this.jwtAuth = localStorage.getItem("jwtAuth");
            } else {
              document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
            }
            console.log(myRequest);
            this.loading = false;
          }
          else {
            this.usernameError= false;
            this.passwordError= false;
            this.errors = this.errors + "EVERYTHING IS MESSED";
          }
        })
        .catch(e => {
          this.errorArray.push(e)
        })
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
          if(finishLogging()){
            this.$emit("authenticated", true);
            this.$router.replace({ name: "Dashboard" });
          }
          else {
            this.usernameError = true;
            this.passwordError = true;
            this.errors = "Bad Credentials\n";
          }
        }

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
