<template>

<div class="wrapper">
  <AddOrganization></AddOrganization>
</div>
</template>
<script>
import AddOrganization from './AddOrganization';

export default {
  name: 'AddOrganizationPage',
  components:{
        'AddOrganization': AddOrganization,
  },
  data() {
    return{

    }
  },
  mounted(){
    this.$emit('backButton', true);
  }
}

</script>
