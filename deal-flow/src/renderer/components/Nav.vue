<template>
  <div style="z-index: 2500;">
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-col :span="6">
        <el-button class="uk-button uk-button-default uk-margin-small-right" type="button" uk-toggle="target: #offcanvas-push">Nav bar</el-button>
      </el-col>
      <el-col :span="6">
        <!-- <SearchBar></SearchBar> -->
      </el-col>
      <el-col :span="6">
      </el-col>

    </el-row>

    <nav>

      <div id="offcanvas-push" uk-offcanvas="mode: push; overlay: true;">
        <div class="uk-offcanvas-bar">
            <button class="uk-offcanvas-close" type="button" uk-close></button>
            <li class="nav-item" v-for="routes in links">
              <router-link
                v-bind:key="routes.id"
                :to="`${routes.page}`"
                >
                {{routes.text}}
              </router-link>
            </li>
        </div>
      </div>

<!--

      <li class="nav-item" v-for="routes in links">
        <router-link
          v-bind:key="routes.id"
          :to="`${routes.page}`">{{routes.text}}
        </router-link>
      </li> -->
    </nav>
  </div>
</template>
<script>
import SearchBar from './SearchBar'
export default {
  name: 'Nav',
  components:{
        'SearchBar': SearchBar,
  },
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'Dashboard',
          page:'/Dahsboard'
        },
        {
          id: 1,
          text: 'Contacts',
          page:'/Contacts'
        },
        {
          id: 2,
          text: 'Companies',
          page:'/Organizations'
        },
        {
          id: 3,
          text: 'Deals',
          page:'/Deals'
        },
        {
          id: 4,
          text: 'Settings',
          page:'/Settings'
        },
      ]
    }
  }
}
</script>
