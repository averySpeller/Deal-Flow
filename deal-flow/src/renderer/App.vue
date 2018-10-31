<template>
  <div id="app">
    <Nav v-if="authenticated"></Nav>
    <router-view @authenticated="setAuthenticated"></router-view>

  </div>

</template>

<script>
  import Nav from './components/Nav'
  export default {
    name: 'deal-flow',
    components:{
          'Nav': Nav,
    },
    data() {
      return{
        authenticated: false,
        Authorization: "",
        mockAccount: {
          username: "kevin",
          password: "12345"
        },
        baseUrl: "http://24.138.161.30:5000/"
      }
    },
    created() {
      console.log("CHECKING TOKEN");
      this.checkForToken();

      if(!this.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    },
    methods: {
      checkForToken() {
        var jwtAuth = localStorage.getItem("jwtAuth");
        if (jwtAuth) {
          console.log(jwtAuth);
          this.Authorization = "Bearer ".concat(jwtAuth);
          this.authenticated = true;
        }
        else {
          console.log("ERROR: No Authentification token found in localStorage");
        }
      },
      setAuthenticated(status) {
        this.authenticated = status;
      },
      logout() {
        console.log("Logging Out Goobye");
        localStorage.removeItem("jwtAuth");
        this.authenticated = false;
      },
      goBack () {
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')
      },
      createGetRequest(path){
        var myRequest = this.baseUrl.concat(path)
        console.log(this.Authorization);
        return {
          myRequest: myRequest,
          auth: {
            headers: {
              Authorization: this.Authorization
            }
          }
        };
        // , { headers:{ this.header }}
      },
      parseJwt (token) {
        var base64Url = token.split('.')[0];
        var base64 = base64Url.replace('-', '+').replace('_', '/');
        return JSON.parse(window.atob(base64));
      }
    },
  }
</script>

<style>
  /* CSS */
</style>
