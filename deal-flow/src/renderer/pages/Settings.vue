<template>
  <div>
    <h1>Settings</h1>
    <p>Settings page</p>
  </div>
</template>

<script>
export default {
  name: 'Settings' //this is the name of the component
  ,
  mounted(){
    this.$emit('backButton', false);
  }
}
</script>
<style>
</style>
