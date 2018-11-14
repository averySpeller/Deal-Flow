<template>
  <div id="app">
    <el-container v-if="authenticated">
      <el-header class="topnav-container">
        <!-- <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
          <el-radio-button :label="false">expand</el-radio-button>
          <el-radio-button :label="true">collapse</el-radio-button>
        </el-radio-group> -->
        <el-menu :default-active="activeIndex" class="topnav-right" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">Kevin</el-menu-item>
          <el-menu-item index="2">Logout</el-menu-item>
        </el-menu>
      </el-header>
      <el-container>
        <el-aside width="auto" height="100%">
          <Nav v-bind:isCollapse="this.isCollapse"></Nav>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>

    <router-view v-else @authenticated="setAuthenticated" v-bind:authenticated="this.authenticated"></router-view>
  </div>

</template>

<script>
  import lib from './lib'
  import Nav from './components/Nav'
  import TopBar from './components/TopBar'
  export default {
    name: 'deal-flow',
    components:{
          'Nav': Nav,
          'TopBar': TopBar,
    },
    data() {
      return{
        isCollapse: false,
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
      this. authenticated = lib.checkForToken();

      if(!this.authenticated) {
        this.$router.replace({ name: "Login" });
      }
    },
    methods: {
      checkForToken() {
        this.authenticated = true;
      },
      setAuthenticated(status) {
        this.authenticated = status;
      },
      logout() {
        console.log("Logging Out Goobye");
        localStorage.removeItem("jwtAuth");
        this.authenticated = false;
        location.reload();
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        if (key == 2) {
          console.log("IN HEREEEEE");
          this.logout();
        }
      },
      goBack () {
        window.history.length > 1
          ? this.$router.go(-1)
          : this.$router.push('/')
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
  .topnav-right {
    float: right;
  }
  .topnav-container{
    border-bottom: 3px;
    border-color: black;
  }
</style>
