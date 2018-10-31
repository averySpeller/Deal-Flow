<template>

<div class="wrapper">
  <AddContact></AddContact>
</div>
</template>
<script>
import AddContact from './AddContact';

export default {
  name: 'AddContactPage',
  components:{
        'AddContact': AddContact,
  },
  data() {
    return{
      
    }
  }
}

</script>
