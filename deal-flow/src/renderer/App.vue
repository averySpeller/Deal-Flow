<template>
  <div id="app">
    <Nav v-if="authenticated"></Nav>
    <SearchBar v-if="authenticated"></SearchBar>
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
        authenticated: true,
        mockAccount: {
          username: "kevin",
          password: "12345"
        },
        baseUrl: "http://24.138.161.30:5000/"
      }
    },
    mounted() {
      this.jwtAuth = localStorage.getItem("jwtAuth");

      if(!this.authenticated) {
        this.$router.replace({ name: "Login" });
      }

      this.jwtAuth = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg"; //
      var output = this.parseJwt(this.jwtAuth);
      console.log("RIGHT HERE RIGHT NOW");
      console.log(output);
    },
    methods: {

      setAuthenticated(status) {
        this.authenticated = status;
      },
      logout() {
        this.authenticated = false;
      },
      goBack () {
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')
      },
      createGetRequest(path){
        var myRequest = this.baseUrl.concat(path)
        return myRequest
      },
      createPostRequest(path){
        var myRequest = this.baseUrl.concat(path)
        return myRequest
      },
      createDeleteRequest(path){
        var myRequest = this.baseUrl.concat(path)
        console.log(myRequest);
        return myRequest
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
