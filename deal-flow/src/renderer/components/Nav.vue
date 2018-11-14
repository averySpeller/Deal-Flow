<template>
  <div style="z-index: 2500;" class="uk-margin">
    <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <router-link
        v-for="routes in links"
        v-bind:key="routes.id"
        :to="`${routes.page}`">

        <el-menu-item index="2">
          <i
            v-bind:uk-icon="routes.icon"
            class="el-icon">
          </i>
          <!-- <i v-bind:class="routes.icon"></i> -->
          <span slot="title">{{routes.text}}</span>
        </el-menu-item>
      </router-link>
    </el-menu>

  </div>

</template>
<script>
import SearchBar from './SearchBar'
export default {
  name: 'Nav',
  props:['isCollapse'],
  components:{
        'SearchBar': SearchBar,
  },
  data() {
    return {
      links: [
        {
          id: 0,
          icon: 'icon: home',
          text: 'Dashboard',
          page:'/Dahsboard'
        },
        {
          id: 1,
          icon: 'icon: user',
          text: 'Contacts',
          page:'/Contacts'
        },
        {
          id: 2,
          icon: 'icon: grid',
          text: 'Deals',
          page:'/Organizations'
        },
        {
          id: 4,
          icon: 'icon: cog',
          text: 'Settings',
          page:'/Settings'
        },
      ]
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>
