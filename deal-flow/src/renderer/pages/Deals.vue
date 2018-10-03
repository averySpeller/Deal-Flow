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
	    <div>
	    	Big Data List:
    		<ul>
    			<li v-for="item in bigdata">{{item.last}}, {{item.first}}</li>
    		</ul>
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
    		variable: null,
    		bigdata: [
    			{ first: 'Carter', last: 'Bourette' },
    			{ first: 'Avery', last: 'Speller' },
    			{ first: 'Kevin', last: 'Prince' }
    		]
    	}
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      somefunc() {
      	var splitty = this.variable.split(' ')
      	this.bigdata.push({ first: splitty[0], last: splitty[1]})
      	this.variable = ''
      }
    }
  }
</script>