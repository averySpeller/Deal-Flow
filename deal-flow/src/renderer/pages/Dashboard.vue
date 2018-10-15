<template>
  <div>
    <h1>Dashboard</h1>
    <div id="slider1">
      <h2>Browsers</h2>
      <carousel :perPageCustom="[[768, 3], [1024, 4]]">
        <slide v-for="company in companies" v-if="company.tagging === 'browser'">
          <div>
            <img v-bind:src="company.logo" height="200" width="200"/>
            <h5>{{company.name}}</h5>
            {{company.valuation}}
          </div>
        </slide>
      </carousel>
    </div>
    <div id="slider2">
      <h2>Jobs</h2>
      <carousel :perPageCustom="[[768, 3], [1024, 4]]">
        <slide v-for="company in companies" v-if="company.tagging === 'jobs'">
          <div>
            <img v-bind:src="company.logo" height="200" width="200"/>
            <h5>{{company.name}}</h5>
            {{company.valuation}}
          </div>
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard', //this is the name of the component
  data() {
    return {
      variable: null,
      examplelogo: '../assets/randomLogo1.png',
      companies: [
        { name: 'Gmail', logo: 'static/imgs/randomLogo1.png', tagging: 'browser', valuation:'1.2' },
        { name: 'CHEP', logo: 'static/imgs/randomLogo2.jpg', tagging: 'browser', valuation:'1.2' },
        { name: 'Shopify', logo: 'static/imgs/randomLogo3.png', tagging: 'jobs', valuation:'1.2' },
        { name: 'Internet Explorer', logo: 'static/imgs/randomLogo4.png', tagging: 'browser', valuation:'1.2' },
        { name: 'LinkedIn', logo: 'static/imgs/randomLogo5.png', tagging: 'jobs', valuation:'1.2' },
        { name: 'Chrome', logo: 'static/imgs/randomLogo6.png', tagging: 'browser', valuation:'1.2' },
      ]
    }
  },
}
</script>
<style>
</style>
