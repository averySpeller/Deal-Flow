<template>
  <div>
    <h1>Contact Catalogue</h1>
  <p>

    <div class="uk-flex uk-flex-column"></div>
    <ul class="uk-list uk-list-striped">
      <li class="" v-for="company in sortedArray">{{ company.name }}</li>
    </ul>
  </p>
  </div>
</template>

<script>
export default {
  name: 'ContactCatalogue',
  data(){
    return {
      email: 'email@email.com',
      web: 'dealflow.com',
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
  computed: {
    sortedArray: function() {
      function compare(a, b) {
        if (a.name < b.name)
          return -1;
        if (a.name > b.name)
          return 1;
        return 0;
      }

      return this.companies.sort(compare);
    }
  }

}
</script>
view raw
