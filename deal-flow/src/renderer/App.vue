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
          'Nav': Nav
    },
    data() {
      return{
        authenticated: false,
        mockAccount: {
          username: "kevin",
          password: "12345"
        }
      }
    },
    mounted() {
      if(!this.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    },
    methods: {
      setAuthenticated(status) {
        this.authenticated = status;
      },
      logout() {
        this.authenticated = false;
      }
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  }
</script>

<style>
  /* CSS */
</style>
