<template>
  <div style="z-index: 2500;" class="uk-margin">
    <el-menu :default-active="activeIndex" class="topnav-right" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">Processing Center</el-menu-item>
      <el-menu-item index="2">Logout</el-menu-item>
    </el-menu>
  </div>

</template>
<script>
export default {
  name: 'TopBar',
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    };
  },
  methods: {
     handleSelect(key, keyPath) {
       console.log(key, keyPath);
       if (key == 2) {
         console.log("IN HEREEEEE");
         this.$parent.logout();
       }
     }
   }
}
</script>
<style scoped="">
  .topnav-right {
    float: right;
  }
</style>
