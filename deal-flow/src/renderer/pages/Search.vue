<template>
  <div class="">
    <br><br>
    <el-row type="flex" class="" justify="center">
      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>

        <div class="uk-navbar-container uk-search uk-search-large">
          <span uk-search-icon></span>
          <input @keyup.enter.native="submitSearch()" class="uk-search-input" type="search" placeholder="Search..."/>
        </div>

      <el-col :xs="0" :sm="1" :md="2" :lg="3" :xl="4"><div class="grid-content bg-purple"></div></el-col>
  </el-row>
  </div>
</template>

<script>
import lib from '../lib'
export default {
  name: 'Search',
  methods: {
    submitSearch(){
      console.log("SUBMTED");
    }
  }
}
</script>

<style>
</style>
