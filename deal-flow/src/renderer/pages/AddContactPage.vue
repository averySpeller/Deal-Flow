<template>

<div class="wrapper">
  <div class="title uk-flex uk-flex-center">
      <h1>Add Contact</h1>
  </div>
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
