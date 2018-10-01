<template>
  <div id="wrapper">
	<html>
	  <body>
	    <div id="example">
	      <h1 v-if="variable">{{variable}}</h1>
	      <h1 v-else>Welcome User!</h1>      
	      <input v-model="variable" type="text">
	      <button @click="somefunc()">Click me!</button>
	    </div>
	  </body>
	</html>
  </div>
</template>
<script>
  export default {
    name: 'deals',
    data() {
    	return {
    		variable: null
    	}
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      somefunc() {
      	alert(this.variable)
      }
    }
  }
</script>